#!/usr/bin/env python3
"""Regenerate wiki/index.md and wiki/log.md with English titles from frontmatter."""
import os, re
from pathlib import Path

WIKI_DIR = Path("/home/dev/lgensol-wiki/wiki")
SKIP = {"SCHEMA.md", "log.md", "index.md", "README.md"}

TYPE_LABELS = {
    "entity": "Entities",
    "concept": "Concepts",
    "comparison": "Comparisons",
    "glossary": "Glossary",
    "meta": "Meta",
}

def extract_fm(fp):
    text = fp.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n(.*)", text, re.DOTALL)
    if not m:
        return {}, "", ""
    fm = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip()
    body = m.group(2)
    # Extract first 100 chars of body for description
    desc = re.sub(r"#.*?\n", "", body)[:200].strip()
    desc = re.sub(r"\s+", " ", desc)
    return fm, body, desc

# Collect by type
by_type = {}
for fp in sorted(WIKI_DIR.glob("**/*.md")):
    if fp.name in SKIP:
        continue
    rel = fp.relative_to(WIKI_DIR)
    fm, _, desc = extract_fm(fp)
    t = fm.get("type", "unknown")
    by_type.setdefault(t, []).append({
        "slug": fp.stem,
        "title": fm.get("title", fp.stem),
        "desc": desc,
    })

# Build index.md
lines = ["---", "title: Index", "created: 2026-06-05", "updated: 2026-06-05", "type: meta", "tags: [meta]", "---", ""]
lines.append("# Index — LG Energy Solution Battery Wiki")
lines.append("")
lines.append("Compiled from 556 Korean blog posts into **95 wiki pages in English**. See [[SCHEMA]] for authoring rules, [[log]] for work log.")
lines.append("")
lines.append("| Category | Count |")
lines.append("|---|---|")

total = 0
for t in ["entity", "concept", "comparison", "glossary", "meta"]:
    items = by_type.get(t, [])
    if items:
        count = len(items)
        label = TYPE_LABELS.get(t, t)
        lines.append(f"| {label} | {count} |")
        total += count
lines.append(f"| **Total** | **{total}** |")
lines.append("")

for t in ["entity", "concept", "comparison", "glossary"]:
    items = by_type.get(t, [])
    if not items:
        continue
    label = TYPE_LABELS.get(t, t)
    lines.append(f"## {label}  ({len(items)})")
    lines.append("")
    items.sort(key=lambda x: x["slug"])
    for item in items:
        slug = item["slug"]
        title = item["title"]
        desc = item["desc"]
        if desc:
            lines.append(f"- [[{slug}|{title}]] — {desc}")
        else:
            lines.append(f"- [[{slug}|{title}]]")
    lines.append("")

(WIKI_DIR / "index.md").write_text("\n".join(lines), encoding="utf-8")
print(f"index.md written — {len(lines)} lines")

# Build log.md
log_lines = ["---", "title: Work Log", "created: 2026-06-05", "updated: 2026-06-05", "type: meta", "tags: [meta]", "---", "", "# Work Log — Phase 3 Wiki Compilation", "", "See [[SCHEMA]] for authoring rules, [[index]] for full index.", "", "## 2026-06-05 — Phase 3 Initial Compilation", "", f"**Input:** `raw/ko/` 556 posts (tech 146 · news 237 · story 66 · about-us 50 · uncategorized 43 · opinion 14).", "", f"**Output:** `wiki/` {total} pages + SCHEMA · index · log.", "", "### Steps", "1. **Metadata collection** — Catalog from 556 post frontmatters (title/date/category).", "2. **Series identification** — Mapped blog series to wiki categories.", "3. **Content extraction** — Cleaned body text, grouped by topic.", f"4. **Page creation** — {total} pages created in 4 categories.", "5. **Verification & editing** — Wikilink integrity, source path correction.", "", "## 2026-06-05 — Phase 4 English Translation", "", f"- Translated all {total} pages from Korean to English via Ollama Cloud API (deepseek-v4-flash:cloud).", "- Updated SCHEMA.md, index.md, log.md to English.", "- Frontend adjustments: graph colors, show/hide toggle, chat prompt.", "", "Related: [[index]] · [[SCHEMA]]"]
(WIKI_DIR / "log.md").write_text("\n".join(log_lines), encoding="utf-8")
print(f"log.md written — {len(log_lines)} lines")