# LG Energy Solution Source Discovery

Last checked: 2026-06-08

This document maps publicly discoverable LG Energy Solution web sources before
the scraper is expanded. It is a source perimeter, not a claim that every
possible hostname or historical page has been found.

## Priority 1: LGES First-Party Content

### Battery Inside

- Base: `https://inside.lgensol.com/`
- Korean REST API: `https://inside.lgensol.com/wp-json/wp/v2`
  - 556 posts
  - 13 pages
  - 6,295 media records
- English REST API: `https://inside.lgensol.com/en/wp-json/wp/v2`
  - 389 posts
  - 7 pages
  - 6,720 media records
- Sitemap indexes:
  - `https://inside.lgensol.com/sitemap_index.xml`
  - `https://inside.lgensol.com/en/sitemap_index.xml`
- Machine-readable inventory:
  - `https://inside.lgensol.com/llms.txt`
  - `https://inside.lgensol.com/en/llms.txt`
- Additional sitemap families:
  - pages
  - categories
  - B-Lab topic hubs
  - video-bearing posts
  - local content

The root sitemap contains 946 unique post URLs across Korean and English. The
English sitemap contains 390 post URLs, while the English REST API reports 389
posts. That one-record difference should be resolved during ingestion.

The current repo ingested only the 556 Korean REST posts. It did not ingest the
English posts, pages, B-Lab hubs, or other sitemap families.

### ENSOLPEDIA E-Book

- Landing pages:
  - `https://inside.lgensol.com/ensolpedia/`
  - `https://inside.lgensol.com/en/ensolpedia/`
- Readers:
  - `https://inside.lgensol.com/src/ebook/2026/ko/ecatalog5.php?Dir=`
  - `https://inside.lgensol.com/src/ebook/2026/en/ecatalog5.php?Dir=`
- Both editions contain 126 pages.
- Page images are directly addressable:
  - Korean: `/src/ebook/2026/ko/catImage/657/s001.jpg` through `s126.jpg`
  - English: `/src/ebook/2026/en/catImage/658/s001.jpg` through `s126.jpg`
- Extracted page text:
  - Korean: `/src/ebook/2026/ko/catImage/657/search.xml`
  - English: `/src/ebook/2026/en/catImage/658/search.xml`
- Text coordinates are available as `coords.xml`.

This is a separate ingestion format and was completely missed by the current
WordPress post scraper.

### Corporate Website

- Base: `https://www.lgensol.com/`
- Working desktop languages: Korean, English, Chinese, German, and Polish.
- Japanese is advertised through `hreflang`, but `/ja/index` returned 404 when
  checked.
- The English navigation exposes about 80 content routes covering products,
  services, company information, R&D, sustainability, IR, careers, and support.
- There is no public `sitemap.xml`; discovery must crawl navigation and page
  links.
- Corporate newsroom:
  - Page: `https://www.lgensol.com/en/company/newsroom`
  - AJAX list: `/company/company-newsroom/newsroomListAjax.ajax`
  - AJAX count: `/company/company-newsroom/newsroomListCountAjax.ajax`
  - 45 English newsroom records were reported when checked.
- Download library:
  - Page: `https://www.lgensol.com/en/etc/cs-filedown`
  - AJAX list: `/etc/fileDown/fileDownListAjax.ajax`
  - AJAX count: `/etc/fileDown/fileDownListCountAjax.ajax`
  - 103 English download records were reported when checked.
- Documents are hosted primarily under `/upload/file/` and `/assets/file/`.

The download library includes product catalogs, safety guides, ESG reports,
financial statements, earnings materials, shareholder materials, and bond
reports.

### Global Newsroom

- Base: `https://news.lgensol.com/`
- Search engines expose press releases, supplementary stories, contact pages,
  and subscriptions.
- Direct requests from the current runtime receive HTTP 403 from the load
  balancer, including `robots.txt`, feeds, and sitemap candidates.

Treat this as a distinct source. It requires a compliant access strategy or a
comparison against the corporate site's AJAX newsroom before ingestion.

## Priority 2: Regional and Product Sites

### Regional LGES Sites

- `https://lgensol.pl/`
  - 303 posts and 46 pages in its WordPress sitemaps
- `https://lgenergymi.com/`
  - 86 posts and 18 pages
- `https://lgensol-vt.com/`
  - 22 posts, 10 pages, and 50 job records
- `https://www.lghomebattery.com.au/`
  - 34 blog posts and 23 pages
- `https://www.lgessbattery.com/`
  - Regional content trees for US, Europe, and Australia
  - Product information, grid-scale ESS, home batteries, news, case stories,
    FAQs, and partner information
- `https://recall.lgessbattery.com/`
  - Product recall and serial-number checking; operational rather than general
    wiki content

### Product and Service Sites

- `https://www.kooroo.co.kr/` - KooRoo battery swapping service
- `https://bridge.lgensol.com/` - open innovation programs such as BIC and OSS

BRIDGE is public but application-oriented. Only public program descriptions and
announcements are likely useful to the wiki.

## Priority 3: Joint Ventures and Affiliates

These sites are linked by LGES's corporate global-network or careers pages.

- `https://www.ultiumcell.com/` - 14 sitemap pages
- `https://nextstar-energy.com/` - 37 posts and 22 pages
- `https://lhbattery.com/` - LGES/Honda venture; 8 posts and 5 pages
- `https://hlgabattery.com/` - Hyundai/LGES Georgia venture; 6 sitemap pages
- `https://www.hligreenpower.com/` - Hyundai/LGES Indonesia venture
- `https://www.lgchemmich.com/` - legacy Michigan domain; currently protected
  by Cloudflare from this runtime

These sources are useful for plant history, local operations, employment,
community programs, and venture-specific announcements. They should remain
separate source namespaces to avoid presenting venture claims as general LGES
claims.

## Authoritative External Sources

Useful for verification rather than primary bulk scraping:

- Korean DART and English DART regulatory filings
- LG Corp press releases
- partner press rooms such as GM, Honda, Hyundai, and Stellantis
- peer-reviewed papers and university announcements for joint research
- official LGES YouTube channels for videos and transcripts

## Excluded Operational Systems

Do not crawl these into the wiki corpus:

- `https://vars.lgensol.com/` - Vendor Account Registration System
- `https://partners.lgensol.com:8001/` - partner portal
- `https://gcp.lgensol.com/` - authenticated portal
- `https://global.lgensol.com/` - corporate VPN/login
- procurement and supplier registration portals
- job boards, application forms, installer searches, and serial-number tools

## Recommended Ingestion Order

1. Complete Battery Inside discovery using both REST APIs and sitemap
   reconciliation.
2. Ingest the Korean and English ENSOLPEDIA text XML, retaining page-level image
   references and license metadata.
3. Crawl the corporate site's language navigation, AJAX newsroom, and AJAX
   download library.
4. Compare and deduplicate the separate global newsroom.
5. Add regional LGES sites and ESS product sites.
6. Add joint-venture sites under separate source namespaces.
7. Use regulatory filings and partner sources for verification and conflict
   resolution.

Every ingested record should retain `source_url`, source family, language,
publication/modified date, retrieval date, content hash, and licensing or usage
restrictions.
