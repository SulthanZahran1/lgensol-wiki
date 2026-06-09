---
title: SoH (State of Health)
created: 2026-06-05
updated: 2026-06-08
type: glossary
tags: [soh, bms, cycle-life]
sources:
  - raw/ko/tech/%eb%b0%b0%ed%84%b0%eb%a6%ac-%ec%9a%a9%ec%96%b4%ec%82%ac%ec%a0%84-soh-state-of-health.md
  - raw/battery-inside-en/en/tech-en/battery-glossary-soh.md
  - raw/battery-inside-en/en/interview-en/lg-energy-solutions-bms-the-doctor-ensuring-battery-safety-and-efficiency.md
  - raw/battery-inside-en/en/tech-en/battery-glossary-bms-battery-management-system.md
  - raw/ko/story/making-every-possibility-bms.md
confidence: high
---
# SoH (State of Health)

## Overview

State of Health (SoH) is a key performance indicator that estimates the remaining capability of a rechargeable battery relative to its initial, fresh state. Expressed as a percentage, 100% SoH represents a new battery meeting all original specifications, while 0% would indicate complete failure. For lithium-ion batteries in electric vehicles (EVs), SoH is the primary metric for determining first-life retirement, typically defined at 80% capacity retention. However, SoH is not a single value — it is a multi-dimensional assessment that encompasses capacity fade, internal resistance growth, power capability loss, and changes in safety margins.

SoH enables transparent used-battery transactions, guides second-life deployment in [[energy-storage-system|ESS (Energy Storage System)]], and helps users optimize charging and driving habits to extend battery life. The difference between two batteries of the same age can be significant: one may retain 95% SoH under gentle use, while another may drop to 85% under aggressive cycling or high temperatures. Understanding SoH is essential for any application relying on battery performance and longevity.

## Technical Details

### Capacity Fade and Resistance-Based SoH

The most common definition of SoH is based on capacity fade:

\[
\text{SoH (\%)} = \frac{\text{Current Capacity}}{\text{Initial Capacity}} \times 100
\]

For example, if a battery originally rated at 60 Ah now delivers only 48 Ah, its SoH is 80%. But this single metric does not tell the full story. As a battery ages, its internal resistance rises — often by 50–100% or more — reducing its ability to deliver high current without excessive voltage drop. A battery at 90% capacity may still suffer from significant power loss if its resistance has doubled. Therefore, modern [[battery-management-system|BMS (Battery Management System)]] uses a combination of capacity, resistance, self-discharge rate, and other health signals to produce a robust SoH estimate.

### Degradation Mechanisms and Non-Linearity

SoH decline follows a characteristic non-linear pattern: a rapid drop early in life (formation period), a long and gradual linear decrease (steady aging), and finally an accelerated degradation as the battery approaches end of life. This behavior is driven by multiple aging mechanisms:
- **Cycle aging** — influenced by depth of discharge, charge/discharge rate (C-rate), and operating temperature.
- **Calendar aging** — time-dependent degradation even when the battery is not cycling, accelerated at high states of charge (SoC) and elevated temperatures.
- **Lithium plating** — a safety-critical degradation mode that occurs under fast charging in cold conditions, leading to capacity loss and internal short-circuit risk.

These factors are interdependent; for instance, high temperature speeds up both cycle and calendar aging, while deep discharge cycles accelerate capacity fade.

### Advanced Diagnostics: dSOH and AI-Driven Models

LG Energy Solution's BMS technology uses a proprietary delta SoH (dSOH) algorithm to track incremental changes in health between diagnostic events. This approach, combined with [[bmts|BMTS (B.around Total Solution)]], leverages big data analytics and electrochemical models to achieve industry-leading accuracy. The company's safety diagnostics include MAVD (Moving Average Voltage Deviation) and RdV (Relaxation Deviation Voltage), which detect subtle voltage anomalies indicative of internal degradation or lithium plating. With over 8,000 BMS-related patents and analysis of 13,000+ cells and 1,000 modules, LG's SoH estimation achieves a degradation prediction error rate of just 1% — the highest precision in the industry.

## Significance and LG Energy Solution Context

SoH is the cornerstone of battery lifecycle management. Accurate SoH enables:
- **Predictive maintenance** — alerting users to accelerated degradation before failure.
- **Residual value assessment** — essential for EV battery resale and [[battery-recycling|end-of-life reuse and recycling]].
- **Second-life repurposing** — batteries below 80% SoH can be deployed in stationary [[energy-storage-system|ESS]] for another 10–15 years.
- **Customer transparency** — services like LG's B·once provide one-time SoH diagnostics for used EV batteries, enabling fair transactions.

LG Energy Solution integrates SoH diagnostics into its **B·lifecare** service, which connects to a vehicle’s data port and analyzes driving and charging habits, weather impact, and battery health scores. The company’s **B.around** platform goes further, combining on-device and cloud-based analytics with AI. A landmark partnership with Qualcomm has produced the industry's first SoC (System-on-Chip) based BMS, using Snapdragon Digital Chassis computing power — 80 times that of conventional BMS hardware. This enables real-time execution of complex degradation algorithms (e.g., anode/cathode-specific aging models) and onboard safety diagnostics without server dependency. The result is a BMS that not only reports SoH with 1% error but also predicts future capacity and resistance trends, empowering drivers and fleet operators to make data-driven decisions.

## Related Pages

- [[battery-management-system|BMS (Battery Management System)]]
- [[bmts|BMTS (B.around Total Solution)]]
- [[internal-resistance|Internal Resistance]]
- [[sox|SoX (State of X)]]
- [[energy-storage-system|ESS (Energy Storage System)]]
- [[battery-recycling|End-of-Life Battery Reuse and Recycling]]