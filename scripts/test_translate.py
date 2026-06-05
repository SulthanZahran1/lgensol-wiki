#!/usr/bin/env python3
"""Test translation on one short file."""
import os, re, json, requests, time
from pathlib import Path

key = os.environ.get("OLLAMA_API_KEY")
env_path = Path.home() / ".hermes" / ".env"
if not key and env_path.exists():
    for line in env_path.read_text().splitlines():
        if line.startswith("OLLAMA_API_KEY="):
            key = line.split("=", 1)[1].strip().strip("\"'")
            break

print(f"Key found: {bool(key)}, length: {len(key) if key else 0}")

fp = Path("wiki/glossary/soc.md")
text = fp.read_text(encoding="utf-8")
m = re.match(r"^---\n(.*?)\n---\n(.*)", text, re.DOTALL)
fm = {}
for line in m.group(1).splitlines():
    if ":" in line:
        k, v = line.split(":", 1)
        fm[k.strip()] = v.strip()
body = m.group(2)

input_text = f"--- FILE 0 ---\nTitle: {fm.get('title', 'Untitled')}\nBody:\n{body}\n\n"
system = "You are a Korean→English translator. Translate to natural English. Preserve ALL [[wikilinks]] and ^[citations] and markdown EXACTLY. Translate the Title field too. Output format: --- RESULT 0 ---\nTitle: <translated title>\nBody:\n<translated body>"

resp = requests.post("https://ollama.com/v1/chat/completions", json={
    "model": "deepseek-v4-flash:cloud",
    "messages": [
        {"role": "system", "content": system},
        {"role": "user", "content": input_text}
    ],
    "stream": False
}, headers={
    "Content-Type": "application/json",
    "Authorization": f"Bearer {key}"
}, timeout=30)

print(f"Status: {resp.status_code}")
data = resp.json()
content = data["choices"][0]["message"]["content"]
print("Response:")
print(content[:800])