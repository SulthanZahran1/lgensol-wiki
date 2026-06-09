---
title: Battery Manufacturing Process Overview
created: 2026-06-05
updated: 2026-06-08
type: concept
tags: [electrode, stacking, winding, formation, aging]
sources:
  - raw/battery-inside-en/en/tech-en/infographics4-how-to-make-a-battery-step-1-electrode-manufacturing.md
  - raw/battery-inside-en/en/news-en/lg-energy-solution-to-invest-krw-7-2-trillion-to-build-battery-manufacturing-complex-in-0983e6c0be.md
  - raw/battery-inside-en/en/interview-en/lg-energy-solutions-azs-advanced-z-stacking-ensuring-a-stable-electrode-stacking-structure.md
  - raw/battery-inside-en/en/tech-en/infographics-16-wet-electrode-process-dry-electrode-process.md
  - raw/ko/tech/battery-manufacturing-efficiency-%ea%b1%b4%ec%8b%9d-%ec%a0%84%ea%b7%b9-%ea%b3%b5%ec%a0%95.md
confidence: high
---
# Battery Manufacturing Process Overview

## Overview / Introduction

Battery manufacturing is a multi‑stage process that transforms raw powders, metal foils, separator, electrolyte, and enclosure materials into tested, ready‑to‑ship cells and packs. The entire cycle — from powder mixing to finished cell — typically takes 15 to 30 days, with the slowest steps being the activation (formation and aging) processes. Yield, safety, cost, and energy density are determined as much by process capability as by chemistry itself. LG Energy Solution (LGES) has pioneered several advanced manufacturing techniques, including double‑layer slot‑die coating (DLD), Lamination & Stacking (L&S), and Advanced Z‑Stacking (AZS), and is actively developing dry electrode technology for next‑generation cells.

The manufacturing flow is divided into four major stages: **electrode process**, **assembly process**, **activation process**, and **pack process**. Each stage contains multiple sub‑processes that require precise control of temperature, pressure, alignment, and cleanliness. The following sections provide a detailed technical breakdown, incorporating specific numbers and mechanisms from LGES’s own manufacturing knowledge.

## Technical Details

### Stage 1: Electrode Process

The electrode process creates the coated cathode and anode rolls. It consists of four key sub‑steps:

1. **Mixing (slurry preparation)**
   Active material (e.g., NCM, LFP, or graphite), conductive additive (carbon black or carbon nanotubes), and binder (PVDF in wet processes) are blended with a solvent to form a homogeneous slurry. For cathodes, the solvent is typically N‑Methyl‑2‑pyrrolidone (NMP); for anodes, water is used. The binder provides adhesion between active particles and to the current collector; the conductive additive ensures electronic pathways. In LGES’s dry electrode process, these same solids are mixed without solvent to create a dry powder, which is then fibrillation‑coated using methods such as Maxwell‑type lamination (powder is first made into a film then laminated onto the current collector) or powder‑spray calendering (powder is sprayed onto the foil and then calendered). Dry processing eliminates the cost and environmental burden of NMP recovery and can reduce electrode manufacturing cost by 17–30%.

2. **Coating & Drying**
   The slurry is applied onto aluminium foil (cathode) or copper foil (anode) using slot‑die coating. LGES introduced the world’s first **Double‑Layer Slot‑Die Coating (DLD)** in 2018, which applies two different slurries simultaneously — one for the bulk electrode layer and another for a functional top layer — enabling higher charging rates and improved performance. After coating, the web passes through drying ovens up to 100 m long at temperatures above 100 °C to evaporate the solvent. Drying alone accounts for over 90 % of the electrode process time and approximately 40 % of total battery manufacturing cost, making it a prime target for innovation. In the dry process, no drying step is required, dramatically cutting time and energy.

3. **Calendering (roll pressing)**
   The dried electrode is passed between two heavy rollers to compress it to a target density and thickness. This step reduces porosity, improves adhesion between the coating and foil, and enhances lithium‑ion transport pathways. The “mix density” (degree of compaction) directly influences cell energy density and power capability. Typical compression ratios are 1.5–2.0×, achieving porosities of 20–35%.

4. **Slitting & Notching**
   The rolled electrode is first slit lengthwise to the required width using a slitter. For prismatic and pouch cells, a notching step then cuts the electrode sheets to shape, creating “tab” regions (uncoated foil areas) for current collection. Notching is increasingly performed with laser cutters rather than mechanical knives because lasers produce fewer burrs, less debris, and require less maintenance — improving both quality and production speed. LGES has adopted laser notching across its lines to minimise particulate contamination, which is critical for preventing internal short circuits.

### Stage 2: Assembly Process

Assembly combines the finished cathode, anode, and separator into a cell structure. Three main architectures exist:

- **Winding (jelly‑roll)**: Used for cylindrical and prismatic cells. The separator, cathode, separator, and anode are stacked and wound into a spiral roll. Alignment precision is critical to avoid misalignment that can lead to lithium plating.
- **Stacking**: For pouch cells, sheets of electrode and separator are stacked in alternating layers. LGES’s proprietary **Lamination & Stacking (L&S)** and **Advanced Z‑Stacking (AZS)** technologies use heat and pressure to bond the separator to the electrodes before stacking, reducing misalignment and improving safety by suppressing internal short circuits. AZS can achieve a stacking speed of up to 1 s per layer while maintaining ±0.5 mm alignment.
- **Z‑folding**: A single continuous separator is folded in a zig‑zag pattern with electrode sheets inserted between folds. This method reduces separator waste but requires careful tension control.

After assembly, the cell is injected with electrolyte under vacuum, then sealed. The wetting process continues during the subsequent aging step.

### Stage 3: Activation Process (Formation & Aging)

This stage transforms the assembled but chemically inert cell into an active energy‑storage device. It typically requires 7–14 days and is the throughput bottleneck of the entire factory.

1. **Aging (soaking)**: The cell rests for 1.5–3 days at room temperature or slightly elevated temperature to allow electrolyte to fully penetrate the electrode pores. Incomplete wetting can cause local lithium depletion and capacity fade.
2. **First charge (formation)**: A controlled low‑current charge (typically C/20 to C/10) is applied to form the **solid‑electrolyte interphase (SEI)** layer on the anode. This passivation layer is critical for long life and safety. Formation is performed at precise temperatures (25–45 °C) and currents to optimise SEI composition — tailoring the ratio of inorganic (LiF, Li₂CO₃) to organic components.
3. **Degassing**: Gas generated during SEI formation (e.g., ethylene, CO₂, H₂) is removed, usually by vacuum degassing followed by resealing of the cell. Some designs include a gas‑collection pouch.
4. **Secondary aging**: Cells are stored at elevated temperatures (40–60 °C) for additional days to stabilise the SEI and detect self‑discharge or micro‑short circuits. Voltage drop over 24–72 h is monitored; any cell exceeding a threshold (e.g., >2 mV/day) is rejected.
5. **Final testing**: Each cell is screened for capacity, resistance, voltage, and open‑circuit voltage (OCV) stability. Defective cells are rejected before packing.

### Stage 4: Pack Process

Cells are assembled into modules with structural frames, thermal management systems (cooling plates, heat spreaders), busbars, voltage/temperature sensing, and a battery management system (BMS). Modules are then integrated into packs with enclosures, high‑voltage connectors, and safety components (fuses, contactors). Emerging **Cell‑to‑Pack (CTP)** designs eliminate module‑level structure, raising pack energy density by 10–30 % at the cost of increased thermal and mechanical engineering demands. LGES is also developing Cell‑to‑Chassis concepts for future EVs.

## Significance / LG Energy Solution Context

LGES invests heavily in process innovation to reduce cost, increase energy density, and improve yield. Key initiatives include:

- **Dry electrode process**: LGES began developing dry electrode technology about a decade ago. By eliminating solvent and the drying step, dry processing can reduce electrode manufacturing cost by 17–30% and enable thicker electrodes with more uniform binder distribution — avoiding the binder migration phenomenon that plagues wet‑coated thick electrodes. In dry processing, PTFE binder fibrillates during mixing, forming a continuous network that binds active particles and conductive additive even at low binder content (1–3 wt%). LGES plans to build a pilot line at its Ochang Energy Plant by the end of 2024, target commercialization by 2028, and eventually apply the process to all global sites. Dry electrode technology is also being explored for all‑solid‑state batteries, where solvent‑free processing is especially advantageous.

- **Double‑layer coating (DLD)**: First commercialised by LGES, DLD allows simultaneous coating of two functional layers, enabling fast‑charging designs without sacrificing energy density. For example, a top layer with higher conductive additive content can improve rate capability while the bulk layer retains high active material loading.

- **Laser notching**: Adoption of laser cutting for slitting and notching reduces particulate contamination and improves edge quality, directly benefiting cell safety and consistency. LGES uses high‑power nanosecond and picosecond lasers to achieve clean cuts with heat‑affected zones below 20 μm.

- **Smart‑factory / AI / DX**: Real‑time monitoring, predictive maintenance, and digital‑twin stabilization are deployed to maximise line utilisation and defect detection. LGES uses machine vision systems to inspect electrode coatings for pinholes, agglomerates, and thickness variations at speeds exceeding 50 m/min.

- **Stacking speed improvements**: AZS technology has increased stacking throughput from 0.5 s per layer in older generations to 0.3 s per layer in the latest lines, enabling pouch cell production of over 10 GWh per line.

These innovations position LGES to maintain leadership in both conventional liquid‑electrolyte lithium‑ion cells and next‑generation solid‑state batteries. The company’s focus on process engineering, combined with its deep chemistry expertise, creates a formidable competitive advantage.

## Related Pages

- [[assembly-process|Assembly Process]]
- [[formation-aging|Activation Process (Formation & Aging)]]
- [[electrode-process|Electrode Process]]
- [[dry-electrode-process|Dry Electrode Process]]
- [[dld|DLD (Double Layer Slot Die Coating)]]
- [[azs-stacking|AZS (Advanced Z‑Stacking)]]
- [[pack-process|Pack Process]]
- [[active-material|Active Material]]
- [[binder|Binder]]
- [[cell-to-pack|Cell‑to‑Pack (CTP)]]