---
title: Mono-Cell
created: 2026-06-05
updated: 2026-06-08
type: glossary
tags: [mono-cell, stacking, lamination, pouch]
sources:
  - raw/battery-inside-en/en/interview-en/i-manage-the-stacking-process-of-the-global-sites-to-manufacture-the-worlds-best-pouch-t-e7395d1990.md
  - raw/battery-inside-en/en/tech-en/battery-glossary-mono-cell.md
  - raw/battery-inside-en/en/interview-en/lg-energy-solutions-azs-advanced-z-stacking-ensuring-a-stable-electrode-stacking-structure.md
  - raw/battery-inside-en/en/interview-en/incharge-areum-lee-of-the-pouch-type-big-data-team-manages-the-quality-of-pouch-type-bat-250b116575.md
  - raw/battery-inside-en/en/tech-en/infographic21-azs.md
confidence: high
---
# Mono-Cell

## Overview

A **mono-cell** is the fundamental laminated electrode‑separator building block used in the assembly of stacked pouch‑type lithium‑ion batteries. It consists of one central electrode (either a cathode or an anode) sandwiched between two separator layers, with an outer electrode of opposite polarity on each side. The repeating structure follows the pattern: **separator – center electrode – separator – outer electrode**. For example, a cathode‑centered mono‑cell has the configuration: anode / separator / cathode / separator / anode.

Mono‑cells are the primary unit in LG Energy Solution’s proprietary **Lamination & Stacking (L&S)** process, which is the dominant manufacturing method for large‑format pouch cells used in electric vehicles (EVs) and energy storage systems. The mono‑cell concept is distinct from the [[bi-cell|Bi-Cell]], where the outer electrodes share the same polarity (e.g., cathode / separator / anode / separator / cathode). Bi‑cells are typically employed in the Stack & Folding (S&F) process, often for smaller consumer‑electronics cells.

## Technical Details

### Mono‑Cell Formation

A mono‑cell is created through a precise lamination process that bonds electrodes and separators without damaging the porous separator structure. The key steps are:

1. **Electrode preparation**: Cathodes (e.g., NMC, LFP, NCMA) and anodes (graphite‑based or silicon‑doped) are coated onto current collectors—aluminum for cathodes, copper for anodes—with active‑material layer thickness typically 100–150 µm per side. Electrodes are then slit to required widths.
2. **Separator placement**: A microporous polyolefin separator (thickness 12–25 µm, porosity ~40%) is placed on each side of the central electrode. The separator may be coated with a ceramic or PVDF layer to improve thermal stability and adhesion.
3. **Lamination**: Heat (150–200 °C) and pressure (2–5 kgf/cm²) are applied via heated rollers or platens to partially melt the separator’s surface or a separate adhesive layer, bonding it to the electrode. Alignment tolerances during lamination are typically ±0.3–0.5 mm to ensure edge‑to‑edge precision.

After lamination, the mono‑cell is cut to final dimensions. The outer electrodes in a mono‑cell are single‑sided coated (only on the side facing the center electrode) to avoid wasted active material, while the center electrode is double‑sided coated, maximizing energy density.

### Stacking into a Full Cell

To build a pouch cell of a given capacity, a prescribed number of mono‑cells are stacked vertically. For a typical 60 Ah EV pouch cell, the stack may comprise 20–30 mono‑cells, depending on electrode areal capacity (3–5 mAh/cm²). The stacking process repeats the mono‑cell unit exactly: each new mono‑cell is placed so that its outer electrode contacts the outer electrode of the previous unit, forming a serial electrical connection through the tabs.

At the top of the stack, a **half‑cell** (two separator layers + an anode, or the cathode equivalent) is added to ensure the outermost electrodes are of opposite polarity and can be connected to the cell terminals. The entire stack is then wrapped in a final separator layer and inserted into a pouch envelope.

### Comparison with Bi‑Cell and Wound Cells

- **Mono‑cell vs. Bi‑cell**: In a bi‑cell, the outer electrodes share the same polarity. Bi‑cells are used in the Stack & Folding process, where a long strip of bi‑cells is folded into a stack. Bi‑cells offer slightly faster assembly but can suffer from uneven electrode alignment due to folding stresses. Mono‑cells, being individually laminated and stacked, provide tighter alignment control—critical for high‑rate performance and safety.
- **Mono‑cell vs. Wound (jelly‑roll) cells**: Cylindrical and prismatic cells use spiral winding, which can cause misalignment of inner layers and restricts the cell aspect ratio. Mono‑cell stacking allows arbitrary cell dimensions and uniform compression across the stack, improving cycle life and reducing swelling in pouch formats.

### Process Tolerances and Yield

State‑of‑the‑art stacking equipment, such as LG Energy Solution’s [[azs-stacking|AZS (Advanced Z‑Stacking)]], achieves layer‑by‑layer alignment within ±0.2 mm and stacking speeds of 0.3 seconds per layer. High precision reduces the risk of internal shorts from electrode protrusion. Yield rates for mono‑cell stacking are typically above 98% in well‑optimized lines—AZS lines reached 99% yield within four months of production start (2024, HLI Green Power, Indonesia). In contrast, conventional winding processes often achieve only 90–95% yield.

### Advanced Z‑Stacking (AZS) Integration

LG Energy Solution’s AZS process combines L&S with a Z‑shaped separator folding method. In AZS, a separator is first folded in a zigzag pattern, and electrodes are inserted into each fold. A **Heat Press** step then applies heat and pressure to bond the electrodes to the separator, improving structural integrity and minimizing overhang—where an electrode protrudes beyond its neighboring electrode. This integration enhances safety by preventing electrode misalignment during later handling and accelerates manufacturing by allowing multiple cells to be transported as a bonded unit.

## Significance and LG Context

The mono‑cell architecture is a cornerstone of modern pouch‑cell manufacturing for several reasons:

- **Energy Density**: By allowing arbitrary stacking counts, mono‑cells enable high‑capacity cells (up to 200 Ah) with volumetric energy densities of 700–800 Wh/L (NMC‑based) while maintaining a low aspect ratio ideal for under‑vehicle floor packaging.
- **Thermal Management**: The flat, planar stack provides a large surface area for direct cooling plates between cells, reducing thermal gradients and enabling fast charging (e.g., 10–80% in 18 minutes for 4C‑capable cells).
- **Manufacturing Flexibility**: The same mono‑cell unit can be used across multiple cell sizes by simply varying stacking count—reducing tooling costs and accelerating new product development.
- **Reliability**: Lamination eliminates gaps between electrodes and separators, suppressing lithium plating during fast charging. Combined with precise AZS alignment, mono‑cell stacks exhibit low self‑discharge and high consistency (~99% capacity yield in first‑grade cells).

LG Energy Solution’s investment in AZS technology has set an industry benchmark for speed and accuracy. Major automakers, including General Motors and Hyundai, source pouch cells built with mono‑cell stacking from LG’s factories. The Indonesia plant (PT. HLI Green Power) began mass production with AZS in April 2024, achieving rapid yield improvement and demonstrating the scalability of the mono‑cell approach.

## Related Pages

- [[assembly-process|Assembly Process]]
- [[azs-stacking|AZS (Advanced Z‑Stacking)]]
- [[bi-cell|Bi-Cell]]
- [[battery-manufacturing|Battery Manufacturing Process Overview]]
- [[cell-format-comparison|Cell Form Factor Comparison (Cylindrical vs Pouch vs Prismatic)]]
- [[cell-to-pack|Cell‑To‑Pack (CTP)]]
- Lamination Process in Battery Manufacturing
- Stacking Methods for Pouch Cells
