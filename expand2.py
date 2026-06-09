#!/usr/bin/env python3
"""Force-expand pages to 600+ words."""
import json, os, re, sys, urllib.request, urllib.error

WORKDIR = "/home/dev/lgensol-wiki"

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
        "temperature": 0.4,
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

def rewrite_page(page_path, current_words):
    full = os.path.join(WORKDIR, page_path)
    with open(full) as f:
        content = f.read()

    m = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
    if not m:
        print("  no frontmatter", flush=True)
        return False

    fm = m.group(1)
    body = content[m.end():]

    prompt = "EXPAND this currently " + str(current_words) + "-word wiki page to 700-1000 words.\n\n"
    prompt += "Current frontmatter (keep unchanged, only update 'updated' to 2026-06-06):\n"
    prompt += fm + "\n\n"
    prompt += "Current body:\n" + body.strip() + "\n\n"
    prompt += "INSTRUCTIONS:\n"
    prompt += "This is an LG Energy Solution Battery Wiki page.\n"
    prompt += "1. Keep frontmatter EXACTLY as shown, only change 'updated' to 2026-06-06.\n"
    prompt += "2. Expand body to 700-1000 words of substantive content.\n"
    prompt += "3. Write from general battery industry knowledge. Include specific numbers, specs, mechanisms.\n"
    prompt += "4. Use sections: Overview, Technical Details, Market Significance, Related Pages.\n"
    prompt += "5. Maintain 3-5+ [[wikilinks]] to related pages.\n"
    prompt += "6. Write in English only.\n"
    prompt += "7. Output ONLY the complete rewritten .md file (frontmatter + body)."

    messages = [
        {"role": "system", "content": "You are a battery technology wiki author. Write substantive pages at 700-1000 words."},
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
        result = "---\n" + fm + "\n---\n" + result

    result = re.sub(r'^updated: .*$', 'updated: 2026-06-06', result, count=1, flags=re.MULTILINE)

    wc = len(result.split())
    print("  rewrote from " + str(current_words) + " to " + str(wc) + " words", flush=True)

    if wc < 400:
        print("  still too short", flush=True)
        return False

    with open(full, 'w') as f:
        f.write(result)
    return True

def main():
    pages = []
    with open(sys.argv[1]) as f:
        pages = [l.strip() for l in f if l.strip()]

    success, fail = 0, 0
    for i, page in enumerate(pages):
        full = os.path.join(WORKDIR, page)
        with open(full) as f:
            wc = len(f.read().split())
        print("[" + str(i+1) + "/" + str(len(pages)) + "] " + page + " (" + str(wc) + "w)...", end=" ", flush=True)
        if rewrite_page(page, wc):
            success += 1
        else:
            fail += 1
    print("\nDone: " + str(success) + " expanded, " + str(fail) + " failed", flush=True)

if __name__ == "__main__":
    main()
