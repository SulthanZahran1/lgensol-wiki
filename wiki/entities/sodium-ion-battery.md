---
title: Sodium-ion Battery
created: 2026-06-05
updated: 2026-06-08
type: entity
tags: [sodium-ion, anode, cathode, energy-density, supply-chain, ess]
sources:
  - raw/battery-inside-en/en/tech-en/battery-pioneer-sodium-ion-batteries.md
  - raw/ko/tech/sodium-ion-battery-%ec%86%8c%eb%93%90%ec%9d%b4%ec%98%a8%eb%b0%b0%ed%84%b0%eb%a6%ac.md
  - raw/battery-inside-en/en/tech-en/what-makes-lg-energy-solutions-ess-batteries-different-as-tesla-ess-partner.md
  - raw/battery-inside-en/en/tech-en/infographics-12-anode.md
  - raw/battery-inside-en/en/tech-en/the-next-generation-anode-material-silicon.md
confidence: high
---
# Sodium-ion Battery

## Overview

Sodium-ion batteries (SIBs) replace lithium ions with sodium ions as the charge carrier, leveraging the fifth most abundant element on Earth—sodium, found in rock salt and seawater. The operating principle mirrors lithium-ion batteries (LIBs): sodium ions shuttle between a cathode and anode during charge/discharge, while electrons flow through an external circuit. However, distinct material chemistries and electrochemical behaviors define the technology.

Global interest in SIBs has surged since 2020, driven by volatile lithium prices, geopolitical concentration of lithium reserves, and rising demand for stationary energy storage systems (ESS), low-speed electric vehicles, backup power, and lead-acid replacement. Major players including CATL, BYD, and LG Energy Solution have announced production roadmaps. BloombergNEF projects sodium-ion could capture up to 10% of the global battery market by 2030, primarily in stationary storage and entry-level EVs.

The history of SIBs dates back to the same era as lithium-ion. In the 1970s, intercalation of sodium into titanium disulfide (TiS₂) was demonstrated, and by the 1980s, sodium cobalt oxide (NaₓCoO₂) showed electrochemistry analogous to LiCoO₂. Despite this early promise, SIB development lagged because lithium-ion offered higher energy density. The recent cost and supply-chain pressures have rekindled interest.

## Technical Details

### Cathode Chemistries
Three principal cathode families are in development:

- **Layered sodium transition metal oxides (NaTMO₂)**: Similar to NMC in LIBs, common compositions like NaFe₁/₂Mn₁/₂O₂ offer capacities up to 160 mAh/g. However, they are moisture‑sensitive—exposure to air causes surface degradation and capacity fade. Cation mixing and phase transitions during cycling reduce long‑term stability.

- **Polyanionic compounds**: Sodium vanadium fluorophosphate (Na₃V₂(PO₄)₂F) and sodium vanadium phosphate (Na₃V₂(PO₄)₃) provide high voltage (~3.7 V vs. Na/Na⁺) and excellent structural stability. Vanadium toxicity and cost are concerns; iron‑based phosphates (NaFePO₄) are cheaper but have lower voltage.

- **Prussian blue analogs (PBAs)**: Open‑framework materials (e.g., Na₂FeFe(CN)₆) enable rapid sodium diffusion and high‑rate performance. PBA cathodes are synthesized from abundant, non‑toxic elements but suffer from low density (~1.6 g/cm³) and water in interstitial sites. Recent improvements have achieved ~120 mAh/g with cycle life exceeding 10,000 cycles.

### Anode Materials
Graphite, the standard LIB anode, cannot effectively host sodium ions due to the larger ionic radius (102 pm vs. 76 pm for Li⁺). Instead, most SIBs use **hard carbon**—a disordered, non‑graphitizable carbon from biomass (e.g., coconut shells) or petroleum precursors. Hard carbon stores sodium via intercalation between disordered graphene layers and micropore filling, delivering 300–350 mAh/g. However, its first‑cycle Coulombic efficiency is only 80–90% due to a thick SEI formation. Strategies to improve efficiency include carbon coating, electrolyte additives, and pre‑sodiation. Soft carbon and alloy anodes (Sn, Sb, P) are also studied—phosphorus offers theoretical capacities >2,500 mAh/g but suffers from >300% volume changes.

### Electrolyte and SEI
Standard electrolytes use sodium hexafluorophosphate (NaPF₆) in carbonate solvents. The SEI on hard carbon is thicker and more resistive than on graphite in LIBs. Additives like fluoroethylene carbonate (FEC) improve stability and Coulombic efficiency. NaPF₆ is less thermally stable than LiPF₆, limiting operation to about 60°C unless using ionic‑liquid electrolytes.

### Performance Metrics
Current commercial SIBs achieve:

- **Gravimetric energy density**: 140–160 Wh/kg (versus 200–300 Wh/kg for mainstream LIBs); research cells reach 180 Wh/kg.
- **Volumetric energy density**: 250–375 Wh/L (LIBs: 400–700 Wh/L), limited by larger sodium ions and less compact electrode architectures.
- **Cycle life**: 3,000–8,000 cycles; PBA and polyanionic systems exceed 10,000 cycles at 1C depth.
- **Low‑temperature performance**: ~90% capacity retention at –20°C, significantly better than LIBs (60–70%), making SIBs attractive for cold‑climate ESS and starter batteries.
- **Rate capability**: 1–3C for hard carbon; up to 10C for PBA cathodes.
- **Safety**: Thermal runaway onset typically above 250°C (versus 150–180°C for LIBs) because sodium deposits more evenly during overcharge, reducing dendrite formation.

### Cost Structure
Material cost of SIBs is estimated 20–30% lower than LFP batteries. Key savings: (i) no lithium; (ii) no cobalt or nickel in typical cathodes; (iii) aluminum current collectors for both electrodes (sodium does not alloy with aluminum at low potentials, replacing copper). With aluminum priced about one‑third that of copper, cell costs further decrease. Manufacturing processes are largely compatible with existing LIB lines.

## Significance and LG Energy Solution Context

Sodium‑ion batteries are positioned to disrupt markets where lithium‑ion’s high energy density is not critical. Primary applications include:

- **Stationary energy storage (ESS)**: Grid‑scale systems for peak shaving and renewable integration benefit from SIBs’ long cycle life and low cost.
- **Low‑cost electric vehicles**: Two‑wheelers, three‑wheelers, and entry‑level passenger cars (range under 300 km). India and Southeast Asia are lead markets.
- **Lead‑acid replacement**: Automotive start‑stop (12/24V), UPS backup, and industrial traction batteries. SIBs offer >3,000 cycles versus ~500 for lead‑acid, with better low‑temperature performance.
- **Backup power and telecom tower batteries**: Reliable, cost‑effective off‑grid energy.

LG Energy Solution’s roadmap, unveiled at InterBattery 2025, targets two generations:

- **Gen1 (2027 production)**: High‑power cells for lead‑acid replacement and UPS, optimized for 5C power delivery and long calendar life. Uses a hybrid cathode (layered oxide + PBA) and advanced hard carbon. Energy density target: 120–140 Wh/kg.
- **Gen2 (2030)**: High‑energy cells for EV traction, aiming at 450 Wh/L volumetric energy density. LG plans to apply dry electrode processing (similar to its dry‑coating technology for LIBs) to lower production cost and improve electrode uniformity. The cathode will likely be a polyanionic compound selected for high voltage stability.

LG also integrates SIBs into its broader ESS ecosystem, including its EMO (Energy Market Optimizer) software for real‑time battery state and electricity market analysis, and its North American manufacturing network (Holland, Michigan; Lansing; and joint ventures) to supply up to 60 GWh of ESS batteries by 2026. The company’s partnership with Tesla for Megapack 3 (2027 start) further underscores its commitment to scalable, cost‑competitive storage solutions.

Competitors like CATL have shipped SIB cells in small volumes since 2023 (AB series blending LFP), and BYD announced a dedicated sodium‑ion platform for its Seagull model in 2026. Price parity with LFP is expected by 2028–2029, with cell costs below $50/kWh at large volumes.

## Related

- [[lfp-battery|LFP (Lithium Iron Phosphate) Battery]]
- [[next-gen-battery-overview|Next-Generation Battery Comprehensive Comparison]]
- [[solid-state-battery|All-Solid-State Battery]]
- [[lithium-sulfur-battery|Lithium-Sulfur Battery]]
- [[high-nickel-battery|High-Nickel Battery]]
- ESS Battery Technologies
- Lead-Acid Battery Replacement Markets