---
title: Coulombic Efficiency (CE)
created: 2026-06-05
updated: 2026-06-08
type: glossary
tags: [cycle-life, electrolyte]
sources:
  - raw/battery-inside-en/en/tech-en/battery-glossary-coulombic-efficiency-ce.md
  - raw/ko/tech/terminology-coulombic-efficiency.md
  - raw/battery-inside-en/en/tech-en/a-better-life-with-batteries-the-electrolyte-additives-for-ev-batteries.md
  - raw/battery-inside-en/en/tech-en/a-better-life-with-batteries-solid-electrolyte.md
  - raw/battery-inside-en/en/tech-en/battery-glossary-sei-solid-electrolyte-interphase.md
confidence: high
---
# Coulombic Efficiency (CE)

## Overview

Coulombic efficiency (CE), also called Faradaic efficiency or current efficiency, is the ratio of discharge capacity to charge capacity in a single charge‑discharge cycle. It quantifies how faithfully a battery preserves charge during cycling, expressed as a percentage. A CE of 100 % would mean that every coulomb of charge put into the cell during charging is recovered during discharge, with no losses to parasitic side reactions. In practice, real cells always show some irreversible loss, making CE one of the most revealing metrics for battery health and longevity.

A simple analogy from the LG blog compares CE to transferring water between bottles: if you pour 100 mL from one bottle to another and back, and only 99 mL remains (1 mL spilled), the retention is 99 %—exactly what CE describes for charge. The spilled water represents charge consumed by irreversible processes such as electrolyte decomposition or [[sei|SEI]] growth.

CE is calculated as:

\[
\text{CE} (\%) = \frac{\text{Discharge Capacity (mAh)}}{\text{Charge Capacity (mAh)}} \times 100
\]

For example, if a cell accepts 100 mAh on charge but delivers only 80 mAh on discharge, CE = 80 %. The missing 20 mAh has been consumed by irreversible side reactions.

## Technical Details

### Initial Coulombic Efficiency (ICE) and the Role of SEI/CEI

The first cycle of a fresh lithium‑ion battery always exhibits a noticeably lower CE, termed the initial Coulombic efficiency (ICE). This is because the initial charge irreversibly consumes lithium to form the [[sei|Solid Electrolyte Interphase]] (SEI) on the anode and the [[cei|Cathode Electrolyte Interphase]] (CEI) on the cathode. These passivation layers are essential for stable cycling, but their formation permanently consumes active lithium from the cathode, reducing the cell’s first‑cycle discharge capacity. Typical ICE values range from 85–95 % depending on electrode chemistry, electrolyte formulation, and formation protocol. After the first few cycles, CE rises dramatically, often exceeding 99.9 % in well‑designed cells.

### Cumulative Impact of Small CE Losses

Even minute CE losses accumulate over many cycles. A cell with a steady CE of 99.9 % loses 0.1 % of its capacity per cycle. After 100 cycles, this corresponds to roughly 10 % capacity fade; after 500 cycles, approximately 50 % of the initial capacity is lost. For applications demanding long life (e.g., electric vehicles, grid storage), CE must reach 99.95 % or higher. Achieving such values requires careful electrolyte engineering, optimized electrode surfaces, and precise voltage control to limit parasitic reactions.

### CE vs. Energy Efficiency

CE should not be confused with energy efficiency. CE measures only charge preservation (coulomb counting), whereas energy efficiency also accounts for voltage losses due to [[internal-resistance|internal resistance]]. A battery can have near‑100 % CE yet exhibit only 90 % energy efficiency if its internal resistance causes significant IR drop during discharge. Both metrics are needed for a complete performance picture.

### Measurement: CC/CV Protocols

CE is routinely evaluated using constant‑current (CC) and constant‑voltage (CV) charge‑discharge tests. In a typical protocol, the cell is charged at a fixed current (e.g., C/5) until the upper cutoff voltage is reached, then held at that voltage (CV step) until the current decays to a low threshold (e.g., C/100). The cell is then discharged at constant current to the lower cutoff. The charge and discharge capacities are integrated from the current‑time data, and CE is computed. High‑precision coulometric measurements (e.g., using ultra‑stable cyclers and temperature‑controlled chambers) can resolve CE differences as small as 0.001 %, which is crucial for diagnosing subtle degradation mechanisms.

## Significance and LG Energy Solution Context

### Importance for Cycle Life and BMS

CE is a direct indicator of side‑reaction intensity. Low CE signals ongoing electrolyte decomposition, SEI/CEI growth, lithium plating, or transition‑metal dissolution. Battery management systems (BMS) use CE data (often via coulomb counting) for [[soc|State of Charge (SoC)]] estimation. Accurate CE knowledge enables precise SoC tracking and prevents overcharge/overdischarge, improving safety and usable energy.

### Critical Role in Next‑Generation Batteries

CE is especially demanding for advanced anodes. In [[lithium-metal-battery|Lithium Metal Batteries]] and [[anodeless-battery|Anodeless Batteries]], the entire lithium inventory originates from the cathode. Any lithium lost to side reactions (e.g., reaction with the liquid electrolyte or dendrite formation) directly reduces capacity. A typical lithium‑metal cell requires CE > 99.9 % to achieve even modest cycle life. The LG Energy Solution blog highlights that in liquid‑electrolyte anodeless cells, CE suffers from lithium–electrolyte reactions and dendrite growth. LG’s solution for anodeless cells employs a solid electrolyte (in its solid‑state battery development) and surface treatments such as lithiophilic material (LPM) coatings and oxidation to suppress dendrites and improve CE.

### LG’s Electrolyte and Material Development

LG Energy Solution uses CE as a key screening metric in electrolyte and electrode material programs. The company’s [[gas-free-solvent|Gas Free Solvent]] technology aims to minimize side reactions that consume lithium, thereby raising CE. Optimization of CE is also central to LG’s work on high‑nickel cathodes and silicon‑containing anodes, where parasitic reactions are more pronounced. By pushing CE above 99.95 %, LG prolongs cycle life and enables higher energy density designs.

CE is not a static property—it evolves with cycling, temperature, charge rate, and depth of discharge. Understanding and controlling CE is fundamental to building safer, longer‑lasting batteries.

## Related Pages
- [[cei|CEI (Cathode Electrolyte Interphase)]]
- [[electrolyte-additive|Electrolyte Additive]]
- [[sei|SEI (Solid Electrolyte Interphase)]]
- [[anode-materials|Anode Material]]
- [[dendrite|Dendrite]]
- [[dod|DoD (Depth of Discharge)]]
- [[anodeless-battery|Anodeless Battery]]
- [[potential-window|Potential Window]]