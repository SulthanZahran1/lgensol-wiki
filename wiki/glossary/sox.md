---
title: SoX (State of X)
created: 2026-06-05
updated: 2026-06-08
type: glossary
tags: [soc, soh, bms]
sources:
  - raw/battery-inside-en/en/tech-en/battery-glossary-sox-state-of-x.md
  - raw/battery-inside-en/en/interview-en/lg-energy-solutions-bms-the-doctor-ensuring-battery-safety-and-efficiency.md
  - raw/ko/tech/%eb%b0%b0%ed%84%b0%eb%a6%ac-%ec%9a%a9%ec%96%b4%ec%82%ac%ec%a0%84-soxstate-of-x.md
  - raw/battery-inside-en/en/tech-en/battery-glossary-soc.md
  - raw/battery-inside-en/en/tech-en/battery-glossary-bms-battery-management-system.md
confidence: high
---
# SoX (State of X)

## Overview

SoX (State of X) is the umbrella term for all state estimators used in modern battery management systems (BMS). It encompasses critical indicators such as SoC (State of Charge), SoH (State of Health), SoP (State of Power), SoE (State of Energy), SoF (State of Function), and SoS (State of Safety). The “X” in SoX represents the specific battery characteristic being estimated, reflecting the industry's evolution from simple voltage monitoring to comprehensive, model-based battery diagnosis. As electric vehicles and grid-scale energy storage demand ever-higher performance and safety, accurate SoX estimation has become a cornerstone of intelligent battery control.

## Technical Details

Each SoX estimator serves a distinct purpose and employs a unique set of algorithms:

- **SoC (State of Charge)** – Indicates the remaining charge as a percentage of total capacity. Common estimation methods include open-circuit voltage (OCV) measurement, coulomb counting (current integration), and advanced Kalman filters (including extended Kalman filters). Coulomb counting is simple but suffers from cumulative error, while Kalman filtering provides higher accuracy at the cost of computational complexity.

- **SoH (State of Health)** – Measures the battery's degradation relative to its initial state. It is typically expressed as a percentage, with 100% at manufacture and gradual decline over charge/discharge cycles. For lithium-ion cells, replacement is generally recommended when SoH falls below 80%. SoH is determined by combining capacity fade (loss of usable energy), resistance growth (increased internal impedance), and power capability reduction. LG Energy Solution's BMS achieves a degradation diagnosis error rate of just 1% (industry-leading).

- **SoP (State of Power)** – Estimates the maximum instantaneous power the battery can deliver (discharge) or accept (charge) over a specified time interval (e.g., 2 seconds, 10 seconds, 30 seconds). SoP is critical for vehicle acceleration, regenerative braking, and peak shaving in ESS. It relies on real-time measurements of voltage, current, temperature, and the battery's impedance model.

- **SoE (State of Energy)** – Expresses the remaining usable energy in watt-hours (Wh), accounting for voltage variations and efficiency losses. Unlike SoC (which is a ratio), SoE provides an absolute energy value useful for range prediction in EVs.

- **SoF (State of Function)** – A binary or tiered assessment of whether the battery can perform its intended function under current conditions. For example, an EV battery may have sufficient SoC but be too cold to deliver high power; SoF indicates operational readiness.

- **SoS (State of Safety)** – Evaluates the risk of unsafe events such as over-temperature, over-voltage, under-voltage, or internal short circuits. LG Energy Solution's BMS incorporates patented safety diagnostics like MAVD (Moving Average Voltage Deviation), RdV (Relaxation Deviation Voltage), and dSOH (Delta State of Health), achieving a detection rate of over 90%.

The estimation of multiple SoX parameters is interdependent. For instance, SoH directly influences SoC accuracy because capacity fade changes the baseline for coulomb counting. Similarly, SoP depends on both SoC and SoH. Modern BMS platforms use AI and machine learning to fuse these signals into a coherent state model, enabling predictive, rather than reactive, battery management.

LG Energy Solution's advanced BMS leverages a system-on-chip (SoC) architecture co-developed with Qualcomm. The Snapdragon Digital Chassis platform provides 80 times the computing power of conventional BMS hardware, allowing real-time execution of complex degradation algorithms and collection of much larger datasets for anomaly detection. This enables features such as residual capacity prediction over a defined period and component-level (anode/cathode) degradation tracking.

## Significance and LG Energy Solution Context

The SoX framework represents a paradigm shift from simple monitoring to predictive, model-based control. By integrating multiple state estimates, a BMS can optimize charging profiles, extend cycle life, prevent thermal runaway, and maximize usable energy. SoX data is also essential for Battery Passport compliance, second-life battery valuation, and Battery-as-a-Service (BaaS) business models.

LG Energy Solution has embedded comprehensive SoX estimation into its **BMTS (B.around Total Solution)** platform, which combines cloud-based analytics with proprietary algorithms trained on data from over 130,000 cells and 1,000 modules. The **B·once** service provides a one-time SoX assessment for used EV batteries, while **B-Lifecare** offers continuous monitoring through a data collection device connected to the vehicle. These services report driving range, energy consumption, charging habits, and even weather-related efficiency – giving drivers actionable insight into their battery's health.

With more than 8,000 BMS-related patents (world-leading), LG Energy Solution continues to push the boundaries of SoX accuracy. The recent collaboration with Qualcomm has resulted in the industry's first SoC-based BMS diagnostic solution, bringing 80x higher computing performance and the ability to run advanced safety and degradation algorithms directly on the vehicle without cloud dependency.

## Related Pages

- [[battery-management-system|BMS (Battery Management System)]]
- [[bmts|BMTS (B.around Total Solution)]]
- [[cell-balancing|Cell Balancing]]
- [[soc|SoC (State of Charge)]]
- [[soh|SoH (State of Health)]]
- [[battery-recycling|End-of-Life Battery Reuse and Recycling]]
- [[battery-passport|Battery Passport]]
- [[baas|BaaS (Battery as a Service)]]
