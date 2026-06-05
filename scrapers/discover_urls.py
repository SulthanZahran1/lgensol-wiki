#!/usr/bin/env python3.10
"""
Fase 1: Discover all article URLs from inside.lgensol.com (Korean)
Uses WordPress REST API — much cleaner than HTML pagination.
Output: JSON with all discovered articles + metadata.
"""

import json
import time
from pathlib import Path

import requests

API_BASE = "https://inside.lgensol.com/wp-json/wp/v2"
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
PER_PAGE = 100  # Max allowed by WP REST API

OUTPUT_DIR = Path("/home/dev/battery-inside-wiki")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Known category mapping (from REST API inspection)
CATEGORY_MAP = {
    3: "news",
    4: "tech",
    6: "opinion",
    2016: "story",
    2017: "interview",
    2018: "interview",
    2019: "about-us",
    1: "uncategorized",
}

# Category name normalization
CATEGORY_NAMES = {
    4: "tech",
    3: "news",
    2018: "story",     # Interview → story
    2016: "story",     # Story
    2019: "about-us",
    6: "opinion",
    1: "uncategorized",
}


def fetch_all_posts():
    """Fetch all Korean posts via WP REST API pagination."""
    # First, get total count
    resp = requests.get(
        f"{API_BASE}/posts?per_page=1",
        headers=HEADERS,
        timeout=15,
    )
    total = int(resp.headers.get("X-WP-Total", 0))
    total_pages = (total + PER_PAGE - 1) // PER_PAGE
    print(f"Total posts: {total}")
    print(f"Pages (at {PER_PAGE}/page): {total_pages}")
    print()

    all_posts = []

    for page in range(1, total_pages + 1):
        url = f"{API_BASE}/posts?per_page={PER_PAGE}&page={page}&_fields=id,title,link,date,modified,categories,tags,excerpt,content,_links"
        print(f"  Fetching page {page}/{total_pages}...")

        resp = requests.get(url, headers=HEADERS, timeout=30)
        if resp.status_code != 200:
            print(f"  [FAIL] Page {page}: HTTP {resp.status_code}")
            continue

        posts = resp.json()
        all_posts.extend(posts)
        print(f"  Got {len(posts)} posts (total: {len(all_posts)})")

        # Rate limiting
        if page < total_pages:
            time.sleep(0.5)

    return all_posts


def extract_article_data(posts):
    """Extract clean metadata from raw WP posts."""
    articles = []
    for p in posts:
        # Get category name
        cats = p.get("categories", [])
        cat_name = "uncategorized"
        for cid in cats:
            if cid in CATEGORY_NAMES:
                cat_name = CATEGORY_NAMES[cid]
                break

        # Clean title (strip HTML entities)
        title = p["title"]["rendered"]
        # Clean excerpt (strip HTML)
        excerpt = p.get("excerpt", {}).get("rendered", "")
        # Clean content (strip HTML for size estimate)
        content = p.get("content", {}).get("rendered", "")

        articles.append({
            "id": p["id"],
            "title": title,
            "url": p["link"],
            "date": p.get("date", ""),
            "modified": p.get("modified", ""),
            "category": cat_name,
            "category_ids": cats,
            "tags": p.get("tags", []),
            "excerpt_len": len(excerpt),
            "content_len": len(content),
        })

    return articles


def main():
    print("=" * 60)
    print("BATTERY INSIDE — URL Discovery (Korean)")
    print("Source: WordPress REST API")
    print("=" * 60)

    # Fetch all posts
    raw_posts = fetch_all_posts()

    if not raw_posts:
        print("\n[FAIL] No posts fetched!")
        return

    print(f"\nFetched {len(raw_posts)} posts total")

    # Extract metadata
    articles = extract_article_data(raw_posts)

    # Calculate size statistics
    total_content_bytes = sum(a["content_len"] for a in articles)
    total_excerpt_bytes = sum(a["excerpt_len"] for a in articles)
    avg_content = total_content_bytes / len(articles) if articles else 0

    # Count by category
    cat_counts = {}
    for a in articles:
        cat = a["category"]
        cat_counts[cat] = cat_counts.get(cat, 0) + 1

    # Save
    output = {
        "total_articles": len(articles),
        "total_content_bytes": total_content_bytes,
        "total_excerpt_bytes": total_excerpt_bytes,
        "avg_content_bytes_per_article": round(avg_content, 0),
        "estimated_plaintext_mb": round(total_content_bytes / 1024 / 1024, 1),
        "categories": cat_counts,
        "articles": articles,
    }

    output_path = OUTPUT_DIR / "discovered_urls.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print(f"\n{'='*60}")
    print(f"DISCOVERY COMPLETE")
    print(f"{'='*60}")
    for cat, count in sorted(cat_counts.items(), key=lambda x: -x[1]):
        print(f"  {cat}: {count} articles")
    print(f"  TOTAL: {len(articles)} articles")
    print(f"  Total HTML content: ~{total_content_bytes / 1024 / 1024:.1f} MB")
    print(f"  Estimated plaintext after strip: ~{output['estimated_plaintext_mb']} MB")
    print(f"\nSaved to: {output_path}")


if __name__ == "__main__":
    main()