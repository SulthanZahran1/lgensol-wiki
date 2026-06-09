---
title: SoC (State of Charge)
created: 2026-06-05
updated: 2026-06-08
type: glossary
tags: [soc, bms]
sources:
  - raw/battery-inside-en/en/tech-en/battery-glossary-soc.md
  - raw/ko/tech/%eb%b0%b0%ed%84%b0%eb%a6%ac-%ec%9a%a9%ec%96%b4%ec%82%ac%ec%a0%84-soc-state-of-charge.md
  - raw/battery-inside-en/en/interview-en/lg-energy-solutions-bms-the-doctor-ensuring-battery-safety-and-efficiency.md
  - raw/battery-inside-en/en/tech-en/battery-glossary-bms-battery-management-system.md
  - raw/battery-inside-en/en/interview-en/incharge-jeong-hyeon-in-of-the-diagnostic-development-for-bms-safety-team-builds-data-ma-d492da0d25.md
confidence: high
---
# SoC (State of Charge)

## Overview / Introduction

State of Charge (SoC) is the estimated remaining capacity of a battery, expressed as a percentage of its total usable capacity. It serves as the battery's fuel gauge, telling the user how much energy is left before the next recharge is required. SoC is a fundamental parameter managed by the [[battery-management-system|BMS (Battery Management System)]], and its accurate estimation directly impacts battery safety, performance, and user confidence.

In everyday terms, when a smartphone shows 75% or an electric vehicle dashboard reads 120 km of range, that number is derived from the SoC. For rechargeable lithium-ion batteries—used in everything from mobile phones to large-scale [[energy-storage-system|ESS (Energy Storage System)]]—SoC must be continuously monitored and controlled to prevent overcharge, overdischarge, and thermal runaway.

## Technical Details

SoC is defined mathematically as:

**SoC (%) = (Remaining Capacity / Total Usable Capacity) × 100**

A fully charged battery has an SoC of 100%, while a fully discharged battery (at the manufacturer's cutoff voltage) is at 0%. However, the "usable capacity" is not the same as the absolute chemical capacity; it is the capacity window that the BMS allows for safe operation.

### Measurement Methods

Accurate SoC estimation is a core competitive capability for battery makers. Several methods exist, each with trade-offs:

- **Chemical Method**: Measures electrolyte specific gravity or pH. Only applicable to flooded lead-acid batteries where the electrolyte is accessible. Not used for modern lithium-ion cells.

- **Voltage Method**: Correlates open-circuit voltage (OCV) to SoC using a pre-characterized lookup table. Simple and low-cost, but inaccurate under load or at partial states of charge because voltage depends on current rate, temperature, and age.

- **Current Integration (Coulomb Counting)**: Integrates charge/discharge current over time. Straightforward, but suffers from cumulative drift due to sensor offset and noise. Requires periodic recalibration (e.g., at full charge or rest).

- **Pressure Method**: Used for nickel-metal hydride cells, where internal pressure correlates with charge level.

Advanced BMS implementations combine these methods with model-based algorithms. The most common industrial approach uses an **extended Kalman filter (EKF)** that fuses voltage, current, and temperature measurements with an electrochemical or equivalent-circuit battery model. This provides real-time, high-accuracy SoC estimation even under dynamic loads.

### Key Challenges

SoC estimation is difficult because battery voltage is a nonlinear function of many variables:

- **Load current**: A cell at 50% SoC under a high discharge pulse may show the same terminal voltage as a nearly empty cell at rest.
- **Temperature**: Lower temperatures increase internal resistance and shift the OCV curve, causing underestimation if not corrected.
- **Aging ([[soh|SoH – State of Health]])**: Capacity fade and impedance growth alter the relationship between voltage and SoC.

Modern BMS systems therefore use **adaptive algorithms** that update the battery model in real time, accounting for aging and changing conditions. LG Energy Solution’s BMS, for example, leverages more than 13,000 cells and 1,000 modules’ worth of empirical data to train its estimation models, achieving a degradation prediction error of just 1%—the industry's best.

## Significance / LG Context

### Safety and Usability

SoC directly enables safe battery operation. Manufacturers set charge voltage limits below 100% SoC and discharge limits above 0% SoC to create a safety buffer. This prevents overcharge (which can trigger lithium plating and thermal runaway) and overdischarge (which can cause copper dissolution and internal short circuits). For users, accurate SoC provides reliable range estimation in EVs and runtime prediction in portable devices.

### LG Energy Solution’s BMS Leadership

LG Energy Solution has developed advanced SoC estimation algorithms as part of its broader BMS technology portfolio. Key highlights include:

- **B.around / BMTS (Battery Management Total Solution)**: An integrated platform combining cloud connectivity, AI, and real-time diagnostics. BMTS uses high-performance System-on-Chip (SoC) computing—partnering with Qualcomm’s Snapdragon Digital Chassis—to process 80 times more data than conventional BMS hardware. This enables:
  - Real-time safety diagnostics (fire risk detection, MAVD, RdV, dSOH algorithms) with over 90% detection accuracy.
  - Degradation forecasting and cell-level health indicators.
  - On‑board analytics without requiring a cloud connection.

- **B-Lifecare Service**: A customer-facing app that provides driving range, charging habits, battery health scores, and nearby charger information—all derived from precise SoC and [[soh|SoH]] estimation.

- **Cell Balancing**: Accurate SoC is essential for [[cell-balancing|Cell Balancing]], where the BMS equalizes voltage differences among cells in a pack. Without precise SoC, balancing can waste energy or damage cells.

- **Patent Portfolio**: LG holds over 8,000 BMS-related patents, the largest such portfolio in the industry, reflecting deep investment in SoC and state estimation technologies.

By combining hardware (Qualcomm SoC) with proprietary software (BMTS), LG Energy Solution delivers SoC estimates that are faster, more accurate, and safer than conventional approaches, setting a new benchmark for battery intelligence.

## Related Pages

- [[battery-management-system|BMS (Battery Management System)]]
- [[bmts|BMTS (B.around Total Solution)]]
- [[cell-balancing|Cell Balancing]]
- [[sox|SoX (State of X)]]
- [[soh|SoH (State of Health)]]
- [[dod|DoD (Depth of Discharge)]]
- [[pack-process|Pack Process]]