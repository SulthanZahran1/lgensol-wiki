---
title: BMS (Battery Management System)
created: 2026-06-05
updated: 2026-06-08
type: concept
tags: [bms, cell-balancing, soc, soh, safety]
sources:
  - raw/battery-inside-en/en/tech-en/battery-glossary-bms-battery-management-system.md
  - raw/battery-inside-en/en/interview-en/lg-energy-solutions-bms-the-doctor-ensuring-battery-safety-and-efficiency.md
  - raw/battery-inside-en/en/news-en/lg-energy-solution-announces-availability-of-advanced-battery-management-system-solution-2bff100a25.md
  - raw/battery-inside-en/en/interview-en/incharge-jeong-hyeon-in-of-the-diagnostic-development-for-bms-safety-team-builds-data-ma-d492da0d25.md
  - raw/battery-inside-en/en/tech-en/battery-glossary-bmts-battery-management-total-solution.md
confidence: high
---
# BMS (Battery Management System)

## Overview

The Battery Management System (BMS) is the electronic brain of a lithium-ion battery pack. It continuously monitors voltage, current, and temperature at the cell and pack level, ensuring every cell operates within safe limits. Without a BMS, a multi-cell battery would quickly become unsafe: small manufacturing variations in capacity, internal resistance, and self-discharge accumulate over cycles, leading to overcharge, over-discharge, and thermal runaway. The BMS acts as a "choir conductor" — it harmonizes individual cell voltages and currents into a balanced, high-performing, and safe energy source. Modern BMS technology has evolved from simple protection circuits into sophisticated, cloud-connected platforms that predict degradation and detect early signs of failure.

## Technical Details

A BMS performs three core functions: monitoring, cell management, and control.

**Monitoring.** Sensors measure individual cell voltages (or small parallel groups), pack current via a shunt or Hall-effect sensor, and temperature at multiple locations. These measurements feed algorithms that estimate the battery's **State of Charge (SoC)** — how much energy remains — and **State of Health (SoH)** — how much capacity has been lost relative to the initial rating. SoC estimation typically uses Coulomb counting combined with open-circuit voltage lookup tables, corrected by Kalman filters to reduce drift. SoH is derived from capacity fade and impedance growth over time.

**Cell Management.** Even cells from the same production batch have slight differences. Over hundreds of cycles, voltage divergence increases, limiting usable capacity to the weakest cell. Cell balancing counteracts this drift. **Passive balancing** bleeds excess charge from higher-voltage cells through resistors as heat. **Active balancing** uses capacitors or inductors to transfer energy from higher- to lower-voltage cells, achieving greater efficiency and faster correction. LG Energy Solution implements balancing algorithms that balance only during specific SoC windows to minimize energy loss.

**Control.** The BMS prevents overcharge, over-discharge, and overcurrent by opening high-voltage contactors (disconnect relays) when thresholds are exceeded. It communicates via CAN bus with the vehicle's main controller to request power reduction or shutdown. Thermal management is also controlled: cooling fans, liquid coolant pumps, or heaters are activated to keep the battery in its optimal range of 15–35 °C. The BMS also manages pre-charge circuits to prevent inrush current when connecting the pack to the inverter.

**Advanced Safety Diagnostics.** LG Energy Solution has developed proprietary algorithms that go beyond basic voltage and temperature thresholds. Three key techniques are:
- **MAVD (Moving Average Voltage Deviation)** — tracks the deviation of each cell's voltage from its moving average over time; an abnormal rise signals internal short-circuit or lithium plating.
- **RdV (Relaxation Deviation Voltage)** — measures voltage recovery after charging stops; deviations from the expected relaxation curve indicate micro-shorts or separator damage.
- **dSOH (Delta State of Health)** — compares the rate of capacity fade between cells; a cell degrading faster than its neighbors may have a latent defect.

These diagnostics achieve over 90% detection accuracy for incipient faults, based on analysis of more than 130,000 cells and 1,000 modules of real-world data.

## Significance and LG Context

LG Energy Solution has been a pioneer in BMS development since 2005, holding over 8,000 BMS-related patents — the most in the industry. The company's BMS technology is grounded in extensive empirical data: analysis of over 130,000 individual cells and 1,000 battery modules from real-vehicle operation and laboratory testing. This data is used to train degradation models that achieve a degradation diagnostic error rate of just 1–2%, the industry's best.

A landmark partnership with Qualcomm Technologies launched in 2024 aims to deliver the industry's first SoC (System-on-Chip) based BMS. By running LG's advanced algorithms on Qualcomm's Snapdragon Digital Chassis platform, the new BMS gains more than 80× the computational power of conventional microcontrollers. This enables real-time execution of complex models — such as lithium-ion aging simulation, cathode/anode aging separation (via LG's LLAZER algorithm), and remaining useful life (RUL) prediction — entirely on the vehicle, without cloud connectivity.

The evolution of BMS toward a total solution is branded as **B.around (BMTS, Battery Management Total Solution)** . BMTS integrates hardware BMS with cloud services, AI-driven diagnostics, and SDV (Software-Defined Vehicle) platforms. Examples include:
- **B-Lifecare**, a consumer-facing service that monitors battery health via a connected device, providing driving/charging habit analysis, state-of-health scores, and weather-based efficiency tips.
- **FRISM (Cell Data Free SOH Model)** , which estimates SoH without needing full cell data.
- **BLiS (Battery Life Simulator)** , which predicts aging trajectories under different usage scenarios.

These capabilities extend battery life, enhance safety, and enable new business models like Battery-as-a-Service (BaaS), where the battery is leased and managed continuously by the supplier.

## Related Pages

- [[bmts|BMTS (B.around Total Solution)]]
- [[soc|SoC (State of Charge)]]
- [[soh|SoH (State of Health)]]
- [[cell-balancing|Cell Balancing]]
- [[battery-safety|Battery Safety and Thermal Runaway]]
- [[sox|SoX (State of X)]]
- [[battery-recycling|End-of-Life Battery Reuse and Recycling]]