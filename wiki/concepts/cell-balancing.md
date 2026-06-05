---
title: Cell Balancing
created: 2026-06-05
updated: 2026-06-05
type: concept
tags: [cell-balancing, bms, soc, safety]
sources:
  - raw/ko/tech/%ec%a0%84%ec%a7%80%ec%a0%84%eb%8a%a5%ed%95%9c-%ec%a0%84%ec%a7%80-%ec%9d%b4%ec%95%bc%ea%b8%b0-%ec%97%90%eb%84%88%ec%a7%80%ec%9d%98-%ea%b7%a0%ed%98%95%ec%9d%84-%eb%a7%9e%ec%b6%94%eb%8b%a4-2.md
  - raw/ko/tech/%eb%b0%b0%ed%84%b0%eb%a6%ac-%ec%9a%a9%ec%96%b4%ec%82%ac%ec%a0%84-%ec%85%80-%eb%b0%b8%eb%9f%b0%ec%8b%b1cell-balancing.md
  - raw/ko/story/making-every-possibility-bms.md
  - raw/ko/news/%ea%b0%81%ed%98%95-%eb%b0%b0%ed%84%b0%eb%a6%ac-%ea%b0%9c%eb%b0%9c-%eb%82%98%ec%84%a0%eb%8b%a4-%e7%be%8e-gm%ea%b3%bc-%ea%b3%b5%eb%8f%99-%ea%b0%9c%eb%b0%9c-%ea%b3%84%ec%95%bd-%ec%b2%b4%ea%b2%b0-2.md
  - raw/ko/news/lg%ec%97%90%eb%84%88%ec%a7%80%ec%86%94%eb%a3%a8%ec%85%98-%ed%80%84%ec%bb%b4-%ec%b2%a8%eb%8b%a8-bms-%ec%86%94%eb%a3%a8%ec%85%98-%ea%b0%9c%eb%b0%9c-%eb%82%98%ec%84%a0%eb%8b%a4.md
confidence: high
---
# Cell Balancing

## Core Idea
Cell balancing reduces imbalance among series-connected cells so usable pack capacity and safety are not limited by the weakest cell. It connects directly to [[battery-management-system|BMS (Battery Management System)]], [[bmts|BMTS (B.around Total Solution)]], and [[pcm|PCM (Protection Circuit Module)]].

## Technical Notes
- Passive balancing burns excess energy as heat; active balancing moves charge between cells but adds circuit complexity.
- Balancing works with SoC estimation, voltage sensing, temperature sensing, and BMS control logic.
- It is essential in EV and ESS packs because small cell differences become pack-level constraints over many cycles.

## LG Energy Solution Context
In the raw corpus, this concept appears as a practical engineering lever rather than a standalone textbook term. It affects how LG Energy Solution balances performance, safety, manufacturability, cost, and customer requirements.

## Related
- [[battery-management-system|BMS (Battery Management System)]]
- [[bmts|BMTS (B.around Total Solution)]]
- [[pcm|PCM (Protection Circuit Module)]]
- [[soc|SoC (State of Charge)]]
- [[sox|SoX (State of X)]]
- [[azs-stacking|AZS (Advanced Z-Stacking)]]
