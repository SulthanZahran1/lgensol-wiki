---
title: Fast Charging
created: 2026-06-05
updated: 2026-06-08
type: concept
tags: [fast-charging, power-density, cycle-life, ev]
sources:
  - raw/battery-inside-en/en/tech-en/questions-about-all-batteries-of-the-world-what-are-rapid-charging-and-standard-charging.md
  - raw/ko/tech/%ec%84%b8%ec%83%81%ec%9d%98-%eb%aa%a8%eb%93%a0-%eb%b0%b0%ed%84%b0%eb%a6%ac%ec%97%90-%eb%8c%80%ed%95%9c-%ea%b6%81%ea%b8%88%ec%a6%9d-%ec%a0%84%ea%b8%b0%ec%b0%a8%ec%9d%98-%ea%b8%89%ec%86%8d.md
  - raw/battery-inside-en/en/tech-en/battery-glossary-cc-cv-charging.md
  - raw/battery-inside-en/en/interview-en/better-life-i-conduct-the-performance-test-for-high-safety-and-charging-speed-of-ev-batt-7a89c4eabf.md
  - raw/battery-inside-en/en/culture-en/charging-moment-running-a-marathon-every-day-has-made-me-healthier-both-physically-and-m-7333ac631d.md
confidence: high
---
# Fast Charging

## Overview / Introduction

Fast charging is a critical enabler for electric vehicle (EV) adoption, addressing the “range anxiety” that arises from long refueling times. In practical terms, fast charging (DC) delivers power directly to the battery at 50 kW or more, enabling an 80% state-of-charge (SoC) in roughly one hour, while slow charging (AC) uses an onboard converter to supply 3–7 kW over 5–12 hours for a full 100% charge. The fundamental trade‑off is speed versus battery health: high currents accelerate degradation mechanisms such as lithium plating, SEI growth, and thermal stress. Modern EVs therefore rely on sophisticated charging protocols—most commonly Constant Current/Constant Voltage (CC/CV)—and a combination of material, electrode, and system‑level innovations to push charging rates higher without sacrificing cycle life.

## Technical Details

### Charging Protocol: CC/CV and the 80% Limit

Lithium‑ion cells are charged using a two‑stage CC/CV protocol. First, a constant current (CC) is applied while voltage rises; once the cell reaches its maximum voltage (e.g., 4.2 V), the charger switches to constant voltage (CV) mode, gradually reducing current until a cutoff threshold (typically C/20) is reached. This CV stage is essential to avoid overvoltage and to complete the filling of active sites. In practice, fast charging is usually limited to ~80% SoC because the CV phase becomes prohibitively long at high states of charge—lithium‑ion diffusion slows as the anode nears saturation, and forcing high current would raise the risk of plating lithium metal on the anode surface.

### Lithium Plating and Dendrite Formation

When the lithium de‑intercalation rate from the anode cannot keep pace with the incoming flux, metallic lithium deposits on the graphite or silicon surface—a phenomenon called “lithium plating.” Plated lithium is electrochemically inactive, causing irreversible capacity loss. Worse, it can grow dendritic structures that may pierce the separator and cause internal short‑circuits, a severe safety hazard. Fast charging exacerbates plating because high overpotentials drive lithium deposition before intercalation. Mitigation strategies include lowering the anode’s lithiation potential (e.g., by using silicon with a potential ~0.3–0.4 V vs. Li/Li⁺ instead of near‑0 V for graphite) and designing electrolyte systems that form stable, uniform solid‑electrolyte interphase (SEI) layers.

### Material‑Level Solutions

- **Anode materials:** Silicon offers a lithium diffusion coefficient up to two orders of magnitude higher than graphite and a more forgiving operating potential. However, its ~300% volume expansion during lithiation demands advanced binders, conductive additive networks (e.g., CNTs), and electrolyte formulations to maintain mechanical integrity.
- **Electrolyte additives:** Compounds such as fluoroethylene carbonate (FEC) and lithium bis(fluorosulfonyl)imide (LiFSI) improve SEI stability at high rates. For example, LG Energy Solution and KAIST recently developed a new liquid electrolyte that uses weakly coordinating anions to suppress dendrite formation even under extreme fast charging.
- **Electrode architecture:** Optimizing porosity and reducing tortuosity in the anode coating creates faster ion‑transport pathways, while conductive additives ensure a more uniform current distribution across the electrode thickness.

### System‑Level Innovations

- **Thermal management:** I²R heating during fast charging requires active liquid cooling to keep cell temperatures within safe limits (typically 15–45 °C). LG Energy Solution holds extensive patents in liquid‑cooled pack designs and BMS thermal control.
- **BMS algorithms:** Model‑based state estimation (e.g., extended Kalman filters) enables the BMS to track internal states like local lithium concentration and temperature gradients, dynamically adjusting current to avoid plating.
- **Advanced cell chemistries:** The LG‑KAIST Frontier Research Laboratory (FRL) demonstrated a lithium metal battery capable of 12‑minute fast charging, 800 km range per charge, and 300,000 km cumulative life. Their breakthrough relies on a new liquid electrolyte that minimizes interfacial heterogeneity, effectively preventing dendrite growth even under high current densities.

### Charging Infrastructure and the 80% Convention

Public DC fast chargers typically stop at 80% SoC to protect battery health. This practice reflects the steep increase in charging time beyond that point (due to the CV phase) and the elevated risk of lithium plating at high voltages and elevated temperatures. Future standards, such as the “Energy Superstation” concept (integrating solar, fuel cells, and fast chargers on existing gas‑station sites), aim to expand high‑power charging availability while managing grid load.

## Significance / LG Context

LG Energy Solution views fast charging as a central pillar of its EV battery strategy. The company’s market segmentation (Premium, Standard, Affordable) targets specific performance milestones by 2028: for example, premium packs of 150 kWh delivering over 750 km range, while standard packs (120 kWh) achieve over 720 km. Achieving these ranges with acceptable charging times requires continuous improvement in anode materials (silicon‑dominant anodes), electrolyte formulations (the KAIST‑LG liquid electrolyte), and system integration (Cell‑to‑Pack (CTP) technology that reduces module‑level weight and improves thermal propagation paths).

The LG‑KAIST FRL partnership exemplifies how industry‑academia collaboration accelerates breakthrough technologies. The 12‑minute lithium metal battery not only closes the charging‑time gap with gasoline refueling but also maintains high energy density—a combination previously considered impossible. By leveraging proprietary BMS algorithms and extensive thermal management patents, LG is well positioned to bring these advances to production vehicles.

## Related Pages

- [[cc-cv-charging|CC/CV Charging (Constant Current/Constant Voltage)]]
- [[silicon-anode|Silicon Anode Material]]
- [[lithium-metal-battery|Lithium Metal Battery]]
- [[battery-management-system|Battery Management System (BMS)]]
- [[internal-resistance|Internal Resistance]]
- Thermal Management System
- [[c-rate|C‑rate (Current / Charge‑Discharge Rate)]]