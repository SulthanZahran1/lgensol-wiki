---
title: Ternary Battery
created: 2026-06-05
updated: 2026-06-08
type: glossary
tags: [ncm, nca, cathode, energy-density]
sources:
  - raw/battery-inside-en/en/tech-en/battery-glossary-ternary-battery.md
  - raw/battery-inside-en/en/tech-en/infographics-10-nca-cathode.md
  - raw/battery-inside-en/en/tech-en/infographics-9-ncm-cathode.md
  - raw/battery-inside-en/en/tech-en/infographics-cathode-materials.md
  - raw/battery-inside-en/en/tech-en/infographics-11-ncma-cathode.md
confidence: high
---
# Ternary Battery

## Overview

A ternary battery uses a three-metal cathode system based on layered lithium metal oxides (Li[Ni,Co,Mn]O₂ or Li[Ni,Co,Al]O₂), where M represents three different transition metals. The two most common ternary families are **NCM** (Nickel-Cobalt-Manganese) and **NCA** (Nickel-Cobalt-Aluminum). Both are derived from the foundational **LCO** (Lithium Cobalt Oxide, LiCoO₂) structure, with additional metal elements substituted to tailor performance. Ternary cathodes are the dominant chemistry for high-energy-density applications, particularly in electric vehicles (EVs) and premium portable electronics.

The term “ternary” refers to the three transition metal cations in the cathode active material. In NCM, these are Ni, Co, and Mn; in NCA, Ni, Co, and Al. Each element contributes distinct properties: Nickel primarily drives energy density, Cobalt ensures structural stability and rate capability, Manganese improves safety and reduces cost, and Aluminum enhances power output and structural integrity. The exact ratio of these elements, denoted by numbers following the chemistry name (e.g., NCM811, NCM622), allows manufacturers to optimize for specific trade-offs between energy, power, safety, and cost.

## Technical Details

### Composition and Elemental Roles

- **Nickel (Ni)**: The primary active redox center. Higher nickel content increases the number of lithium ions that can be reversibly extracted (delithiation), directly boosting specific capacity and energy density. Modern high‑nickel compositions (NCM811, NCM9, NCA with 80–90% Ni) achieve gravimetric capacities exceeding 200 mAh/g.
- **Cobalt (Co)**: Stabilizes the layered α‑NaFeO₂ crystal structure, reducing cation mixing and suppressing phase transitions during cycling. Cobalt also enhances rate capability (fast charge/discharge) by improving lithium‑ion diffusion kinetics. However, Co is expensive, geopolitically concentrated, and accounts for roughly 20% of total battery material cost.
- **Manganese (Mn)**: Provides a robust structural framework at low cost. Mn⁴⁺ remains electrochemically inactive above ~4.3 V vs. Li/Li⁺, acting as a “spacer” that improves thermal stability and reduces oxygen release during overcharge or abuse. Manganese also lowers raw material cost.
- **Aluminum (Al)**: In NCA, Al substitutes for Mn. Al³⁺ strengthens the metal‑oxygen bonds, improving structural integrity at high states of charge and delivering superior power output. NCA cells typically exhibit higher operating voltage (up to 4.2 V) and good cycle life for cylindrical‑format cells.

### Notation and Stoichiometry

Ternary compositions are specified by the molar ratio of Ni:Co:Mn (or Ni:Co:Al) in the cathode. For example:
- **NCM111** (1:1:1): symmetric, moderate energy density (~160 mAh/g), balanced safety and cost.
- **NCM523** (5:2:3): mid‑nickel, common in early‑generation EV batteries.
- **NCM622** (6:2:2): higher energy density with still‑manageable cobalt content.
- **NCM712** (7:1:2): further reduced Co, enabled by advanced synthesis and surface coatings.
- **NCM811** (8:1:1): high‑nickel (80% Ni), specific capacity ~190–200 mAh/g, but requires careful electrolyte and separator engineering to mitigate degradation.
- **NCA** typically has Ni ≥80%, Co 5–15%, Al 1–5%. For instance, Panasonic/LG‑style NCA used in cylindrical cells often contains ~80 % Ni, 15 % Co, 5 % Al.

The push toward **high‑nickel** (Ni ≥60%, often 80‑90%) aims to maximize energy density and reduce cobalt dependency. Conversely, **mid‑nickel** formulations (Ni 40–60%) with elevated Mn content are developed for higher safety and longer cycle life, often paired with high‑voltage operation (above 4.45 V) to compensate for lower capacity.

### Crystal Structure and Degradation Mechanisms

Ternary cathodes adopt a layered α‑NaFeO₂ structure (space group R‾3m) where lithium ions occupy octahedral sites between transition‑metal‑oxygen slabs. During charging, lithium is deintercalated, and the oxidation state of Ni changes from Ni²⁺ to Ni⁴⁺ (and Co³⁺ to Co⁴⁺ at high voltages). This reversible process can be compromised by:

- **Cation mixing**: Ni²⁺ ions (similar ionic radius to Li⁺) can migrate into lithium sites, blocking diffusion paths and reducing capacity.
- **Oxygen release**: At high states of charge and elevated temperatures, the lattice can lose oxygen, leading to thermal runaway. High‑nickel compositions are more prone to this.
- **CEI (Cathode Electrolyte Interphase)**: A passivation layer formed on the cathode surface during initial cycles by oxidative decomposition of the electrolyte. Ideally, the CEI is Li‑ion conductive but electron‑blocking, preventing further electrolyte breakdown. In high‑voltage or high‑nickel systems, CEI stability becomes critical for cycle life. LG Energy Solution has dedicated research to [[cei|CEI stabilization]] to reduce transition metal dissolution (Ni, Co, Mn) and parasitic reactions.

### Electrochemical Performance

- **Voltage**: Typical operating window: 2.5–4.2 V (NCA), up to 4.45 V for mid‑nickel NCM with advanced electrolytes. Higher voltage increases energy but accelerates degradation.
- **Capacity**: Specific capacity ranges from ~150 mAh/g (low‑Ni) to >200 mAh/g (NCM9/NCA with 90% Ni).
- **Rate capability**: Cobalt and aluminum improve Li⁺ diffusivity; NCA generally rates higher than NCM for identical Ni content.
- **Cycle life**: Mid‑nickel (NCM523, NCM622) often exceeds 1500 cycles at 1C/1C; high‑nickel NCM811 or NCA may achieve 800–1200 cycles under moderate conditions, depending on cell design and thermal management.

## Significance and LG Energy Solution Context

### Market Dominance

Ternary batteries power the vast majority of current‑generation EVs—from compact cars to long‑range sedans and SUVs—because they offer the highest commercially available energy density (250–300 Wh/kg at cell level). The flexibility to tune Ni/Co/Mn ratios enables automakers to balance range, cost, and safety. For example, Tesla’s 4680 cells use a high‑nickel NCA/LFP‑blended approach, while GM’s Ultium platform employs NCMA (quaternary, adding Al to NCM) to reduce cobalt and improve safety.

### LG Energy Solution’s Portfolio

LG Energy Solution is a leading manufacturer of ternary cathode cells, supplying both NCM and NCA chemistries to global automakers and the energy storage industry. Key formulations include:

- **Mid‑nickel NCM (NCM523, NCM622)**: Used in earlier‑generation EVs (Chevrolet Bolt, Renault Zoe) and for applications favoring long cycle life and high safety.
- **High‑nickel NCM (NCM712, NCM811)**: Deployed in long‑range EVs (e.g., Hyundai Ioniq 5, Kia EV6) with improved energy density.
- **NCMA (Nickel‑Cobalt‑Manganese‑Aluminum)**: A quaternary cathode that combines the advantages of NCM (Mn for safety) and NCA (Al for structural stability). LG has commercialized NCMA for cylindrical (2170, 4680) and pouch cells, achieving high energy density with reduced cobalt (typically 5% or less).
- **NCA for cylindrical cells**: Used in power tools and early Tesla Roadster/Model S packs; LG’s NCA cells feature high power output and compact form factor.

### Safety and Reliability Innovations

To address the inherent risks of ternary chemistries—thermal runaway at high states of charge, and degradation at high voltage—LG Energy Solution has developed proprietary technologies:
- **[[srs|SRS (Safety Reinforced Separator)]]**: A ceramic‑coated separator that resists dendrite penetration and thermal shrinkage.
- **Surface coatings**: Alumina, boehmite, or lithium‑ion conductive oxides on cathode particles to suppress oxygen evolution and CEI instability.
- **Electrolyte additives**: Fluorinated solvents and film‑forming agents (e.g., LiDFOB, FEC) to form robust CEI layers.

### Future Directions

The industry continues to push toward higher nickel content (up to 90–95%) while reducing cobalt below 1%. LG is also researching **cobalt‑free layered cathodes** (e.g., LNMO, LMR‑NMC) and high‑voltage spinels. However, ternary batteries remain the workhorse for next‑generation EVs until solid‑state or lithium‑sulfur technologies mature.

## Related Pages

- [[cathode-materials|Cathode Material]]
- [[nca-battery|NCA Battery]]
- [[ncm-battery|NCM (Ternary) Battery]]
- [[cathode-tier-comparison|High-Nickel vs Mid-Nickel vs LFP]]
- [[high-nickel-battery|High-Nickel Battery]]
- [[lfp-battery|LFP (Lithium Iron Phosphate) Battery]]
- [[cei|CEI (Cathode Electrolyte Interphase)]]
- [[srs|SRS (Safety Reinforced Separator)]]