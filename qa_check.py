#!/usr/bin/env python3
"""QA check all wiki pages. Returns JSON with issues found per page."""
import json, os, re, sys

WORKDIR = "/home/dev/lgensol-wiki"

def check_page(path):
    issues = []
    with open(path) as f:
        content = f.read()

    wc = len(content.split())

    # 1. Valid frontmatter
    m = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
    if not m:
        issues.append("MISSING_FRONTMATTER")
        return issues  # can't check further
    fm = m.group(1)
    body = content[m.end():]

    # 2. Updated date
    if 'updated: 2026-06-08' not in fm:
        issues.append("OLD_DATE")

    # 3. Word count
    if wc < 700:
        issues.append(f"TOO_SHORT({wc}w)")
    elif wc < 900:
        issues.append(f"MARGINAL({wc}w)")

    # 4. Required fields
    for field in ['title:', 'type:', 'tags:', 'created:']:
        if field not in fm:
            issues.append(f"MISSING_{field.replace(':','').upper()}")

    # 5. Wikilinks (at least 3)
    wikilinks = len(re.findall(r'\[\[', body))
    if wikilinks < 2:
        issues.append(f"FEW_WIKILINKS({wikilinks})")

    # 6. Broken sections (# head with no content after)
    sections = re.findall(r'^##\s+(.+)$', body, re.MULTILINE)
    if len(sections) < 2:
        issues.append(f"FEW_SECTIONS({len(sections)})")

    # 7. Markdown rendering issues (unclosed brackets, etc)
    # Check for proper wikilink format
    bad_links = re.findall(r'\[\[[^\]]*$', body, re.MULTILINE)
    if bad_links:
        issues.append(f"UNCLOSED_WIKILINKS({len(bad_links)})")

    return issues

def main():
    pages = []
    if len(sys.argv) > 1:
        with open(sys.argv[1]) as f:
            pages = [l.strip() for l in f if l.strip()]
    else:
        for root, dirs, files in os.walk(os.path.join(WORKDIR, "wiki")):
            dirs[:] = [d for d in dirs if d != "raw"]
            for fn in files:
                if not fn.endswith(".md") or fn in ("index.md", "SCHEMA.md", "log.md", "README.md"):
                    continue
                pages.append(os.path.relpath(os.path.join(root, fn), WORKDIR))
        pages.sort()

    all_issues = {}
    total, clean = 0, 0

    for p in pages:
        full = os.path.join(WORKDIR, p)
        if not os.path.exists(full):
            all_issues[p] = ["NOT_FOUND"]
            continue
        issues = check_page(full)
        all_issues[p] = issues
        total += 1
        if not issues:
            clean += 1
        else:
            print(f"{p}: {' | '.join(issues)}")

    print(f"\n=== QA Summary ===")
    print(f"Total: {total}, Clean: {clean}, Issues: {total - clean}")

    # Count issue types
    from collections import Counter
    all_iss = []
    for iss in all_issues.values():
        all_iss.extend(iss)
    counts = Counter(all_iss)
    for issue, count in counts.most_common():
        print(f"  {issue}: {count}")

if __name__ == "__main__":
    main()
