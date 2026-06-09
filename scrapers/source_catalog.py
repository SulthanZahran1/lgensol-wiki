#!/usr/bin/env python3
"""Shared source discovery helpers for the LG Energy Solution corpus."""
from __future__ import annotations

import hashlib
import html
import re
import time
import xml.etree.ElementTree as ET
from collections import deque
from pathlib import Path
from urllib.parse import unquote, urljoin, urlparse

import requests
from bs4 import BeautifulSoup


ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "discovered_urls.json"
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9,ko;q=0.8",
}
TIMEOUT = 30


CORPORATE_LANGUAGES = {
    "kr": ("KR", "KO"),
    "en": ("US", "EN"),
    "zh": ("CN", "ZH"),
    "de": ("DE", "DE"),
    "pl": ("PL", "PL"),
}


SITEMAP_SOURCES = [
    {
        "source": "lg-energy-solution-poland",
        "family": "regional",
        "language": "pl",
        "index": "https://lgensol.pl/sitemap_index.xml",
        "include": ("post-sitemap", "page-sitemap"),
    },
    {
        "source": "lg-energy-solution-michigan",
        "family": "regional",
        "language": "en",
        "index": "https://lgenergymi.com/sitemap_index.xml",
        "include": ("post-sitemap", "page-sitemap"),
    },
    {
        "source": "lg-energy-solution-vertech",
        "family": "regional",
        "language": "en",
        "index": "https://lgensol-vt.com/sitemap_index.xml",
        "include": ("post-sitemap", "page-sitemap"),
    },
    {
        "source": "lg-home-battery-australia",
        "family": "product",
        "language": "en",
        "index": "https://www.lghomebattery.com.au/sitemap.xml",
        "include": ("blog-posts-sitemap", "pages-sitemap"),
    },
    {
        "source": "nextstar-energy",
        "family": "joint-venture",
        "language": "en",
        "index": "https://nextstar-energy.com/wp-sitemap.xml",
        "include": ("posts-post", "posts-page"),
    },
    {
        "source": "lg-honda-battery",
        "family": "joint-venture",
        "language": "en",
        "index": "https://lhbattery.com/sitemap_index.xml",
        "include": ("post-sitemap", "page-sitemap"),
    },
    {
        "source": "hl-ga-battery",
        "family": "joint-venture",
        "language": "en",
        "index": "https://hlgabattery.com/sitemap.xml",
        "include": ("sitemap-1.xml",),
    },
    {
        "source": "ultium-cells",
        "family": "joint-venture",
        "language": "en",
        "index": "https://www.ultiumcell.com/sitemap.xml",
        "include": (),
    },
]


def request(
    method: str,
    url: str,
    *,
    data: dict[str, object] | None = None,
    timeout: int = TIMEOUT,
    retries: int = 5,
) -> requests.Response:
    last_error: Exception | None = None
    for attempt in range(retries):
        try:
            response = requests.request(
                method,
                url,
                headers=HEADERS,
                data=data,
                timeout=timeout,
            )
            response.raise_for_status()
            return response
        except requests.RequestException as exc:
            last_error = exc
            if attempt + 1 < retries:
                retry_after = None
                response = getattr(exc, "response", None)
                if response is not None:
                    retry_after = response.headers.get("Retry-After")
                try:
                    wait = float(retry_after) if retry_after else 2**attempt
                except ValueError:
                    wait = 2**attempt
                if response is not None and response.status_code == 429:
                    wait = max(wait, 10.0)
                time.sleep(wait)
    assert last_error is not None
    raise last_error


def clean_title(value: str) -> str:
    return re.sub(r"\s+", " ", html.unescape(value or "")).strip()


def safe_slug(value: str, fallback: str = "page") -> str:
    value = unquote(value).strip().lower()
    value = re.sub(r"<[^>]+>", "", value)
    value = re.sub(r"[^a-z0-9가-힣]+", "-", value).strip("-")
    if not value:
        value = fallback
    if len(value) > 100:
        digest = hashlib.sha1(value.encode("utf-8")).hexdigest()[:10]
        value = f"{value[:88].rstrip('-')}-{digest}"
    return value


def slug_from_url(url: str, fallback: str = "page") -> str:
    parsed = urlparse(url)
    part = Path(parsed.path.rstrip("/")).name
    if not part:
        part = fallback
    slug = safe_slug(part, fallback)
    if parsed.query:
        digest = hashlib.sha1(parsed.query.encode("utf-8")).hexdigest()[:8]
        slug = f"{slug}-{digest}"
    return slug


def record_id(source: str, key: object) -> str:
    return f"{source}:{key}"


def raw_path(source: str, language: str, category: str, slug: str) -> str:
    category = safe_slug(category, "uncategorized")
    slug = safe_slug(slug)
    return f"raw/{source}/{language}/{category}/{slug}.md"


def category_map(api_base: str) -> dict[int, str]:
    response = request("GET", f"{api_base}/categories?per_page=100")
    return {
        int(item["id"]): safe_slug(item.get("slug") or item.get("name"), "uncategorized")
        for item in response.json()
    }


def existing_wordpress_paths(language: str) -> dict[str, str]:
    base = ROOT / "raw" / language
    paths: dict[str, str] = {}
    if not base.exists():
        return paths
    for path in base.glob("**/*.md"):
        text = path.read_text(encoding="utf-8", errors="ignore")[:4000]
        match = re.search(r"^wp_id:\s*(\S+)", text, re.M)
        if match:
            paths[match.group(1)] = path.relative_to(ROOT).as_posix()
    return paths


def discover_wordpress_posts(
    api_base: str,
    *,
    source: str,
    family: str,
    language: str,
    preserve_korean_paths: bool = False,
) -> list[dict[str, object]]:
    categories = category_map(api_base)
    existing_paths = existing_wordpress_paths(language) if preserve_korean_paths else {}
    first = request("GET", f"{api_base}/posts?per_page=100&_fields=id")
    total_pages = int(first.headers.get("X-WP-TotalPages", "0"))
    records: list[dict[str, object]] = []
    fields = "id,title,link,date,modified,categories,tags,excerpt,content"
    for page in range(1, total_pages + 1):
        response = request(
            "GET",
            f"{api_base}/posts?per_page=100&page={page}&_fields={fields}",
        )
        for post in response.json():
            category = next(
                (categories[cid] for cid in post.get("categories", []) if cid in categories),
                "uncategorized",
            )
            url = post["link"]
            slug = slug_from_url(url, f"post-{post['id']}")
            existing_path = existing_paths.get(str(post["id"]))
            if existing_path:
                destination = existing_path
            elif preserve_korean_paths:
                # Keep the original Korean scrape path shape so existing files
                # are detected and skipped by the generalized scraper.
                legacy_slug = urlparse(url).path.rstrip("/").split("/")[-1] or slug
                destination = f"raw/ko/{category}/{legacy_slug}.md"
            else:
                destination = raw_path(source, language, category, slug)
            records.append(
                {
                    "id": record_id(source, post["id"]),
                    "source": source,
                    "source_family": family,
                    "language": language,
                    "kind": "wordpress-post",
                    "title": clean_title(post["title"]["rendered"]),
                    "url": url,
                    "date": post.get("date", ""),
                    "modified": post.get("modified", ""),
                    "category": category,
                    "category_ids": post.get("categories", []),
                    "tags": post.get("tags", []),
                    "raw_path": destination,
                }
            )
    return records


def discover_ensolpedia(language: str) -> list[dict[str, object]]:
    catalog_id = "657" if language == "ko" else "658"
    reader = (
        f"https://inside.lgensol.com/src/ebook/2026/{language}/"
        "ecatalog5.php?Dir="
    )
    reader_text = request("GET", reader).text
    match = re.search(
        r"set_pageinfo\('[^']*','(?P<catalog>\d+)',\d+,(?P<pages>\d+),",
        reader_text,
    )
    if match:
        catalog_id = match.group("catalog")
        page_count = int(match.group("pages"))
    else:
        page_count = 126
    search_url = (
        f"https://inside.lgensol.com/src/ebook/2026/{language}/"
        f"catImage/{catalog_id}/search.xml"
    )
    root = ET.fromstring(request("GET", search_url).content)
    text_by_page: dict[int, str] = {}
    for page_node in root.findall("page"):
        number = int(page_node.findtext("no", "0"))
        text_by_page[number] = clean_title(page_node.findtext("search", ""))
    title = "배터리의 모든 것 ENSOLPEDIA" if language == "ko" else "All About Battery ENSOLPEDIA"
    records = []
    for number in range(1, page_count + 1):
        image_url = (
            f"https://inside.lgensol.com/src/ebook/2026/{language}/"
            f"catImage/{catalog_id}/s{number:03d}.jpg"
        )
        records.append(
            {
                "id": record_id(f"ensolpedia-{language}", number),
                "source": "ensolpedia",
                "source_family": "ebook",
                "language": language,
                "kind": "ebook-page",
                "title": f"{title} - page {number}",
                "url": f"{reader}&page={number}",
                "date": "2026",
                "modified": "2026-06-02",
                "category": "ensolpedia",
                "page_number": number,
                "page_count": page_count,
                "image_url": image_url,
                "content_text": text_by_page.get(number, ""),
                "raw_path": raw_path(
                    "ensolpedia",
                    language,
                    "pages",
                    f"page-{number:03d}",
                ),
            }
        )
    return records


def corporate_navigation(language: str) -> list[dict[str, object]]:
    index_url = f"https://www.lgensol.com/{language}/index"
    response = request("GET", index_url)
    if response.status_code != 200:
        return []
    soup = BeautifulSoup(response.text, "html.parser")
    prefix = f"/{language}/"
    urls = set()
    for anchor in soup.select("a[href]"):
        url = urljoin(index_url, anchor.get("href", ""))
        parsed = urlparse(url)
        if parsed.netloc != "www.lgensol.com" or not parsed.path.startswith(prefix):
            continue
        if parsed.path.startswith(f"/{language}/company/newsroom-detail"):
            continue
        urls.add(parsed._replace(query="", fragment="").geturl())
    records = []
    for url in sorted(urls):
        slug = safe_slug(urlparse(url).path[len(prefix) :].replace("/", "-"), "index")
        if slug == "company-management-intro":
            continue
        records.append(
            {
                "id": record_id(f"corporate-{language}", slug),
                "source": "lgensol-corporate",
                "source_family": "corporate",
                "language": language,
                "kind": "html-page",
                "title": slug.replace("-", " ").title(),
                "url": url,
                "category": urlparse(url).path.split("/")[2] if len(urlparse(url).path.split("/")) > 2 else "corporate",
                "raw_path": raw_path("corporate", language, "pages", slug),
            }
        )
    return records


def parse_xsync_rows(content: bytes) -> list[dict[str, str]]:
    root = ET.fromstring(content)
    multi = root.find("LMultiData")
    if multi is None:
        return []
    columns: dict[str, list[str]] = {}
    for child in multi:
        columns.setdefault(child.tag, []).append(child.text or "")
    row_count = max((len(values) for values in columns.values()), default=0)
    return [
        {
            key: values[index] if index < len(values) else ""
            for key, values in columns.items()
        }
        for index in range(row_count)
    ]


def xsync_count(url: str, data: dict[str, object]) -> int:
    root = ET.fromstring(request("POST", url, data=data).content)
    value = root.findtext(".//cnt", "0")
    return int(value or "0")


def discover_corporate_news(language: str) -> list[dict[str, object]]:
    country_code, language_code = CORPORATE_LANGUAGES[language]
    base_data = {
        "listSiteCountryCode": country_code,
        "listSiteLanguageCode": language_code,
        "typeGbn": "",
        "recentNewsroomSeq": "",
        "keyword": "",
    }
    count_url = (
        "https://www.lgensol.com/company/company-newsroom/"
        "newsroomListCountAjax.ajax"
    )
    list_url = (
        "https://www.lgensol.com/company/company-newsroom/"
        "newsroomListAjax.ajax"
    )
    total = xsync_count(count_url, base_data)
    if total == 0:
        return []
    rows = parse_xsync_rows(
        request(
            "POST",
            list_url,
            data={**base_data, "startRnum": 1, "endRnum": total},
        ).content
    )
    records = []
    for row in rows:
        sequence = row.get("newsroomSeq", "")
        title = clean_title(row.get("title", ""))
        if not sequence or not title:
            continue
        records.append(
            {
                "id": record_id(f"corporate-news-{language}", sequence),
                "source": "lgensol-corporate-newsroom",
                "source_family": "newsroom",
                "language": language,
                "kind": "corporate-news",
                "title": title,
                "url": (
                    f"https://www.lgensol.com/{language}/company/"
                    f"newsroom-detail?seq={sequence}"
                ),
                "date": row.get("postFromDate", ""),
                "modified": row.get("postFromDate", ""),
                "category": "newsroom",
                "content_text": clean_title(
                    BeautifulSoup(row.get("summary", ""), "html.parser").get_text(" ")
                ),
                "image_url": row.get("thumbUrl", ""),
                "attachment_url": row.get("imgZipUrl", ""),
                "raw_path": raw_path(
                    "corporate",
                    language,
                    "newsroom",
                    f"{sequence}-{safe_slug(title)}",
                ),
            }
        )
    return records


def discover_corporate_downloads(language: str) -> list[dict[str, object]]:
    country_code, language_code = CORPORATE_LANGUAGES[language]
    base_data = {
        "listSiteCountryCode": country_code,
        "listSiteLanguageCode": language_code,
        "category1": "",
        "category2": "",
        "category3": "",
        "category4": "",
        "keyword": "",
    }
    count_url = "https://www.lgensol.com/etc/fileDown/fileDownListCountAjax.ajax"
    list_url = "https://www.lgensol.com/etc/fileDown/fileDownListAjax.ajax"
    total = xsync_count(count_url, base_data)
    if total == 0:
        return []
    rows = []
    # This endpoint caps each response at roughly ten rows even when a larger
    # endRnum is supplied, so page explicitly and deduplicate below.
    for start in range(0, total, 10):
        rows.extend(
            parse_xsync_rows(
                request(
                    "POST",
                    list_url,
                    data={
                        **base_data,
                        "startRnum": start,
                        "endRnum": min(start + 10, total),
                    },
                ).content
            )
        )
    records = []
    seen_file_numbers = set()
    for row in rows:
        file_number = row.get("fileInfoNo", "")
        url = row.get("fileUrl", "")
        title = clean_title(row.get("fileTitle", ""))
        if (
            not file_number
            or file_number in seen_file_numbers
            or not url
            or not title
        ):
            continue
        seen_file_numbers.add(file_number)
        url = urljoin("https://www.lgensol.com", url)
        category = row.get("category1", "") or "downloads"
        records.append(
            {
                "id": record_id(f"corporate-download-{language}", file_number),
                "source": "lgensol-corporate-downloads",
                "source_family": "documents",
                "language": language,
                "kind": "document",
                "title": title,
                "url": url,
                "category": category,
                "file_name": row.get("fileName", ""),
                "file_code": row.get("fileCode", ""),
                "raw_path": raw_path(
                    "corporate",
                    language,
                    "documents",
                    f"{file_number}-{safe_slug(title)}",
                ),
            }
        )
    return records


def sitemap_documents(index_url: str) -> tuple[list[str], list[str]]:
    if "lghomebattery.com.au" in urlparse(index_url).netloc:
        response = requests.get(
            index_url,
            headers={"User-Agent": "curl/8.0", "Accept": "application/xml,text/xml,*/*"},
            timeout=TIMEOUT,
        )
        response.raise_for_status()
    else:
        response = request("GET", index_url)
    root = ET.fromstring(response.content)
    namespace = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    sitemap_urls = [
        node.text.strip()
        for node in root.findall("sm:sitemap/sm:loc", namespace)
        if node.text
    ]
    page_urls = [
        node.text.strip()
        for node in root.findall("sm:url/sm:loc", namespace)
        if node.text
    ]
    return sitemap_urls, page_urls


def discover_sitemap_source(config: dict[str, object]) -> list[dict[str, object]]:
    sitemap_urls, page_urls = sitemap_documents(str(config["index"]))
    include = tuple(config.get("include", ()))
    if sitemap_urls:
        selected = [
            url
            for url in sitemap_urls
            if not include or any(marker in url for marker in include)
        ]
        for sitemap_url in selected:
            time.sleep(0.5)
            try:
                _nested, urls = sitemap_documents(sitemap_url)
            except requests.RequestException:
                continue
            page_urls.extend(urls)
    records = []
    source = str(config["source"])
    default_language = str(config["language"])
    for url in sorted(set(page_urls)):
        parsed = urlparse(url)
        path = parsed.path.lower()
        if any(
            marker in path
            for marker in (
                "/privacy",
                "/terms",
                "/author/",
                "/category/",
                "/tag/",
                "/sample-page",
            )
        ):
            continue
        language = "en" if "/en/" in path else default_language
        slug = slug_from_url(url)
        records.append(
            {
                "id": record_id(source, hashlib.sha1(url.encode()).hexdigest()[:16]),
                "source": source,
                "source_family": config["family"],
                "language": language,
                "kind": "html-page",
                "title": slug.replace("-", " ").title(),
                "url": url,
                "category": "site-content",
                "raw_path": raw_path(source, language, "pages", slug),
            }
        )
    return records


def discover_linked_site(
    *,
    source: str,
    family: str,
    language: str,
    seeds: list[str],
    allowed_prefixes: tuple[str, ...] = (),
    max_pages: int = 200,
) -> list[dict[str, object]]:
    queue = deque(seeds)
    seen: set[str] = set()
    records: list[dict[str, object]] = []
    allowed_hosts = {urlparse(seed).netloc for seed in seeds}
    while queue and len(seen) < max_pages:
        url = queue.popleft()
        parsed = urlparse(url)
        normalized = parsed._replace(fragment="").geturl()
        if normalized in seen or parsed.netloc not in allowed_hosts:
            continue
        if allowed_prefixes and not any(parsed.path.startswith(p) for p in allowed_prefixes):
            continue
        seen.add(normalized)
        try:
            response = request("GET", normalized, retries=2)
        except requests.RequestException:
            continue
        if "text/html" not in response.headers.get("Content-Type", ""):
            continue
        slug = safe_slug(
            parsed.path.strip("/").replace("/", "-") or source,
            source,
        )
        records.append(
            {
                "id": record_id(source, hashlib.sha1(normalized.encode()).hexdigest()[:16]),
                "source": source,
                "source_family": family,
                "language": language,
                "kind": "html-page",
                "title": slug.replace("-", " ").title(),
                "url": normalized,
                "category": "site-content",
                "raw_path": raw_path(source, language, "pages", slug),
            }
        )
        soup = BeautifulSoup(response.text, "html.parser")
        for anchor in soup.select("a[href]"):
            linked = urljoin(response.url, anchor.get("href", ""))
            linked_parsed = urlparse(linked)
            if linked_parsed.scheme not in ("http", "https"):
                continue
            if linked_parsed.netloc not in allowed_hosts:
                continue
            if re.search(r"\.(?:jpg|jpeg|png|gif|svg|pdf|zip)$", linked_parsed.path, re.I):
                continue
            queue.append(linked_parsed._replace(fragment="").geturl())
    return records


def deduplicate(records: list[dict[str, object]]) -> list[dict[str, object]]:
    output: list[dict[str, object]] = []
    seen_ids: set[str] = set()
    seen_paths: set[str] = set()
    for record in records:
        identifier = str(record["id"])
        destination = str(record["raw_path"])
        if identifier in seen_ids or destination in seen_paths:
            continue
        seen_ids.add(identifier)
        seen_paths.add(destination)
        output.append(record)
    return output
