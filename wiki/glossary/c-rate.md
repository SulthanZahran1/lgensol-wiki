---
title: C-rate (Current Rate / Charge-Discharge Rate)
created: 2026-06-05
updated: 2026-06-08
type: glossary
tags: [fast-charging, power-density]
sources:
  - raw/battery-inside-en/en/tech-en/battery-glossary-c-rate-current-rate.md
  - raw/ko/tech/%eb%b0%b0%ed%84%b0%eb%a6%ac-%ec%9a%a9%ec%96%b4%ec%82%ac%ec%a0%84-c-rate-current-rate.md
  - raw/ensolpedia/en/pages/page-099.md
  - raw/ensolpedia/ko/pages/page-099.md
  - raw/corporate/en/pages/investors-general-meeting-of-shareholders.md
confidence: high
---
# C-rate (Current Rate / Charge-Discharge Rate)

## Overview / Introduction

C-rate is the standardized metric for expressing the charge or discharge current of a battery relative to its nominal capacity. Defined as the current (in amperes) divided by the nominal capacity (in ampere-hours), a 1C rate corresponds to the current that would fully charge or discharge the battery in one hour. For example, a 2,000 mAh battery at 1C draws 2 A; at 0.5C it draws 1 A (2‑hour discharge); at 2C it draws 4 A (30‑minute discharge). This dimensionless ratio allows direct comparison of charge/discharge speed across batteries of differing capacities, making it indispensable for application design and performance specification.

Understanding C-rate is critical for managing thermal behavior, degradation, and system safety, as higher rates generate more Joule heating and accelerate aging mechanisms such as SEI growth and lithium plating. Modern applications—from drones demanding 100C bursts to grid storage operating at 0.5–1C—rely on precise C-rate knowledge to balance power, energy, and life.

## Technical Details

**Calculation and Practical Charging Time**

The theoretical charging time at a constant C-rate is simply 1 hour divided by the C-rate: 1C → 1 h, 2C → 30 min, 0.5C → 2 h, 10C → 6 min. In practice, the actual time is longer due to internal resistance (IR) losses and the constant‑voltage (CV) phase of [[cc-cv-charging|CC/CV Charging]]. During CC mode, the battery voltage rises to its upper limit; then the CV phase tapers current, extending the total charge time. A 1C charge might take 65–70 minutes instead of 60 minutes. Similarly, discharge at high C-rates experiences IR‑induced voltage drops that reduce usable capacity before the lower voltage cutoff is reached.

**Heat Generation and Degradation**

Higher C-rates increase I²R heating proportionally. As documented in LG Energy Solution’s internal resistance analysis and an external thermal study, at 10C discharge the cell temperature can soar to ~187 °C (from an initial 18 °C), while 10C charge reaches ~117 °C. This elevated temperature accelerates SEI growth, electrolyte decomposition, and active material degradation. At low temperatures (<15 °C), high C-rates promote Lithium Plating on the anode, further increasing internal resistance and reducing cycle life. The thermal runaway risk also escalates: external short‑circuit tests show that with external resistance below 2 mΩ, temperatures can exceed 150 °C, underscoring the safety implications of extreme C-rates.

**Factors Governing C-rate Capability**

C-rate performance depends on:
- **Ionic conductivity** of the electrolyte—higher conductivity supports faster ion transport.
- **Electrode thickness and porosity**—thinner, more porous electrodes lower diffusion resistance but sacrifice energy density.
- **Active material particle size and morphology**—smaller particles shorten lithium diffusion paths, enabling higher rates.
- **Cell design**—tab location and current collector thickness affect ohmic losses.

The trade-off between power and energy is fundamental: cells optimized for high C-rates (e.g., 10–20C for power tools or drone bursts) typically have lower energy density due to thinner electrodes and increased current collector mass. Conversely, cells for grid ESS (0.5–1C) maximize energy density and cycle life. LG’s DLD (Double Layer Slot Die Coating) technology improves C-rate capability by reducing electrode resistance through precise coating of two active layers with optimized porosity and conductive additive distribution, enhancing ionic transport without sacrificing energy density.

**Internal Resistance and C-rate Interplay**

Internal resistance (IR) is a composite of electronic resistance (current collectors, tabs, electrode materials) and ionic resistance (electrolyte, separator). IR increases with aging, and higher IR reduces the achievable C-rate—the battery hits voltage limits sooner, dropping effective capacity. At moderate rates (~0.5‑1C), IR growth of 50% may only cause 2–6% RTE reduction, but at high C-rates the effect is magnified. The [[internal-resistance|Internal Resistance]] page details how DC-IR and AC-IR measurement techniques are used to monitor this parameter in real‑world applications, including LG’s BMS for cell balancing.

## Significance / LG Energy Solution Context

C-rate knowledge is essential for matching batteries to applications. For example, LG Energy Solution’s participation at RE 2025 highlighted a next‑generation UPS battery capable of 20C discharge for AI data centers, delivering 527 kW per cabinet for 5 minutes—doubling the power density of previous designs while reducing cabinet count by 50%. This enables compact, high‑power backup for fluctuating data center loads.

The company’s [[46-series-battery|46-Series Cylindrical Battery (4680/4695)]] cells are engineered for high‑rate charging in electric vehicles, leveraging low‑IR tab design and advanced electrolyte formulations. Conversely, LG’s LFP cells for ESS applications (e.g., JF2/JF3 modules) operate at moderate rates (0.5–1C) to maximize cycle life and safety, with UL9540A compliance and Made‑in‑USA production for IRA benefits.

Source materials also illustrate extreme C-rate examples: drone batteries rated at 100C can deliver 100× capacity current for bursts lasting only 36 seconds, enabling aggressive maneuvers. Such designs require specialized electrode architectures (very thin, high‑porosity coatings) and advanced thermal management. In ESS, the EMO (Energy Market Optimizer) solution uses C-rate as a critical input to dynamically estimate DME (Dynamic Marketable Energy), optimizing charging/discharging schedules for grid participation while preserving battery health.

C-rate directly influences [[fast-charging|Fast Charging]] capability, Power Density, and overall system design. Understanding its interplay with [[ionic-conductivity|Ionic Conductivity]] and [[conductive-additive|Conductive Additives]] allows engineers to push the boundaries of battery performance without compromising safety or longevity.

## Related Pages

- [[fast-charging|Fast Charging]]
- [[internal-resistance|Internal Resistance]]
- [[cc-cv-charging|CC/CV Charging (Constant Current/Constant Voltage Charging)]]
- [[46-series-battery|46-Series Cylindrical Battery (4680/4695)]]
- [[conductive-additive|Conductive Additive (CNT)]]
- [[ionic-conductivity|Ionic Conductivity]]