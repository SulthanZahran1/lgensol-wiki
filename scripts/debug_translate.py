#!/usr/bin/env python3
"""Debug: check why Korean detection fails in batches."""
import os, re
from pathlib import Path

WIKI_DIR = Path("/home/dev/lgensol-wiki/wiki")
SKIP = {"SCHEMA.md", "log.md", "index.md", "README.md"}

files = []
for root, dirs, fnames in os.walk(WIKI_DIR):
    for f in fnames:
        if f.endswith(".md") and f not in SKIP and not f.startswith("_"):
            files.append(Path(root) / f)
files.sort()

# Check a few files
for fp in files[:10]:
    text = fp.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n(.*)", text, re.DOTALL)
    has_fm = bool(m)
    if m:
        body = m.group(2)
        k = len(re.findall(r"[\uac00-\ud7af\u1100-\u11ff\u3130-\u318f]", body))
    else:
        body = text
        k = len(re.findall(r"[\uac00-\ud7af\u1100-\u11ff\u3130-\u318f]", body))
    print(f"{fp.name:40s} FM={has_fm} Korean={k} size={len(text):6d}")