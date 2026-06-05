#!/usr/bin/env python3
"""EMERGENCY RECOVERY — regenerate wiki page bodies from raw Korean articles.
Each wiki file still has English frontmatter (title, sources). We read the raw
Korean articles listed in sources: and regenerate the English body via Ollama.

CRITICAL: writes to .recovered/ first for verification, not in-place.
"""
import os, re, sys, json, time
from pathlib import Path
import requests

WIKI_DIR = Path("/home/dev/lgensol-wiki/wiki")
RAW_DIR = Path("/home/dev/lgensol-wiki/raw/ko")
OUT_DIR = Path("/home/dev/lgensol-wiki/wiki_recovered")
API_URL = "https://ollama.com/v1/chat/completions"
MODEL = "deepseek-v4-flash:cloud"
LOG_FILE = Path("/home/dev/lgensol-wiki/scripts/recovery_log.txt")
BATCH_SIZE = 1  # 1 file at a time for safety

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
            if line.startswith("OLLAMA_API_KEY=***                key = line.split("=", 1)[1].strip().strip("\"'")
    return key

def parse_fm(text):
    m = re.match(r"^---\n(.*?)\n---\n(.*)", text, re.DOTALL)
    if not m:
        return {}, text
    fm = {}
    sources = []
    for line in m.group(1).splitlines():
        if line.startswith("  - "):
            sources.append(line.strip()[4:])
        elif ":" in line:
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip()
    if sources:
        fm["_sources"] = sources
    return fm, m.group(2)

def rebuild_fm(fm):
    lines = ["---"]
    for k, v in fm.items():
        if k.startswith("_"):
            continue
        lines.append(f"{k}: {v}")
    if "_sources" in fm:
        lines.append("sources:")
        for s in fm["_sources"]:
            lines.append(f"  - {s}")
    lines.append("---")
    return "\n".join(lines)

def read_raw(source_path):
    fp = RAW_DIR / source_path
    if not fp.exists():
        # Try relative from project root
        fp2 = Path("/home/dev/lgensol-wiki") / source_path
        if fp2.exists():
            fp = fp2
        else:
            log(f"  WARN source not found: {source_path}")
            return None
    text = fp.read_text(encoding="utf-8")
    # Strip frontmatter for content
    m = re.match(r"^---\n.*?\n---\n(.*)", text, re.DOTALL)
    if m:
        return m.group(1).strip()
    return text.strip()

def generate_body(fm, raw_content, api_key):
    title = fm.get("title", "Untitled")
    ptype = fm.get("type", "page")
    tags = fm.get("tags", "")

    prompt = f"""You are a battery technology wiki author. Write an English wiki page based on the following Korean source material.

PAGE INFO:
- Title: {title}
- Type: {ptype}
- Tags: {tags}

RULES:
1. Write in natural English — this is an encyclopedia entry
2. Structure with ## headers and bullet points
3. Use [[wikilinks]] for related technical terms (e.g. [[cathode-materials]], [[electrolyte]], [[separator]])
4. Include at least 3-5 [[wikilinks]] to related pages
5. Be factual and concise (200-800 words)
6. Do NOT wrap the response in markdown code blocks — just raw markdown

KOREAN SOURCE:
{raw_content[:5000]}

Write the body content only (NOT the frontmatter):"""

    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"}
    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": "You write battery technology wiki pages in English. Output raw markdown only."},
            {"role": "user", "content": prompt}
        ],
        "stream": False,
        "temperature": 0.3,
    }

    for attempt in range(3):
        try:
            resp = requests.post(API_URL, json=payload, headers=headers, timeout=120)
            if resp.status_code == 200:
                content = resp.json()["choices"][0]["message"]["content"]
                # Strip any code block wrapping
                content = re.sub(r"^```.*?\n", "", content.strip())
                content = re.sub(r"\n```$", "", content.strip())
                if len(content) > 50:
                    return content
                log(f"  WARN short body ({len(content)} chars)")
                return content
            elif resp.status_code == 429:
                log("  Rate limit, waiting...")
                time.sleep(15)
            else:
                log(f"  API {resp.status_code}")
                time.sleep(5)
        except Exception as e:
            log(f"  Error: {e}")
            time.sleep(5)
    return None

def main():
    api_key = get_api_key()
    if not api_key:
        log("ERROR: No API key")
        return

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    # Collect all wiki files
    files = sorted(WIKI_DIR.glob("**/*.md"))
    files = [f for f in files if f.name not in SKIP and "raw" not in str(f)]
    total = len(files)
    log(f"Recovering {total} files")

    recovered = 0
    errors = 0

    for i, fp in enumerate(files):
        text = fp.read_text(encoding="utf-8")
        fm, _ = parse_fm(text)
        if not fm:
            log(f"SKIP {fp.name} no FM")
            continue

        sources = fm.get("_sources", [])
        if not sources:
            log(f"SKIP {fp.name} no sources")
            continue

        # Read raw Korean content
        all_raw = []
        for src in sources[:3]:  # max 3 sources
            r = read_raw(src)
            if r:
                all_raw.append(r)
        if not all_raw:
            log(f"SKIP {fp.name} no raw content found")
            continue
        raw_content = "\n\n---\n\n".join(all_raw)

        log(f"[{i+1}/{total}] {fp.name}")
        body = generate_body(fm, raw_content, api_key)
        if not body:
            log(f"  FAILED {fp.name}")
            errors += 1
            continue

        # Write to recovery dir
        out_fp = OUT_DIR / fp.name
        new_text = rebuild_fm(fm) + "\n" + body
        out_fp.write_text(new_text, encoding="utf-8")

        # Verify
        m = re.match(r"^---\n.*?\n---\n(.*)", new_text, re.DOTALL)
        if m and len(m.group(1).strip()) > 100:
            wikilinks = len(re.findall(r"\[\[(.+?)\]\]", new_text))
            log(f"  OK body={len(m.group(1))}ch wikilinks={wikilinks}")
            recovered += 1
        else:
            log(f"  VERIFY FAIL body={len(m.group(1)) if m else 0}")
            errors += 1

        if i < total - 1:
            time.sleep(1)

    log(f"\nDONE! Recovered: {recovered}, Errors: {errors}")
    log(f"Files in: {OUT_DIR}")
    log(f"Run: cp -r wiki_recovered/*.md wiki/ to apply")

if __name__ == "__main__":
    main()