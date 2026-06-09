---
title: CC/CV Charging (Constant Current/Constant Voltage Charging)
created: 2026-06-05
updated: 2026-06-08
type: glossary
tags: [fast-charging, safety, voltage]
sources:
  - raw/battery-inside-en/en/tech-en/battery-glossary-cc-cv-charging.md
  - raw/battery-inside-en/en/tech-en/questions-about-all-batteries-of-the-world-what-are-rapid-charging-and-standard-charging.md
  - raw/battery-inside-en/en/interview-en/better-life-i-conduct-the-performance-test-for-high-safety-and-charging-speed-of-ev-batt-7a89c4eabf.md
  - raw/battery-inside-en/en/tech-en/game-changer-battery-high-voltage-mid-nickel-batteries-securing-both-energy-density-and-ea70153231.md
  - raw/battery-inside-en/en/news-en/lg-energy-solution-to-pioneer-battery-safety-diagnostics-software-business-exploring-unl-a59e221a94.md
confidence: high
---
# CC/CV Charging (Constant Current/Constant Voltage Charging)

## Overview

CC/CV charging is the standard charging protocol for lithium-ion batteries, consisting of two sequential phases: a constant-current (CC) phase followed by a constant-voltage (CV) phase. This two-stage approach balances fast charging with electrochemical stability, preventing overvoltage while maximizing charge speed. The protocol is mandated in battery safety guidelines and is implemented by all commercial lithium-ion battery chargers and Battery Management Systems (BMS). Understanding CC/CV is essential for designing charging infrastructure, BMS algorithms, and cell designs optimized for [[fast-charging|Fast Charging]].

## Technical Details

During the **CC phase**, the charger delivers a constant current (specified in amperes, typically at a defined [[c-rate|C-rate]] such as 0.5C, 1C, or higher) to the battery. The battery voltage rises gradually as lithium ions deintercalate from the cathode and intercalate into the anode. The rate of voltage increase depends on the internal resistance and the state of charge (SoC). The CC phase continues until the battery voltage reaches the maximum specified voltage – typically 4.2 V for standard lithium-ion cells, or up to 4.4–4.5 V for high-voltage [[mid-nickel-battery|High-Voltage Mid-Nickel]] or high-nickel cells. At this voltage limit, the electrochemical potential window of the electrolyte is approached; exceeding it would trigger oxidative decomposition of the electrolyte at the cathode or reductive decomposition at the anode, leading to gas generation, swelling, and capacity fade.

At the voltage limit, the charger switches to the **CV phase**. The voltage is held constant at the maximum level (e.g., 4.2 V) while the current gradually decreases. This decay is necessary because as the battery approaches full charge, the rate of lithium-ion intercalation slows. Continuing to push high current would cause the voltage to exceed safe limits, potentially triggering lithium plating on the anode (especially at low temperatures or high rates) or accelerating electrolyte decomposition and uncontrolled SEI (Solid Electrolyte Interphase) growth. The current decay follows an exponential trend: initially high, it falls as concentration polarization and charge-transfer resistance increase. The CV phase continues until the current drops to a predefined cutoff value, typically C/20 or C/10 (e.g., 50 mA for a 1 Ah cell). At that point, charging is terminated.

The total charging time is the sum of the CC phase duration and the CV phase duration. **Fast charging technologies** aim to minimize both phases: the CC phase by increasing the maximum allowable current (e.g., from 1C to 3C or higher) and the CV phase by improving electrode kinetics and reducing internal resistance. However, at higher C-rates, the battery reaches the voltage limit sooner, so a greater proportion of total capacity is delivered during the CV phase. For example, a 1C charge may deliver ~80 % capacity in CC and 20 % in CV, while a 3C charge may deliver only 60 % in CC and 40 % in CV. Designs such as LG Energy Solution's [[46-series-battery|46‑Series Cylindrical Battery (4680/4695)]] are engineered to accept higher CC currents and to transition efficiently through the CV phase through optimized electrode architectures, advanced electrolytes, and improved thermal management.

Discharge typically uses a **CC-only protocol**, where a constant current is drawn until the voltage reaches the minimum specified cutoff (e.g., 2.5 V for standard Li‑ion cells). This avoids the need for a CV stage during discharge because the depletion of active material naturally limits the voltage.

## Significance & LG Energy Solution Context

The CC/CV protocol is fundamental to safe and efficient lithium-ion battery operation. It directly prevents overvoltage damage and minimizes parasitic side reactions that degrade [[coulombic-efficiency|Coulombic Efficiency]] and shorten cycle life. In practice, accurate CC/CV control relies on precise voltage and current sensing, often integrated into the [[battery-management-system|BMS (Battery Management System)]].

LG Energy Solution's BMS technology implements precise CC/CV control as part of its Battery Management Total Solution ([[bmts|BMTS, branded as B.around]]). The B.around platform uses cloud‑connected algorithms and machine learning to optimize CC/CV parameters in real time. For example, the system adapts the CC current limit based on temperature, SoC, and cell aging (SOH), and it dynamically adjusts the CV cutoff threshold to balance charge speed with longevity. LG's proprietary algorithms—such as FRISM (cell‑data‑free SOH model) and BLiS (battery life simulator)—allow the BMS to predict how different CC/CV profiles will affect future capacity retention.

In fast‑charging applications, LG Energy Solution's high‑nickel and mid‑nickel cells are designed with enhanced electrode structures (e.g., advanced [[anode-materials|Anode Materials]] like SiOx‑graphite composites) and safety‑reinforced separators ([[srs|SRS®]]) that withstand the higher thermal and mechanical stresses during the CC phase. The SRS® separator, coated with ceramic particles and polymer binder, maintains integrity up to 200 °C, allowing the charging protocol to operate safely at high currents without thermal runaway risk. By combining robust cell designs with intelligent BMTS control, LG Energy Solution delivers charging solutions that maximize speed while respecting the electrochemical boundaries defined by the [[potential-window|potential window]] of the electrolyte.

## Related Pages

- [[lithium-metal-battery|Lithium Metal Battery]]
- [[mid-nickel-battery|High-Voltage Mid-Nickel Battery]]
- [[46-series-battery|46-Series Cylindrical Battery (4680/4695)]]
- [[anode-materials|Anode Material]]
- [[battery-management-system|BMS (Battery Management System)]]
- [[bmts|BMTS (B.around Total Solution)]]
- [[srs|SRS (Safety Reinforced Separator)]]
- [[coulombic-efficiency|Coulombic Efficiency]]
- [[potential-window|Potential Window]]