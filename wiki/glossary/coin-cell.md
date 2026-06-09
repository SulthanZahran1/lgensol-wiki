---
title: Coin-Cell
created: 2026-06-05
updated: 2026-06-08
type: glossary
tags: [mobility, energy-density]
sources:
  - raw/battery-inside-en/en/tech-en/batteries-flying-in-the-skies-all-about-urban-air-mobility-uam-batteries.md
  - raw/battery-inside-en/en/opinion-en/the-future-mobility-industry-is-in-the-hands-of-the-battery-industry.md
  - raw/battery-inside-en/en/tech-en/battery-glossary-coin-cell.md
  - raw/ko/tech/battery-terminology-coin-cell.md
  - raw/corporate/zh/pages/business-mobility.md
confidence: high
---
# Coin-Cell

## Overview

A coin cell (also called a button cell) is a compact, disc-shaped battery format widely used in portable electronics and battery research. Its flat geometry typically ranges from 6 mm to 25 mm in diameter and 1 mm to 6 mm in thickness. Coin cells are manufactured as both primary (non‑rechargeable) and secondary (rechargeable) cells, with the rechargeable variants sharing the same fundamental lithium‑ion architecture as larger formats like [[46-series-battery|46‑Series Cylindrical Battery (4680/4695)]].

Common designations follow the International Electrotechnical Commission (IEC) standard: for example, CR2032 denotes a primary lithium‑manganese dioxide cell of 20 mm diameter and 3.2 mm thickness, while LIR2032 designates a rechargeable lithium‑ion coin cell of the same physical dimensions. A typical coin cell occupies approximately 1/20 of the volume of an 18650 cylindrical cell (18 mm × 65 mm), yet delivers stable voltage, low self‑discharge, and long‑term reliability. Applications include real‑time clocks (RTCs), memory backup, medical devices (hearing aids, insulin pumps), wearables (smartwatches, fitness bands), and IoT sensors.

## Technical Details

Rechargeable lithium‑ion coin cells contain a cathode (e.g., NCM, LCO, or mid‑nickel compositions), a graphite‑based anode, a microporous separator, and a liquid electrolyte — the same components found in cylindrical, prismatic, or pouch cells. However, the small form factor imposes unique design constraints: electrode coatings are thin (typically 50–100 µm) to maintain acceptable rate capability, and the cell casing itself acts as both current collector and seal. The crimped closure must withstand internal pressure while preventing electrolyte leakage over years of operation.

Coin cells are assembled in a dry‑room environment to prevent moisture ingress. In a typical laboratory process, electrodes are punched into discs, a separator is placed between them, the stack is wetted with electrolyte, and the assembly is crimped inside a metal can. This manual method introduces variability in torque, alignment, and electrolyte volume. To improve consistency, LG Energy Solution has introduced automated coin‑cell production equipment capable of fabricating up to 360 LIR2032 cells per day — equivalent to the output of four researchers working manually. Automation eliminates human error, enabling tight control over crimp pressure, electrolyte fill, and assembly order, resulting in higher reproducibility and more reliable electrochemical test data.

Electrochemical performance is typically evaluated using galvanostatic charge‑discharge cycling, cyclic voltammetry, and electrochemical impedance spectroscopy. Capacity, Coulombic efficiency, and cycle life are measured under standardized current rates (e.g., 0.1 C, 0.5 C, 1 C). Because they consume only a few milligrams of active material per cell, coin cells are the preferred platform for screening new cathode chemistries (such as high‑voltage mid‑nickel NCM, see [[cathode-tier-comparison|High‑Nickel vs Mid‑Nickel vs LFP]]), anode materials (including silicon‑dominant or lithium‑metal), and electrolyte additives. They bridge the gap between half‑cell testing and full‑size prototype cells, providing rapid feedback at minimal cost.

## Significance and LG Energy Solution Context

Coin cells serve as the workhorse of battery R&D, allowing researchers to validate new concepts with high throughput. At LG Energy Solution, coin‑cell testing is integral to the development of next‑generation technologies including [[46-series-battery|46‑Series Cylindrical Battery (4680/4695)]], [[anodeless-battery|Anodeless Battery]], [[azs-stacking|AZS (Advanced Z‑Stacking)]], and advanced electrolyte systems. The company’s investment in automated coin‑cell production not only accelerates development cycles but also enhances data quality — automated cells exhibit narrower variance in capacity and impedance, enabling more confident go/no‑go decisions before scaling to pouch or cylindrical formats.

Beyond R&D, coin cells power a vast ecosystem of consumer and industrial devices. They are the energy source for smartwatches, fitness bands, hearing aids, insulin pumps, wireless sensors, and electronic shelf labels. Their ability to provide a stable 3 V output for years with negligible leakage (<1% per year for primary cells) makes them ideal for backup power in RTC modules and SRAM memory. In medical applications, reliability is paramount: a hearing‑aid coin cell must deliver consistent voltage under variable load while being small enough to fit inside the ear canal.

The standardization of coin‑cell sizes (CR16xx, CR20xx, CR23xx, etc.) ensures cross‑manufacturer interchangeability. As IoT and wearable markets grow, demand for higher energy density, thinner profiles, and improved safety drives innovation in electrode engineering, electrolyte formulation, and packaging. LG Energy Solution’s automated production and cutting‑edge R&D — including work on single‑crystal cathodes for high‑voltage mid‑nickel chemistries — are already making an impact. Coin cells have also been showcased at InterBattery exhibitions (e.g., 2023) as part of LG Energy Solution’s portfolio of small‑format cells for portable electronics and new applications.

## Related Pages

- [[46-series-battery|46‑Series Cylindrical Battery (4680/4695)]]
- [[anodeless-battery|Anodeless Battery]]
- [[azs-stacking|AZS (Advanced Z‑Stacking)]]
- [[bipolar-technology|Bipolar Technology]]
- [[cathode-tier-comparison|High‑Nickel vs Mid‑Nickel vs LFP]]
- [[cell-format-comparison|Cell Form Factor Comparison (Cylindrical vs Pouch vs Prismatic)]]