---
title: UPS (Uninterruptible Power Supply)
created: 2026-06-05
updated: 2026-06-08
type: glossary
tags: [ess, safety]
sources:
  - raw/battery-inside-en/en/tech-en/what-makes-lg-energy-solutions-ess-batteries-different-as-tesla-ess-partner.md
  - raw/battery-inside-en/en/tech-en/the-core-of-renewable-energy-the-entire-world-is-starting-to-take-notice-of-ess.md
  - raw/battery-inside-en/en/news-en/lg-energy-solution-secures-grid-scale-ess-supply-agreement-in-europe-with-polands-pge.md
  - raw/battery-inside-en/en/news-en/freudenberg-e-power-systems-and-lg-energy-solution-sign-long-term-supply-partnership-for-4dcd0b459c.md
  - raw/battery-inside-en/en/interview-en/what-codes-and-standards-are-applied-to-ess-in-lg-energy-solution-currently-leading-the-bess-market.md
confidence: high
---
# UPS (Uninterruptible Power Supply)

## Overview
An Uninterruptible Power Supply (UPS) is a critical backup power system that provides instantaneous electrical power when the primary grid source fails. Unlike standby generators that may take seconds to minutes to start, a UPS delivers power within milliseconds—fast enough that connected equipment experiences no interruption. This bridging capability protects data centers, semiconductor fabs, hospitals, telecommunications infrastructure, and any facility where even a momentary outage can cause data loss, process stoppage, or equipment damage. UPS systems are a fundamental component of modern energy resilience, often deployed alongside [[energy-storage-system|Energy Storage Systems (ESS)]] to ensure continuous operation.

## Technical Details
A UPS continuously monitors incoming AC power. When it detects an interruption, voltage sag, or frequency deviation, its internal circuitry switches to battery power in under 4–10 milliseconds—well within the hold-up time of most sensitive electronics. The stored DC energy from the battery is inverted back to regulated AC power for the load.

### Traditional Lead-Acid UPS
For decades, lead-acid batteries were the standard for UPS applications. Their key drawbacks include:
- **Limited service life:** Replacement required every 5–7 years.
- **Low energy density:** Approximately 30–50 Wh/kg, requiring large physical footprints.
- **Hazardous materials:** Sulfuric acid and lead pose environmental and safety risks.
- **Poor cycle life:** Typically 200–500 cycles at deep discharge.
- **Slow charging:** Full recharge can take 8–12 hours.
Diesel generators are often paired with lead-acid UPS for extended runtime, but generators produce emissions, require regular maintenance, and have startup delays.

### Lithium-Ion UPS Advantages
Lithium-ion batteries are rapidly replacing lead-acid in UPS systems due to several quantifiable benefits:
- **Longer service life:** 15+ years versus 5–7 years, reducing total cost of ownership.
- **Higher energy density:** 2–3 times greater (100–265 Wh/kg), enabling smaller footprints—critical for space-constrained data centers.
- **Higher power output:** Up to 3 times the power density of lead-acid, supporting more equipment per unit volume.
- **Faster charging:** Full recharge in 1–3 hours, improving readiness for back-to-back outages.
- **Integrated BMS (Battery Management System):** The BMS provides real-time monitoring of voltage, current, temperature, and state of charge. It enables remote health checks, predictive maintenance alerts, and automated cell balancing—eliminating the need for manual inspections. This intelligent management directly enhances reliability and safety.
- **Cycle life:** Lithium iron phosphate (LFP) cells can achieve 5,000–15,000 cycles, compared to lead-acid’s few hundred, making them ideal for frequent charge-discharge scenarios.

### UPS Power Topologies
While not the focus of this article, UPS systems commonly use one of three topologies: standby, line-interactive, or online double-conversion. Modern lithium-ion UPS often employs the online topology, where the inverter continuously powers the load, ensuring zero transfer time and pure sine wave output.

## Significance and LG Context
The transition to lithium-ion UPS is accelerating globally, driven by rising power densities in data centers (especially with AI and high-performance computing), stricter carbon regulations, and the need for lower operational costs. Lithium-ion UPS also enables new business models such as [[eaas|EaaS (Energy as a Service)]], where backup assets can participate in grid frequency regulation or peak shaving during non-emergency periods.

### LG Energy Solution UPS Products
LG Energy Solution develops dedicated UPS battery solutions optimized for backup power applications. Key features include:
- **High energy density and high power output:** LG’s cells are designed to deliver maximum backup capacity within minimal space, using advanced [[lfp-battery|LFP (Lithium Iron Phosphate)]] chemistry for thermal stability and long life.
- **Integrated Switching Mode Power Supply (SMPS):** LG’s UPS battery systems incorporate an SMPS for autonomous operation without requiring external power, improving reliability and installation flexibility.
- **Transportable rack solution:** LG’s modular racks allow easy movement and installation of battery cells, simplifying maintenance and system expansion. This design reduces installation time and labor costs.
- **Comprehensive BMS integration:** LG’s BMS supports real-time state tracking, automated health checks, and predictive alerts, enabling proactive maintenance without manual intervention.
- **LFP and NCM options:** For safety-critical environments, LFP cells provide superior thermal stability, while NCM cells offer higher energy density for applications with tighter space constraints.

LG’s UPS solutions are part of a broader portfolio that includes [[bbu|BBU (Battery Backup Unit)]] for edge data centers and high-power cylindrical cells for rapid response backup. The company’s expertise in cell design, lamination and stacking processes, and [[azs-stacking|AZS (Advanced Z-Stacking)]] ensures consistent quality and performance across all UPS battery offerings.

## Related Pages
- [[bbu|BBU (Battery Backup Unit)]]
- [[lfp-battery|LFP (Lithium Iron Phosphate) Battery]]
- [[energy-storage-system|ESS (Energy Storage System)]]
- [[battery-management-system|BMS (Battery Management System)]]
- [[battery-safety|Battery Safety and Thermal Runaway]]
- [[eaas|EaaS (Energy as a Service)]]