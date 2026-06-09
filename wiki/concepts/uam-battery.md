---
title: Batteries for UAM
created: 2026-06-05
updated: 2026-06-08
type: concept
tags: [uam, aerospace, energy-density, lithium-sulfur]
sources:
  - raw/ko/tech/uam-%ec%83%81%ec%9a%a9%ed%99%94-%ec%99%9c-%eb%b0%b0%ed%84%b0%eb%a6%ac-%ea%b8%b0%ec%88%a0%ec%97%90-%eb%8b%ac%eb%a0%a4-%ec%9e%88%ec%9d%84%ea%b9%8c.md
  - raw/battery-inside-en/en/tech-en/game-changer-battery-lighter-weight-and-longer-lasting-lithium-sultur-battery.md
  - raw/battery-inside-en/en/tech-en/batteries-flying-in-the-skies-all-about-urban-air-mobility-uam-batteries.md
  - raw/battery-inside-en/en/interview-en/better-life-i-place-orders-for-lfp-cells-for-ess-and-check-the-result-a-day-in-the-life-f26d55305b.md
  - raw/battery-inside-en/en/opinion-en/what-are-the-latest-technology-trends-and-industry-outlook-for-lithium-sulfur-batteries-c9bb9470a6.md
confidence: high
---
# Batteries for UAM

## Overview

Urban Air Mobility (UAM) refers to an air transportation system operating at altitudes of 300–600 meters in urban environments, using electric vertical takeoff and landing (eVTOL) aircraft to carry passengers or cargo. Unlike ground-based electric vehicles, UAM imposes extreme demands on batteries: they must simultaneously deliver high specific energy (300–500 Wh/kg) for range, high power (4–6 C-rate) for takeoff and climb, uncompromising safety (thermal runaway prevention, redundant fail-safe), long cycle life for economic viability, and resilience to altitude-induced temperature and pressure variations. The global eVTOL battery market is projected to grow from approximately $500 million (2024) to $4.5 billion by the early 2030s, with annual growth of 20–25%. Key regulatory bodies—FAA (USA), EASA (Europe), and CAAC (China)—are actively certifying airworthiness and operational frameworks. South Korea’s K-UAM program targets commercial service by 2028, with the “K-UAM Grand Challenge” and nationwide testbeds validating integrated operations including vertiport management and AI-based traffic control.

## Technical Details

### Specific Energy and Power

UAM batteries must achieve cell-level specific energy of at least 300–400 Wh/kg for 30–50 km urban missions (taxi-like service) and 400–500 Wh/kg for 50–150 km intercity routes (replacing buses or regional rail). For missions extending beyond 150 km, specific energy targets exceed 500 Wh/kg, approaching the range of high-speed trains or aircraft. This surpasses current EV cells (~250–300 Wh/kg). The weight penalty is severe: each kilogram of battery subtracts directly from payload, and unlike fuel, battery weight does not decrease during flight. Power density is equally critical; eVTOL requires sustained 4–6 C discharge during vertical lift and climb, with additional reserve for go-around during landing. High C-rate operation generates substantial I²R heat, demanding advanced thermal management and precise battery management system (BMS) control.

### Safety and Certification

Aviation safety standards require that a single cell thermal runaway must not propagate to neighboring cells (thermal propagation prevention). The battery pack must survive crash impacts without catastrophic failure and maintain operation after a single cell failure (redundant architecture). Certification by FAA, EASA, or CAAC involves rigorous testing: overcharge, short circuit, crush, altitude cycling, and thermal abuse. LG Energy Solution’s UAM battery designs incorporate cell-level safety features, flame-retardant separators, and a BMS that continuously monitors state-of-charge, temperature, and pressure to enable early fault detection. For extreme low-temperature environments (down to -60°C), LG has partnered with South8 Technologies to develop a liquefied gas electrolyte that remains functional in deep-space or high-altitude conditions. This technology, recognized by TIME as one of the “200 Best Inventions of 2024,” is being applied within a NASA- and KULR-funded project for next-generation space battery solutions. In case of a thermal event, the liquefied gas electrolyte rapidly vaporizes, cooling the cell and converting it into a non-functional “dummy cell,” drastically reducing fire risk.

### Promising Chemistries

**Lithium-sulfur (Li-S) batteries** offer theoretical specific energy of 2600 Wh/kg; practical cells target 400–600 Wh/kg with lower weight than lithium-ion. However, Li-S faces cycle-life limitations (hundreds vs. thousands of cycles), polysulfide shuttling, and lower rate capability. LG Energy Solution, in collaboration with KAIST, has developed a fluorinated ether solvent that suppresses electrode corrosion and reduces electrolyte volume by more than 60%, improving stability and cycle life. **Lithium metal batteries with high-nickel cathodes** deliver 350–450 Wh/kg with better rate capability, while **all-solid-state batteries** (solid electrolyte, no liquid) promise both high energy density and intrinsic safety, making them strong candidates for aviation. LG is also pioneering **LMR (Lithium-Manganese-Rich) cells** for balanced cost and performance, first showcased at InterBattery 2026 alongside UAM, robotics, and drone applications.

## Significance and LG Context

LG Energy Solution has identified UAM as a strategic growth market and established a “Future Technology Center” in 2023 dedicated to next-generation batteries for aerospace and robotics. Beyond UAM, these developments extend to drones, humanoid robots, and cube satellites—all requiring lightweight, high-energy, high-power solutions. At InterBattery 2026, LG exhibited UAM batteries alongside home robots (LG CLOiD), autonomous delivery robots (Carti100), blood-transport drones, and cube satellites, underscoring a portfolio expansion beyond EV and ESS. The partnership with South8 Technologies for liquefied gas electrolyte batteries is a key enabler for aerospace and space applications, funded by the Texas Space Commission and involving KULR Technology Group. LG also continues to advance solid-state and bipolar technologies through its global R&D network, positioning itself as a leader in the emerging UAM battery market.

## Related Pages

- [[lithium-sulfur-battery|Lithium-Sulfur Battery]]
- [[next-gen-battery-overview|Next-Generation Battery Comprehensive Comparison]]
- [[solid-state-battery|Solid-State Battery]]
- [[anodeless-battery|Anodeless Battery]]
- [[bipolar-technology|Bipolar Technology]]
- [[humanoid-robot-battery|Batteries for Humanoid Robots]]