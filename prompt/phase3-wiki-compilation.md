# Phase 3: Wiki Compilation — Build a Karpathy-Style LLM Wiki from 556 Korean Battery Blog Posts

You are building a Karpathy-style LLM wiki from 556 Korean-language blog posts scraped from LG Energy Solution's official blog (inside.lgensol.com/ko). The raw data is at `~/lgensol-wiki/raw/ko/`. Your output goes to `~/lgensol-wiki/wiki/`.

## Output Structure

Create this directory and populate it:

```
~/lgensol-wiki/wiki/
├── SCHEMA.md              # Domain rules, tag taxonomy, conventions
├── index.md               # Sectioned content catalog with one-line summaries
├── log.md                 # Chronological action log
├── raw/                   # Layer 1: Symlinks or references to raw/ko/ files
├── entities/              # Layer 2: Entity pages (people, orgs, products, models)
│   ├── lg-energy-solution.md
│   ├── tesla.md
│   ├── lfp-battery.md     # Lithium Iron Phosphate
│   ├── ncm-battery.md      # Nickel Cobalt Manganese
│   ├── solid-state-battery.md
│   ├── ...
├── concepts/              # Layer 2: Concept/topic pages
│   ├── electrolyte.md
│   ├── anode-materials.md
│   ├── cathode-materials.md
│   ├── separator.md
│   ├── battery-management-system.md
│   ├── energy-storage-system.md
│   ├── fast-charging.md
│   ├── thermal-runaway.md
│   ├── battery-recycling.md
│   ├── cell-to-pack.md
│   ├── ...
├── comparisons/           # Layer 2: Side-by-side analyses
│   ├── lfp-vs-ncm.md
│   ├── liquid-vs-solid-electrolyte.md
│   ├── pouch-vs-prismatic-vs-cylindrical.md
│   └── ...
└── glossary/              # Layer 2: Dictionary/glossary terms
    ├── baas.md
    ├── coulombic-efficiency.md
    ├── ionic-conductivity.md
    ├── dendrite.md
    ├── c-rate.md
    ├── soc-soh.md
    └── ...
```

## Step-by-Step Instructions

### Step 1: Create SCHEMA.md

Write SCHEMA.md with:
- **Domain:** Battery technology, LG Energy Solution, EV/ESS industry
- **Conventions:** lowercase-hyphen filenames, YAML frontmatter on every page, [[wikilinks]] between pages, every page must have 2+ outbound links
- **Tag taxonomy** (categories below)
- **Frontmatter template** with: title, created, updated, type (entity|concept|comparison|glossary), tags, sources (list of raw file paths), confidence (high|medium|low)
- **Page thresholds:** Create a page when topic appears in 2+ sources OR is central to one source
- **Update policy:** Newer sources supersede older ones; note contradictions explicitly

### Step 2: Ingest Raw Sources (Batch Processing)

Read ALL files in `~/lgensol-wiki/raw/ko/tech/` first (the deepest content), then `news/`, then `story/`, then the rest. For each source:

1. Extract the title, date, category, tags from YAML frontmatter
2. Read the markdown body and identify key entities, concepts, and glossary terms mentioned
3. For entities/concepts that meet the page threshold, add to your mental map for wiki page creation
4. For glossary terms (Battery Glossary series), note them separately

### Step 3: Create Wiki Pages

#### Entity Pages
Create one page per notable entity. Examples:
- LG Energy Solution (the company itself — central entity)
- Tesla (ESS partner, customer)
- GM, Stellantis, Honda, Hyundai (partners/customers)
- LFP Battery, NCM Battery, LMR Battery, Solid-State Battery, Lithium-Sulfur Battery, Sodium-Ion Battery
- Key technologies: AZS (Advanced Z-Stacking), EOL Process, CTP (Cell-to-Pack), LPM Coating

For each entity page include:
- Overview / what it is
- Key facts and dates
- Relationships to other entities ([[wikilinks]])
- Source references to raw files

#### Concept Pages
Create one page per concept or topic. Examples:
- Electrolyte (composition, types, market outlook)
- Anode Materials (graphite, silicon, silicon oxide, carbon composites)
- Cathode Materials (NCM, LFP, LMR, high-nickel)
- Separator technology
- Battery Management System (BMS)
- Energy Storage System (ESS)
- Battery Manufacturing Process (electrode, assembly, formation, aging, EOL)
- Thermal Runaway and safety
- Fast Charging technology
- Battery Recycling
- Cell Balancing
- Battery degradation mechanisms

For each concept page include:
- Definition / explanation
- Current state of knowledge (from the blog posts)
- Related concepts ([[wikilinks]])
- Source references

#### Glossary Pages
Create one page per glossary term from the "Battery Glossary" series. Terms found so far include:
- BaaS (Battery as a Service)
- BMTS (Battery Management Total Solution)
- CTP (Cell-to-Pack)
- Coulombic Efficiency (CE)
- Ionic Conductivity
- TP Prevention Technology
- EaaS (Energy as a Service)
- Anodeless Battery
- Internal Resistance
- Dendrite
- SoC (State of Charge) / SoH (State of Health)
- Gas Free Solvent
- BBU (Battery Backup Unit)

#### Comparison Pages
Create side-by-side analyses. Examples:
- LFP vs NCM: cost, safety, energy density, lifespan
- Liquid Electrolyte vs Solid Electrolyte
- Pouch vs Prismatic vs Cylindrical cell formats
- High-Nickel vs Mid-Nickel vs LFP cathodes
- Wet vs Dry electrode processes

### Step 4: Create index.md

Build a sectioned index with one-line summaries for every page. Sections:
- Entities
- Concepts
- Comparisons
- Glossary

### Step 5: Create log.md

Write an initial log entry documenting what was created.

## Quality Standards

1. **Every wiki page must have YAML frontmatter** with: title, created, updated, type, tags, sources
2. **Every page must have 2+ [[wikilinks]]** to other pages
3. **Every page must reference source files** in the `sources:` frontmatter field (list of raw file paths relative to ~/lgensol-wiki/raw/ko/)
4. **Keep pages scannable** — readable in 30 seconds, split over 200 lines
5. **Use the tag taxonomy** — do not invent freeform tags
6. **Update index.md** after every page creation
7. **Write in Korean** since all source material is in Korean
8. **For claims from specific sources**, append `^[raw/ko/<category>/<file>.md]` markers at paragraph end when combining 3+ sources on one page

## Tag Taxonomy

Use these tags consistently:

- **Chemistry:** lfp, ncm, nca, lmrp, lithium-sulfur, sodium-ion, solid-state, lmo
- **Components:** cathode, anode, electrolyte, separator, binder, conductive-additive, current-collector
- **Properties:** energy-density, power-density, cycle-life, fast-charging, safety, thermal-stability
- **Manufacturing:** electrode, slurry, coating, drying, calendering, stacking, winding, formation, aging, eol
- **Applications:** ev, ess, uam, aerospace, mobility, battery-swapping, ess-storage
- **Business:** earnings, partnership, investment, plant, supply-chain, recycling, esg, open-innovation
- **Technology:** bms, bmts, ctp, ccb, azs, lpm, cell-balancing, thermal-management
- **Meta:** comparison, glossary, interview, news, opinion, timeline

## Important Notes

- You have ~800 MB of images at `~/lgensol-wiki/assets/ko/` — do NOT copy them. Reference them in wiki pages using local paths: `![alt](assets/ko/<category>/<slug>/<image>.png)`
- The raw markdown files contain WordPress image URLs — those images may 404. Use the local asset paths from the YAML frontmatter `images:` field instead.
- Do NOT modify any files under `raw/` or `assets/` — they are immutable source material.
- Work in phases within the session: first SCHEMA.md + index.md + log.md, then batch-create entity pages, then concept pages, then glossary, then comparisons.
- If you hit the max turns limit before finishing, note what was completed and what remains.
- Focus on quality over quantity — a well-structured 80-page wiki is better than a bloated 200-page one with thin content.

## Verification Checklist

Before finishing:
- [ ] All pages have YAML frontmatter
- [ ] All pages have [[wikilinks]] to other pages
- [ ] index.md lists every page created
- [ ] log.md has entries documenting the work
- [ ] Tag taxonomy is respected
- [ ] No raw files were modified