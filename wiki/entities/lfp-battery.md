---
title: LFP (Lithium Iron Phosphate) Battery
created: 2026-06-05
updated: 2026-06-08
type: entity
tags: [lfp, cathode, energy-density, safety, ess, ev]
sources:
  - raw/battery-inside-en/en/tech-en/lfp-batteries-reshaping-the-market-with-cost-competitiveness-and-safety.md
  - raw/battery-inside-en/en/tech-en/whats-the-difference-between-lithium-hydroxide-and-lithium-carbonate.md
  - raw/battery-inside-en/en/tech-en/game-changer-battery-lithium-metal-battery-achieving-both-energy-density-and-compact-volume.md
  - raw/battery-inside-en/en/tech-en/what-makes-lg-energy-solutions-ess-batteries-different-as-tesla-ess-partner.md
  - raw/battery-inside-en/en/interview-en/better-life-i-place-orders-for-lfp-cells-for-ess-and-check-the-result-a-day-in-the-life-f26d55305b.md
confidence: high
---
# LFP (Lithium Iron Phosphate) Battery

## Overview

Lithium iron phosphate (LiFePO₄, LFP) batteries are a class of lithium-ion battery that uses an olivine-structured cathode composed of abundant iron rather than scarce nickel or cobalt. LFP has become the dominant chemistry for stationary energy storage systems (ESS) and is rapidly gaining share in entry-level electric vehicles (EVs) due to its inherent safety, long cycle life, and low material cost. LG Energy Solution (LGES) is a leading manufacturer of large-format LFP pouch cells for ESS, with production lines in North America and Asia and a strategic partnership with Tesla for Megapack 3 deployment.

## Technical Details

### Crystal Structure and Lithium Diffusion

LFP crystallizes in an olivine structure (space group Pnma) where PO₄ tetrahedra are linked by FeO₆ and LiO₆ octahedra. The strong P–O covalent bonds within the phosphate tetrahedra confer exceptional thermal and chemical stability. Lithium ions migrate through one-dimensional channels along the [010] direction, giving LFP a characteristic flat voltage plateau at ~3.45 V vs. Li/Li⁺. This 1D diffusion path is sensitive to defects: any blocking impurity or antisite defect can severely impede ionic transport, motivating the use of carbon coatings and nanosized particles to shorten diffusion lengths.

### Safety and Thermal Runaway

The olivine structure resists oxygen release up to 500–600 °C, far above the decomposition temperature of layered oxides (NCM/NCA). In thermal runaway tests, LFP cells peak at around 400 °C with limited gas evolution and no flame propagation. This safety margin makes LFP the preferred choice for megawatt-scale ESS installations where fire risk must be minimized.

### Energy Density and Cycle Life

Commercial LFP cells deliver 90–170 Wh/kg and 200–450 Wh/L — roughly 30–40% lower than high-nickel NCM. However, cycle life is exceptional: LFP pouch cells routinely achieve 8,000–10,000 cycles, and LGES reports up to 15,000 cycles in its ESS-grade products under controlled conditions. The ultralong life derives from the stable Fe²⁺/Fe³⁺ redox couple and minimal volume change (~6 %) during delithiation, preserving the cathode lattice over thousands of cycles.

### Key Challenges and Mitigations

- **Low electronic conductivity** (~10⁻⁹ S/cm): addressed by carbon coating, carbon nanotube (CNT) conductive additives, and nanosizing (100–200 nm primary particles).
- **Voltage hysteresis**: the 1D diffusion path and two-phase (FePO₄/LiFePO₄) reaction create a voltage gap between charge and discharge, complicating state-of-charge (SoC) estimation. Advanced BMS algorithms are required.
- **Poor low-temperature performance**: below 0 °C, viscosity of electrolyte increases and lithium diffusivity drops sharply; LGES uses tailored electrolytes and thermal management to maintain acceptable capacity down to –20 °C.

## Significance and LG Energy Solution Context

LGES has invested heavily in LFP for ESS, leveraging its proprietary pouch-cell manufacturing technologies:

- **Lamination & Stacking (L&S)** : instead of conventional winding, LGES uses a Z-folding stacking process that improves active-material loading by 12 % compared to wound cells of the same footprint, boosting energy density.
- **Safety Reinforced Separator (SRS)** : a ceramic-coated separator that suppresses internal short circuits and maintains integrity at elevated temperatures.
- **Cell-to-Pack (CTP)** : LGES integrates LFP pouch cells directly into pack-level structures without intermediate modules, increasing system-level energy density by 10–15 % and simplifying thermal management.

In 2026, LGES became the official battery supplier for Tesla’s Megapack 3, with cells produced at its Lansing, Michigan plant from 2027 onward. The company operates LFP production in Nanjing (China), Holland and Lansing (USA), and plans a dedicated LFP line in Ochang (Korea) by 2027. LGES is the only major battery manufacturer with large-scale LFP pouch production in the United States, underpinning its strategy to capture a 60 GWh ESS production capacity in North America by 2026.

The company’s vertically integrated offering includes system integration through its subsidiary Vertech (formerly NEC Energy Solutions), providing turnkey ESS design, installation, and maintenance. LGES has also achieved UL9540A certification for large-scale fire testing on its LFP modules, a critical requirement for utility and commercial deployments.

Understanding LFP’s role in the broader cathode landscape is essential for comparing it with other technologies: see [[lfp-vs-ncm|LFP vs NCM Comparison]]. For more on ESS applications, visit [[energy-storage-system|Energy Storage System]]. The manufacturing innovations described here are detailed in [[cell-to-pack|Cell-To-Pack (CTP)]] and Pouch Cell Design. Finally, LGES's relationship with [[tesla|Tesla]] illustrates the strategic importance of LFP in the global energy transition.

## Related Pages

- [[lfp-vs-ncm|LFP vs NCM Comparison]]
- [[energy-storage-system|Energy Storage System (ESS)]]
- [[cell-to-pack|Cell-To-Pack (CTP)]]
- Pouch Cell Design
- [[srs|SRS (Safety Reinforced Separator)]]
- [[tesla|Tesla]]