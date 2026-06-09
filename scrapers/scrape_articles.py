#!/usr/bin/env python3
"""Scrape discovered LG Energy Solution source records into raw markdown."""
from __future__ import annotations

import argparse
import concurrent.futures
import hashlib
import json
import re
import shutil
import subprocess
import sys
import tempfile
import threading
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup

try:
    import html2text

    H2T = html2text.HTML2Text()
    H2T.body_width = 0
    H2T.ignore_links = False
    H2T.ignore_images = False
    H2T.ignore_emphasis = False
    H2T.protect_links = True
    H2T.unicode_snob = True
    H2T.skip_internal_links = True
    H2T.wrap_links = False
    H2T.mark_code = True
except ImportError:
    H2T = None

try:
    import yaml
except ImportError:
    yaml = None


ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "discovered_urls.json"
CHECKPOINT_FILE = ROOT / "scrape_checkpoint.json"
ASSETS_DIR = ROOT / "assets"
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9,ko;q=0.8",
}
MAX_RETRIES = 3
MAX_DOCUMENT_BYTES = 80 * 1024 * 1024
CHECKPOINT_EVERY = 25
PRINT_LOCK = threading.Lock()


def headers_for_url(url: str) -> dict[str, str]:
    parsed = urlparse(url)
    if "lghomebattery.com.au" in parsed.netloc:
        return {
            "User-Agent": "curl/8.0",
            "Accept": "text/html,application/xhtml+xml,*/*",
            "Accept-Language": "en-US,en;q=0.9",
        }
    return HEADERS


def log(message: str) -> None:
    with PRINT_LOCK:
        print(message, flush=True)


def split_filter(value: str) -> set[str]:
    return {item.strip() for item in value.split(",") if item.strip()}


def fetch(url: str, *, max_retries: int = MAX_RETRIES) -> requests.Response | None:
    for attempt in range(max_retries):
        try:
            response = requests.get(url, headers=headers_for_url(url), timeout=45)
            response.raise_for_status()
            return response
        except requests.RequestException as exc:
            if attempt + 1 == max_retries:
                log(f"    [FAIL] {url}: {exc}")
                return None
            response = getattr(exc, "response", None)
            retry_after = response.headers.get("Retry-After") if response is not None else None
            try:
                wait = float(retry_after) if retry_after else 2**attempt
            except ValueError:
                wait = 2**attempt
            if response is not None and response.status_code == 429:
                wait = max(wait, 15.0)
            time.sleep(wait)
    return None


def safe_destination(raw_path: object) -> Path:
    rel = Path(str(raw_path))
    if rel.is_absolute() or ".." in rel.parts or rel.parts[:1] != ("raw",):
        raise ValueError(f"unsafe raw_path: {raw_path}")
    return ROOT / rel


def clean_markdown(markdown: str) -> str:
    markdown = re.sub(r"\n\s*\n\s*\n+", "\n\n", markdown)
    markdown = re.sub(r"[ \t]+\n", "\n", markdown)
    return markdown.strip()


def markdown_from_html(node) -> str:
    if H2T:
        try:
            return clean_markdown(H2T.handle(str(node)))
        except Exception:
            pass
    return clean_markdown(node.get_text("\n", strip=True))


def absolutize_links(node, base_url: str) -> None:
    for tag in node.find_all(["a", "img", "source"]):
        for attr in ("href", "src"):
            value = tag.get(attr)
            if value:
                tag[attr] = urljoin(base_url, value)
        srcset = tag.get("srcset")
        if srcset:
            converted = []
            for item in srcset.split(","):
                parts = item.strip().split()
                if parts:
                    parts[0] = urljoin(base_url, parts[0])
                    converted.append(" ".join(parts))
            tag["srcset"] = ", ".join(converted)


def remove_noise(node) -> None:
    for tag in node.find_all(
        [
            "script",
            "style",
            "noscript",
            "nav",
            "header",
            "footer",
            "form",
            "iframe",
            "svg",
        ]
    ):
        tag.decompose()
    for selector in (
        ".cookie",
        ".cookies",
        ".breadcrumb",
        ".breadcrumbs",
        ".pagination",
        ".share",
        ".sns",
        ".related",
        ".recommend",
        ".newsletter",
        ".modal",
    ):
        for tag in node.select(selector):
            tag.decompose()


def select_content_node(soup: BeautifulSoup):
    selectors = [
        ".entry-content",
        ".post-content",
        ".elementor-widget-theme-post-content",
        ".article-content",
        ".article_body",
        ".article-body",
        ".newsroom-detail",
        ".news_view",
        ".view-content",
        ".board_view",
        ".contents",
        ".content",
        "#content",
        "#container",
        "article",
        "main",
        "body",
    ]
    candidates = []
    for selector in selectors:
        for node in soup.select(selector):
            text_len = len(node.get_text(" ", strip=True))
            if text_len > 0:
                candidates.append((text_len, node))
    if not candidates:
        return None
    return max(candidates, key=lambda item: item[0])[1]


def real_image_url(img) -> str | None:
    for attr in ("data-src", "data-lazy-src", "data-original"):
        value = img.get(attr)
        if value and not value.startswith("data:"):
            return value
    srcset = img.get("data-srcset") or img.get("srcset") or ""
    if srcset:
        choices = []
        for entry in srcset.split(","):
            parts = entry.strip().split()
            if not parts:
                continue
            weight = 0
            if len(parts) > 1:
                try:
                    weight = int(parts[1].rstrip("wx"))
                except ValueError:
                    weight = 0
            choices.append((weight, parts[0]))
        if choices:
            return max(choices)[1]
    src = img.get("src", "")
    return src if src and not src.startswith("data:") else None


def image_urls_from_node(node, base_url: str) -> list[str]:
    urls = []
    for img in node.find_all("img"):
        image_url = real_image_url(img)
        if not image_url:
            continue
        absolute = urljoin(base_url, image_url)
        if absolute not in urls:
            urls.append(absolute)
    return urls


def sanitize_filename(value: str) -> str:
    cleaned = re.sub(r"[^\w.\-]+", "_", value)
    return cleaned[:180] or "image"


def download_images(record: dict[str, object], images: list[str]) -> list[str]:
    saved = []
    if not images:
        return saved
    source = str(record.get("source", "unknown"))
    language = str(record.get("language", "unknown"))
    category = str(record.get("category", "uncategorized"))
    slug = Path(str(record.get("raw_path", "page.md"))).stem
    asset_dir = ASSETS_DIR / source / language / category / slug
    asset_dir.mkdir(parents=True, exist_ok=True)
    for index, image_url in enumerate(images):
        parsed = urlparse(image_url)
        filename = sanitize_filename(Path(parsed.path).name or f"image-{index}.jpg")
        destination = asset_dir / filename
        if not destination.exists():
            response = fetch(image_url, max_retries=2)
            if response is None:
                continue
            if "image" not in response.headers.get("Content-Type", ""):
                continue
            destination.write_bytes(response.content)
        saved.append(destination.relative_to(ROOT).as_posix())
    return saved


def extract_html(record: dict[str, object]) -> tuple[str, dict[str, object]]:
    url = str(record["url"])
    response = fetch(url)
    if response is None:
        fallback = str(record.get("content_text", "")).strip()
        if fallback:
            return fallback, {"extraction_warning": "used_manifest_text_after_fetch_failure"}
        raise RuntimeError("fetch failed")
    soup = BeautifulSoup(response.text, "html.parser")
    node = select_content_node(soup)
    if node is None:
        fallback = str(record.get("content_text", "")).strip()
        if fallback:
            return fallback, {"extraction_warning": "used_manifest_text_no_content_node"}
        return fallback_body(record, "no content node"), {"extraction_warning": "no_content_node"}
    remove_noise(node)
    absolutize_links(node, response.url)
    images = image_urls_from_node(node, response.url)
    markdown = markdown_from_html(node)
    fallback = str(record.get("content_text", "")).strip()
    if len(markdown) < 80 and fallback:
        markdown = fallback
    metadata: dict[str, object] = {
        "final_url": response.url,
        "content_type": response.headers.get("Content-Type", ""),
    }
    if images:
        metadata["image_urls"] = images[:50]
    return markdown, metadata


def extract_ebook(record: dict[str, object]) -> tuple[str, dict[str, object]]:
    text = str(record.get("content_text", "")).strip()
    page_number = record.get("page_number", "")
    page_count = record.get("page_count", "")
    image_url = str(record.get("image_url", ""))
    lines = [
        f"# {record.get('title', 'ENSOLPEDIA page')}",
        "",
        f"Reader URL: {record.get('url', '')}",
        f"Page: {page_number} / {page_count}",
    ]
    if image_url:
        lines.extend(["", f"Page image: {image_url}", "", f"![Page {page_number}]({image_url})"])
    lines.extend(["", "## Searchable Text", "", text or "(No embedded searchable text was available for this page.)"])
    return "\n".join(lines).strip(), {}


def pdf_text(content: bytes) -> str:
    if shutil.which("pdftotext") is None:
        return ""
    with tempfile.NamedTemporaryFile(suffix=".pdf") as pdf:
        pdf.write(content)
        pdf.flush()
        result = subprocess.run(
            ["pdftotext", "-layout", pdf.name, "-"],
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=90,
            check=False,
        )
    if result.returncode != 0:
        return ""
    return clean_markdown(result.stdout)


def extract_document(record: dict[str, object]) -> tuple[str, dict[str, object]]:
    url = urljoin("https://www.lgensol.com", str(record["url"]))
    response = fetch(url)
    if response is None:
        raise RuntimeError("document fetch failed")
    content_type = response.headers.get("Content-Type", "")
    metadata: dict[str, object] = {
        "final_url": response.url,
        "content_type": content_type,
        "document_bytes": len(response.content),
    }
    if len(response.content) > MAX_DOCUMENT_BYTES:
        body = (
            f"# {record.get('title', 'Document')}\n\n"
            f"Document URL: {response.url}\n\n"
            f"Skipped text extraction because the file is larger than {MAX_DOCUMENT_BYTES // 1024 // 1024} MB."
        )
        metadata["extraction_warning"] = "document_too_large"
        return body, metadata
    parsed = urlparse(response.url)
    if "pdf" in content_type.lower() or parsed.path.lower().endswith(".pdf"):
        text = pdf_text(response.content)
        if not text:
            text = "(PDF fetched, but pdftotext did not return extractable text.)"
            metadata["extraction_warning"] = "pdf_text_empty"
        body = f"# {record.get('title', 'Document')}\n\nDocument URL: {response.url}\n\n{text}"
        return body, metadata
    if "html" in content_type.lower() or response.text.strip().startswith("<"):
        soup = BeautifulSoup(response.text, "html.parser")
        node = select_content_node(soup) or soup.body
        if node is not None:
            remove_noise(node)
            absolutize_links(node, response.url)
            body = markdown_from_html(node)
            return body, metadata
    body = (
        f"# {record.get('title', 'Document')}\n\n"
        f"Document URL: {response.url}\n\n"
        "No text extractor is configured for this document type."
    )
    metadata["extraction_warning"] = "unsupported_document_type"
    return body, metadata


def fallback_body(record: dict[str, object], reason: str) -> str:
    lines = [
        f"# {record.get('title', 'Untitled source')}",
        "",
        f"Source URL: {record.get('url', '')}",
        f"Source: {record.get('source', '')}",
        f"Kind: {record.get('kind', '')}",
        "",
        f"Extraction warning: {reason}",
    ]
    text = str(record.get("content_text", "")).strip()
    if text:
        lines.extend(["", "## Manifest Text", "", text])
    return "\n".join(lines)


def dump_frontmatter(frontmatter: dict[str, object]) -> str:
    if yaml:
        return yaml.safe_dump(
            frontmatter,
            allow_unicode=True,
            sort_keys=False,
            default_flow_style=False,
        ).strip()
    lines = []
    for key, value in frontmatter.items():
        if isinstance(value, list):
            lines.append(f"{key}:")
            lines.extend(f"  - {item}" for item in value)
        elif isinstance(value, dict):
            lines.append(f"{key}: {json.dumps(value, ensure_ascii=False)}")
        else:
            lines.append(f"{key}: {value}")
    return "\n".join(lines)


def write_record(
    record: dict[str, object],
    body: str,
    metadata: dict[str, object],
    *,
    download_image_files: bool,
) -> int:
    body = clean_markdown(body)
    if not body:
        body = fallback_body(record, "empty extracted body")
        metadata["extraction_warning"] = "empty_extracted_body"
    images = list(metadata.get("image_urls", [])) if isinstance(metadata.get("image_urls"), list) else []
    saved_images = download_images(record, images) if download_image_files else []
    sha256 = hashlib.sha256(body.encode("utf-8")).hexdigest()
    frontmatter: dict[str, object] = {
        "source_url": record.get("url", ""),
        "source": record.get("source", ""),
        "source_family": record.get("source_family", ""),
        "language": record.get("language", ""),
        "kind": record.get("kind", ""),
        "record_id": record.get("id", ""),
        "title": record.get("title", ""),
        "date": record.get("date", ""),
        "modified": record.get("modified", ""),
        "category": record.get("category", ""),
        "ingested": datetime.now(timezone.utc).isoformat(),
        "sha256": sha256,
    }
    for key in (
        "category_ids",
        "tags",
        "page_number",
        "page_count",
        "image_url",
        "attachment_url",
        "file_name",
        "file_code",
    ):
        if key in record and record[key] not in ("", None, []):
            frontmatter[key] = record[key]
    for key, value in metadata.items():
        if value not in ("", None, []):
            frontmatter[key] = value
    if saved_images:
        frontmatter["images"] = saved_images

    destination = safe_destination(record["raw_path"])
    destination.parent.mkdir(parents=True, exist_ok=True)
    content = f"---\n{dump_frontmatter(frontmatter)}\n---\n\n{body}\n"
    destination.write_text(content, encoding="utf-8")
    return len(content.encode("utf-8"))


def scrape_record(
    record: dict[str, object],
    *,
    force: bool,
    download_image_files: bool,
    delay: float,
) -> dict[str, object]:
    record_id = str(record["id"])
    destination = safe_destination(record["raw_path"])
    if destination.exists() and not force:
        return {"status": "skipped", "id": record_id, "path": destination.relative_to(ROOT).as_posix()}
    if delay > 0:
        time.sleep(delay)
    try:
        kind = str(record.get("kind", "html-page"))
        if kind == "ebook-page":
            body, metadata = extract_ebook(record)
        elif kind == "document":
            body, metadata = extract_document(record)
        else:
            body, metadata = extract_html(record)
        content_size = write_record(
            record,
            body,
            metadata,
            download_image_files=download_image_files,
        )
        return {
            "status": "success",
            "id": record_id,
            "path": destination.relative_to(ROOT).as_posix(),
            "content_size": content_size,
        }
    except Exception as exc:
        metadata = {"extraction_warning": str(exc)}
        content_size = write_record(
            record,
            fallback_body(record, str(exc)),
            metadata,
            download_image_files=False,
        )
        return {
            "status": "success",
            "id": record_id,
            "path": destination.relative_to(ROOT).as_posix(),
            "content_size": content_size,
            "warning": str(exc),
        }


def load_checkpoint() -> set[str]:
    if not CHECKPOINT_FILE.exists():
        return set()
    with CHECKPOINT_FILE.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    return {str(item) for item in data.get("completed_ids", [])}


def save_checkpoint(results: dict[str, object]) -> None:
    CHECKPOINT_FILE.write_text(
        json.dumps(results, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def filter_records(records: list[dict[str, object]], args: argparse.Namespace) -> list[dict[str, object]]:
    selected = records
    if args.sources:
        allowed = split_filter(args.sources)
        selected = [r for r in selected if str(r.get("source", "")) in allowed]
    if args.families:
        allowed = split_filter(args.families)
        selected = [r for r in selected if str(r.get("source_family", "")) in allowed]
    if args.kinds:
        allowed = split_filter(args.kinds)
        selected = [r for r in selected if str(r.get("kind", "")) in allowed]
    if args.limit > 0:
        selected = selected[: args.limit]
    return selected


def main() -> int:
    parser = argparse.ArgumentParser(description="Scrape discovered LG Energy Solution sources")
    parser.add_argument("--resume", action="store_true", help="Skip IDs listed in scrape_checkpoint.json")
    parser.add_argument("--limit", type=int, default=0, help="Limit records after filtering")
    parser.add_argument("--force", action="store_true", help="Re-scrape existing raw files")
    parser.add_argument("--workers", type=int, default=6, help="Concurrent scrape workers")
    parser.add_argument("--delay", type=float, default=0.0, help="Per-record delay before fetching")
    parser.add_argument("--sources", default="", help="Comma-separated source filter")
    parser.add_argument("--families", default="", help="Comma-separated source_family filter")
    parser.add_argument("--kinds", default="", help="Comma-separated kind filter")
    parser.add_argument("--download-images", action="store_true", help="Download newly discovered inline images")
    args = parser.parse_args()

    if not MANIFEST_PATH.exists():
        print("[FAIL] Run scrapers/discover_urls.py first")
        return 1
    data = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    records = filter_records(list(data["articles"]), args)
    completed = load_checkpoint() if args.resume and not args.force else set()
    to_process = [record for record in records if str(record["id"]) not in completed]
    print(f"Loaded {len(data['articles'])} discovered records")
    print(f"Selected {len(records)} records; processing {len(to_process)}")

    results: dict[str, object] = {
        "success": 0,
        "skipped": len(records) - len(to_process),
        "failed": 0,
        "total_content_bytes": 0,
        "completed_ids": sorted(completed),
        "failed_ids": [],
        "started_at": datetime.now(timezone.utc).isoformat(),
    }
    completed_ids = set(completed)
    failed_ids: list[dict[str, str]] = []
    start = time.time()

    if not to_process:
        save_checkpoint(results)
        return 0

    with concurrent.futures.ThreadPoolExecutor(max_workers=max(1, args.workers)) as executor:
        futures = {
            executor.submit(
                scrape_record,
                record,
                force=args.force,
                download_image_files=args.download_images,
                delay=args.delay,
            ): record
            for record in to_process
        }
        for index, future in enumerate(concurrent.futures.as_completed(futures), start=1):
            record = futures[future]
            try:
                result = future.result()
            except Exception as exc:
                result = {"status": "failed", "id": str(record.get("id", "")), "error": str(exc)}
            status = str(result["status"])
            record_id = str(result["id"])
            if status in ("success", "skipped"):
                if status == "success":
                    results["success"] = int(results["success"]) + 1
                    results["total_content_bytes"] = int(results["total_content_bytes"]) + int(result.get("content_size", 0))
                else:
                    results["skipped"] = int(results["skipped"]) + 1
                completed_ids.add(record_id)
                path = result.get("path", "")
                log(f"[{index}/{len(to_process)}] {status.upper()} {path}")
            else:
                results["failed"] = int(results["failed"]) + 1
                failed = {"id": record_id, "error": str(result.get("error", "unknown"))}
                failed_ids.append(failed)
                log(f"[{index}/{len(to_process)}] FAIL {record_id}: {failed['error']}")
            if index % CHECKPOINT_EVERY == 0:
                results["completed_ids"] = sorted(completed_ids)
                results["failed_ids"] = failed_ids
                save_checkpoint(results)

    results["completed_ids"] = sorted(completed_ids)
    results["failed_ids"] = failed_ids
    results["elapsed_seconds"] = time.time() - start
    results["finished_at"] = datetime.now(timezone.utc).isoformat()
    save_checkpoint(results)

    print("\nScraping complete")
    print(f"  Success: {results['success']}")
    print(f"  Skipped: {results['skipped']}")
    print(f"  Failed:  {results['failed']}")
    print(f"  Text:    {int(results['total_content_bytes']) / 1024 / 1024:.1f} MB")
    print(f"  Time:    {float(results['elapsed_seconds']) / 60:.1f} min")
    print(f"  Checkpoint: {CHECKPOINT_FILE}")
    return 0 if int(results["failed"]) == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
