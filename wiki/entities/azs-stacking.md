---
title: AZS (Advanced Z-Stacking)
created: 2026-06-05
updated: 2026-06-08
type: entity
tags: [azs, stacking, lamination, pouch, safety, energy-density]
sources:
  - raw/battery-inside-en/en/tech-en/a-better-life-with-batteries-azs-advanced-z-stacking.md
  - raw/battery-inside-en/en/interview-en/lg-energy-solutions-azs-advanced-z-stacking-ensuring-a-stable-electrode-stacking-structure.md
  - raw/battery-inside-en/en/tech-en/infographic21-azs.md
  - raw/ko/story/lgenergysolution-azs-advanced-z-stacking.md
  - raw/ko/tech/infographics21-azsadvanced-z-stacking.md
confidence: high
---
# AZS (Advanced Z-Stacking)

## Overview

Advanced Z-Stacking (AZS) is a proprietary pouch-cell assembly technology developed by LG Energy Solution (LGES) that combines the structural benefits of Z-stacking with the bonding precision of lamination and heat pressing. Unlike conventional stacking methods that build individual mono-cells and then stack them, AZS creates the entire electrode–separator stack in a single integrated process. This tight integration delivers measurable improvements in energy density (5–10% higher than traditional stacking), internal short-circuit prevention, and manufacturing consistency. AZS is a core enabler of LGES’s high‑safety, high‑energy‑density pouch cells used by OEMs such as GM (Ultium Cells), Stellantis (NextStar Energy), and Honda.

## Technical Details

### Process Steps

1. **Separator Z‑folding** – A continuous separator sheet is folded into a zigzag (Z) shape, creating a series of pockets.
2. **Electrode insertion** – Die‑cut anode and cathode sheets are sequentially placed into the separator pockets in an alternating pattern (anode, cathode, anode…). The Z‑folded separator physically isolates each electrode layer, preventing contact even if slight misalignment occurs during handling.
3. **Heat press lamination** – The layered assembly undergoes a controlled heat‑press process. Heat and pressure bond the electrodes to the separator, forming a unified stack. LGES has developed proprietary know‑how to optimise temperature, pressure, and dwell time to achieve the ideal adhesion strength.

### Key Parameters & Mechanisms

- **Adhesion strength** is a critical trade‑off. Too weak, and electrodes can detach during formation cycling, leading to lithium plating and capacity fade. Too strong, and thermal expansion/contraction during charge‑discharge can cause structural deformation, reducing electrode surface area and increasing local current density. LGES calibrates the heat‑press conditions to a narrow window that balances both risks.
- **Alignment precision** – The Z‑folded separator acts as a physical barrier. Even if an electrode shifts slightly, the neighbouring layers are structurally separated, dramatically reducing the risk of internal short circuits. This is fundamentally different from conventional stacking where a misaligned electrode can directly contact the opposite polarity.
- **Overhang elimination** – In conventional stacking, protruding electrode edges (overhang) can cause localised current concentration and dendrite growth. AZS eliminates overhang because the Z‑folded separator conforms tightly around each electrode, and the subsequent heat press bonds the layers in their correct positions.

### Comparison with Conventional Methods

| Aspect | Conventional L&S | Conventional Z‑Stacking | AZS |
|--------|------------------|------------------------|-----|
| Process | Build mono‑cells (electrode + 2 separators) then stack them with half‑cells. | Fold separator in Z‑shape; insert electrodes without bonding. | Same folding as Z‑stacking, then heat‑press to bond. |
| Alignment stability | Moderately stable; prone to layer shift during handling. | Structure reduces shift, but no bonding means electrodes can move. | Fully bonded; layers cannot shift during transport or formation. |
| Energy density | Good (space efficient). | Moderate (no bonding leaves small gaps). | 5–10% higher than conventional stacking; 2‑mm‑thin cells possible. |
| Yield ramp | Typical learning curve. | – | Achieved >99% yield in 4 months at Indonesia plant (HLI Green Power). |

## Significance & LG Context

### Manufacturing & OEM Impact

AZS is deployed at LGES’s global pouch‑cell production lines. The first mass‑production site using AZS was PT. HLI Green Power in Indonesia (started April 2024), where the process reached >99% yield within four months. This rapid ramp demonstrates the robustness of the AZS process and its compatibility with high‑volume manufacturing. LGES is actively exploring extending AZS beyond Indonesia and beyond the pouch form factor.

The technology directly supports the safety and energy‑density requirements of key OEM customers. For example, Ultium Cells (a GM‑LGES joint venture) uses AZS‑based pouch cells to achieve the 400‑mile range targets for GM’s electric vehicles. Similarly, NextStar Energy (Stellantis‑LGES) relies on AZS for consistent cell‑to‑cell performance in battery packs.

### Future Developments

LGES is developing next‑generation AZS equipment that will increase stacking speed while maintaining alignment precision. Machine‑learning and AI models are being trained on real‑time process data (temperature profiles, pressure uniformity, electrode positioning) to predict and prevent defects. This digital integration is expected to further improve yield and reduce energy consumption per cell.

## Related Pages

- [[assembly-process|Assembly Process]]
- [[separator|Separator]]
- [[cell-format-comparison|Cell Form Factor Comparison (Cylindrical vs Pouch vs Prismatic)]]
- [[lg-energy-solution|LG Energy Solution]]
- [[ultium-cells|Ultium Cells]]
- Lithium Plating
- [[formation-aging|Formation Process]]
