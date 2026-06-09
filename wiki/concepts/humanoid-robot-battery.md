---
title: Batteries for Humanoid Robots
created: 2026-06-05
updated: 2026-06-08
type: concept
tags: [humanoid, power-density, cylindrical, 46-series]
sources:
  - raw/ko/tech/%ed%9c%b4%eb%a8%b8%eb%85%b8%ec%9d%b4%eb%93%9c-%eb%a1%9c%eb%b4%87%ec%9d%80-%ec%99%9c-%eb%b0%b0%ed%84%b0%eb%a6%ac%ea%b0%80-%ec%a4%91%ec%9a%94%ed%95%a0%ea%b9%8c.md
  - raw/battery-inside-en/en/tech-en/humanoid-robots-are-changing-everyday-life-why-do-batteries-matter.md
  - raw/battery-inside-en/en/interview-en/everything-about-cylindrical-batteries-the-power-source-of-future-ev-transport.md
  - raw/battery-inside-en/en/news-en/lg-energy-solution-to-exclusively-supply-cylindrical-batteries-for-apteras-solar-electric-vehicles.md
  - raw/battery-inside-en/en/interview-en/better-life-i-place-orders-for-lfp-cells-for-ess-and-check-the-result-a-day-in-the-life-f26d55305b.md
confidence: high
---
# Batteries for Humanoid Robots

## Overview

Humanoid robots represent one of the fastest-growing applications for lithium-ion batteries, with the global installed base projected to surge from approximately 23,000 units in 2025 to 6.79 million by 2035 and 53.3 million by 2040, according to SNE Research. Correspondingly, the battery demand for humanoid robots is forecast to rise from 1.37 GWh in 2030 to 138.3 GWh in 2040. Unlike electric vehicles (EVs) or stationary energy storage, humanoid robots impose a unique combination of requirements: high energy density for extended operation (target 8–12 hours per shift vs. current 2–4 hours), high power density for pulsed actuation demands (5–10× peak-to-average ratio), extreme safety due to close human collaboration, compact packaging within the robot torso (dead-space minimization), and cycle life of thousands of cycles for commercial viability. These constraints push battery technology beyond conventional EV and ESS designs.

## Technical Details

### Energy and Power Density

A humanoid robot performing tasks such as walking, lifting, and balancing requires several kilowatt-hours of energy stored in a confined space—typically the torso—without compromising the robot’s center of gravity or range of motion. For example, an 8-hour work shift at an average power draw of 500–1000 W demands 4–8 kWh. Simultaneously, instantaneous power for joint motors and AI computation can exceed average draw by 5–10×, necessitating cells with high rate capability. This dual requirement favors high-nickel NCMA (nickel-cobalt-manganese-aluminum) cathodes, which offer energy densities above 270 Wh/kg and excellent power delivery.

### Cell Format and Chemistry

Cylindrical cells are the dominant format for humanoid robots due to their robust steel or aluminum can, standardized dimensions, mature production, and structural benefits when integrated into the robot’s chassis. Two key sizes are relevant:

- **2170 cells** (21 mm diameter × 70 mm height): LG Energy Solution offers two families—the M-series (high energy density / long life, e.g., M58) and the H-series (high power / fast charge, e.g., H51, H52A). The M58, for instance, is optimized for extended runtime, while H51 and H52A prioritize pulsed power for dynamic motions.
- **46-series cells** (46 mm diameter, variable heights such as 4680 or 4695): These larger-format cylinders provide even higher energy per cell and improved structural integration, enabling “cell-to-body” designs where the battery pack becomes a load-bearing element.

Safety is paramount. LG’s cylindrical cells incorporate a ceramic-coated separator (SRS, Safety Reinforced Separator) and a high-quality NCMA cathode to reduce thermal runaway risk. The robust can also resists mechanical abuse from robot impacts or falls.

### Thermal Management and BMS

Humanoid robots generate significant heat from both the battery and actuators. Advanced thermal management systems—such as liquid cooling plates or phase-change materials—are essential to maintain cell temperatures within safe operating windows (typically 15–45°C). The battery management system (BMS) must monitor individual cell voltages, temperatures, and currents, and implement predictive algorithms to detect anomalies (e.g., internal short circuits) before they escalate. LG’s software-diagnostics platform, including the award-winning “Better.Re” solution, applies AI to extend battery life and predict failures.

## Significance and LG Context

LG Energy Solution has identified humanoid robots as a strategic growth market beyond EVs and ESS. In 2024, the company signed a supply agreement with Bear Robotics (a Silicon Valley-based autonomous mobile robot manufacturer) to exclusively supply 2170 cylindrical cells for its “Servi Plus” and “Carty 100” service/logistics robots. This partnership demonstrates LG’s ability to tailor cell performance (energy vs. power) to specific robot motion profiles.

At InterBattery 2026 and CES 2026, LG showcased its humanoid robot battery portfolio, including the LG CLOiD home robot powered by LG cells. The company also emphasized its commitment to next-generation technologies: solid-state batteries (which could double energy density) and LMR (lithium-manganese-rich) cells for cost-performance balance.

A key differentiator is LG’s use of artificial intelligence in R&D and manufacturing. The “Virtual Lab” initiative uses computational science and generative AI to accelerate cathode material discovery and optimize cell design. The “One Day RFx” project reduces the design-optimization cycle from weeks to under 24 hours by training AI on thousands of parameters (capacity, life, fast-charge, cost) and employing a “Many-to-One” neural network architecture. This AI-driven approach enables rapid customization for diverse robot customer requirements.

## Related Pages

- [[46-series-battery|46-Series Cylindrical Battery (4680/4695)]]
- [[cell-format-comparison|Cell Form Factor Comparison (Cylindrical vs Pouch vs Prismatic)]]
- [[nca-battery|NCA Battery]]
- [[battery-management-system|Battery Management System (BMS)]]
- [[rivian|Rivian]]
- [[tesla|Tesla]]
- [[uam-battery|Batteries for UAM]]