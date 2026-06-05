# LG Energy Solution Wiki — Project Context

## About
A Karpathy-style LLM wiki built from 556 Korean blog articles from LG Energy Solution's official blog (inside.lgensol.com/ko). The blog covers battery technology, company news, stories, and industry insights from 2020 to 2026.

## Directory Structure
```
~/lgensol-wiki/
├── raw/ko/              # Layer 1: 556 scraped blog posts (markdown + YAML frontmatter)
│   ├── tech/            # 146 articles — battery technology, deep dives
│   ├── news/            # 237 articles — press releases, earnings, partnerships
│   ├── story/           # 66 articles — behind-the-scenes, interviews, culture
│   ├── about-us/        # 50 articles — company intro
│   ├── uncategorized/   # 43 articles — interviews/culture
│   └── opinion/         # 14 articles — expert columns
├── assets/ko/           # 1,763 images organized by article slug (~800 MB)
├── prompt/              # Phase 3 prompts for Claude Code
│   └── phase3-wiki-compilation.md
├── discovered_urls.json # All 556 article metadata
└── scrapers/            # Python scraper scripts
```

## Raw File Format
Each `raw/ko/<category>/<slug>.md` file has:
- YAML frontmatter: `source_url`, `wp_id`, `title`, `date`, `modified`, `category`, `tags`, `sha256`, `ingested`, `featured_image`, `images: [asset paths]`
- Markdown body: HTML-to-markdown converted content via html2text
- Image references use WordPress URLs in markdown (e.g., `![](https://inside.lgensol.com/wp-content/...)` )
- Asset paths reference local files under `assets/ko/<category>/<slug>/`

## Phase 3 Goal
Compile a Karpathy-style LLM wiki at `~/lgensol-wiki/wiki/` from all 556 raw posts:
1. Read SCHEMA.md template from prompt file
2. Read all raw files in `raw/ko/` (start with tech, then news, story, etc.)
3. Identify entities (LG Energy Solution, Tesla, LFP, NCM, etc.), concepts (electrolyte, anode, cathode, BMS, ESS, etc.), and comparisons (LFP vs NCM, liquid vs solid electrolyte, etc.)
4. Create wiki pages with [[wikilinks]], cross-references
5. Build SCHEMA.md, index.md, log.md per Karpathy pattern

## Domain
Battery technology, LG Energy Solution, electric vehicles, energy storage systems (ESS), battery materials (cathode, anode, electrolyte, separator), battery manufacturing, next-gen batteries (solid-state, lithium-sulfur, sodium-ion), battery glossary terms, company news and partnerships.

## Key Tags for Taxonomy
- Battery chemistry: lfp, ncm, nca, lmrp, lithium-sulfur, sodium-ion, solid-state
- Components: cathode, anode, electrolyte, separator, binder, conductive-additive
- Concepts: energy-density, power-density, fast-charging, cycle-life, safety, thermal-runaway
- Manufacturing: electrode, slurry, coating, drying, stacking, formation, aging, eol
- Applications: ev, ess, uam, aerospace, battery-swapping, baas
- Business: earnings, partnership, investment, plant, supply-chain, recycling, esg