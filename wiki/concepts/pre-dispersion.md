---
title: Pre-Dispersion Process
created: 2026-06-05
updated: 2026-06-08
type: concept
tags: [mixing, conductive-additive, binder, electrode]
sources:
  - raw/battery-inside-en/en/tech-en/batteries-pre-dispersion-process-importance.md
  - raw/battery-inside-en/en/tech-en/a-better-life-with-batteries-how-to-make-a-battery-step1-electrode-manufacturing-mixing.md
  - raw/battery-inside-en/en/tech-en/infographics-16-wet-electrode-process-dry-electrode-process.md
  - raw/battery-inside-en/en/tech-en/a-better-life-with-batteries-binder.md
  - raw/battery-inside-en/en/tech-en/infographics-22-slurry-components-and-their-roles-active-material-conductive-additive-and-binder.md
confidence: high
---
# Pre-Dispersion Process

## Overview / Introduction

The pre-dispersion process is the critical first step in battery electrode slurry preparation. It specifically targets the uniform dispersion of conductive additives—particularly carbon nanotubes (CNTs)—before they are mixed with the active material and binder. Conductive additives, due to their nanometer-scale particle size and extremely high aspect ratio (CNTs are typically 1 nm in diameter and up to several micrometers long), naturally form strong agglomerates through van der Waals forces. These agglomerates can grow to tens or even hundreds of micrometers in size—far too large to be broken apart by conventional mixing blades during the main mixing step. If these agglomerates remain intact, the resulting electrode will contain uneven conductivity paths, leading to higher electrical resistance, reduced rate capability, and inconsistent cell performance. Pre-dispersion ensures that the conductive additive is fully separated and uniformly suspended, laying the foundation for a high-quality slurry.

In the overall mixing sequence, pre-dispersion occurs first, followed by binder dissolution (where the binder is dissolved in solvent), and finally main mixing (combining active material, pre-dispersed conductive additive, and dissolved binder under controlled speed and temperature). The success of this entire sequence hinges on the quality of the pre-dispersion; poor dispersion at this stage cannot be corrected in later steps.

## Technical Details

### The Agglomeration Problem

Conductive additives like CNTs and carbon black are supplied as dry powders. Individual CNTs have diameters around 1 nm and lengths up to several micrometers. Their high aspect ratio and strong inter-particle forces cause them to form tight bundles that resemble ropes or tangled masses. These bundles can be tens to hundreds of micrometers in size. If introduced directly to the main mixer, typical planetary or disperser blades cannot provide enough shear to disentangle them. The resulting slurry will contain large agglomerates that act as electrical bottlenecks, increasing overall electrode resistivity. For carbon black, the agglomerates are more granular but still require high shear to achieve a uniform dispersion.

### Two-Step Pre-Dispersion Procedure

1. **Pre-mixing:** The conductive additive, dispersant, and solvent are combined in a high-speed mixer to create a pre-dispersion solution. The dispersant—commonly cellulose-based compounds like carboxymethyl cellulose (CMC) or vinyl/acrylic polymers—adsorbs onto the particle surfaces, providing steric or electrostatic repulsion to prevent re-agglomeration. The solvent, typically N‑methyl-2-pyrrolidone (NMP) for organic systems or water for aqueous systems, wets the powder and facilitates initial separation. This step reduces the size of the largest agglomerates but does not fully disentangle the bundles.

2. **Bead Mill Process:** The pre-mixed solution is passed through a bead mill containing small ceramic beads (typically 0.1–1 mm diameter, with 0.3–0.6 mm being optimal for CNT dispersion). These beads rotate at high speed, generating intense shear and impact forces that mechanically break apart remaining agglomerates. The milling time and energy input are carefully controlled to reach a target particle size distribution, often measured by laser diffraction or rheology. After bead milling, the resulting dispersion contains well-separated individual conductive particles or small clusters, typically below 1–10 µm. This process is essential for CNTs, which cannot be fully disentangled by pre-mixing alone.

### Dispersion Methods

Three primary methods are used, often in combination:

- **Mechanical dispersion:** Uses physical energy (shear, impact, ultrasonic vibration). Bead mills and jet mills are common. Technically simplest, but limited in completely unraveling CNT bundles. Ultrasonic dispersion can achieve finer sizes but may damage the CNT structure if overused.
- **Chemical dispersion:** Treats the conductive additive surface with acids or surfactants. Reduces van der Waals forces but can introduce surface defects that degrade electrical conductivity. Moderate technical difficulty.
- **Dispersant-based dispersion:** Uses specialized polymers (cellulose-based, vinyl-based, acrylic) that adsorb onto particles. This is the most sophisticated method, preventing re-agglomeration without damaging the additive. It requires careful selection of dispersant molecular weight and concentration.

### Process Control Parameters

Key parameters that affect pre-dispersion quality include:

- **Mixing speed (rpm):** Too high can damage active material particles later; in pre-dispersion, it must be sufficient for wetting but not excessive to avoid foaming or overheating.
- **Temperature:** Excessive temperature rise during milling can cause gelation of the pre-dispersion solution, reducing dispersibility and potentially degrading the dispersant.
- **Bead size and loading:** Smaller beads generate higher shear but require longer residence time. Optimal bead size is typically 0.3–0.6 mm for CNT dispersion.
- **Dispersant-to-additive ratio:** Typically optimized to achieve full surface coverage without excess free dispersant that could interfere with binder adhesion.

## Significance / LG Context

Pre-dispersion is not merely a procedural convenience; it directly determines the final electrode's electrical performance. Without it, the conductive additive network is incomplete, leading to higher internal resistance, reduced power output, and lower energy efficiency. In high-performance cells (e.g., for electric vehicles), even a 5% increase in resistance can translate to several percent loss in capacity during high-rate discharge. LG Energy Solution emphasizes pre-dispersion as a key lever for improving cell-to-cell consistency and manufacturing yield.

In the context of LG’s technology roadmap, effective pre-dispersion enables the use of advanced conductive additives like CNTs, which can reduce conductive additive loading by up to 80% compared to carbon black, thereby allowing higher active material content and increased energy density. This aligns with the company's focus on next-generation high-energy-density batteries.

Furthermore, pre-dispersion plays a role in enabling thicker electrodes—a trend in high-energy designs—by ensuring uniform conductivity throughout the electrode thickness, mitigating issues like binder migration that occur during wet coating and drying. The process also interfaces with dry electrode process development, where pre-dispersion concepts are adapted for solid-state mixing without solvents.

## Related Pages

- [[binder|Binder]]
- [[conductive-additive|Conductive Additive (CNT)]]
- [[dry-electrode-process|Dry Electrode Process]]
- [[electrode-process|Electrode Process]]
- [[active-material|Active Material]]
- [[battery-manufacturing|Battery Manufacturing Process Overview]]
