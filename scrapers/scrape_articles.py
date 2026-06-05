#!/usr/bin/env python3.10
"""
Fase 2: Scrape all Korean articles from inside.lgensol.com
- Extract content → Markdown
- Download all images (featured + inline)
- Resume-able via checkpoint

Usage:
    python3.10 scrapers/scrape_articles.py              # Full run
    python3.10 scrapers/scrape_articles.py --resume      # Resume from checkpoint
    python3.10 scrapers/scrape_articles.py --limit 10    # Test with 10 articles
"""

import argparse
import hashlib
import json
import os
import re
import sys
import time
from pathlib import Path
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup

# ── Config ──────────────────────────────────────────────────────────────

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/131.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
}

BASE_DIR = Path("/home/dev/battery-inside-wiki")
RAW_DIR = BASE_DIR / "raw" / "ko"
ASSETS_DIR = BASE_DIR / "assets" / "ko"
CHECKPOINT_FILE = BASE_DIR / "scrape_checkpoint.json"
CHUNK_SIZE = 8192
REQUEST_DELAY = 1.0       # seconds between requests
MAX_RETRIES = 3

# html2text config
try:
    import html2text
    H2T = html2text.HTML2Text()
    H2T.body_width = 0          # no line wrapping
    H2T.ignore_links = False
    H2T.ignore_images = False
    H2T.ignore_emphasis = False
    H2T.protect_links = True
    H2T.unicode_snob = True
    H2T.skip_internal_links = True
    H2T.images_to_alt = False
    H2T.wrap_links = False
    H2T.mark_code = True
except ImportError:
    H2T = None
    print("[WARN] html2text not installed. Using basic HTML stripping.")
    print("  Install: pip3 install html2text")


# ── Helpers ─────────────────────────────────────────────────────────────

def slugify(text):
    """Create a filesystem-safe slug from title."""
    slug = text.lower()
    slug = re.sub(r'[^a-z0-9가-힣]+', '-', slug)
    slug = slug.strip('-')
    slug = slug[:100]
    return slug or f"post-{hash(text) % 100000}"


def extract_slug_from_url(url):
    """Extract slug from WordPress URL like /2026/06/slug-name/"""
    path = urlparse(url).path.rstrip('/')
    parts = path.split('/')
    return parts[-1] if parts else "untitled"


def sanitize_filename(name):
    """Clean filename for saving images."""
    name = re.sub(r'[^\w\.\-]', '_', name)
    return name[:200]


def fetch_with_retry(url, max_retries=MAX_RETRIES):
    """Fetch URL with retry and backoff."""
    for attempt in range(max_retries):
        try:
            resp = requests.get(url, headers=HEADERS, timeout=30)
            resp.raise_for_status()
            return resp
        except requests.RequestException as e:
            if attempt < max_retries - 1:
                wait = 2 ** attempt
                print(f"    [retry {attempt+1}/{max_retries}] {e} — waiting {wait}s...")
                time.sleep(wait)
            else:
                print(f"    [FAIL] {url}: {e}")
                return None


def get_real_image_url(img):
    """
    Extract the actual image URL from an <img> tag.
    Handles: src, data-src, data-lazy-src, srcset
    """
    # Check for lazy-loaded images
    for attr in ['data-src', 'data-lazy-src', 'data-original']:
        val = img.get(attr)
        if val and not val.startswith('data:'):
            return val

    # Check srcset for a reasonable size
    srcset = img.get('data-srcset') or img.get('srcset') or ''
    if srcset:
        urls = []
        for entry in srcset.split(','):
            parts = entry.strip().split()
            if parts:
                size_val = 9999
                if len(parts) > 1:
                    size_str = parts[1].rstrip('w').rstrip('x')
                    try:
                        size_val = int(size_str)
                    except ValueError:
                        size_val = 9999
                urls.append((parts[0], size_val))
        # Sort by size descending, pick the largest
        urls.sort(key=lambda x: -x[1])
        if urls:
            return urls[0][0]

    # Fall back to src if it's a real image
    src = img.get('src', '')
    if src and not src.startswith('data:'):
        return src

    return None


def download_image(url, dest_path):
    """Download a single image file. Returns (success, bytes_written)."""
    try:
        resp = requests.get(url, headers=HEADERS, timeout=30, stream=True)
        resp.raise_for_status()

        content_type = resp.headers.get('Content-Type', '')
        if 'image' not in content_type:
            return False, 0

        dest_path.parent.mkdir(parents=True, exist_ok=True)

        bytes_written = 0
        with open(dest_path, 'wb') as f:
            for chunk in resp.iter_content(chunk_size=CHUNK_SIZE):
                if chunk:
                    f.write(chunk)
                    bytes_written += len(chunk)

        return True, bytes_written
    except Exception as e:
        print(f"    [IMG FAIL] {url}: {e}")
        return False, 0


# ── Core scraper ────────────────────────────────────────────────────────

def scrape_article(article, force=False):
    """
    Scrape a single article: get HTML, extract content, convert to markdown,
    download images. Returns dict with result metadata.
    """
    url = article["url"]
    art_id = article["id"]
    category = article["category"]
    title = article["title"]
    slug = extract_slug_from_url(url)

    # Paths
    raw_file = RAW_DIR / category / f"{slug}.md"
    asset_dir = ASSETS_DIR / category / slug

    # Skip if already done (unless force)
    if raw_file.exists() and not force:
        return {"status": "skipped", "id": art_id, "slug": slug}

    print(f"  [{art_id}] {title[:60]}...")
    print(f"    URL: {url}")

    # Fetch HTML
    resp = fetch_with_retry(url)
    if not resp:
        return {"status": "failed", "id": art_id, "slug": slug, "error": "fetch failed"}

    soup = BeautifulSoup(resp.text, 'lxml')

    # ── Extract featured image ──
    featured_url = None
    for sel in [
        '.post-thumbnail img',
        '.wp-post-image',
        'img.wp-post-image',
        'article img[class*="wp-image"]',
        'article img[class*="attachment"]',
    ]:
        img = soup.select_one(sel)
        if img:
            featured_url = get_real_image_url(img)
            if featured_url:
                break

    # ── Extract entry content ──
    entry = soup.select_one('.entry-content, .post-content, .elementor-widget-theme-post-content')
    if not entry:
        # Fallback: try to find main article body
        article_tag = soup.find('article')
        if article_tag:
            entry = article_tag
        else:
            entry = soup.select_one('.content-area, #primary, main')

    if not entry:
        print(f"    [WARN] Could not find content area")
        return {"status": "failed", "id": art_id, "slug": slug, "error": "no content"}

    # ── Extract and download inline images ──
    images = []
    for img in entry.find_all('img'):
        img_url = get_real_image_url(img)
        if not img_url:
            continue

        # Only download images hosted on this domain
        if not img_url.startswith('https://inside.lgensol.com'):
            continue

        # Determine filename
        parsed = urlparse(img_url)
        img_path = parsed.path.lstrip('/')
        img_filename = Path(img_path).name or f"img-{len(images)}.jpg"

        # Handle uploaded images: preserve subdir structure
        img_subdir = ""
        if 'wp-content/uploads' in img_path:
            # Use date-based subdir for organization
            date_part = img_path.replace('wp-content/uploads/', '').split('/')
            if len(date_part) >= 2:
                img_subdir = '/'.join(date_part[:-1])  # e.g., 2026/06
                img_filename = date_part[-1]
            else:
                img_filename = '_'.join(date_part)

        local_asset_dir = asset_dir
        if img_subdir:
            local_asset_dir = asset_dir / img_subdir

        local_path = local_asset_dir / sanitize_filename(img_filename)
        asset_rel_path = local_path.relative_to(BASE_DIR)

        # Download if not exists
        if not local_path.exists():
            ok, size = download_image(img_url, local_path)
            if ok:
                images.append({
                    "url": img_url,
                    "path": str(asset_rel_path),
                    "size": size,
                })
                print(f"    [IMG] {img_filename} ({size/1024:.0f} KB)")
            else:
                # Still record the URL reference even if download failed
                images.append({"url": img_url, "path": None, "error": "download failed"})
        else:
            size = local_path.stat().st_size
            images.append({
                "url": img_url,
                "path": str(asset_rel_path),
                "size": size,
                "cached": True,
            })

    # ── Convert content to markdown ──
    content_html = str(entry)

    # Remove script and style tags
    for tag in entry.find_all(['script', 'style', 'nav', 'header', 'footer']):
        tag.decompose()

    # Get the cleaned HTML
    clean_html = str(entry)

    if H2T:
        markdown = H2T.handle(clean_html)
    else:
        # Fallback: basic strip
        text = entry.get_text(separator='\n', strip=True)
        markdown = text

    # Clean up the markdown
    markdown = re.sub(r'\n\s*\n\s*\n+', '\n\n', markdown)  # remove excessive blank lines
    markdown = markdown.strip()

    # ── Build frontmatter ──
    # Compute sha256 of the content
    content_bytes = markdown.encode('utf-8')
    sha256 = hashlib.sha256(content_bytes).hexdigest()

    frontmatter = {
        "source_url": url,
        "wp_id": art_id,
        "title": title,
        "date": article.get("date", ""),
        "modified": article.get("modified", ""),
        "category": category,
        "category_ids": article.get("category_ids", []),
        "tags": article.get("tags", []),
        "ingested": time.strftime("%Y-%m-%d %H:%M:%S"),
        "sha256": sha256,
    }

    # Add featured image reference
    if featured_url:
        frontmatter["featured_image"] = featured_url

    # Build list of image references for frontmatter
    image_refs = []
    for img in images:
        if img.get("path"):
            image_refs.append(str(img["path"]))
    if image_refs:
        frontmatter["images"] = image_refs

    # ── Write markdown file ──
    raw_file.parent.mkdir(parents=True, exist_ok=True)

    # Format frontmatter as YAML
    fm_lines = ["---"]
    for key, value in frontmatter.items():
        if isinstance(value, list):
            items = "\n".join(f"  - {v}" for v in value)
            fm_lines.append(f"{key}:\n{items}")
        elif isinstance(value, dict):
            fm_lines.append(f"{key}:")
            for k, v in value.items():
                fm_lines.append(f"  {k}: {v}")
        else:
            fm_lines.append(f"{key}: {value}")
    fm_lines.append("---")
    fm_lines.append("")
    fm_lines.append(markdown)

    raw_content = "\n".join(fm_lines)

    with open(raw_file, 'w', encoding='utf-8') as f:
        f.write(raw_content)

    content_size = len(raw_content.encode('utf-8'))

    print(f"    [OK] Saved: {raw_file.relative_to(BASE_DIR)} ({content_size/1024:.0f} KB)")

    return {
        "status": "success",
        "id": art_id,
        "slug": slug,
        "content_size": content_size,
        "images": len(images),
        "image_size": sum(i.get("size", 0) for i in images),
    }


def main():
    parser = argparse.ArgumentParser(description="Scrape all Korean articles from Battery Inside")
    parser.add_argument("--resume", action="store_true", help="Resume from checkpoint")
    parser.add_argument("--limit", type=int, default=0, help="Limit articles to process")
    parser.add_argument("--force", action="store_true", help="Re-scrape already done articles")
    parser.add_argument("--delay", type=float, default=REQUEST_DELAY, help=f"Delay between requests (default: {REQUEST_DELAY}s)")
    args = parser.parse_args()

    # Load discovered articles
    discovered_path = BASE_DIR / "discovered_urls.json"
    if not discovered_path.exists():
        print("[FAIL] Run discover_urls.py first!")
        sys.exit(1)

    with open(discovered_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    all_articles = data["articles"]
    total = len(all_articles)
    print(f"Loaded {total} articles from discovered_urls.json")

    # Limit for testing
    if args.limit > 0:
        all_articles = all_articles[:args.limit]
        print(f"Limited to {len(all_articles)} articles")

    # Resume: load checkpoint
    processed_ids = set()
    if args.resume and CHECKPOINT_FILE.exists():
        with open(CHECKPOINT_FILE, 'r', encoding='utf-8') as f:
            checkpoint = json.load(f)
        processed_ids = set(checkpoint.get("completed_ids", []))
        print(f"Resuming from checkpoint — {len(processed_ids)} already completed")

    # ── Run ──
    print(f"\n{'='*60}")
    print(f"SCRAPING {len(all_articles)} ARTICLES")
    print(f"{'='*60}")

    results = {
        "success": 0,
        "skipped": 0,
        "failed": 0,
        "total_content_bytes": 0,
        "total_image_bytes": 0,
        "completed_ids": [],
        "failed_ids": [],
    }

    start_time = time.time()

    for i, article in enumerate(all_articles):
        art_id = article["id"]

        # Skip if already processed (for resume)
        if art_id in processed_ids and not args.force:
            results["skipped"] += 1
            continue

        print(f"\n[{i+1}/{len(all_articles)}] ", end="")

        result = scrape_article(article, force=args.force)

        if result["status"] == "success":
            results["success"] += 1
            results["completed_ids"].append(art_id)
            results["total_content_bytes"] += result.get("content_size", 0)
            results["total_image_bytes"] += result.get("image_size", 0)
        elif result["status"] == "skipped":
            results["skipped"] += 1
            results["completed_ids"].append(art_id)
        else:
            results["failed"] += 1
            results["failed_ids"].append({"id": art_id, "error": result.get("error", "unknown")})
            print(f"    [FAIL] Article {art_id}: {result.get('error', 'unknown')}")

        # Save checkpoint every 10 articles
        if (i + 1) % 10 == 0:
            with open(CHECKPOINT_FILE, 'w', encoding='utf-8') as f:
                json.dump(results, f, ensure_ascii=False, indent=2)

        # Rate limiting
        if i < len(all_articles) - 1:
            time.sleep(args.delay)

    # Final save
    results["elapsed_seconds"] = time.time() - start_time
    with open(CHECKPOINT_FILE, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    # ── Summary ──
    elapsed = time.time() - start_time
    print(f"\n{'='*60}")
    print(f"SCRAPING COMPLETE")
    print(f"{'='*60}")
    print(f"  Success:  {results['success']}")
    print(f"  Skipped:  {results['skipped']}")
    print(f"  Failed:   {results['failed']}")
    print(f"  Text:     {results['total_content_bytes'] / 1024 / 1024:.1f} MB")
    print(f"  Images:   {results['total_image_bytes'] / 1024 / 1024:.1f} MB")
    print(f"  Elapsed:  {elapsed:.0f}s ({elapsed/60:.1f} min)")
    print(f"  Checkpoint: {CHECKPOINT_FILE}")


if __name__ == "__main__":
    main()