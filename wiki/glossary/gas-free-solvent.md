---
title: Gas Free Solvent
created: 2026-06-05
updated: 2026-06-08
type: glossary
tags: [electrolyte, safety, thermal-stability]
sources:
  - raw/ko/story/%ec%a0%84%ed%95%b4%ec%a7%88-%ec%9a%a9%eb%a7%a4-%ea%b5%ac%ec%a1%b0%eb%a5%bc-%eb%b0%94%ea%bf%94-%ea%b0%80%ec%8a%a4-%eb%b0%9c%ec%83%9d%ec%9d%84-%ec%a4%84%ec%9d%b4%eb%8b%a4-lg%ec%97%90%eb%84%88%ec%a7%80.md
  - raw/ko/tech/%eb%b0%b0%ed%84%b0%eb%a6%ac-%ec%9a%a9%ec%96%b4%ec%82%ac%ec%a0%84-gas-free-%ec%9a%a9%eb%a7%a4.md
  - raw/battery-inside-en/en/tech-en/a-better-life-with-batteries-the-electrolyte-additives-for-ev-batteries.md
  - raw/battery-inside-en/en/tech-en/a-better-life-with-batteries-solid-electrolyte.md
  - raw/battery-inside-en/en/opinion-en/getting-closer-to-a-gasoline-free-society-with-energy-super-station.md
confidence: high
---
# Gas Free Solvent

## Overview / Introduction

Gas Free Solvent is a class of electrolyte solvents engineered with a fundamentally redesigned molecular backbone to suppress gas generation during lithium-ion battery operation. Unlike conventional approaches that rely on functional additives to manage decomposition byproducts, Gas Free Solvent technology re-engineers the solvent molecule itself to be inherently resistant to electrochemical breakdown under high-voltage and elevated-temperature conditions. This shift from additive-level mitigation to molecular-level stability represents a paradigm change in electrolyte design.

Conventional lithium-ion battery electrolytes comprise approximately 80% organic carbonate solvents (e.g., ethylene carbonate EC, dimethyl carbonate DMC, ethyl methyl carbonate EMC, diethyl carbonate DEC), 10–15% lithium salt (typically LiPF₆), and 0.5–5% functional additives (e.g., vinylene carbonate VC, propane sultone PS). These carbonates contain carbonate groups (−O−C(=O)−O−) and alkyl chains. Under high voltage (above 4.2 V vs. Li/Li⁺) or high temperature (>55 °C), the carbonate groups decompose electrochemically at both cathode and anode interfaces, releasing carbon dioxide (CO₂) and carbon monoxide (CO) at the cathode, and hydrocarbon gases at the anode. LiPF₆ also reacts with trace moisture to form hydrofluoric acid (HF), which further attacks the solvent, accelerating decomposition and gas evolution.

Conventional mitigation uses additives that form protective interphases—[[sei|SEI (Solid Electrolyte Interphase)]] on the anode and [[cei|CEI (Cathode Electrolyte Interphase)]] on the cathode. However, additives constitute only a tiny fraction of the electrolyte. Over extended cycling or under aggressive conditions, additives are gradually consumed, and the majority solvent resumes decomposing. Gas Free Solvent technology directly addresses this limitation by making the bulk solvent stable.

## Technical Details

### Molecular Design Principle

LG Energy Solution’s Gas Free Solvent abandons the traditional carbonate architecture entirely. The new molecular structure is inspired by the anion of LiFSI (lithium bis(fluorosulfonyl)imide), a salt known for its high oxidative stability and ability to form robust SEI layers. By redesigning the solvent to incorporate a non-carbonate, imide-based or similarly stable framework, the solvent becomes resistant to oxidation at the cathode and reduction at the anode. The molecule is also functionalized to promote formation of a durable, inorganic-rich SEI on the anode during the first charge, reducing further electrolyte consumption.

### Suppression of Gas Evolution

In a carbonate-based system, the carbonate group is the primary source of CO₂ and CO upon oxidation. The alkyl chains generate hydrocarbon gases upon reduction. Gas Free Solvent eliminates these susceptible moieties. Lab tests show that assemblies employing the first-generation Gas Free Solvent exhibit a significant reduction in cumulative gas volume over cycling compared to baseline carbonate electrolytes with optimized additive packages. The solvent itself resists breakdown even when additives are depleted over long-term use.

### Performance Enhancements

The first-generation Gas Free Solvent delivers measurable improvements:

- **Internal resistance growth rate improves by approximately 53%** (lower resistance increase over 1,000 cycles), indicating better long-term durability.
- **Operating temperature window expands from ~58 °C to ~68 °C**, enabling 8-minute fast charging without accelerated degradation.
- **Additive package is simplified from 8 components to 5**, reducing cost and process complexity.
- **Electrolyte fill volume is reduced by ~4.2%** because less solvent is consumed by side reactions, lowering material cost and cell weight.

### Second-Generation Development

The second-generation Gas Free Solvent improves physical properties such as viscosity and wettability, making it easier to integrate into existing electrode processing and cell assembly. The goal is to eventually replace most carbonate solvents across LG’s product portfolio, from cylindrical cells for EVs to pouch cells for energy storage systems.

## Significance and LG Context

Gas Free Solvent technology is a key pillar of LG Energy Solution’s multi-layered safety and performance strategy, alongside [[srs|SRS (Safety Reinforced Separator)]] (a ceramic-coated separator that maintains integrity up to 200 °C) and [[tp-prevention|TP Prevention Technology]] (thermal propagation prevention). Together, these technologies address the three main failure modes in lithium-ion batteries: electrolyte decomposition (gas generation), separator shrinkage/short circuits, and thermal runaway propagation from cell to cell.

By reducing internal gas pressure, the solvent technology also mitigates cell swelling—a critical concern for high-energy-density cells where even small volume expansions can stress the battery pack. The ability to fast charge in 8 minutes without excessive electrolyte degradation is directly enabled by the wider temperature tolerance (68 °C vs. 58 °C). This positions LG to meet automotive OEM demands for extreme fast charging (XFC) while maintaining safety margins.

The development of Gas Free Solvent reflects a deeper understanding of electrode–electrolyte interphase chemistry. Unlike additive-only solutions that act as sacrificial “band-aids,” this solvent engineering approach strengthens the electrolyte itself. The redesigned solvent also influences the quality of the [[cei|CEI]] and [[sei|SEI]]; the first-generation solvent promotes an SEI that is richer in inorganic species such as LiF, which improves mechanical stability and lithium-ion conductivity.

## Related Pages

- [[liquid-vs-solid-electrolyte|Liquid Electrolyte vs Solid Electrolyte]]
- [[battery-safety|Battery Safety and Thermal Runaway]]
- [[separator|Separator]]
- [[solid-state-battery|All-Solid-State Battery]]
- [[srs|SRS (Safety Reinforced Separator)]]
- [[tp-prevention|TP Prevention Technology (Thermal Propagation Prevention)]]
- [[sei|SEI (Solid Electrolyte Interphase)]]
- [[cei|CEI (Cathode Electrolyte Interphase)]]