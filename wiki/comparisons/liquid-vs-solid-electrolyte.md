---
title: Liquid Electrolyte vs Solid Electrolyte
created: 2026-06-05
updated: 2026-06-08
type: comparison
tags: [comparison, electrolyte, solid-state, safety, thermal-stability]
sources:
  - raw/battery-inside-en/en/tech-en/game-changer-battery-all-solid-state-battery-the-ultimate-battery-that-delivers-higher-s-79332ecd61.md
  - raw/battery-inside-en/en/interview-en/how-will-semi-solid-state-batteries-change-our-lives.md
  - raw/battery-inside-en/en/news-en/a-new-solid-state-battery-surprises-the-researchers-that-created-it-2.md
  - raw/battery-inside-en/en/tech-en/a-better-life-with-batteries-solid-electrolyte.md
  - raw/battery-inside-en/en/tech-en/battery-glossary-sei-solid-electrolyte-interphase.md
confidence: high
---
# Liquid Electrolyte vs Solid Electrolyte

## Overview / Introduction

The electrolyte is the ion-transport medium that enables lithium ions to shuttle between the anode and cathode during charge and discharge. In commercial lithium-ion batteries (LIBs), the electrolyte is a liquid solution—a mixture of lithium salts (primarily LiPF₆), organic carbonate solvents (EC, DMC, EMC), and functional additives. This liquid electrolyte provides high ionic conductivity (10⁻²–10⁻³ S/cm) and excellent electrode wetting, but it also introduces significant safety risks: flammability, thermal runaway, and gas generation under high-voltage or high-temperature stress.

Solid electrolytes (SEs) replace the liquid with a solid material—sulfide, oxide, or polymer—that conducts lithium ions while acting as both electrolyte and separator. Solid electrolytes are inherently non-flammable, thermally stable up to much higher temperatures, and enable the use of lithium metal anodes (theoretical capacity ~10× that of graphite) and bipolar cell stacking, potentially doubling energy density. However, they face challenges in ionic conductivity (especially at room temperature for oxides and polymers), interfacial contact resistance, and cost‑effective manufacturing.

## Technical Details

### Liquid Electrolytes: Composition and Degradation

A typical liquid electrolyte comprises three components:

- **Lithium salt**: LiPF₆ is the most widely used salt because of its high ionic conductivity and good solubility in carbonate solvents. However, it is moisture-sensitive, generating corrosive HF (hydrofluoric acid) upon contact with trace water. Emerging alternatives like LiFSI (lithium bis(fluorosulfonyl)imide) offer improved thermal stability, lower viscosity, and the formation of a stable LiF‑rich SEI (solid electrolyte interphase) that suppresses dendrite growth. LiFSI is increasingly used as a co-salt or additive to boost low‑temperature performance.
- **Organic solvent**: Carbonate solvents (e.g., EC, DMC, EMC) dissolve the lithium salt and provide the necessary liquid medium. They must balance high dielectric constant (for ion dissociation) with low viscosity (for fast ion transport). EC has a high dielectric constant but high viscosity; DMC/EMC have low viscosity but lower dielectric constant—so a blend is used.
- **Additives**: Typically 0.5–5 wt% of the total electrolyte, additives protect electrode surfaces. For example, vinylene carbonate (VC) helps form a stable SEI on the anode, while propane sultone (PS) protects the cathode. But under high‑Ni cathodes, high voltage (>4.5V), or extended cycling, the additives become depleted, leaving the bulk carbonate solvent vulnerable to oxidative decomposition, generating CO₂, CO, and hydrocarbon gases. LG Energy Solution has developed a fundamentally new “Gas‑Free” solvent architecture (inspired by the FSI⁻ anion) that resists decomposition without relying on conventional carbonate structures.

### Solid Electrolytes: Three Main Types

1. **Sulfide‑based**: (e.g., Li₆PS₅Cl, Li₃PS₄) – Ionic conductivity near 10⁻²–10⁻³ S/cm at room temperature, comparable to liquid. The soft sulfide particles deform under pressure, enabling good interfacial contact with electrodes. However, they are extremely sensitive to moisture, releasing toxic H₂S gas, and require dry‑room or inert‑gas manufacturing.

2. **Oxide‑based**: (e.g., LLZO, LATP) – Lower ionic conductivity (~10⁻⁴–10⁻⁵ S/cm at RT) but excellent chemical and thermal stability (stable in air, up to >600°C). The rigid nature makes intimate electrode contact difficult; high‑temperature sintering is needed, and the brittle material can crack during cycling.

3. **Polymer‑based**: (e.g., PEO‑LiTFSI) – Process‑friendly (coating and lamination similar to liquid-electrolyte manufacturing), but conductivity is only ~10⁻⁴–10⁻⁵ S/cm at 60°C and drops significantly below room temperature. Polymers are often used in hybrid or semi‑solid configurations.

### Key Comparison Metrics

| Property | Liquid Electrolyte | Solid Electrolyte |
|----------|-------------------|-------------------|
| Ionic conductivity (RT) | 10⁻²–10⁻³ S/cm | 10⁻²–10⁻⁵ S/cm (sulfide > polymer ≈ oxide) |
| Safety | Flammable, thermal runaway risk | Non-flammable, stable to >300°C |
| Voltage window | ≤4.5V vs Li⁺/Li | Up to 5–6V (oxides); enables high‑voltage cathodes |
| Separator required | Yes | No (solid acts as separator) |
| Anode compatibility | Graphite, limited Si | Li metal, high‑Si, graphite |
| Manufacturing maturity | Very high (wet‑process filling) | Low (coating, sintering, or thin‑film deposition) |
| Relative cost | ~$5–10/kg | ~$50–500/kg (lab‑scale) |

## Significance / LG Context

LG Energy Solution (LGES) is actively developing all three solid‑electrolyte families, with clear commercial roadmaps:

- **Polymer‑based**: Targeting commercialization around 2026. Polymer electrolytes can leverage existing liquid‑filling equipment, reducing capital investment. LGES is optimizing the polymer‑salt‑additive formulation to increase low‑temperature conductivity.
- **Sulfide‑based**: Targeting commercialization before 2030. In 2021, LGES and UC San Diego published in *Science* (vol. 373, no. 6562) a room‑temperature fast‑charging all‑solid‑state battery using a sulfide electrolyte—a breakthrough that previously required >60°C. LGES’s Future Technology Center is also developing a bipolar‑stacked design where cells are connected in series inside a single package, dramatically increasing pack‑level energy density.
- **Oxide‑based**: Being researched for low‑cost, high‑safety applications. LGES is exploring thin‑film LLZO deposition techniques to reduce interfacial resistance.

The shift from liquid to solid electrolyte also addresses the intrinsic gas‑evolution problem. LGES’s innovative Gas‑Free solvent (announced in 2026) aims to stabilize the liquid electrolyte itself, but the ultimate solution—solid electrolyte—eliminates solvent decomposition altogether. As LGES moves toward all‑solid‑state, key remaining challenges include achieving defect‑free electrolyte layers over large areas, reducing solid‑solid interfacial resistance (especially during volume changes of Si or Li anodes), and scaling cost‑effective production.

A middle ground is emerging in the form of **semi‑solid and hybrid electrolytes**, which blend liquid and solid components to balance performance with manufacturability. These include gel polymer electrolytes (polymer matrices swollen with liquid electrolyte), ceramic‑in‑polymer composites, and liquid‑infused sulfide systems. Semi‑solid designs offer improved safety over pure liquid while avoiding the interfacial contact and scalability challenges of fully solid electrolytes. Several manufacturers, including LGES, are exploring hybrid approaches as near‑term stepping stones toward all‑solid‑state batteries, targeting commercialization timelines ahead of pure solid‑state systems.

## Related Pages

- [[electrolyte|Electrolyte / Electrolyte Solution]]
- [[solid-state-battery|All-Solid-State Battery]]
- [[separator|Separator]]
- [[lithium-metal-battery|Lithium Metal Battery]]
- [[next-gen-battery-overview|Next-Generation Battery Comprehensive Comparison]]
- [[gas-free-solvent|Gas-Free Solvent Development]]