#!/usr/bin/env python3
"""Discover public LG Energy Solution content across official web properties."""
from __future__ import annotations

import argparse
import json
import time
from collections import Counter
from datetime import datetime, timezone

import requests

from source_catalog import (
    MANIFEST_PATH,
    SITEMAP_SOURCES,
    deduplicate,
    discover_corporate_downloads,
    discover_corporate_news,
    discover_ensolpedia,
    discover_linked_site,
    discover_sitemap_source,
    discover_wordpress_posts,
    corporate_navigation,
)


FAMILIES = {
    "battery-inside",
    "ensolpedia",
    "corporate",
    "regional",
    "product",
    "joint-venture",
}


def add_records(
    target: list[dict[str, object]],
    errors: list[dict[str, str]],
    label: str,
    callback,
) -> None:
    print(f"Discovering {label}...", flush=True)
    try:
        records = callback()
    except (requests.RequestException, ValueError) as exc:
        print(f"  FAIL: {exc}", flush=True)
        errors.append({"source": label, "error": str(exc)})
        return
    target.extend(records)
    print(f"  {len(records)} records", flush=True)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--families",
        default="all",
        help="Comma-separated source families, or all",
    )
    args = parser.parse_args()
    selected = (
        FAMILIES
        if args.families == "all"
        else {item.strip() for item in args.families.split(",") if item.strip()}
    )
    unknown = selected - FAMILIES
    if unknown:
        parser.error(f"Unknown families: {', '.join(sorted(unknown))}")

    records: list[dict[str, object]] = []
    errors: list[dict[str, str]] = []

    if "battery-inside" in selected:
        add_records(
            records,
            errors,
            "Battery Inside Korean",
            lambda: discover_wordpress_posts(
                "https://inside.lgensol.com/wp-json/wp/v2",
                source="battery-inside-ko",
                family="battery-inside",
                language="ko",
                preserve_korean_paths=True,
            ),
        )
        add_records(
            records,
            errors,
            "Battery Inside English",
            lambda: discover_wordpress_posts(
                "https://inside.lgensol.com/en/wp-json/wp/v2",
                source="battery-inside-en",
                family="battery-inside",
                language="en",
            ),
        )

    if "ensolpedia" in selected:
        for language in ("ko", "en"):
            add_records(
                records,
                errors,
                f"ENSOLPEDIA {language}",
                lambda language=language: discover_ensolpedia(language),
            )

    if "corporate" in selected:
        for language in ("kr", "en", "zh", "de", "pl"):
            add_records(
                records,
                errors,
                f"corporate navigation {language}",
                lambda language=language: corporate_navigation(language),
            )
            add_records(
                records,
                errors,
                f"corporate newsroom {language}",
                lambda language=language: discover_corporate_news(language),
            )
            add_records(
                records,
                errors,
                f"corporate downloads {language}",
                lambda language=language: discover_corporate_downloads(language),
            )

    for config in SITEMAP_SOURCES:
        family = str(config["family"])
        if family not in selected:
            continue
        add_records(
            records,
            errors,
            str(config["source"]),
            lambda config=config: discover_sitemap_source(config),
        )

    if "product" in selected:
        add_records(
            records,
            errors,
            "LG ESS Battery",
            lambda: discover_linked_site(
                source="lg-ess-battery",
                family="product",
                language="en",
                seeds=[
                    "https://www.lgessbattery.com/us/main/main.lg",
                    "https://www.lgessbattery.com/eu/main/main.lg",
                    "https://www.lgessbattery.com/au/main/main.lg",
                    "https://www.lgessbattery.com/en/lgenblock/index.html",
                ],
                allowed_prefixes=("/us/", "/eu/", "/au/", "/en/"),
                max_pages=250,
            ),
        )
        add_records(
            records,
            errors,
            "KooRoo",
            lambda: discover_linked_site(
                source="kooroo",
                family="product",
                language="ko",
                seeds=["https://www.kooroo.co.kr/"],
                max_pages=50,
            ),
        )

    if "joint-venture" in selected:
        add_records(
            records,
            errors,
            "HLI Green Power",
            lambda: discover_linked_site(
                source="hli-green-power",
                family="joint-venture",
                language="en",
                seeds=["https://www.hligreenpower.com/en"],
                max_pages=30,
            ),
        )

    records = deduplicate(records)
    counts = Counter(str(record["source"]) for record in records)
    family_counts = Counter(str(record["source_family"]) for record in records)
    output = {
        "schema_version": 2,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "total_articles": len(records),
        "sources": dict(sorted(counts.items())),
        "families": dict(sorted(family_counts.items())),
        "errors": errors,
        "articles": records,
    }
    MANIFEST_PATH.write_text(
        json.dumps(output, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print("\nDiscovery complete")
    print(f"  Records: {len(records)}")
    print(f"  Errors:  {len(errors)}")
    for family, count in sorted(family_counts.items()):
        print(f"  {family}: {count}")
    print(f"  Saved: {MANIFEST_PATH}")
    return 0


if __name__ == "__main__":
    started = time.time()
    raise SystemExit(main())
