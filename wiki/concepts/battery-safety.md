---
title: Battery Safety and Thermal Runaway
created: 2026-06-05
updated: 2026-06-08
type: concept
tags: [safety, thermal-stability, separator, srs]
sources:
  - raw/battery-inside-en/en/tech-en/infographics-15-lg-energy-solution-suggests-12-battery-safety-tips.md
  - raw/corporate/en/documents/4420-global-human-rights-labor-policy.md
  - raw/corporate/en/documents/4419-global-environmental-policy.md
  - raw/corporate/en/documents/4423-code-of-conduct-for-suppliers.md
  - raw/battery-inside-en/en/interview-en/lg-energy-solutions-bms-the-doctor-ensuring-battery-safety-and-efficiency.md
confidence: high
---
# Battery Safety and Thermal Runaway

## Overview

Battery safety is the integrated control of electrochemistry, materials, cell design, manufacturing quality, battery management system (BMS) logic, and pack-level protection. The most critical failure mode in lithium-ion batteries is **thermal runaway** — a self-accelerating exothermic chain reaction that can lead to fire or explosion. Triggers include mechanical abuse (puncture, crush), electrical abuse (overcharge, external short), thermal abuse (overheating), and internal defects such as metallic contamination or separator failure. Understanding the mechanisms and prevention strategies is essential for safe deployment across electric vehicles (EVs), energy storage systems (ESS), and consumer electronics.

## Technical Details

### Thermal Runaway Mechanism

Thermal runaway progresses through distinct temperature regimes:

- **80–120 °C:** The anode solid-electrolyte interphase (SEI) begins to decompose exothermically, exposing fresh lithium to the electrolyte and generating additional heat.
- **130–180 °C:** The separator shrinks or melts, potentially causing large-area internal short circuits. For conventional polyolefin separators, degradation is severe above 100 °C.
- **>180 °C:** Cathode materials (especially NCM) release oxygen via decomposition, which reacts with the flammable electrolyte. This further accelerates heat generation and can lead to cell rupture and propagation to adjacent cells — a phenomenon known as thermal propagation (TP).

### Safety Engineering at Multiple Levels

Safety is engineered at the material, cell, and pack levels:

- **Separator Technology:** LG Energy Solution’s **Safety Reinforced Separator (SRS®)**, developed in 2004, coats ceramic particles and a polymer binder onto the separator surface. This allows the separator to maintain mechanical integrity up to 200 °C, compared to conventional separators that degrade above 100 °C. SRS enables safe operation in high-energy-density nickel-rich cells.
- **Electrolyte Additives:** Additives such as flame retardants and SEI‑forming compounds suppress gas generation and improve thermal stability.
- **Cathode Chemistry:** Lithium iron phosphate (LFP) is inherently more thermally stable than NCM due to its olivine structure, which resists oxygen release at high temperatures.
- **BMS Diagnostics:** Advanced monitoring includes voltage, current, and temperature tracking, as well as **electrochemical impedance spectroscopy (EIS)** to detect internal resistance changes. LG’s BMS also incorporates **lithium plating detection** using pulse signals and EIS, identifying a key precursor to thermal runaway.
- **TP Prevention:** At the pack level, barriers such as ceramic pads, phase-change materials (PCMs), and venting channels are used to isolate heat and gases. Cell clustering physically separates modules to stop flame propagation.

## Significance / LG Context

### LG Energy Solution’s Safety Portfolio

LG Energy Solution’s comprehensive safety approach spans:

- **SRS® Separator:** Already deployed in mass production and proven in nail penetration and overcharge tests. The ceramic coating also improves mechanical strength and prevents internal shorts.
- **Thermal Propagation (TP) Prevention:** LG has developed multi-layer defense: first, early detection via gas and pressure sensors and EIS‑based diagnostics; second, structural barriers and venting to contain any single‑cell event. TP prevention is a key requirement for EV and ESS regulations.
- **ESS Fire Safety Standards:** In January 2026, LG Energy Solution signed an MOU with the Korea Electrical Safety Corporation to jointly strengthen ESS safety management, including new inspection protocols for LFP‑based ESS sites. Given that over 90% of global ESS installations use LFP, this partnership aims to establish dedicated safety standards that reflect LFP’s lower risk profile.
- **Environmental & Occupational Safety:** LG’s Environmental Health & Safety management system is certified under ISO 14001 and ISO 45001 across six production sites in Korea, China, Poland, and the US. The company operates a dedicated **Safety Reinforcement Division** that conducts regular drills, monitors near‑miss events, and integrates safety performance into employee evaluations.

### Future Directions

LG is advancing **smart diagnostics** that combine real-time impedance spectroscopy with machine learning to predict thermal runaway precursors. For ESS, LFP‑specific safety management protocols are being codified through the partnership with the Korea Electrical Safety Corporation. At the cell level, ongoing development of **self‑extinguishing electrolytes** and **reinforced SRS** variants aims to further reduce thermal runaway risk while maintaining high energy density.

## Related Pages

- [[separator|Separator]]
- [[srs|SRS (Safety Reinforced Separator)]]
- [[tp-prevention|TP Prevention Technology (Thermal Propagation Prevention)]]
- [[battery-management-system|BMS (Battery Management System)]]
- [[cell-balancing|Cell Balancing]]
- [[gas-free-solvent|Gas Free Solvent]]
- [[electrolyte-additive|Electrolyte Additive]]