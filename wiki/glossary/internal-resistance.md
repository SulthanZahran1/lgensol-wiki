---
title: Internal Resistance
created: 2026-06-05
updated: 2026-06-08
type: glossary
tags: [power-density, soh, cycle-life]
sources:
  - raw/battery-inside-en/en/tech-en/battery-glossary-soh.md
  - raw/ko/tech/%eb%b0%b0%ed%84%b0%eb%a6%ac-%ec%9a%a9%ec%96%b4%ec%82%ac%ec%a0%84-soh-state-of-health.md
  - raw/ko/tech/%eb%b0%b0%ed%84%b0%eb%a6%ac-%ec%9a%a9%ec%96%b4%ec%82%ac%ec%a0%84-%eb%82%b4%eb%b6%80%ec%a0%80%ed%95%ad.md
  - raw/battery-inside-en/en/tech-en/battery-glossary-sox-state-of-x.md
  - raw/ko/tech/%eb%b0%b0%ed%84%b0%eb%a6%ac-%ec%9a%a9%ec%96%b4%ec%82%ac%ec%a0%84-soxstate-of-x.md
confidence: high
---
# Internal Resistance

## Overview

Internal resistance (IR) is the total opposition to current flow within a battery cell, comprising both **electronic resistance** (through active materials, current collectors, tabs, and inter-cell connections) and **ionic resistance** (through the electrolyte, porous electrode structure, and the solid-electrolyte interphase, or SEI). It is a fundamental parameter that determines a battery’s power capability, energy efficiency, thermal behavior, and aging trajectory. As batteries cycle, internal resistance gradually increases due to chemical and mechanical degradation, directly impacting [[soh|State of Health (SoH)]] and usable life.

## Technical Details

Internal resistance is not a single lumped resistor but the sum of distributed resistive contributions across the cell. Electronic resistance originates from particle-to-particle contacts within electrodes, the resistivity of active material and conductive additives, and the ohmic losses in current collectors and welds. Ionic resistance arises from the electrolyte’s limited ionic conductivity (typically 1–10 mS/cm for Li-ion electrolytes), tortuosity of the porous electrode structure, and the resistance of the SEI layer—a passivation film that grows over time on the anode.

Two primary measurement methods are used: **DC-IR** and **AC-IR**. DC-IR applies a direct current pulse (typically 10–30 seconds at a defined C-rate) and measures the resulting voltage drop. This method captures the total resistance under realistic load conditions and is sensitive to both ohmic and polarization contributions. AC-IR applies a small-amplitude alternating current at a fixed frequency (1 kHz is standard) and measures the impedance magnitude. AC-IR is fast and non-intrusive, making it suitable for production quality control, but it predominantly reflects ohmic (electronic) resistance at high frequency, missing slower polarization effects.

As the battery ages, internal resistance increases through several mechanisms:
- **SEI growth** on the anode thickens the ion barrier, raising ionic resistance.
- **Electrolyte decomposition** reduces ionic conductivity and wets the separator less effectively.
- **Active material particle cracking** and loss of electrical contact increase electronic resistance.
- **Current collector corrosion** and tab degradation add contact resistance.

The rate of increase is strongly influenced by temperature (optimal 15–35 °C), charge/discharge C-rate (0.5–1 C minimizes acceleration), and state-of-charge (SoC) operating window (avoiding prolonged high SoC and deep cycles). Proper [[battery-management-system|BMS]] strategies, including cell balancing, can mitigate IR growth by preventing overcharge and overdischarge of individual cells.

## Significance and LG Context

Internal resistance directly governs several performance metrics:
- **Power capability** – Higher IR causes a larger voltage drop (V = I × R) under load, reducing available peak power. At 20% IR increase, output power declines nearly proportionally.
- **Energy efficiency** – Resistive losses (I²R) convert electrical energy to waste heat. A 50% IR rise reduces round-trip efficiency (RTE) by roughly 2–6% under typical cycling.
- **Thermal management** – Increased heat generation accelerates degradation and can push cells into unsafe temperature regimes.
- **Usable capacity** – Under load, the voltage cutoff is reached earlier, effectively reducing accessible capacity—especially pronounced in Li-ion systems.

The EU Battery Regulation mandates manufacturers to disclose both initial internal resistance and its increase rate, reflecting IR’s role as a key health indicator. In LG Energy Solution’s ecosystem, internal resistance is tracked continuously and used as a core input for SoH estimation. The company’s [[bmts|BMTS (B.around Total Solution)]] platform integrates IR data with voltage, current, and temperature signals to deliver real-time diagnostics and predictive algorithms such as FRISM (cell-data-free SoH model) and LLAZER (loss analysis of active material and lithium inventory). IR is also a primary parameter in the **B·once** service, which offers two tiers of evaluation:
- **QuickScan** – Uses OBD-II data and a 2–5 minute drive cycle to estimate SoH via IR and capacity trends, leveraging a database of over 30,000 EVs.
- **PowerScan** – Performs a 30–50 minute charging session (50% to 100% SoC) to compute IR and capacity with higher precision, suitable for insurance certification.

LG’s electrode and cell design innovations—such as DLD (Double Layer Slot Die Coating) coating technology—aim to minimize initial IR and retard its growth, thereby extending cycle life and maintaining high power density.

## Related Pages

- [[fast-charging|Fast Charging]]
- [[soh|SoH (State of Health)]]
- [[anode-materials|Anode Material]]
- [[battery-management-system|BMS (Battery Management System)]]
- [[battery-recycling|End-of-Life Battery Reuse and Recycling]]
- [[bmts|BMTS (B.around Total Solution)]]
- [[soc|SoC (State of Charge)]]
- [[sox|SoX (State of X)]]