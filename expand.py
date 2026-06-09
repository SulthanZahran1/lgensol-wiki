#!/usr/bin/env python3
"""Expand wiki pages to 2-3 minute reading depth via LLM API."""
import json, os, re, sys, urllib.request, urllib.error

WORKDIR = "/home/dev/lgensol-wiki"
TODAY = "2026-06-08"

def get_api_key():
    with open("/home/dev/.hermes/profiles/whatsapp/.env") as f:
        for line in f:
            line = line.strip()
            if line.startswith("OLLAMA_API_KEY"):
                parts = line.split("=", 1)
                if len(parts) > 1:
                    return parts[1]
    return ""

API_KEY = get_api_key()
API_URL = "https://ollama.com/v1/chat/completions"

def call_llm(messages, max_tokens=5000):
    data = json.dumps({
        "model": "deepseek-v4-flash",
        "messages": messages,
        "max_tokens": max_tokens,
        "temperature": 0.3,
    }).encode()
    req = urllib.request.Request(
        API_URL, data=data,
        headers={"Content-Type": "application/json", "Authorization": "Bearer " + API_KEY},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=180) as resp:
            return json.loads(resp.read())["choices"][0]["message"]["content"]
    except Exception as e:
        print("  API error: " + str(e), flush=True)
        return None

def read_file(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        print("  Read error " + path + ": " + str(e), flush=True)
        return None

def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

def get_body_plus_source(page_path):
    content = read_file(page_path)
    if not content:
        return None, None, None
    m = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
    if not m:
        return None, None, None
    fm_yaml = m.group(1)
    body = content[m.end():]
    source_paths = re.findall(r'^  - (raw/.+)$', fm_yaml, re.MULTILINE)
    sources_text = ""
    for sp in source_paths:
        sp = sp.strip()
        full = os.path.join(WORKDIR, sp)
        src = read_file(full)
        if src:
            sm = re.match(r'^---\n.*?\n---\n', src, re.DOTALL)
            if sm:
                src_body = src[sm.end():]
            else:
                src_body = src
            if len(src_body) > 4000:
                src_body = src_body[:4000] + "\n[...truncated]"
            sources_text = sources_text + "\n### " + sp + "\n" + src_body.strip() + "\n"
    return fm_yaml, body.strip(), sources_text

def expand_page(page_path):
    fm_yaml, body, sources_text = get_body_plus_source(page_path)
    if fm_yaml is None:
        print("  Bad frontmatter", flush=True)
        return False

    page_type = "concept"
    pt = re.search(r'type: (\w+)', fm_yaml)
    if pt:
        page_type = pt.group(1)

    if sources_text.strip():
        prompt = """Expand this wiki page for the LG Energy Solution Battery Wiki to 2-3 minutes reading depth (~500-1000 words).

Current page frontmatter (keep unchanged, only update 'updated' to """ + TODAY + """):
""" + fm_yaml + """

Current body:
""" + body + """

Raw source material from LG Energy Solution's official blog:
""" + sources_text + """

INSTRUCTIONS:
1. Keep frontmatter EXACTLY as shown, only change 'updated' to """ + TODAY + """.
2. Rewrite body to ~500-1000 words of substantive, technically rich content.
3. Use ## sections: Overview/Introduction, Technical Details, Significance/LG Context, Related Pages.
4. Include specific numbers, mechanisms, processes from source material.
5. Maintain 3-5+ [[wikilinks]] to related pages.
6. Write in English only.
7. Output ONLY the complete rewritten .md file (frontmatter + body). No commentary."""
    else:
        prompt = """Create a substantive wiki page for the LG Energy Solution Battery Wiki.

Page frontmatter (keep unchanged, only update 'updated' to """ + TODAY + """):
""" + fm_yaml + """

INSTRUCTIONS:
1. Keep frontmatter EXACTLY as shown, only change 'updated' to """ + TODAY + """.
2. Write ~500-1000 words of substantive, technically accurate content about this battery topic.
3. Use ## sections: Overview, Technical Details, Significance in Battery Industry, Related Pages.
4. Include specific data, mechanisms, and processes.
5. Maintain 3-5+ [[wikilinks]].
6. Write in English only.
7. Output ONLY the complete .md file (frontmatter + body)."""

    messages = [
        {"role": "system", "content": "You are a battery technology wiki author. Write substantive, technically accurate pages at 2-3 minute reading depth. Output valid markdown with YAML frontmatter. Write in English."},
        {"role": "user", "content": prompt}
    ]

    result = call_llm(messages)
    if not result:
        return False

    result = result.strip()
    if result.startswith("```"):
        result = re.sub(r'^```(?:markdown|yaml)?\n?', '', result)
        result = re.sub(r'\n?```$', '', result)
        result = result.strip()

    if not result.startswith("---"):
        result = "---\n" + fm_yaml + "\n---\n" + result

    result = re.sub(r'^updated: .*$', 'updated: ' + TODAY, result, count=1, flags=re.MULTILINE)

    word_count = len(result.split())
    if word_count < 300:
        print("  Too short (" + str(word_count) + " words), retrying...", flush=True)
        messages.append({"role": "assistant", "content": result})
        messages.append({"role": "user", "content": "Expand to at least 500-1000 words of substantive content."})
        result2 = call_llm(messages)
        if result2:
            result2 = result2.strip()
            if result2.startswith("```"):
                result2 = re.sub(r'^```(?:markdown|yaml)?\n?', '', result2)
                result2 = re.sub(r'\n?```$', '', result2)
            if result2.startswith("---"):
                result = result2
            else:
                result = "---\n" + fm_yaml + "\n---\n" + result2
            result = re.sub(r'^updated: .*$', 'updated: ' + TODAY, result, count=1, flags=re.MULTILINE)

    write_file(page_path, result)
    return True

def main():
    pages = sys.argv[1:] if len(sys.argv) > 1 else []
    if not pages:
        print("Usage: python3 expand.py wiki/page1.md ...")
        sys.exit(1)
    success, fail = 0, 0
    for i, page in enumerate(pages):
        full = os.path.join(WORKDIR, page) if not page.startswith("/") else page
        rel = os.path.relpath(full, WORKDIR)
        print("[" + str(i+1) + "/" + str(len(pages)) + "] " + rel + "...", end=" ", flush=True)
        if expand_page(full):
            wc = len(open(full).read().split())
            print("OK (" + str(wc) + " words)", flush=True)
            success += 1
        else:
            print("FAIL", flush=True)
            fail += 1
    print("\nDone: " + str(success) + " expanded, " + str(fail) + " failed", flush=True)

if __name__ == "__main__":
    main()
