---
title: SEI (Solid Electrolyte Interphase)
created: 2026-06-05
updated: 2026-06-08
type: glossary
tags: [anode, electrolyte, cycle-life]
sources:
  - raw/battery-inside-en/en/tech-en/battery-glossary-sei-solid-electrolyte-interphase.md
  - raw/battery-inside-en/en/tech-en/game-changer-battery-all-solid-state-battery-the-ultimate-battery-that-delivers-higher-s-79332ecd61.md
  - raw/battery-inside-en/en/tech-en/a-better-life-with-batteries-solid-electrolyte.md
  - raw/ko/tech/%eb%b0%b0%ed%84%b0%eb%a6%ac-%ec%9a%a9%ec%96%b4%ec%82%ac%ec%a0%84-sei-solid-electrolyte-interphase.md
  - raw/battery-inside-en/en/interview-en/a-battery-without-an-anode-lg-energy-solutions-research-on-combining-anodeless-and-solid-ae5b6bf6d7.md
confidence: high
---
# SEI (Solid Electrolyte Interphase)

## Overview / Introduction

The Solid Electrolyte Interphase (SEI) is a nanometer-scale passivation layer that forms on the anode surface during the first charge of a lithium-ion battery. It is the product of the electrochemical reduction of electrolyte components—solvents (e.g., EC, DEC), lithium salts (e.g., LiPF₆, LiFSI), and additives—at the anode interface when the potential drops below ~0.8 V vs. Li/Li⁺. Although only 10–50 nm thick, the SEI is one of the most critical determinants of battery performance, cycle life, safety, and coulombic efficiency. A stable SEI allows lithium ions to pass while blocking electrons, thereby suppressing continuous electrolyte decomposition. Conversely, an unstable or overly thick SEI increases internal resistance, consumes active lithium irreversibly, and accelerates capacity fade. The quality of the SEI directly influences initial coulombic efficiency (the irreversible capacity loss in the first cycle) and long-term aging behavior.

## Technical Details

**Formation Mechanism**
When a freshly assembled cell is first charged, the anode potential descends below the reduction potential of the electrolyte. Solvent molecules (e.g., ethylene carbonate, EC) and lithium salt anions (e.g., PF₆⁻) are reduced, generating insoluble species that precipitate onto the anode. This process consumes a small amount of lithium from the cathode, which is irreversibly lost—a phenomenon known as *first-cycle irreversible capacity loss*. The reduction products accumulate into a mosaic-like layer that is both ionically conductive and electronically insulating. The initial formation takes place primarily during the first few cycles and can be optimized through controlled formation protocols (e.g., low current density, elevated temperature).

**Composition**
The SEI has a dual-phase structure:
- **Inorganic components**: LiF, Li₂CO₃, Li₂O, LiOH—dense, mechanically robust, and good Li⁺ conductors but electronic insulators.
- **Organic components**: ROLi, ROCO₂Li (lithium alkyl carbonates), oligomeric species—more flexible but less stable chemically.

The relative proportions evolve with cycling. A LiF-rich SEI (promoted by LiFSI salt or FEC additive) is particularly effective at suppressing dendrite growth and improving high-voltage stability. The SEI is not static; it undergoes continuous restructuring during cycling, especially under dynamic operating conditions.

**Key Properties**
- **Li⁺ conductivity**: Typically ~10⁻⁶ S/cm, sufficient for normal rates but becomes limiting at high C-rates (e.g., >3C), contributing to increased [[internal-resistance]].
- **Electronic insulation**: Prevents further electrolyte reduction after formation, limiting capacity loss beyond the first cycle.
- **Elasticity**: Must accommodate anode volume changes during cycling—especially critical for silicon anodes (which expand >300%) and for lithium metal anodes. An elastic SEI reduces mechanical fracture and re-exposure of fresh anode.

**Degradation and Aging Mechanisms**
Over repeated cycles, the SEI degrades through multiple pathways:
- **Thickening**: Slow, ongoing electrolyte reduction continues, building a thicker, more resistive layer → increased [[internal-resistance]] and higher overpotential.
- **Cracking**: Volume changes during lithiation/delithiation cause mechanical fractures, exposing fresh anode to electrolyte, triggering new SEI formation, and consuming additional lithium.
- **Dissolution**: Some organic SEI components are soluble in the electrolyte, especially at elevated temperatures (>45 °C), leading to thinning and local exposure.
- **Thermal runaway**: In extreme cases, SEI decomposition at high temperature can accelerate heat generation and gas evolution.

**Temperature Effects**
At high temperatures (>45 °C), SEI growth accelerates, leading to impedance rise and faster capacity fade. At low temperatures (<0 °C), Li⁺ transport through the SEI becomes sluggish, increasing polarization and the risk of lithium plating, which can form [[dendrite|dendrites]] and reduce coulombic efficiency.

## Significance / LG Energy Solution Context

In the LG Energy Solution knowledge corpus, SEI is a central design parameter linking electrolyte formulation, anode material choice, formation protocol, and operational BMS strategy.

**Electrolyte Design**
LG has extensively studied the role of LiFSI (the "F electrolyte") and FEC additives to form a thin, LiF-rich SEI that minimizes first-cycle loss and improves high-voltage endurance. LiFSI-based SEIs exhibit higher Li⁺ conductivity and better thermal stability compared to those formed from LiPF₆ alone. The SEI quality is a key criterion for selecting [[electrolyte-additive|electrolyte additives]].

**Anode Innovation**
For next-generation anodes—high-Si content composites and Li-metal—a robust SEI is even more critical. Si anodes require an elastic SEI that can withstand volume changes without fracturing. LG’s research into artificial SEI coatings (e.g., pre-formed LiF layers) and advanced electrolyte formulations (dual-salt systems that generate a mechanically resilient SEI) directly targets this challenge.

**BMS and Operation**
BMS algorithms monitor voltage, temperature, and DC internal resistance (DCIR) to infer SEI health. A rapid rise in DCIR often signals SEI degradation. LG’s battery management systems enforce voltage limits within the [[potential-window]] and temperature windows to preserve SEI stability. The SEI also interacts with the cathode-side [[cei|CEI (Cathode Electrolyte Interphase)]]—both layers must be simultaneously optimized to achieve balanced cell aging and long-term reliability.

**Manufacturing**
Formation steps—conditioning cycles at controlled low rates—are designed to establish a stable SEI before the cell enters service. LG uses proprietary formation protocols to ensure uniform SEI coverage, minimizing first-cycle loss and initial [[internal-resistance]].

## Related Pages

- [[anode-materials|Anode Material]]
- [[cei|CEI (Cathode Electrolyte Interphase)]]
- [[coulombic-efficiency|Coulombic Efficiency (CE)]]
- [[dendrite|Dendrite]]
- [[electrolyte-additive|Electrolyte Additive]]
- [[internal-resistance|Internal Resistance]]
- [[potential-window|Potential Window]]
- [[lithium-ion-battery|Lithium-Ion Battery Structure & Operating Principle]]