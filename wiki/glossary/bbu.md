---
title: BBU (Battery Backup Unit)
created: 2026-06-05
updated: 2026-06-08
type: glossary
tags: [ess, safety]
sources:
  - raw/ko/tech/%eb%b0%b0%ed%84%b0%eb%a6%ac-%ec%9a%a9%ec%96%b4%ec%82%ac%ec%a0%84-bbu-battery-backup-unit.md
  - raw/battery-inside-en/en/tech-en/what-makes-lg-energy-solutions-ess-batteries-different-as-tesla-ess-partner.md
  - raw/ko/tech/%ed%85%8c%ec%8a%ac%eb%9d%bc%ec%9d%98-ess-%ed%8c%8c%ed%8a%b8%eb%84%88-lg%ec%97%90%eb%84%88%ec%a7%80%ec%86%94%eb%a3%a8%ec%85%98%ec%9d%98-ess-%eb%b0%b0%ed%84%b0%eb%a6%ac%eb%8a%94-%eb%ac%b4%ec%97%87.md
  - raw/ko/tech/%ec%8b%a0%ec%9e%ac%ec%83%9d%ec%97%90%eb%84%88%ec%a7%80%ec%9d%98-%ed%95%b5%ec%8b%ac-%ec%84%b8%ea%b3%84%eb%8a%94-%ec%a7%80%ea%b8%88-ess%ec%97%90-%ec%a3%bc%eb%aa%a9%ed%95%9c%eb%8b%a4.md
  - raw/battery-inside-en/en/tech-en/questions-about-all-batteries-of-the-world-reasons-for-the-global-attention-on-ess.md
confidence: high
---
# BBU (Battery Backup Unit)

## Overview

A Battery Backup Unit (BBU) is a distributed, rack-level energy storage device designed to provide short-duration backup power to individual server racks or cabinets in data centers. Unlike traditional centralized [[ups|UPS (Uninterruptible Power Supply)]] systems, a BBU is mounted directly within or adjacent to the equipment it protects, enabling rapid response to power interruptions at the point of load. BBUs are becoming increasingly critical as AI and high-performance computing (HPC) drive rack power densities from historic 5–10 kW to 50–100 kW or more, where centralized backup systems can no longer guarantee voltage stability or response time within tens of milliseconds.

## Technical Details

### Layered Backup Hierarchy

Modern data centers employ a time-sequenced backup architecture to balance efficiency, cost, and reliability. The chain proceeds as follows:

1. **BBU** – Provides immediate short-term power (≈4 minutes) at the rack. Because it is DC-based and located at the load, it can respond in under 10 ms, covering the critical gap between a power sag and the activation of downstream systems.
2. **Facility UPS** – Takes over after the BBU’s window, supplying power for approximately 10–15 minutes to the entire facility using centralized AC→DC→AC conversion.
3. **Diesel or gas generators** – Start within minutes and sustain long-term power until grid restoration, typically hours.

This layered approach minimizes energy losses: the BBU’s DC‑DC conversion avoids the double-conversion losses (AC→DC→AC) inherent in UPS systems. In high-density racks, the efficiency gain can be as much as 5–8 percentage points at the point of load, reducing total cooling demand.

### BBU vs. UPS: Key Differences

| Feature | BBU | UPS |
|---------|-----|-----|
| **Deployment** | Distributed, inside or next to server rack | Centralized, in a dedicated room |
| **Electrical conversion** | DC‑based (DC‑DC) – single conversion | AC→DC→AC double conversion |
| **Typical backup time** | ~4 minutes | ~10–15 minutes |
| **Scope of protection** | Local (rack/cabinet) | Facility‑wide |
| **Response time** | <10 ms (near-instantaneous) | 10–20 ms (switchover time) |
| **Energy loss** | ~5–8% (DC‑DC) | ~15–20% (double conversion) |

### Battery Performance Requirements

BBU batteries must satisfy four demanding requirements, each directly tied to the operational environment of an AI data center:

1. **High power density** – The ability to deliver large currents (tens of kW) within seconds to prevent server crashes during a power sag or blackout. High-power cylindrical cells (e.g., 21700 form factor) are often favored for their low internal resistance and high rate capability.
2. **High energy density** – The battery must fit within the limited volume of a server rack (typically 1–2 U tall, 19-inch wide). This drives adoption of lithium‑ion chemistries that balance volumetric energy density (Wh/L) with power capability.
3. **High efficiency** – Minimal energy loss during charge/discharge cycles is critical, as data centers operate with rapidly fluctuating demand. DC‑DC converters in BBUs can achieve >95% efficiency under rated loads.
4. **Safety** – The battery operates in close proximity to sensitive electronics. Thermal stability is paramount: during high-power discharge, internal heating can exceed 10 °C per minute if not managed. Advanced [[battery-safety|safety]] features such as ceramic-coated separators, passive propagation resistance (PPR), and active cooling (liquid or forced air) are standard.

## LG Energy Solution Context

### InterBattery 2026 Launch

At InterBattery 2026, LG Energy Solution introduced its first domestic BBU solution specifically designed for AI data centers. The system integrates high-power cylindrical cells into a rack-mounted BBU module, alongside a companion [[lfp-battery|LFP (Lithium Iron Phosphate)]]–based UPS rack system. LG’s BBU leverages three core competencies:

- **High‑power cell design** – Cylindrical cells optimized for >10 C rate discharge, with a proprietary electrolyte formulation that maintains low impedance at high currents.
- **Precise thermal management** – A patented liquid cooling plate that interfaces directly with the cell stack, maintaining cell temperatures below 45 °C even during repeated high‑power discharges.
- **Advanced [[battery-management-system|BMS]] algorithms** – Real‑time state‑of‑charge (SoC) and state‑of‑health (SoH) estimation using dual‑Kalman filtering, ensuring accurate capacity prediction over the BBU’s lifespan (typically 5–7 years in data center cycling).

### Strategic Positioning

LG Energy Solution’s BBU is part of a broader strategy to expand beyond automotive and traditional ESS into emerging infrastructure markets—including UAM (Urban Air Mobility) and AI data centers. By offering both LFP UPS systems (for longer‑duration facility backup) and high‑power BBUs (for immediate rack‑level protection), LG enables data center operators to build a multi‑layer backup architecture that is both efficient and scalable. The company’s North American production footprint (five plants, including Michigan and Tennessee) allows it to supply BBU modules at scale, leveraging 60 GWh of ESS‑dedicated capacity planned by 2026.

### Competitive Edge

Compared to incumbent solutions (often using lead‑acid or supercapacitors for short‑duration backup), LG’s lithium‑ion BBU offers:
- **Higher energy density** (up to 3× that of lead‑acid in the same footprint)
- **Longer cycle life** (>5,000 cycles at 100% DoD for the high‑power cell)
- **Faster recharge** (capable of full recharge within 30 minutes)

These attributes make LG’s BBU particularly suited for the dynamic power profiles of AI training clusters, where load spikes can exceed 100 kW per rack and backup demands shift from seconds to minutes.

## Related Pages

- [[ups|UPS (Uninterruptible Power Supply)]]
- [[lfp-battery|LFP (Lithium Iron Phosphate) Battery]]
- [[battery-management-system|BMS (Battery Management System)]]
- [[battery-safety|Battery Safety and Thermal Runaway]]
- [[avel|AVEL (Energy Aggregation)]]