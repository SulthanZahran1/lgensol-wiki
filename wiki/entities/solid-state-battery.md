---
title: All-Solid-State Battery
created: 2026-06-05
updated: 2026-06-08
type: entity
tags: [solid-state, electrolyte, safety, energy-density, anode]
sources:
  - raw/battery-inside-en/en/tech-en/game-changer-battery-all-solid-state-battery-the-ultimate-battery-that-delivers-higher-s-79332ecd61.md
  - raw/battery-inside-en/en/news-en/a-new-solid-state-battery-surprises-the-researchers-that-created-it-2.md
  - raw/battery-inside-en/en/interview-en/a-battery-without-an-anode-lg-energy-solutions-research-on-combining-anodeless-and-solid-ae5b6bf6d7.md
  - raw/battery-inside-en/en/news-en/lg-energy-solution-demonstrates-sulfur-cathode-technology-for-all-solid-state-batteries.md
  - raw/battery-inside-en/en/interview-en/how-will-semi-solid-state-batteries-change-our-lives.md
confidence: high
---
# All-Solid-State Battery

## Overview

All-Solid-State Batteries (ASSBs) replace the flammable liquid electrolyte and porous separator found in conventional lithium-ion batteries with a solid electrolyte layer that is inherently non-flammable and mechanically robust. This fundamental architectural shift eliminates the risk of electrolyte leakage and thermal runaway while enabling the use of high-capacity anodes—such as lithium metal (theoretical capacity 3,860 mAh/g, over ten times that of graphite’s 372 mAh/g) or advanced silicon composites. By also allowing bipolar stacking of cells, ASSBs can achieve pack-level energy densities exceeding 350 Wh/kg, with roadmaps targeting 500 Wh/kg and beyond by the early 2030s. Prominent automakers and battery manufacturers, including LG Energy Solution, Toyota, and Samsung SDI, have announced mass-production targets around 2027–2028, positioning ASSBs as a transformative technology for electric vehicles (EVs), aerospace, and grid storage.

## Technical Details

### Solid Electrolyte Families

The solid electrolyte is the core enabler. Three major classes are under active development:

- **Sulfide-based electrolytes** (e.g., Li₆PS₅Cl, Li₃PS₄) exhibit the highest room-temperature ionic conductivity, reaching 10⁻² to 10⁻³ S/cm—comparable to liquid electrolytes. Their mechanical softness enables intimate contact with electrode particles without high-temperature sintering. However, sulfides are extremely moisture-sensitive, releasing toxic H₂S gas upon exposure, and have a narrow electrochemical window (stable only up to ~2.5 V vs. Li/Li⁺), necessitating protective coatings on high-voltage cathodes. LG Energy Solution’s research has focused on sulfide-based systems for their superior kinetics.

- **Oxide-based electrolytes** (e.g., Li₇La₃Zr₂O₁₂, LLZO) offer excellent air stability and a wide electrochemical window (up to 5 V vs. Li/Li⁺), but their ionic conductivity is lower, typically 10⁻⁴ to 10⁻⁵ S/cm at 25 °C. They are brittle and require high-temperature sintering (≥1000 °C) for densification, complicating integration with electrode materials. Research continues on reducing grain-boundary resistance and enabling thin-film fabrication.

- **Polymer-based electrolytes** (e.g., PEO-LiTFSI) are flexible and compatible with roll-to-roll processing, allowing thin films down to 10–20 µm. Their conductivity at room temperature is low (10⁻⁶ S/cm), so they often operate at 60–80 °C. Composite variants incorporating ceramic fillers (e.g., LLZO nanoparticles) can boost conductivity to 10⁻⁴ S/cm while retaining flexibility.

### Anode Options and Dendrite Suppression

Lithium metal anodes offer the highest theoretical capacity but are prone to dendrite growth. A solid electrolyte with shear modulus >4 GPa can physically block dendrites, yet defects and grain boundaries still permit lithium penetration at current densities above 1 mA/cm². Strategies include using dense, thin ceramic layers, introducing compliant interlayers (e.g., a polymer film), or adopting hybrid solid-liquid interfaces. Silicon anodes—which undergo ~300% volume expansion during cycling—benefit from the rigid electrolyte’s mechanical constraint, but interfacial contact loss remains a challenge.

LG Energy Solution has pioneered an “anodeless” architecture for ASSBs, where no anode active material is present initially. Instead, lithium plates directly onto a current collector during charging. The company’s patented approach uses a lithiophilic material coating (LPM) combined with oxidation treatment on the current collector, ensuring uniform lithium deposition and suppressing dendrite formation. This design eliminates the need for a thick anode layer, boosting energy density by up to 30% and simplifying manufacturing.

### Cell Architecture and Bipolar Stacking

Because the solid electrolyte is both ion-conducting and electron-insulating, cells can be stacked in a bipolar arrangement: one cell’s cathode current collector directly contacts the next cell’s anode current collector, eliminating copper/aluminum tabs and external wiring. This increases pack-level voltage and energy density by 20–30% compared to conventional parallel-series wiring. LG Energy Solution has demonstrated bipolar-stacked all-solid-state cells using a sulfide electrolyte and nickel-rich layered cathode, targeting 900 Wh/L at the cell level.

## Significance and LG Energy Solution Context

### Safety and Performance Advantages

ASSBs eliminate flammable organic solvents (e.g., EC, DMC), drastically reducing thermal runaway risk. Even under nail penetration or overcharge, solid cells generate minimal heat and no combustible gas. The solid electrolyte also widens the operating temperature range (-20 °C to 100 °C), reducing thermal management costs. Energy density projections for ASSBs range from 350 Wh/kg to over 500 Wh/kg at pack level, compared to ~250 Wh/kg for today’s best liquid-based packs. Additionally, the solid electrolyte acts as a robust barrier against dendrite penetration, enabling safe operation with lithium metal anodes.

### LG’s Research Milestones

LG Energy Solution has pursued multiple solid-state pathways through its Future Technology Center and global collaborations:

- **Room-temperature, long-life cell with UCSD**: In 2021, LGES and UCSD published in *Science* a sulfide-based ASSB using micro-silicon anode (5 µm particles) without conductive additives or binders. This cell retained >80% capacity after 500 cycles at room temperature (25 °C) and offered 40% higher energy density than commercial Li-ion.

- **Sulfur cathode success**: In 2026, LGES announced in *Nature Communications* a sulfide-based ASSB employing a sulfur cathode. By replacing liquid electrolyte with solid, the polysulfide shuttle effect was eliminated, achieving ~1,500 mAh/g capacity in pouch cells—a crucial step toward >600 Wh/kg cells.

- **Anodeless integration**: LGES has filed patents combining anodeless architecture with sulfide solid electrolytes, focusing on uniform lithium plating via lithiophilic coatings and oxidation treatment. This approach simplifies fabrication and reduces material costs while boosting energy density.

- **Bipolar architecture**: LGES is developing scalable manufacturing processes—dry electrode coating and co-sintering—for bipolar-stacked ASSBs, aiming for commercialization by 2028.

### Industry Outlook

Current challenges include high manufacturing cost (estimated >$200/kWh for early production), interfacial resistance between solid electrolyte and electrodes, and long-term cycling stability (target >1,000 cycles at 80% capacity retention). As these are addressed, ASSBs are projected to capture 10–20% of the global battery market by 2035, initially in premium EVs and niche applications such as medical implants and aviation.

## Related Pages

- [[liquid-vs-solid-electrolyte|Liquid Electrolyte vs Solid Electrolyte]]
- [[lithium-metal-battery|Lithium Metal Battery]]
- [[separator|Separator]]
- [[bipolar-technology|Bipolar Technology]]
- [[azs-stacking|AZS (Advanced Z-Stacking)]]
- [[next-gen-battery-overview|Next-Generation Battery Comprehensive Comparison]]
- Sulfur Cathode
- [[cei|Cathode Electrolyte Interphase (CEI)]]