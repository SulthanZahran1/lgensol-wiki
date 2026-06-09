---
title: Lithium Metal Battery
created: 2026-06-05
updated: 2026-06-08
type: entity
tags: [lithium-metal, anode, energy-density, fast-charging, safety]
sources:
  - raw/battery-inside-en/en/tech-en/game-changer-battery-lithium-metal-battery-achieving-both-energy-density-and-compact-volume.md
  - raw/battery-inside-en/en/tech-en/questions-about-all-batteries-in-the-world-why-are-lithium-metal-batteries-in-the-spotlight.md
  - raw/battery-inside-en/en/news-en/lg-energy-solution-to-invest-in-promising-u-s-lithium-metal-battery-technology-startup-s-b483d8c1c0.md
  - raw/battery-inside-en/en/tech-en/whats-the-difference-between-lithium-hydroxide-and-lithium-carbonate.md
  - raw/battery-inside-en/en/tech-en/infographics-18-types-of-anode-materials.md
confidence: high
---
# Lithium Metal Battery

## Overview
Lithium metal batteries represent a paradigm shift in anode technology, replacing conventional graphite (or silicon-doped graphite) with metallic lithium foil. This substitution unlocks a theoretical specific capacity of 3,860 mAh/g for the anode—roughly ten times that of graphite (372 mAh/g). Combined with the low density of lithium (0.534 g/cm³), the anode can be fabricated as an ultrathin foil (typically 20–50 µm), dramatically reducing cell volume and weight. The result is a step-change in gravimetric and volumetric energy density, making lithium metal a cornerstone for next-generation chemistries such as [[lithium-sulfur-battery|Lithium-Sulfur]], [[solid-state-battery|All-Solid-State]], and lithium-air systems.

Unlike intercalation anodes, where Li⁺ ions must diffuse into layered host structures, lithium metal operates through direct electroplating and stripping. This mechanism eliminates the need for a passive host, enabling both higher capacity and inherently faster charge/discharge kinetics—provided the morphology of deposited lithium can be controlled.

## Technical Details

### Anode Performance Metrics
The theoretical specific capacity of 3,860 mAh/g is only part of the advantage. In practical cells, a thin lithium foil (e.g., 20 µm) can achieve an areal capacity of ~4 mAh/cm², matching or exceeding typical NMC cathodes. However, to maximize cell-level energy density, the lithium foil must be as thin as possible—ideally 20 µm or less—without compromising mechanical integrity during manufacturing and cycling.

During discharge, lithium is stripped from the anode; during charge, it is plated back. The efficiency of this plating/stripping cycle (Coulombic efficiency, CE) is critical. For commercial viability, CE must exceed 99.9% over hundreds of cycles. Early lithium metal cells often suffered CE below 99%, leading to rapid capacity fade. Recent electrolyte and interface engineering have pushed CE above 99.5% in lab cells, but sustaining this in large-format cells under realistic conditions remains a challenge.

### The Dendrite Problem
The primary obstacle to commercialization is the formation of lithium dendrites. During charging, lithium ions deposit unevenly on the anode surface due to local variations in current density, surface roughness, and SEI (solid electrolyte interphase) heterogeneity. This leads to tree-like, branched structures that grow toward the cathode. Dendrites pose two critical risks:
1. **Short circuits** – If a dendrite pierces the separator, it creates an internal short, causing rapid self-discharge and thermal runaway.
2. **Capacity fade** – Dendrites increase the active surface area, accelerating parasitic reactions with the electrolyte. Dead lithium (electrically isolated, inactive lithium) accumulates, irreversibly consuming cyclable lithium.

Dendrite growth is aggravated by high charge rates, low temperatures, and non-uniform pressure. Even at moderate rates (e.g., 1C), dendrites can initiate within tens of cycles if not mitigated.

### Mitigation Strategies
A multi-pronged approach is being pursued by industry and academia:

- **Electrolyte Engineering**: The composition of the electrolyte dictates the SEI structure. Additives such as lithium nitrate (LiNO₃), fluoroethylene carbonate (FEC), and lithium difluorophosphate (LiDFP) promote a denser, more uniform SEI. LG Energy Solution and KAIST have developed a borate-pyran-based electrolyte system that restructures the SEI to suppress dendrite formation and enable stable cycling even under lean electrolyte conditions (i.e., low electrolyte-to-capacity ratio, E/C < 3 g/Ah). This system demonstrated 12-minute fast charging (5C rate) with minimal dendrite initiation.

- **Separator Design**: Mechanical reinforcement blocks dendrite penetration. LGES’s Safety Reinforced Separator (SRS) technology applies ceramic coatings (e.g., Al₂O₃) on a polyethylene base, increasing puncture resistance. Advanced separators also incorporate functional layers that chemically deactivate dendrites upon contact.

- **Pressure Management**: External stack pressure (typically 5–20 atm) helps maintain uniform contact between the lithium foil and the current collector, reducing localized current hotspots. Pressure also compresses the separator, closing pore gaps that dendrites could exploit.

- **3D Host Structures**: Instead of a planar lithium foil, some researchers use a porous scaffold (e.g., carbon foam, nickel mesh) to host lithium, distributing the plating current over a larger surface area and reducing local current density. This approach is often paired with pre-lithiation to compensate for initial lithium loss.

- **Solid-State Electrolytes**: Replacing liquid electrolyte with a solid ceramic or polymer electrolyte physically blocks dendrite propagation. While solid-state batteries are a separate category, lithium metal is the preferred anode for many solid-state designs due to its compatibility with non-flammable solid electrolytes.

### LG Energy Solution’s Progress
LGES initiated lithium metal R&D in 2013 through its Future Technology Center. In 2021, the company established the Frontier Research Laboratory (FRL) with KAIST, focused on developing practical lithium metal cells. Key achievements include:
- Demonstration of 12-minute fast charging (5C) for pouch cells using the borate-pyran electrolyte.
- Lean electrolyte systems (E/C ratio < 2.5 g/Ah) achieving >500 cycles with >80% capacity retention at moderate rates (0.5C/1C).
- Scalable lithium foil handling and lamination processes for mass production.

These developments position the technology for high-energy applications where fast charging and lightweight are paramount, such as electric vertical take-off and landing (eVTOL) aircraft, high-performance EVs, and portable electronics.

## Market Significance
Lithium metal batteries promise a 30–50% increase in cell-level energy density over state-of-the-art lithium-ion cells (from ~270 Wh/kg to >400 Wh/kg). For an EV, this translates to 600–800 km range in a pack of the same weight, or a 25–30% reduction in pack weight for the same range. The fast-charging capability (5C or higher) addresses a key consumer pain point.

However, commercial deployment must overcome reliability and safety gaps. Current best-in-class lithium metal cells achieve 500–800 cycles in lab conditions, whereas automotive requirements demand 1,000–1,500 cycles with 80% retention. Safety certification (e.g., UN 38.3, UL 1642) will require robust cell designs that pass nail penetration and thermal abuse tests.

Market entry is expected in segments with less stringent cycle life requirements, such as drones, medical devices, and space applications (2026–2028), followed by premium EVs and aircraft (2030–2035). LGES aims to pilot production of lithium metal cells for eVTOL by 2027.

## Related Pages
- [[lithium-sulfur-battery|Lithium-Sulfur Battery]]
- [[solid-state-battery|All-Solid-State Battery]]
- [[silicon-anode|Silicon Anode Material]]
- [[46-series-battery|46-Series Cylindrical Battery (4680/4695)]]
- [[next-gen-battery-overview|Next-Generation Battery Comprehensive Comparison]]
- Separator Technology and SRS
- Fast-Charging Technologies for Lithium-ion Batteries
