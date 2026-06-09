---
title: Cathode Material
created: 2026-06-05
updated: 2026-06-08
type: concept
tags: [cathode, active-material, ncm, nca, ncma, lfp]
sources:
  - raw/ko/opinion/%eb%a6%ac%ed%8a%ac%ec%9d%b4%ec%98%a8%eb%b0%b0%ed%84%b0%eb%a6%ac%ec%9a%a9-%ec%96%91%ea%b7%b9%ec%9e%ac-%ea%b8%b0%ec%88%a0-%ea%b0%9c%eb%b0%9c-%eb%b0%a9%ed%96%a5-%ea%b3%a0%eb%8b%88%ec%bc%88%ed%99%94.md
  - raw/ko/tech/%ec%9d%b8%ed%8f%ac%ea%b7%b8%eb%9e%98%ed%94%bd19-%ec%96%91%ea%b7%b9%ec%9e%ac-3%eb%8c%80%ec%9e%a5.md
  - raw/battery-inside-en/en/tech-en/infographics-11-ncma-cathode.md
  - raw/battery-inside-en/en/tech-en/infographics-cathode-materials.md
  - raw/battery-inside-en/en/tech-en/infographics-10-nca-cathode.md
confidence: high
---
# Cathode Material

## Overview/Introduction

Cathode material is the most cost‑critical and performance‑defining component of a lithium‑ion battery. It accounts for approximately 40% of the total cell cost and directly determines the cell’s operating voltage, specific capacity, energy density, thermal stability, and cycle life. During charging, lithium ions de‑intercalate from the cathode and migrate through the electrolyte to the anode; during discharge, the ions return while electrons flow through the external circuit. The cathode’s active material is a lithium metal oxide whose composition and crystal structure govern the fundamental electrochemical limits of the cell. Over the past decade, cathode development has focused on two major trends: **high‑nickel chemistries** to boost energy density, and **decobalization** to reduce cost and supply‑chain risk. This article explores the principal cathode families—NCM, NCA, NCMA, and LFP—with emphasis on the mechanisms that control performance and degradation, and on LG Energy Solution’s strategic innovations.

## Technical Details

### Layered Oxide Cathodes: NCM, NCA, and NCMA

The most widely deployed cathode family for electric vehicles (EVs) is based on a layered LiMO₂ structure (M = Ni, Co, Mn, Al). **NCM** (nickel‑cobalt‑manganese) and **NCA** (nickel‑cobalt‑aluminum) are ternary systems; **NCMA** (nickel‑cobalt‑manganese‑aluminum) is a quaternary system. In all these chemistries, the nickel content is the primary driver of energy density because Ni²⁺/Ni⁴⁺ redox provides a high theoretical specific capacity (~280 mAh g⁻¹) and a working voltage of ~3.6 V vs. Li/Li⁺. Nickel’s role is central: it increases the reversible capacity by enabling multiple electron transfers per atom, but this comes at the cost of structural stability.

NCM compositions are designated by the ratio of Ni:Co:Mn—e.g., NCM523 (50% Ni, 20% Co, 30% Mn) or NCM811 (80% Ni, 10% Co, 10% Mn). Higher‑nickel formulations offer higher capacity but introduce significant challenges:

- **Ni⁴⁺ instability:** During charging, nickel oxidizes to Ni⁴⁺, which is highly reactive with the electrolyte. This causes surface decomposition, formation of inactive nickel oxide phases (rock‑salt impurities), and loss of active lithium via side reactions.
- **Microcrack formation:** The anisotropic volume change of high‑Ni particles during cycling generates internal stress, leading to microcracks that propagate from the particle surface inward. These cracks provide pathways for electrolyte penetration, accelerating side reactions and capacity fade. The cracking severity increases with nickel content.
- **Thermal stability degradation:** Ni–O bonding energy is weaker than that of Co–O or Mn–O, making high‑Ni cathodes more prone to oxygen release at elevated temperatures, which can trigger thermal runaway.

To mitigate these issues, industry has adopted several strategies:

1. **Concentration gradient particles:** The nickel content is graded from a high‑Ni core (high capacity) to a low‑Ni, Mn‑rich shell (high stability). This microstructure effectively distributes stress and reduces electrolyte contact. LG Energy Solution has invested in manufacturing this design.
2. **Doping and coating:** Elements such as Al, Ti, or Zr are doped into the lattice to suppress Ni⁴⁺ reactivity, and surface coatings (e.g., Al₂O₃, TiO₂) are applied to block direct electrolyte contact.
3. **Rod‑shaped primary particles:** A radially aligned rod‑shaped morphology facilitates Li⁺ transport by shortening diffusion paths and reduces cracking by accommodating anisotropic strain. This is a key innovation for cobalt‑free cathodes.

**NCA** replaces Mn with Al, which similarly stabilizes the structure and improves power output. NCA typically has a high Ni base (~80 % or more) and is often used in cylindrical cells for its superior energy density. **NCMA** adds Al to the NCM formulation, enabling even higher Ni content (≥85 %) while maintaining thermal stability through the synergetic effect of Al and Mn. LG Energy Solution’s NCMA cells power General Motors’ Ultium platform, delivering extended driving range with reduced cobalt content.

### Cobalt Dependency and Decobalization

Cobalt is crucial for structural stability and rate capability within the layered oxide lattice. It suppresses Ni²⁺/Li⁺ cation mixing and maintains layered ordering during cycling. However, its supply is geopolitically concentrated—~60 % of global reserves are in the Democratic Republic of Congo, and over 50 % of refined cobalt passes through China. Rising EV demand has driven cobalt prices volatile, prompting the industry to pursue **decobalization**—reducing or eliminating cobalt from the cathode.

Reducing cobalt content degrades rate performance and low‑temperature characteristics because Co helps maintain layered ordering and electron conductivity. Current research focuses on:
- Tailoring the primary particle morphology (e.g., radially aligned rods) to improve lithium diffusion in Co‑free compositions.
- Dopant engineering (e.g., Al, Ti, Mg) to compensate for the loss of cobalt’s stabilizing effect.
- Advanced electrolyte additives that protect the cathode surface from parasitic reactions.

### Other Cathode Chemistries

**LFP** (lithium iron phosphate, LiFePO₄) uses an olivine structure with a lower nominal voltage (3.2 V) and energy density (~160 mAh g⁻¹) but offers excellent thermal stability, long cycle life, and no cobalt or nickel cost. LFP has become dominant in the Chinese EV market and is growing globally for entry‑level EVs and stationary energy storage.

**LMR** (lithium‑ and manganese‑rich, xLi₂MnO₃·(1‑x)LiMO₂) leverages both cationic (Ni²⁺/Ni⁴⁺) and anionic (O²⁻/O⁻) redox to achieve capacities >250 mAh g⁻¹. However, it suffers from voltage fade and oxygen loss during cycling—key barriers to commercialization.

## Significance/LG Context

LG Energy Solution has been at the forefront of high‑nickel and quaternary cathode development. The company’s NCMA material, co‑developed with General Motors for the Ultium battery system, balances high energy density with improved safety and reduced cobalt content—achieving up to 85 % nickel while keeping cobalt below 5 % in some formulations. LG has also invested in concentration‑gradient cathode manufacturing and in pilot production of Co‑free cathodes. These innovations directly address the twin pressures of extending EV range and securing cost‑competitive, geopolitically stable raw material supply.

## Related Pages

- [[ternary-battery|Ternary Battery]]
- [[active-material|Active Material]]
- [[cathode-tier-comparison|High-Nickel vs Mid-Nickel vs LFP]]
- [[lfp-battery|LFP (Lithium Iron Phosphate) Battery]]
- [[nca-battery|NCA Battery]]
- [[ncma-battery|NCMA (Quaternary) Battery]]
- [[critical-minerals|Battery Critical Mineral Supply Chain]]