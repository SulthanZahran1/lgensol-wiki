#!/usr/bin/env python3
"""Expand wiki pages to 2-3 minute reading depth via LLM API."""
import json, os, re, sys, time, urllib.request, urllib.error

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

def call_llm(messages, max_tokens=4096):
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
            result = json.loads(resp.read())
            return result["choices"][0]["message"]["content"]
    except Exception as e:
        print("  API error: " + str(e), flush=True)
        return None

def read_file(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        print("  Read error: " + str(e), flush=True)
        return None

def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

def parse_frontmatter(content):
    m = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
    if m:
        return m.group(1), content[m.end():]
    return "", content

def get_source_content(source_path):
    full_path = os.path.join(WORKDIR, source_path)
    content = read_file(full_path)
    if content is None:
        return None
    _, body = parse_frontmatter(content)
    return body.strip()

def expand_page(page_path):
    content = read_file(page_path)
    if not content:
        return False

    frontmatter_str, body = parse_frontmatter(content)
    source_paths = re.findall(r'^  - (raw/.+)$', frontmatter_str, re.MULTILINE)

    sources_text = ""
    for sp in source_paths:
        sp = sp.strip()
        src = get_source_content(sp)
        if src:
            sources_text = sources_text + "\n### Source: " + sp + "\n" + src[:3000] + "\n"

    page_type = "wiki"
    pt_match = re.search(r'type: (\w+)', frontmatter_str)
    if pt_match:
        page_type = pt_match.group(1)

    if not sources_text:
        print("  (no sources found, writing from domain knowledge)", flush=True)
        prompt = """Create a substantive 2-3 minute wiki page for the LG Energy Solution Battery Wiki (""" + page_type + """ page).

---frontmatter---
""" + frontmatter_str + """

Write substantive content based on battery domain knowledge about this topic.

INSTRUCTIONS:
1. Keep frontmatter, only change 'updated' to """ + TODAY + """.
2. Write ~500-1000 words of substantive content.
3. Use ## sections: Overview, Technical Details, Significance, Related.
4. Include specific technical data, mechanisms, and processes.
5. Maintain 3-5+ [[wikilinks]].
6. Keep English throughout.
7. Output complete .md file (frontmatter + body)."""
    else:
        prompt = """Expand this wiki page for the LG Energy Solution Battery Wiki to 2-3 minutes reading depth.

Current page:
---frontmatter---
""" + frontmatter_str + """
---body---
""" + body + """

Raw source material from LG Energy Solution's official blog:
""" + sources_text + """

INSTRUCTIONS:
1. Keep frontmatter, only change 'updated' to """ + TODAY + """.
2. Rewrite body to ~500-1000 words of substantive content. Extract technical depth from sources.
3. Use ## sections: Overview/Introduction, Technical Details, Significance/LG Context, Related.
4. Include specific data, numbers, mechanisms, processes from source material.
5. Maintain 3-5+ [[wikilinks]] to related pages.
6. Keep English throughout.
7. Output ONLY the complete .md file (frontmatter + body)."""

    messages = [
        {"role": "system", "content": "You are a battery technology wiki author. Write substantive, technically accurate pages at 2-3 minute reading depth. Write in English."},
        {"role": "user", "content": prompt}
    ]

    result = call_llm(messages)
    if not result:
        return False

    result = result.strip()
    if result.startswith("```"):
        result = re.sub(r'^```(?:markdown)?\n?', '', result)
        result = re.sub(r'\n?```$', '', result)

    if not result.startswith("---"):
        result = "---\n" + frontmatter_str + "\n---\n" + result

    result = re.sub(r'^updated: .*$', 'updated: ' + TODAY, result, count=1, flags=re.MULTILINE)
    write_file(page_path, result)
    return True

def main():
    pages = sys.argv[1:] if len(sys.argv) > 1 else []
    if not pages:
        print("Usage: python3 expand_pages.py <page1> [page2 ...]")
        sys.exit(1)

    success, fail = 0, 0
    for i, page in enumerate(pages):
        full = page
        if not os.path.isabs(page) and not page.startswith("/"):
            full = os.path.join(WORKDIR, page)
        rel = os.path.relpath(full, WORKDIR)
        print("[" + str(i+1) + "/" + str(len(pages)) + "] " + rel + "...", end=" ", flush=True)

        if expand_page(full):
            print("OK", flush=True)
            success += 1
        else:
            print("FAIL", flush=True)
            fail += 1

    print("\nDone: " + str(success) + " expanded, " + str(fail) + " failed", flush=True)

if __name__ == "__main__":
    main()
