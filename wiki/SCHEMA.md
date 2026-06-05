---
title: SCHEMA — Wiki Authoring Guide
created: 2026-06-05
updated: 2026-06-05
type: meta
tags: [meta]
---

# SCHEMA — LG Energy Solution Battery Wiki Authoring Guide

This wiki is an LLM knowledge base compiled from 556 Korean blog posts from the LG Energy Solution official blog (inside.lgensol.com/ko), compressed and structured in Karpathy style. All pages are maintained in English.

## Domain
Battery technology, LG Energy Solution, electric vehicles (EV), energy storage systems (ESS).
Battery materials (cathode, anode, electrolyte, separator), cell form factors, manufacturing processes, next-generation batteries,
battery management (BMS/BMTS), recycling, mineral supply chains, business and partnerships.

## Directory Structure (4 tiers)
- `raw/` — Primary source material (`raw/ko/`). Sources are **immutable** — do not modify.
- `entities/` — Entities: companies, organizations, people, products, battery types, key technologies.
- `concepts/` — Concepts and topics: materials, processes, properties, applications, safety.
- `comparisons/` — Side-by-side comparisons of two or more items.
- `glossary/` — Dictionary entries based on the "Battery Glossary" series.

## File Naming Convention
- Lowercase with hyphens (`lfp-battery.md`, `cell-to-pack.md`).
- Romanized slugs. Korean titles go in the frontmatter `title` field.

## Frontmatter Template (required on all pages)
```yaml
---
title: English Title
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: entity | concept | comparison | glossary | meta
tags: [taxonomy, tags, only]
sources:
 - raw/ko/<category>/<file>.md
confidence: high | medium | low
---
```
- `sources`: One or more primary source paths (relative to `~/lgensol-wiki/`).
- `confidence`: high if multiple sources agree, medium/low for single source or estimates.

## Link Rules
- Cross-page links use double-bracket wikilinks: format is `slug` or `slug|display name`
 wrapped in double brackets (e.g., `cell-to-pack`, `lfp-battery|LFP Battery`).
- **Every content page must cross-reference at least 3-5 other pages with outbound wikilinks.**
- Links to non-existent pages are allowed (planned content).

## Page Creation Threshold
- Create a page if a topic appears in **2+ sources**, or is **central to a single source**.
- Prefer well-structured pages readable in ~30 seconds over bloated 200+ line pages.

## Update Policy
- Newer sources supersede older ones.
- When sources conflict on numbers or claims, **note the conflict** in the body with dates.
- For amalgamated content (3+ sources), mark specific claims with `^[raw/ko/<category>/<file>.md]`.

## Images
- Images are NOT copied (~800MB total). Reference via local path if needed:
 `![description](assets/ko/<category>/<slug>/<image>.png)`.
- WordPress URLs in original markdown may 404 — use frontmatter `images:` paths instead.

## Tag Taxonomy (select from below only — no free tags)
- **Chemistry:** lfp, ncm, nca, ncma, lmrp, lithium-sulfur, sodium-ion, lithium-metal, solid-state, lmo, high-nickel, mid-nickel
- **Components:** cathode, anode, electrolyte, separator, binder, conductive-additive, current-collector, active-material
- **Properties:** energy-density, power-density, cycle-life, fast-charging, safety, thermal-stability, voltage
- **Manufacturing:** electrode, slurry, mixing, coating, drying, calendering, slitting-notching, stacking, winding, lamination, welding, formation, aging, eol, dry-electrode, wet-electrode
- **Applications:** ev, ess, uam, aerospace, mobility, battery-swapping, humanoid, commercial-vehicle
- **Business:** earnings, partnership, joint-venture, investment, plant, supply-chain, recycling, esg, open-innovation, mineral
- **Technology:** bms, bmts, ctp, ccb, azs, lpm, bipolar, cell-balancing, thermal-management, srs, soc, soh
- **Cell Form Factors:** cylindrical, pouch, prismatic, mono-cell, bi-cell, 46-series, 18650, 21700
- **Meta:** comparison, glossary, interview, news, opinion, timeline, meta, fundamentals

## Series → Wiki Mapping (primary source series)
- **Battery Glossary** (39 posts) → `glossary/`
- **The Omnipotent Battery Story** → materials & processes `concepts/`, some `entities/` (AZS etc.)
- **[Battery Pioneer]** → next-gen batteries `entities/`
- **World of Batteries Q&A / All about Battery** → Q&A → `concepts/`
- **(Infographic #N)** → manufacturing & materials `concepts/`
- **In Search of Battery Origins** → minerals/materials `concepts/`
- **news/about-us** → companies, partnerships, plants, products `entities/`

Related: [[index]] · [[log]]
