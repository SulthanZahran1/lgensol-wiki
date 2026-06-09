---
title: Binder
created: 2026-06-05
updated: 2026-06-08
type: concept
tags: [binder, electrode, active-material]
sources:
  - raw/battery-inside-en/en/tech-en/a-better-life-with-batteries-binder.md
  - raw/ko/tech/binder-help-increase-battery-performance.md
  - raw/battery-inside-en/en/tech-en/infographics-16-wet-electrode-process-dry-electrode-process.md
  - raw/battery-inside-en/en/tech-en/infographics-22-slurry-components-and-their-roles-active-material-conductive-additive-and-binder.md
  - raw/battery-inside-en/en/tech-en/battery-glossary-binder.md
confidence: high
---
# Binder

## Overview / Introduction

In lithium‑ion battery electrodes, the binder is a polymeric adhesive that binds active‑material particles and conductive additives together, and anchors the entire coating to the current collector. Although it typically comprises only 1–5 wt% of the dried electrode, the binder is critical for maintaining mechanical integrity over thousands of charge‑discharge cycles, under wide temperature extremes, and in continuous contact with liquid electrolyte. Without a properly formulated binder, active‑material particles would detach, the conductive network would collapse, and the electrode would suffer rapid capacity fade and increased internal resistance. As next‑generation active materials—such as silicon with up to 300 % volume expansion—push the limits of electrode stability, the binder’s role has evolved from a simple glue to a multifunctional component that also influences ion transport, interfacial stability, and manufacturing efficiency.

## Technical Details

### Key Requirements for High‑Performance Binders

A high‑performance binder must simultaneously satisfy several demanding criteria:

- **Adhesion and mechanical strength:** The binder must firmly fix active‑material and conductive‑additive particles to each other and to the current collector. Sufficient peel strength and cohesive strength prevent delamination during calendering and cycling.
- **Elasticity:** Especially for silicon anodes, the binder must accommodate severe volume changes without cracking. Elastic polymers such as polyacrylic acid (PAA) can relieve stress through deformation, extending cycle life.
- **Chemical stability:** The binder is in direct contact with the electrolyte and must withstand oxidative decomposition at the cathode (>4.5 V vs. Li/Li⁺) and reductive decomposition at the anode (<0.2 V). Any side reactions generate gases, increase impedance, and accelerate capacity loss.
- **Ionic conductivity:** While binders are typically electrical insulators, some—like PVDF—swell in electrolyte up to 30 % by volume, creating ion‑conductive pathways. A binder that impedes ion transport would increase concentration polarization and reduce rate capability.
- **Thermal stability:** Electrodes must withstand temperatures from –20 °C to 60 °C (or higher during fast charging) without softening or decomposing. PVDF remains stable up to approximately 400 °C.

### Non‑Aqueous vs. Aqueous Binders

Binders are classified by the solvent in which they are dissolved.

**Non‑aqueous (organic) binders** use NMP (N‑methyl‑2‑pyrrolidone) as solvent. They are employed primarily for cathodes because cathode active materials (e.g., NCM, NCA) do not disperse well in water. The dominant non‑aqueous binder is **PVDF (polyvinylidene fluoride)**, a linear semi‑crystalline fluoropolymer. PVDF offers excellent adhesion, good dispersion of conductive additive, and electrochemical stability up to about 5 V vs. Li/Li⁺. Its strong C–F bond provides thermal stability to 400 °C, and its swelling in electrolyte enhances ionic conductivity. However, NMP is toxic and costly, requiring energy‑intensive recovery.

Another important non‑aqueous binder is **PTFE (polytetrafluoroethylene)**. PTFE is a fully fluorinated polymer with even higher thermal and chemical resistance. Its key feature is **fibrillation**: under shear during dry mixing, PTFE particles elongate into microfibers that form a continuous binding network without solvent. This makes PTFE the binder of choice for the **dry electrode process**, which eliminates solvent and drying steps, reducing manufacturing cost and environmental footprint.

**Aqueous binders** use water as solvent and are widely used for anodes because graphite and silicon anode materials are naturally compatible with water. The most common combination is **CMC (carboxymethyl cellulose)** and **SBR (styrene‑butadiene rubber)**. CMC provides viscosity and structural stability for slurry dispersion, while SBR adds adhesion and flexibility. Aqueous binders form a “point‑contact” structure (binders mainly at particle‑particle junctions) rather than the “line‑contact” structure of PVDF, which can allow higher active‑material loading. For high‑volume‑change silicon anodes, advanced aqueous binders such as PAA, polyacrylamide (PAM), and polyacrylonitrile (PAN) are being developed, offering tunable elasticity and hydrogen bonding to silicon surfaces.

### Binder Migration and Manufacturing Implications

A critical manufacturing issue is **binder migration** during wet electrode coating and drying. In thick electrodes (used for high energy density), the solvent (NMP or water) evaporates from the surface, drawing the binder toward the top surface via capillary forces. This creates a binder‑poor region near the current collector, degrading adhesion and increasing contact resistance. Binder migration is a major motivation for the dry electrode process, where no solvent is involved and binder distribution remains uniform.

In slurry preparation, binder is first dissolved in the solvent, then combined with pre‑dispersed conductive additive and active material. The order of addition and mixing intensity significantly affect final binder distribution and electrode performance.

## Significance / LG Context

At LG Energy Solution, binder technology is recognized as an enabler for high‑energy‑density cells. As the company advances toward next‑generation chemistries—such as high‑nickel cathodes (NCMA) and silicon‑anode composites—binder selection directly impacts cycle life, rate capability, and manufacturing scalability. LG Energy Solution has invested in aqueous binder systems to reduce reliance on NMP, aligning with sustainability goals. The dry electrode process, leveraging PTFE fibrillation, is being explored to lower cost and energy consumption while enabling thicker electrodes for improved energy density. Understanding binder properties is essential for engineers involved in electrode formulation, process development, and quality control.

## Related Pages

- [[active-material|Active Material]]
- [[conductive-additive|Conductive Additive (CNT)]]
- [[current-collector|Current Collector]]
- [[dry-electrode-process|Dry Electrode Process]]
- [[anode-materials|Anode Material (Silicon)]]
- [[battery-manufacturing|Battery Manufacturing Process Overview]]