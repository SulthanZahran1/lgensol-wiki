#!/usr/bin/env python3
"""Translate remaining Korean wiki .md files to English via Ollama Cloud API.
4 files per batch, skips already-English files.
"""
import os, re, sys, json, time
from pathlib import Path
import requests

WIKI_DIR = Path("/home/dev/lgensol-wiki/wiki")
BATCH_SIZE = 4
API_URL = "https://ollama.com/v1/chat/completions"
MODEL = "deepseek-v4-flash:cloud"
LOG_FILE = Path("/home/dev/lgensol-wiki/scripts/translate_log.txt")
SKIP = {"SCHEMA.md", "log.md", "index.md", "README.md"}

def log(msg):
    LOG_FILE.parent.mkdir(exist_ok=True)
    with open(LOG_FILE, "a") as f:
        f.write(f"{time.strftime('%H:%M:%S')} {msg}\n")
    print(msg)

def get_api_key():
    key = os.environ.get("OLLAMA_API_KEY")
    if key:
        return key
    env_path = Path.home() / ".hermes" / ".env"
    if env_path.exists():
        for line in env_path.read_text().splitlines():
            if line.startswith("OLLAMA_API_KEY="):
                key = line.split("=", 1)[1].strip().strip("\"'")
    return key

def has_korean(text):
    return bool(re.search(r"[\uac00-\ud7af\u1100-\u11ff\u3130-\u318f]", text))

def parse_fm(text):
    m = re.match(r"^---\n(.*?)\n---\n(.*)", text, re.DOTALL)
    if not m:
        return {}, text
    fm = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip()
    return fm, m.group(2)

def rebuild_fm(fm):
    lines = ["---"]
    for k, v in fm.items():
        lines.append(f"{k}: {v}")
    lines.append("---")
    return "\n".join(lines)

def translate_batch(batch_data, api_key):
    input_text = ""
    for i, (fp, fm, body) in enumerate(batch_data):
        input_text += f"--- FILE {i} ---\nTitle: {fm.get('title', 'Untitled')}\nBody:\n{body}\n\n"

    system = """You are a professional Korean->English translator specializing in battery technology.

RULES:
1. Translate ALL Korean text to natural English
2. Preserve ALL [[wikilinks]] EXACTLY as-is (do not modify slug names)
3. Preserve ALL ^[citation markers] EXACTLY as-is
4. Preserve ALL markdown formatting (headers ##, bold **, lists -, etc.)
5. Translate the Title line too
6. Use standard English battery terminology

OUTPUT format for each file exactly:
--- RESULT i ---
Title: <translated title>
Body:
<translated body>"""

    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"}
    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": input_text}
        ],
        "stream": False,
        "temperature": 0.1,
    }

    for attempt in range(3):
        try:
            resp = requests.post(API_URL, json=payload, headers=headers, timeout=120)
            if resp.status_code == 200:
                content = resp.json()["choices"][0]["message"]["content"]
                results = [None] * len(batch_data)
                blocks = re.split(r"^--- RESULT (\d+) ---$", content, flags=re.MULTILINE)
                i = 1
                while i + 1 < len(blocks):
                    idx = int(blocks[i].strip())
                    rt = blocks[i+1].strip()
                    if 0 <= idx < len(batch_data):
                        tm = re.search(r"^Title:\s*(.+)$", rt, re.MULTILINE)
                        bm = re.search(r"^Body:\n(.*)", rt, re.DOTALL)
                        if tm:
                            results[idx] = (tm.group(1).strip(), (bm.group(1).strip() if bm else ""))
                    i += 2
                return results
            elif resp.status_code == 429:
                log("  Rate limited, waiting 15s...")
                time.sleep(15)
            else:
                log(f"  API error {resp.status_code}: {resp.text[:150]}")
                time.sleep(5)
        except Exception as e:
            log(f"  Request failed: {e}")
            time.sleep(5)
    return [None] * len(batch_data)

def main():
    api_key = get_api_key()
    if not api_key:
        log("ERROR: No API key found")
        return

    # Collect only files with Korean in body (not frontmatter)
    korean_files = []
    for root, dirs, fnames in os.walk(WIKI_DIR):
        for f in fnames:
            if not f.endswith(".md") or f in SKIP:
                continue
            fp = Path(root) / f
            text = fp.read_text(encoding="utf-8")
            m = re.match(r"^---\n(.*?)\n---\n(.*)", text, re.DOTALL)
            if m and has_korean(m.group(2)):
                korean_files.append(fp)
            elif m and has_korean(m.group(1)):
                # frontmatter has Korean - translate anyway
                korean_files.append(fp)

    korean_files.sort()
    total = len(korean_files)
    log(f"Found {total} files with Korean content to translate")

    translated = 0
    errors = 0

    for batch_start in range(0, total, BATCH_SIZE):
        batch = korean_files[batch_start:batch_start + BATCH_SIZE]
        bn = batch_start // BATCH_SIZE + 1
        tb = (total + BATCH_SIZE - 1) // BATCH_SIZE
        log(f"\nBatch {bn}/{tb}")

        batch_data = []
        for fp in batch:
            text = fp.read_text(encoding="utf-8")
            fm, body = parse_fm(text)
            if not fm:
                log(f"  SKIP {fp.name} - no frontmatter")
                continue
            batch_data.append((fp, fm, body))

        if not batch_data:
            continue

        results = translate_batch(batch_data, api_key)
        if not results or all(r is None for r in results):
            log(f"  Batch failed entirely")
            errors += len(batch_data)
            continue

        for i, result in enumerate(results):
            if result is None:
                log(f"  ERROR {batch_data[i][0].name} - no result")
                errors += 1
                continue
            fp, fm, _ = batch_data[i]
            new_title, new_body = result
            fm["title"] = new_title
            new_text = rebuild_fm(fm) + "\n" + new_body
            leftover = len(re.findall(r"[\uac00-\ud7af\u1100-\u11ff\u3130-\u318f]", new_body))
            fp.write_text(new_text, encoding="utf-8")
            if leftover > 0:
                log(f"  WARN {fp.name} - {leftover} Korean chars remain")
            else:
                log(f"  OK   {fp.name}")
            translated += 1

        if bn < tb:
            time.sleep(1)

    log(f"\nDONE! Translated: {translated}, Errors: {errors}")

if __name__ == "__main__":
    main()