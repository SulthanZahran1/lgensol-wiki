---
title: Dendrite
created: 2026-06-05
updated: 2026-06-08
type: glossary
tags: [anode, safety, cycle-life, lithium-metal]
sources:
  - raw/battery-inside-en/en/tech-en/the-next-generation-anode-material-silicon.md
  - raw/battery-inside-en/en/tech-en/infographics-18-types-of-anode-materials.md
  - raw/battery-inside-en/en/tech-en/infographics-12-anode.md
  - raw/battery-inside-en/en/tech-en/infographics20-silicon-anode-materials.md
  - raw/battery-inside-en/en/interview-en/a-battery-without-an-anode-lg-energy-solutions-research-on-combining-anodeless-and-solid-ae5b6bf6d7.md
confidence: high
---
# Dendrite

## Overview

A dendrite (from the Greek *dendron*, meaning "tree") is a needle-like or tree‑shaped crystalline structure of metallic lithium that can grow on the anode surface during uneven lithium plating in lithium‑ion and lithium‑metal batteries. In the battery industry, dendrite formation is recognized as one of the most critical barriers to both safety and long cycle life. For next‑generation technologies such as [[lithium-metal-battery|lithium‑metal batteries]] and [[anodeless-battery|anodeless batteries]], controlling dendrites is the primary obstacle to commercialization.

## Technical Details

### Formation Mechanism

During charging, lithium ions (Li⁺) are reduced to lithium metal at the anode surface. Under ideal conditions, lithium plates uniformly across the anode as a smooth, dense layer. However, several factors can cause lithium to deposit preferentially at specific nucleation sites, forming sharp, branching structures that grow outward from the anode.

The process begins when the local current density exceeds the diffusion‑limited current density of Li⁺ in the electrolyte. This creates a concentration gradient that drives uneven deposition. Once a small protrusion forms, the electric field concentrates at its tip, attracting more Li⁺ and accelerating growth—a positive feedback loop. Dendrites typically propagate at rates from micrometers per minute under mild conditions to millimeters per minute during aggressive charging.

### Accelerating Conditions

- **High charge rates (C‑rates):** Fast charging pushes Li⁺ to the anode faster than they can be intercalated into graphite or plated uniformly. At rates above ~1–2 C for graphite anodes, the anode potential may drop below 0 V vs. Li/Li⁺, triggering lithium metal plating.
- **Low temperatures:** Reduced Li⁺ diffusivity in the electrolyte and anode causes surface accumulation. At sub‑zero temperatures, even moderate charge rates can induce dendrite growth.
- **High state of charge (SoC) and overcharging:** Approaching 100% SoC or exceeding the upper voltage limit pushes the anode toward the lithium plating potential.
- **Surface inhomogeneities:** Scratches, impurities, or uneven [[sei|SEI (Solid Electrolyte Interphase)]] layers create preferential nucleation sites.
- **Electrolyte instability:** When the cell voltage exceeds the electrolyte’s [[potential-window|potential window]] (typically ~4.2–4.3 V for conventional carbonate electrolytes), decomposition products can disrupt the SEI and promote dendrite initiation.

### Effects on Battery Performance and Safety

1. **Capacity loss and reduced Coulombic efficiency:** Each dendrite consumes active lithium that is permanently trapped as “dead lithium” (electrically isolated from the anode). This lowers the cell’s reversible capacity and [[coulombic-efficiency|Coulombic Efficiency (CE)]].

2. **Increased internal resistance:** The growing dendrite surface area promotes continuous electrolyte reduction and SEI growth, thickening the passivation layer and raising [[internal-resistance|Internal Resistance]]. This further degrades power capability and accelerates aging.

3. **Internal short circuit and thermal runaway:** The most dangerous consequence occurs when dendrites pierce the [[separator|separator]]—the thin (typically 10–25 µm) porous membrane that physically isolates the anode and cathode. A single dendrite bridge can create a direct electronic connection between electrodes, causing a localized short circuit. The resulting Joule heating can exceed 1000 °C, triggering [[tp-prevention|thermal runaway]] and catastrophic failure (fire or explosion).

### Detection and Analysis

Dendrite initiation can be detected in‑situ through:
- **Voltage relaxation analysis:** A slight drop in open‑circuit voltage after charging indicates microscale shorting.
- **Internal resistance monitoring:** A sudden decrease in resistance between charge cycles suggests dendrite penetration.
- **Thickness swelling:** Dendrite growth pushes the electrode stack, causing measurable cell expansion (swelling) that can be monitored by BMS sensors.
- **dQ/dV analysis:** Abnormal features in the differential capacity curve reveal lithium plating and stripping events.

## Significance and LG Energy Solution Context

### Industry‑wide Challenge

Dendrite control is the linchpin for next‑generation high‑energy‑density batteries. Lithium‑metal anodes offer a tenfold increase in theoretical specific capacity (3860 mAh/g) compared to graphite (372 mAh/g), but they inherently plate and strip lithium metal every cycle, making them highly susceptible to dendrites. Similarly, [[anodeless-battery|anodeless batteries]] (which use no excess lithium) must achieve near‑perfect plating uniformity to avoid rapid failure.

### LG Energy Solution’s Approach

LG Energy Solution has developed a multi‑faceted strategy to suppress dendrites:

1. **SRS® (Safety Reinforced Separator):** LG’s patented SRS technology coats the separator surface with ceramic particles (e.g., Al₂O₃) and a polymer binder. This coating provides mechanical reinforcement that resists dendrite penetration even at 200 °C—far above the 100 °C limit of conventional polyolefin separators. In the “Stack & Folding” assembly process, SRS film is layered between [[bi-cell|Bi‑Cell]] units, creating a dual‑barrier safety system.

2. **Advanced Electrolyte Formulations:** LG’s [[gas-free-solvent|Gas Free Solvent]] technology and optimized additive packages (e.g., FEC, LiBOB) promote the formation of a stable, thin SEI that minimizes current hot spots and nucleation sites. By widening the electrolyte’s potential window, LG can operate cells at higher voltages while suppressing decomposition reactions that seed dendrites.

3. **Anodeless Battery Innovations:** For its anodeless development program, LG applies lithium‑philic coating materials (such as carbon‑based or metal‑oxide layers) to the current collector and performs oxidation treatments that ensure uniform lithium nucleation and dense plating.

4. **Intelligent BMS:** LG’s Battery Management System incorporates real‑time algorithms that detect early signs of lithium plating—such as anomalous voltage relaxation or impedance changes—and dynamically adjust charge current or temperature to prevent dendrite propagation. This predictive control is part of the broader [[sox|SoX (State of X)]] framework, where SoS (State of Safety) is actively monitored.

## Related Pages

- [[lithium-metal-battery|Lithium Metal Battery]]
- [[anodeless-battery|Anodeless Battery]]
- [[anode-materials|Anode Material]]
- [[srs|SRS (Safety Reinforced Separator)]]
- [[separator|Separator]]
- [[sei|SEI (Solid Electrolyte Interphase)]]
- [[coulombic-efficiency|Coulombic Efficiency]]
- [[internal-resistance|Internal Resistance]]
- [[tp-prevention|Thermal Runaway Prevention]]
- [[potential-window|Potential Window]]
- [[bi-cell|Bi‑Cell]]
- [[sox|SoX (State of X)]]