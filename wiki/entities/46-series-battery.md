---
title: 46-Series Cylindrical Battery (4680/4695)
created: 2026-06-05
updated: 2026-06-08
type: entity
tags: [cylindrical, 46-series, energy-density, fast-charging, ev]
sources:
  - raw/battery-inside-en/en/news-en/lg-energy-solution-to-supply-next-generation-4695-cylindrical-batteries-to-rivian.md
  - raw/battery-inside-en/en/interview-en/everything-about-cylindrical-batteries-the-power-source-of-future-ev-transport.md
  - raw/ko/story/%ec%b0%a8%ec%84%b8%eb%8c%80-%ec%a0%84%ea%b8%b0-%ec%9d%b4%eb%8f%99%ec%88%98%eb%8b%a8%ec%9d%98-%eb%8f%99%eb%a0%a5%ec%9b%90-%ec%9b%90%ed%86%b5%ed%98%95-%eb%b0%b0%ed%84%b0%eb%a6%ac%ec%9d%98-%eb%aa%a8.md
  - raw/ko/news/lg%ec%97%90%eb%84%88%ec%a7%80%ec%86%94%eb%a3%a8%ec%85%98-%e7%be%8e-%eb%a6%ac%eb%b9%84%ec%95%88rivian%ec%97%90-%ec%b0%a8%ec%84%b8%eb%8c%80-%ec%9b%90%ed%86%b5%ed%98%95-4695.md
  - raw/corporate/kr/documents/37912-원통형-배터리-카탈로그-46시리즈.md
confidence: high
---
# 46-Series Cylindrical Battery (4680/4695)

## Overview

The 46-series cylindrical battery represents a generational leap in large-format lithium-ion cell design, defined by a 46 mm diameter and heights ranging from 80 mm to 120 mm. The most common variants—4680 (46 mm × 80 mm) and 4695 (46 mm × 95 mm)—deliver 5–6 times the energy capacity of the conventional 2170 cell (~4.8 Ah vs. ~0.8–1.0 Ah for a 2170). This scale-up is possible because active material volume scales with the square of the diameter, and the taller 95 mm variant further increases capacity without altering the cell footprint.

Introduced as the next-generation form factor for electric vehicles, 46-series cells reduce pack complexity dramatically. For example, a 2170-based pack requiring 4,400 cells can be replaced by only 828 cells of the 4680 format. Fewer interconnects improve pack-level reliability, simplify thermal management, and enable high-automation assembly. The format has been widely adopted by Tesla (4680) and LG Energy Solution (both 4680 and 4695), the latter supplying Rivian and Chery.

## Technical Details

**Design and Internal Architecture**
46-series cells employ a tabless or multi-tab electrode architecture. Conventional cylindrical cells use a single tab welded to the electrode foil, which creates a long current path and high internal resistance. In the tabless design, the entire edge of the anode and cathode foil serves as a current collector, reducing the current path length by up to 50%. This lowers internal resistance significantly, enabling higher continuous discharge rates and ultra-fast charging—critical for <15‑minute 10–80% SOC charging.

**Safety Mechanisms**
The rigid steel can withstand internal pressures exceeding 20 bar, and the cell incorporates multiple safety devices:

- **Current Interrupt Device (CID):** If internal gas pressure exceeds a safe threshold (typically 10–15 bar), the CID disconnects the electrical circuit, switching the cell to an open-circuit state.
- **Vent:** A controlled rupture disc releases gas at a defined pressure (e.g., 20–25 bar), preventing catastrophic rupture.
- **Thermal Propagation Resistance:** In honeycomb arrays, a single cell thermal runaway does not propagate to adjacent cells—verified in heater tests where the venting cell’s sidewall remained intact and neighboring cells stayed below ignition temperature.

**Chemistry**
LG Energy Solution’s 46-series cells use a high-nickel NCMA (LiNi₀.₈₉Co₀.₀₅Mn₀.₀₅Al₀.₀₁O₂) cathode, which delivers gravimetric energy density above 270 Wh/kg at the cell level. The quaternary composition balances energy density (via Ni) with structural stability (via Co, Mn) and thermal safety (via Al). For applications requiring robust low-temperature performance—such as Chery’s European-market models—LG Energy Solution offers an NCM variant optimized for output and charging efficiency in cold climates, outperforming LFP cells in sub‑0°C operation.

**Physical Dimensions and Configurations**
- **4680:** 46 mm diameter, 80 mm height; typical capacity 25–30 Ah, energy ~90–110 Wh.
- **4695:** 46 mm diameter, 95 mm height; typical capacity 30–35 Ah, energy ~110–130 Wh.
- **46XX (other heights):** 46mm diameter variants up to 120 mm height allow further capacity tuning for different vehicle platforms.

## Significance and LG Energy Solution Context

LG Energy Solution (LGES) is a leading producer of 46-series cells, having secured two major long-term contracts:

- **Rivian (2024):** 67 GWh of 4695 cells over five years for the R2 SUV, starting 2026. The cells will be produced at LGES’s new Arizona plant in Queen Creek, which has a dedicated cylindrical capacity of 36 GWh (plus 17 GWh for ESS LFP pouch cells). Construction began in 2024, with steel frame work underway and production targeted for 2026.
- **Chery Automobile (2025):** 8 GWh of 46-series cells over six years, beginning in early 2026, for Chery’s flagship EV models. This marks the first large-scale supply of cylindrical cells by a Korean battery maker to a Chinese OEM.

LGES plans to start 4680 mass production at its Ochang Energy Plant in Korea in the second half of 2025, gaining process experience before ramping the Arizona line. The company’s 46-series product line is differentiated by high‑Ni NCMA chemistry, advanced safety features, and a proprietary Cell Array Structure (CAS) module that improves thermal management and structural rigidity at the pack level.

The 46-series format positions LGES to compete directly with Tesla’s in-house 4680 production and with other cylindrical cell manufacturers such as Panasonic and Samsung SDI. By offering both 4680 and 4695 heights, LGES provides customers flexibility to optimize cell capacity for different vehicle architectures—from sedans (4680) to larger SUVs and trucks (4695). The format also supports cell-to-pack (CTP) integration, where cells are directly bonded into the pack structure, eliminating module hardware and boosting volumetric energy density by 10–15%.

## Related Pages

- [[cell-format-comparison|Cell Form Factor Comparison (Cylindrical vs Pouch vs Prismatic)]]
- [[rivian|Rivian]]
- [[tesla|Tesla]]
- [[fast-charging|Fast Charging]]
- [[high-nickel-battery|High-Nickel Battery]]
- [[ncma-battery|NCMA (Quaternary) Battery]]
- [[cell-to-pack|Cell-to-Pack Technology]]
- Thermal Propagation Management
- LG Energy Solution Arizona Plant