---
title: Anodeless Battery
created: 2026-06-05
updated: 2026-06-08
type: glossary
tags: [anode, lithium-metal, energy-density, solid-state]
sources:
  - raw/battery-inside-en/en/interview-en/a-battery-without-an-anode-lg-energy-solutions-research-on-combining-anodeless-and-solid-ae5b6bf6d7.md
  - raw/battery-inside-en/en/tech-en/battery-glossary-anodeless-battery.md
  - raw/battery-inside-en/en/tech-en/the-next-generation-anode-material-silicon.md
  - raw/battery-inside-en/en/tech-en/infographics-18-types-of-anode-materials.md
  - raw/battery-inside-en/en/tech-en/infographics-12-anode.md
confidence: high
---
# Anodeless Battery

## Overview / Introduction

An anodeless battery is a cell architecture that omits a pre‑formed anode active material layer. During the first charge, lithium ions extracted from the cathode (e.g., NCM or LFP) travel through the electrolyte and are reduced directly on the anode current collector—typically a bare copper foil—forming a metallic lithium layer *in situ*. This plating process eliminates the need for conventional anode host materials such as graphite or silicon, and the associated slurry coating, drying, and calendering steps.

In traditional [[lithium-ion-battery|lithium‑ion batteries]] the anode acts as a rigid host structure that intercalates lithium ions during charging. In an anodeless design there is no such host; the lithium metal itself repeatedly plates and strips during every cycle. This concept is closely related to [[lithium-metal-battery|lithium metal batteries]], but with a pivotal difference: anodeless cells contain no pre‑assembled lithium metal foil. All lithium inventory comes solely from the cathode, making cycle‑by‑cycle lithium retention critically dependent on [[coulombic-efficiency|Coulombic Efficiency (CE)]].

The anodeless approach promises a step‑change in [[lithium-ion-battery|energy density]] and cost reduction. When married with [[solid-state-battery|solid‑state electrolytes]], it also mitigates safety issues inherent to lithium metal. LG Energy Solution has been actively developing this technology since at least 2021, patenting a unique combination of lithiophilic coatings and oxidation treatments on the current collector, specifically targeting sulfide‑based solid‑state systems.

## Technical Details

### Working Principle

A conventional lithium‑ion cell contains an anode layer (graphite or silicon composite) that is present from the moment of assembly. In an anodeless cell, that layer is absent: the cell stack starts thinner because only the cathode, separator/electrolyte, and bare current collector occupy volume. On the first charge, Li⁺ ions from the cathode are transported to the anode current collector, where they combine with electrons to plate as metallic lithium. During discharge, the lithium metal strips back to Li⁺ and returns to the cathode. This plating/stripping mechanism replaces intercalation, enabling volumetric energy density gains of 20–30% because the initial stack is thinner and no inactive host material is present.

### Key Challenges

1. **Coulombic Efficiency Loss** – Because the total lithium available is limited to what the cathode can provide, any parasitic reaction that irreversibly consumes lithium (e.g., SEI formation, electrolyte decomposition) directly reduces the usable capacity. In liquid electrolyte systems, the highly reactive lithium surface continuously reacts with the electrolyte, leading to low CE and rapid capacity fade. A CE of 99.9% or higher is required for practical cycle life, a demanding target for liquid‑electrolyte anodeless cells.

2. **Dendrite Formation** – When the current collector surface has poor lithiophilicity (low affinity for lithium), the metal tends to deposit non‑uniformly, preferentially at nucleation points. This leads to the growth of needle‑like dendrites that can penetrate the separator and cause internal short circuits, degrading both safety and cycle life.

### Enabling Technologies

Most practical anodeless designs pair the concept with a solid‑state electrolyte. Solid electrolytes—especially sulfide‑based or oxide‑based—offer two advantages: they mechanically suppress dendrite penetration, and they minimize parasitic side reactions compared to liquid electrolytes, thereby improving CE.

LG Energy Solution has developed a proprietary approach to further enhance plating uniformity. Two process technologies are applied to the anode current collector:

- **Lithiophilic Material Coating**: A thin, uniformly dispersed layer of a metal with high lithium affinity—such as silver (Ag), gold (Au), platinum (Pt), zinc (Zn), or magnesium (Mg)—is deposited on the copper foil. This promotes even nucleation and dense plating, preventing local overgrowth.

- **Oxidation Treatment**: In regions not coated with the lithiophilic material, an oxidation treatment is applied to locally improve lithium affinity while minimizing loss of electrical conductivity. The combination ensures that lithium plates uniformly across the entire current collector surface.

This dual‑treatment approach was patented in October 2021. It enables stable plating/stripping cycling in a solid‑state anodeless configuration. Moreover, because no reactive lithium metal is present until the first charge, cell assembly can be performed without a dry room—a significant manufacturing advantage that reduces capital and operational costs.

### Manufacturing and Cost Benefits

- **Simplified Anode Process**: No slurry mixing, coating, drying, or calendering steps are needed for the anode active material.
- **Material Cost Reduction**: Graphite, silicon, or lithium metal foil is replaced by a bare copper foil with a minimal lithiophilic coating.
- **Higher Energy Density**: The inactive anode layer is eliminated, allowing more active material per unit volume and increasing both gravimetric and volumetric energy density.
- **Easier Recycling**: In the discharged state, no lithium metal is present, making dismantling and material recovery safer and simpler.

## Significance / LG Energy Solution Context

Anodeless batteries are widely regarded as a transformative technology for next‑generation energy storage, particularly for electric vehicles (EVs). By removing the anode host, they simultaneously increase energy density and lower cost. When combined with solid‑state electrolytes, they also address the safety concerns that have historically limited lithium metal anodes.

LG Energy Solution is actively developing anodeless technology as part of its sulfide‑based solid‑state battery roadmap. Researchers from the Future Technology Center (Sulfide Solid‑State Battery 1 Project Team) have demonstrated that anodeless solid‑state cells can achieve stable cycling by controlling nucleation and growth through lithiophilic coating and oxidation. This work positions LG to deliver high‑energy, safe, and cost‑effective batteries for the EV market, potentially exceeding 670 Wh/L while improving safety margins by 30% or more compared to conventional cells.

The anodeless approach also aligns with LG’s broader strategy of diversifying its next‑generation battery portfolio, which includes [[lithium-sulfur-battery|lithium‑sulfur batteries]], [[silicon-anode|silicon anode materials]], and [[mid-nickel-battery|mid‑nickel cells]]. By eliminating the dry‑room requirement for assembly, LG can reduce manufacturing costs and accelerate the transition to solid‑state technology.

## Related Pages

- [[lithium-metal-battery|Lithium Metal Battery]]
- [[solid-state-battery|All‑Solid‑State Battery]]
- [[dendrite|Dendrite Formation]]
- [[coulombic-efficiency|Coulombic Efficiency (CE)]]
- [[next-gen-battery-overview|Next‑Generation Battery Comprehensive Comparison]]
- [[lithium-sulfur-battery|Lithium‑Sulfur Battery]]
- [[silicon-anode|Silicon Anode Material]]
- [[mid-nickel-battery|High‑Voltage Mid‑Nickel Battery]]