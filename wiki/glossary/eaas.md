---
title: EaaS (Energy as a Service)
created: 2026-06-05
updated: 2026-06-08
type: glossary
tags: [ess, esg, partnership]
sources:
  - raw/battery-inside-en/en/tech-en/what-makes-lg-energy-solutions-ess-batteries-different-as-tesla-ess-partner.md
  - raw/battery-inside-en/en/tech-en/battery-glossary-eaas.md
  - raw/corporate/kr/pages/esg-society-esg-management.md
  - raw/corporate/kr/pages/esg-system-partnership.md
  - raw/ko/tech/%ed%85%8c%ec%8a%ac%eb%9d%bc%ec%9d%98-ess-%ed%8c%8c%ed%8a%b8%eb%84%88-lg%ec%97%90%eb%84%88%ec%a7%80%ec%86%94%eb%a3%a8%ec%85%98%ec%9d%98-ess-%eb%b0%b0%ed%84%b0%eb%a6%ac%eb%8a%94-%eb%ac%b4%ec%97%87.md
confidence: high
---
# EaaS (Energy as a Service)

## Overview

Energy as a Service (EaaS) is a subscription-based business model that delivers guaranteed energy outcomes—reliability, savings, or carbon reduction—without requiring customers to own or finance physical energy assets. Under an EaaS contract, a service provider designs, installs, owns, operates, and maintains distributed energy resources (DERs) such as solar arrays, battery [[energy-storage-system|energy storage systems (ESS)]], and energy management software. The customer pays a predictable operational expenditure (OPEX) tied to energy consumption, availability, or performance metrics, thereby eliminating upfront capital expenditure (CAPEX).

EaaS has gained momentum due to three converging trends: the rapid expansion of variable renewable generation, the declining cost of lithium-ion ESS (global system-level prices falling below $200/kWh by 2025), and the digitisation of energy grids via IoT sensors, AI/ML analytics, and cloud platforms. Together, these trends enable third-party aggregators to optimise energy flows across multiple sites, sell performance rather than hardware, and unlock revenue streams from grid services like demand response and frequency regulation.

## Technical Details

### Service Models
EaaS manifests in several distinct operational models:
- **Power Purchase Agreements (PPA)** – A provider installs on-site solar or wind generation; the customer pays per kWh generated, typically at a rate below the local utility tariff.
- **Energy Storage as a Service** – Behind-the-meter ESS (typically 100 kW–10 MW) is deployed to reduce demand charges, provide backup power, and enable participation in demand response programmes. The provider handles all maintenance, lifecycle management, and cell replacement.
- **Virtual Power Plant (VPP) Services** – Aggregated DERs—rooftop solar, EV chargers, stationary batteries—are orchestrated via a cloud platform into a VPP that participates in wholesale electricity markets, capacity auctions, and ancillary services. Revenues are shared with asset owners.
- **Energy Efficiency as a Service** – Providers finance and implement efficiency upgrades (lighting, HVAC, motor drives) and are repaid through a share of measured energy savings.

### Enabling Technologies
Real‑time monitoring and control are foundational. Smart meters, IoT sensors, and AI analytics process voltage, current, temperature, and resistance data from thousands of battery cells. LG Energy Solution’s **EMO (Energy Market Optimizer)** platform calculates **DME (Dynamic Marketable Energy)**—the quantity of stored energy that can be confidently sold into the grid at any given moment. DME is derived by fusing battery telemetry, system efficiency data, and grid price signals through a two‑stage AI/ML pipeline that incorporates weather forecasts and historical generation patterns. This enables season‑ and terrain‑specific optimisation, reducing forecast errors by up to 30% compared to conventional methods.

### LG’s ESS Hardware Foundation
LG Energy Solution supplies ESS batteries based on advanced LFP (lithium iron phosphate) chemistry. Key technical differentiators include:
- **Lamination & Stacking process**: Increases volumetric energy density by up to 12% over conventional winding while ensuring uniform heat dissipation.
- **Cell-to-Pack (CTP) design**: Eliminates module-level housing, improving system-level energy density and simplifying thermal management.
- **Safety Reinforced Separator (SRS)**: Suppresses internal short circuits under high‑temperature or high‑load conditions.
- **Cycle life**: Up to 15,000 charge/discharge cycles, enabling 15–20 years of daily operation in grid applications.

### Production Scale & Localisation
To serve the projected 618 GWh global ESS market by 2035, LG operates five North American manufacturing sites: Holland and Lansing (Michigan), Ultium Cells (Tennessee), Honda JV (Ohio), and NextStar Energy (Ontario). By 2026, LG targets 60 GWh of ESS production capacity (over 50 GWh in North America) and a 90 GWh order backlog. The Lansing facility will begin supplying batteries for Tesla’s Megapack 3 in 2027, leveraging a localised supply chain to meet U.S. content requirements and accelerate delivery timelines.

## Significance & LG Context

EaaS lowers the barrier to adopting advanced energy technologies. Commercial and industrial customers can access ESS, solar, and AI‑driven energy management without large upfront investments. Providers benefit from recurring revenue streams and the ability to optimise across a portfolio of assets, reducing per‑unit costs.

LG Energy Solution has built a full EaaS ecosystem through its subsidiary [[avel|AVEL]]. AVEL operates a VPP platform that aggregates renewable generators, ESS, and demand resources. In Jeju, South Korea, LG is the leading power trading intermediary in the island’s renewable energy pilot programme, operating the country’s first and largest distribution‑connected standalone ESS. The platform uses real‑time AI/ML to forecast generation and load, then dispatches stored energy to arbitrage time‑of‑use prices or provide ancillary services. LG also established Vertech, a North American ESS system integrator, to deliver turnkey solutions from project design through O&M.

The partnership with [[tesla|Tesla]] underscores LG’s position: Tesla selected LG as a battery supplier for its Megapack 3 utility‑scale ESS, citing LG’s production reliability, localised supply chain, and advanced LFP technology. This collaboration validates the importance of integrated hardware–software EaaS offerings.

## Related Pages

- [[avel|AVEL]]
- [[lg-energy-solution|LG Energy Solution]]
- [[energy-storage-system|ESS (Energy Storage System)]]
- [[tesla|Tesla]]
- [[baas|BaaS (Battery as a Service)]]
- [[battery-passport|Battery Passport]]
- Vertech
- Virtual Power Plant (VPP)