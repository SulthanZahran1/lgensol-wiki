---
title: NCA Battery
created: 2026-06-05
updated: 2026-06-08
type: entity
tags: [nca, cathode, energy-density, power-density, cylindrical]
sources:
  - raw/battery-inside-en/en/tech-en/infographics-10-nca-cathode.md
  - raw/battery-inside-en/en/tech-en/infographics-11-ncma-cathode.md
  - raw/battery-inside-en/en/tech-en/infographics-cathode-materials.md
  - raw/ko/opinion/%eb%a6%ac%ed%8a%ac%ec%9d%b4%ec%98%a8%eb%b0%b0%ed%84%b0%eb%a6%ac%ec%9a%a9-%ec%96%91%ea%b7%b9%ec%9e%ac-%ea%b8%b0%ec%88%a0-%ea%b0%9c%eb%b0%9c-%eb%b0%a9%ed%96%a5-%ea%b3%a0%eb%8b%88%ec%bc%88%ed%99%94.md
  - raw/battery-inside-en/en/tech-en/infographics-9-ncm-cathode.md
confidence: high
---
# NCA Battery

## Overview

NCA (Nickel Cobalt Aluminum) batteries use a layered cathode of the form LiNi₁₋ₓ₋ᵧCoₓAlᵧO₂ (space group R‾3m). As a nickel-rich chemistry, NCA delivers high specific energy (250–300 Wh/kg at the cell level, with advanced 21700 cells reaching up to 320 Wh/kg) and excellent power capability—sustained discharge rates above 3C and pulse discharges exceeding 5C. This makes NCA a preferred choice for premium electric vehicles (EVs), power tools, and high-power cylindrical cells. The chemistry was first commercialized by Panasonic for Tesla’s Model S in 2012, and remains a benchmark for high‑energy cylindrical cells.

## Technical Details

### Composition and Elemental Roles

In conventional NCA, nickel (Ni) constitutes 80 mol% of the transition metal content, cobalt (Co) about 15 mol%, and aluminum (Al) about 5 mol%. Nickel provides the primary capacity via the Ni²⁺/Ni³⁺/Ni⁴⁺ redox couple, delivering a reversible capacity of ~200 mAh g⁻¹ at 4.2 V vs. Li/Li⁺. Cobalt stabilises the layered structure, enhances rate capability, and improves cycle life, but its high cost and supply concentration (60 % of global reserves in the Democratic Republic of Congo) drive the industry toward “decobalization.” Aluminum (1–5 mol%) substitutes for part of the cobalt, acting as a structural pillar that suppresses the undesirable H2→H3 phase transition during delithiation. This reduces anisotropic lattice strain and microcracking, thereby improving thermal stability and safety. Newer formulations (e.g., NCA‑90: 90 % Ni, 5 % Co, 5 % Al; NCA‑95: 95 % Ni, 2 % Co, 3 % Al) push energy density further while lowering cobalt content.

### Electrochemical Performance

NCA cells have a nominal voltage of 3.6–3.7 V and a maximum charge voltage of 4.2 V (4.3 V in advanced variants). The high nickel content yields an energy density of 250–300 Wh kg⁻¹ and 650–750 Wh L⁻¹ in cylindrical formats. Cycle life typically ranges from 500 to 1500 cycles to 80 % state of health (SOH), depending on depth of discharge and charging rate. The rate capability is excellent: sustained 3C discharge and pulses above 5C are routine, making NCA suitable for both EV traction and high‑power applications like power tools.

### Degradation Mechanisms

NCA suffers from several degradation pathways, particularly at elevated temperatures (>45 °C):

1. **Electrolyte decomposition** catalysed by highly reactive Ni⁴⁺ species at the cathode surface, leading to impedance growth.
2. **Transition metal dissolution** (Ni, Co) into the electrolyte, followed by deposition on the anode, which disrupts the solid‑electrolyte interphase (SEI).
3. **Oxygen release** from the NCA lattice when overcharged or at high state of charge, a key precursor to thermal runaway.
4. **Microcracking** of secondary particles due to anisotropic volume changes during cycling. These cracks allow electrolyte penetration into the particle interior, accelerating side reactions and capacity fade.

These issues are mitigated by particle coatings (e.g., Al₂O₃, TiO₂, LiNbO₃), electrolyte additives (vinylene carbonate, FEC, PS), and advanced cell design including pressure management, current interrupt devices (CIDs), and rupture vents.

### Safety Characteristics

NCA’s thermal stability is lower than that of mid‑nickel NCM or LFP. Onset temperature for thermal runaway in fully charged cells is typically 150–180 °C, compared to 180–200 °C for NCM 622 and >250 °C for LFP. The Al doping improves structural integrity, but the highly oxidative Ni⁴⁺ state at full charge remains a concern. Consequently, NCA cells require robust pack‑level thermal management (keeping cell temperatures below 45 °C), and the cylindrical format (18650, 21700, 4680) offers inherent pressure containment advantages over pouch cells. Safety features such as CIDs, positive temperature coefficient (PTC) elements, and venting are standard.

## Significance and LG Energy Solution’s Role

LG Energy Solution (LGES) is a leading producer of NCA cylindrical cells for EVs and power tools. The company’s 21700 cells for premium EVs achieve energy densities of 270 Wh kg⁻¹ and are used in high‑performance segments. LGES has invested heavily in securing supply of battery‑grade nickel and cobalt: for example, a 35 billion KRW investment in Greatpower Nickel & Cobalt Materials for 20 kt of nickel over six years, and offtake agreements with Australian Mines (71 kt Ni, 7 kt Co over six years) and QPM (70 kt Ni, 7 kt Co over ten years). These long‑term contracts strengthen LGES’s raw‑material supply chain and enable the company to meet growing global demand for high‑nickel batteries.

LGES is also advancing NCA toward quaternary NCMA (nickel‑cobalt‑manganese‑aluminum) cathodes. By adding manganese, LGES aims to improve thermal stability and cycle life while maintaining the high energy density of NCA. The company’s “Premium” battery segment relies on high‑nickel NCMA, and LGES is developing single‑crystal cathode technology to suppress microcracking and extend lifespan. The shift to single‑crystal particles (instead of polycrystalline aggregates) reduces stress concentration and electrolyte ingress, enabling stable operation at higher voltages and over longer cycle life.

Despite growing competition from LFP in entry‑level EVs and from high‑nickel NCM in pouch/prismatic formats, NCA remains a dominant chemistry in cylindrical form factors—especially the 4680‑format cells that Tesla and LGES are developing. The high power density and mature supply chain ensure NCA’s continued relevance in premium EVs and high‑rate applications.

## Related Pages

- [[ncma-battery|NCMA (Quaternary) Battery]]
- [[ncm-battery|NCM (Ternary) Battery]]
- [[46-series-battery|46‑Series Cylindrical Battery (4680/4695)]]
- [[cathode-tier-comparison|High‑Nickel vs Mid‑Nickel vs LFP]]
- [[high-nickel-battery|High‑Nickel Battery]]
- [[cell-format-comparison|Cell Form Factor Comparison (Cylindrical vs Pouch vs Prismatic)]]
