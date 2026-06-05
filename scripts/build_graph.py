#!/usr/bin/env python3
"""Rebuild graph.json by scanning all wiki .md files for slug mentions (case-insensitive)."""
import os, re, json
from pathlib import Path

WIKI_DIR = Path("/home/dev/lgensol-wiki/wiki")
OUTPUT = Path("/home/dev/lgensol-wiki/server/data/graph.json")
SKIP = {"SCHEMA.md", "log.md", "index.md", "README.md"}

# 1. Collect all pages
pages = {}  # slug -> {title, type, category, tags, body_text}
for fp in sorted(WIKI_DIR.glob("**/*.md")):
    if fp.name in SKIP:
        continue
    rel = fp.relative_to(WIKI_DIR)
    parts = rel.parts
    if len(parts) < 2:
        continue
    category = parts[0]
    slug = fp.stem
    text = fp.read_text(encoding="utf-8")

    # Parse frontmatter
    fm = {}
    m = re.match(r"^---\n(.*?)\n---\n(.*)", text, re.DOTALL)
    if m:
        for line in m.group(1).splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                fm[k.strip()] = v.strip()
        body = m.group(2)
    else:
        body = text

    title = fm.get("title", slug)
    ptype = fm.get("type", "page")
    tags_raw = fm.get("tags", "[]")
    tags = [t.strip() for t in tags_raw.strip("[]").split(",") if t.strip()]

    # Normalize body for matching
    body_lower = re.sub(r"[^a-z0-9\s\-]+", " ", body.lower())

    pages[slug] = {
        "title": title,
        "type": ptype,
        "category": category,
        "tags": tags,
        "body_lower": body_lower,
        "body_snippet": re.sub(r"\s+", " ", body)[:200],
    }

print(f"Loaded {len(pages)} pages")

# 2. Build links by scanning for slug mentions
all_slugs = list(pages.keys())
slug_variants = {}
for s in all_slugs:
    # Normalize: remove hyphens for matching
    n = s.replace("-", " ").replace("_", " ")
    slug_variants.setdefault(n, []).append(s)
    # Also try partial matches (e.g. "lfp" in "lfp-battery")
    for part in s.split("-"):
        if len(part) > 2:
            slug_variants.setdefault(part, []).append(s)

# Score matching: for each page, check how many times other page slugs appear
links = []  # {source, target}
seen_pairs = set()

for source_slug, src_data in pages.items():
    body = src_data["body_lower"]
    matched = set()
    for target_slug in all_slugs:
        if target_slug == source_slug:
            continue
        # Try matching the slug words in the body
        words = target_slug.replace("-", " ").split()
        score = 0
        for w in words:
            if len(w) <= 2:
                continue
            # Count occurrences
            occurrences = body.count(" " + w + " ")
            score += occurrences * 2
            # Also check if the full title appears
            target_title = pages[target_slug]["title"].lower()
            if target_title in body:
                score += 5
        if score >= 3:
            pair = (source_slug, target_slug)
            if pair not in seen_pairs:
                seen_pairs.add(pair)
                links.append({"source": source_slug, "target": target_slug})
                matched.add(target_slug)

print(f"Found {len(links)} links")

# 3. Write graph.json
nodes = []
for slug, data in pages.items():
    nodes.append({
        "slug": slug,
        "title": data["title"],
        "type": data["type"],
        "category": data["category"],
        "tags": data["tags"],
        "summary": data["body_snippet"],
    })

graph = {"nodes": nodes, "links": links}
OUTPUT.parent.mkdir(exist_ok=True)
with open(OUTPUT, "w") as f:
    json.dump(graph, f, indent=2, ensure_ascii=False)

print(f"Written: {len(nodes)} nodes, {len(links)} links -> {OUTPUT}")

# 4. Verify
print(f"\nVerification:")
# Show top linked pages
link_count = {}
for l in links:
    link_count[l["source"]] = link_count.get(l["source"], 0) + 1
    link_count[l["target"]] = link_count.get(l["target"], 0) + 1
top = sorted(link_count.items(), key=lambda x: -x[1])[:10]
for slug, count in top:
    print(f"  {slug}: {count} links")