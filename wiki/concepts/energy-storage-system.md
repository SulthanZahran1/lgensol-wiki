---
title: ESS (Energy Storage System)
created: 2026-06-05
updated: 2026-06-08
type: concept
tags: [ess, partnership, lfp, ctp]
sources:
  - raw/battery-inside-en/en/tech-en/what-makes-lg-energy-solutions-ess-batteries-different-as-tesla-ess-partner.md
  - raw/battery-inside-en/en/interview-en/better-life-i-place-orders-for-lfp-cells-for-ess-and-check-the-result-a-day-in-the-life-f26d55305b.md
  - raw/ko/tech/%ed%85%8c%ec%8a%ac%eb%9d%bc%ec%9d%98-ess-%ed%8c%8c%ed%8a%b8%eb%84%88-lg%ec%97%90%eb%84%88%ec%a7%80%ec%86%94%eb%a3%a8%ec%85%98%ec%9d%98-ess-%eb%b0%b0%ed%84%b0%eb%a6%ac%eb%8a%94-%eb%ac%b4%ec%97%87.md
  - raw/battery-inside-en/en/news-en/lg-energy-solution-unveils-prime-a-residential-energy-storage-system.md
  - raw/ko/tech/%ec%8b%a0%ec%9e%ac%ec%83%9d%ec%97%90%eb%84%88%ec%a7%80%ec%9d%98-%ed%95%b5%ec%8b%ac-%ec%84%b8%ea%b3%84%eb%8a%94-%ec%a7%80%ea%b8%88-ess%ec%97%90-%ec%a3%bc%eb%aa%a9%ed%95%9c%eb%8b%a4.md
confidence: high
---
# ESS (Energy Storage System)

## Overview / Introduction

An Energy Storage System (ESS) stores electrical energy for later use, enabling the integration of variable renewable sources like solar and wind, stabilizing the grid, and providing backup power. ESS installations range from residential (2–20 kWh) to utility-scale (MWh to GWh) deployments. The global ESS market is projected to grow from 235 GWh in 2024 to 618 GWh by 2035, with a compound annual growth rate of 21.5% (IEA). This growth is driven by decarbonization policies, rising electricity demand from AI data centers, and the need for peak shaving and frequency regulation.

A typical ESS consists of four main subsystems: battery cells, a Battery Management System (BMS), a Power Conversion System (PCS), and an Energy Management System (EMS). The battery pack stores DC energy; the PCS converts between DC and AC; the BMS monitors cell voltage, current, and temperature, and can disconnect the system under fault conditions; the EMS optimizes charging/discharging based on grid signals and energy prices.

## Technical Details

### Battery Chemistry – LFP

The dominant chemistry for ESS is Lithium Iron Phosphate (LFP). Its olivine crystal structure (LiFePO₄) provides exceptional thermal stability: internal decomposition temperature exceeds 500°C, and even during thermal runaway, peak temperatures remain around 400°C. This dramatically reduces fire risk compared to NCM or NCA chemistries. LFP cells achieve 5,000–10,000 cycles at 80% depth-of-discharge, with advanced designs reaching 15,000 cycles. The trade-off is lower energy density (90–170 Wh/kg) versus ternary chemistries, which is acceptable for stationary applications where weight and volume are less critical.

LG Energy Solution’s LFP pouch cells employ lamination and stacking processes that boost energy density by up to 12% over conventional wound cells. The uniform stacking also improves heat dissipation, enhancing safety. The cells are paired with a Safety Reinforced Separator (SRS) that resists internal short circuits. For large-scale systems, LG applies Cell-to-Pack (CTP) technology, eliminating intermediate module structures to increase pack-level energy density by ~15% and simplify thermal management.

### System Architecture

A complete ESS integrates multiple battery racks, each containing several modules of series/parallel cells. The BMS ensures cell balancing and monitors state-of-charge (SoC). The PCS (inverter) typically handles bidirectional power flow with efficiency above 97%. Thermal management uses liquid cooling or forced air to maintain the optimum operating range of 15–35°C. Fire protection systems include gas detection, suppression (e.g., Novec 1230), and venting. The EMS aggregates data from BMS and PCS to execute charge/discharge schedules, participate in energy markets, and respond to grid operator signals.

LG’s ESS solutions also incorporate its proprietary Battery Management & Total Solution (BMTS) platform, which provides real-time monitoring, predictive maintenance, and cloud-based analytics. This platform enables remote firmware updates and integration with renewable energy systems.

### Manufacturing and Quality Control

Cell production involves precise electrode coating, drying, slitting, winding/stacking, electrolyte filling, formation, and aging. Every cell undergoes dimensional, weight, voltage, and impedance tests. Sample cells from each batch undergo extended cycling to verify capacity (target ≥ 98% of design) and calendar life. For example, LG’s LFP pouch cells for ESS are tested to confirm >15,000 cycles at 1C/1C. Quality metrics include capacity retention, DC internal resistance growth, and safety tests (overcharge, short circuit, nail penetration).

## Significance / LG Context

LG Energy Solution has emerged as a leading ESS battery supplier, notably as the official battery partner for Tesla’s Megapack 3 (starting 2027 from the Lansing, Michigan plant) and Powerwall. This partnership was publicly disclosed by the U.S. government during the IPEM forum, highlighting the strategic importance of a reliable, localized supply chain.

To support large-scale ESS projects, LG has built a North American production network of five sites: Holland (Michigan), Lansing (Michigan), Ultium Cells JV (Tennessee), Honda JV (Ohio), and NextStar Energy (Ontario). These factories operate a flexible hybrid model, producing both EV and ESS cells to respond to demand shifts. By 2026, LG’s ESS production capacity is targeted at 60 GWh (over 50 GWh in North America), with an order backlog of ~90 GWh.

Beyond cells, LG delivers integrated solutions through its U.S. subsidiary Vertech (formerly NEC Energy Solutions), which provides system integration, design, installation, and maintenance. The company’s AVEL affiliate pursues Energy Aggregation (EA) business, connecting renewables and ESS to predict generation and optimize grid stability. Recent projects include a Jeju Island grid-stabilization pilot with Korea Southern Power Company.

LG’s ESS product portfolio includes the Enblock E (LFP, residential, up to 15.5 kWh stackable) and Enblock S (NCM, high energy density), as well as the Prime+ residential inverter-integrated system for the North American market. The company also supplies grid-scale containers to customers like Tesla.

The shift to LFP is central to LG’s ESS strategy. The company leverages its advanced lamination/stacking process to overcome LFP’s lower energy density, achieving competitive system-level costs. The thermal stability of LFP, combined with CTP packaging and SRS separators, positions LG’s ESS as a safe, long-life solution for 10–20 year installations.

## Related Pages

- [[lfp-battery|LFP (Lithium Iron Phosphate) Battery]]
- [[cell-to-pack|Cell-To-Pack (CTP)]]
- [[pcs|PCS (Power Conversion System)]]
- [[ems|EMS (Energy Management System)]]
- [[battery-safety|Battery Safety and Thermal Runaway]]
- [[avel|AVEL]]
- [[tesla|Tesla]]
- [[eaas|Energy as a Service (EaaS)]]