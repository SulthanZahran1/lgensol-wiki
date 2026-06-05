#!/usr/bin/env python3
"""Clean up ugly URL-encoded Korean filenames from wiki page bodies."""
import os, re, glob

wiki_dir = os.path.expanduser('~/lgensol-wiki/wiki')

pages_cleaned = 0
total_changes = 0

for fpath in sorted(glob.glob(os.path.join(wiki_dir, '**/*.md'), recursive=True)):
    with open(fpath, 'r') as f:
        content = f.read()

    original = content

    # Pattern 1: "The most relevant raw posts selected for this page include `...`, `...`, and `...`."
    # Replace with a clean version without ugly filenames
    content = re.sub(
        r' The most relevant raw posts selected for this page include `[^`]+`(?:, `[^`]+`)*(?:, and `[^`]+`)?\.',
        '',
        content
    )

    # Pattern 2: "The source set includes `...`, `...`, and `...`."
    content = re.sub(
        r' The source set includes `[^`]+`(?:, `[^`]+`)*(?:, and `[^`]+`)?\.',
        '',
        content
    )

    # Pattern 3: standalone backtick reference with %-encoded chars in body (not frontmatter)
    # Split frontmatter from body
    parts = content.split('---\n', 2)
    if len(parts) == 3:
        frontmatter = parts[0] + '---\n' + parts[1] + '---\n'
        body = parts[2]
        # Remove any remaining backtick-enclosed text that has % in body
        body = re.sub(r'`[^`]*%[^`]*`', '', body)
        # Clean up double spaces, trailing spaces
        body = re.sub(r'  +', ' ', body)
        body = re.sub(r'\.\.', '.', body)
        content = frontmatter + body
    else:
        # No frontmatter, clean whole file
        content = re.sub(r'`[^`]*%[^`]*`', '', content)
        content = re.sub(r'  +', ' ', content)

    if content != original:
        pages_cleaned += 1
        # Count changes
        changes = sum(1 for a, b in zip(original, content) if a != b)
        total_changes += changes
        with open(fpath, 'w') as f:
            f.write(content)

print(f"Cleaned: {pages_cleaned} pages, ~{total_changes} chars changed")