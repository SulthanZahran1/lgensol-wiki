---
title: Wet vs Dry Electrode Process
created: 2026-06-05
updated: 2026-06-08
type: comparison
tags: [comparison, wet-electrode, dry-electrode, electrode, drying, coating]
sources:
  - raw/battery-inside-en/en/tech-en/infographics-16-wet-electrode-process-dry-electrode-process.md
  - raw/battery-inside-en/en/tech-en/game-changer-battery-innovative-dry-electrode-process-enhancing-manufacturing-efficiency-495e15ea11.md
  - raw/ko/tech/%ec%a0%84%ec%a7%80%ec%a0%84%eb%8a%a5%ed%95%9c-%ec%a0%84%ec%a7%80-%ec%9d%b4%ec%95%bc%ea%b8%b0-%ea%b1%b4%ec%a1%b0-%ec%97%86%ec%9d%b4-%ec%99%84%ec%84%b1%ed%95%98%eb%8a%94-%ec%a0%84%ea%b7%b9-%ea%b1%b4.md
  - raw/battery-inside-en/en/tech-en/a-better-life-with-batteries-how-to-make-a-battery-step1-electrode-manufacturing-coating.md
  - raw/ko/tech/battery-manufacturing-efficiency-%ea%b1%b4%ec%8b%9d-%ec%a0%84%ea%b7%b9-%ea%b3%b5%ec%a0%95.md
confidence: high
---
# Wet vs Dry Electrode Process

## Overview / Introduction

Electrode manufacturing is the first and most impactful step in battery production. The choice between the conventional **wet electrode process** and the emerging **dry electrode process** directly shapes cell cost, performance, energy density, environmental footprint, and production scalability. The wet process, which relies on solvent-based slurries, has dominated the industry for decades. The dry process, which eliminates solvents entirely, is now advancing rapidly as a transformative alternative. LG Energy Solution (LGES) has been developing dry electrode technology for over a decade and targets commercialization by 2028, with pilot lines already operational at its Ochang Energy Plant in South Korea.

## Technical Details

### Wet Electrode Process (Conventional)

The wet process begins with **mixing**: active material (cathode or anode), conductive additive, and binder are blended with a solvent to form a liquid slurry. For cathodes, the solvent is typically N-Methyl-2-pyrrolidone (NMP), a toxic and expensive organic solvent that requires closed-loop handling and energy-intensive recovery. For anodes, water is commonly used. Following mixing, the slurry is coated onto a current collector foil—aluminum for cathodes, copper for anodes—via slot-die coating. LGES pioneered **Double Layer Slot Die (DLD)** coating, a platform technology that simultaneously coats two different slurries, enabling functional optimization of top and bottom electrode layers (e.g., enhancing fast-charging capability at the top and adhesion at the bottom).

After coating, the electrode moves through long drying ovens, often exceeding 100 meters in length and operating above 100°C, to evaporate the solvent. This drying step is the most energy-intensive and cost-prohibitive part of the wet process: it alone accounts for approximately **40% of total electrode manufacturing cost**. The solvent must be recovered, condensed, and recycled, adding both capital expense and operational complexity.

A critical technical challenge in wet processing is **binder migration**. During drying, the liquid solvent carries binder and conductive additive toward the electrode surface, resulting in a non-uniform distribution through the electrode thickness. This migration weakens internal cohesion and adhesion to the current collector, particularly problematic for thick electrodes designed for higher energy density. It limits achievable electrode loading and can reduce manufacturing yield and cell capacity.

### Dry Electrode Process (Emerging)

The dry process eliminates solvent entirely. Active material, conductive additive, and binder—often PTFE, a non-aqueous polymer—are mixed in solid powder form. The core innovation lies in **fibrillation**: mechanical shearing forces PTFE particles to elongate into thin fibers, creating a continuous adhesive network that binds active material and conductive additive particles together. These “bonding bridges” provide excellent internal cohesion and adhesion to the current collector without requiring a liquid phase.

Several dry coating approaches exist:
- **Maxwell-type method**: The powder is calendered into a self-supporting film, then laminated onto the current collector.
- **Powder coating method**: Dry powder is directly sprinkled or sprayed onto the current collector, then compacted via roll pressing.

After coating, only **roll pressing (calendering)** is needed—no drying ovens. This eliminates the long drying step, reducing floor space by up to 50% and dramatically cutting energy consumption. Without solvent migration, binder and conductive additive remain uniformly distributed through the electrode thickness. Dry-processed electrodes can achieve **significantly higher active material loading** (thicker electrodes) with improved structural stability, potentially increasing energy density by 10–20% for the same cell volume.

However, dry processing has challenges: uniform mixing of solid powders is more difficult than liquid blending; maintaining consistent film thickness and density requires precise process control; fibrillation must be carefully optimized to avoid over- or under-fibrillation; adhesion between the dry electrode film and the current collector can be weaker; and current line speeds for dry processing are generally lower than for wet processing in some designs.

### Key Comparison

| Aspect | Wet Process | Dry Process |
|--------|-------------|-------------|
| Solvent | NMP (cathode) or water (anode) | None |
| Drying | Required (long ovens, ~40% of electrode cost) | Eliminated |
| Binder migration | Yes (limits thickness, reduces yield) | No (uniform distribution) |
| Floor space | Large drying ovens | Reduced up to 50% |
| Technology maturity | Mature, widely deployed | Emerging, pilot stage |
| Line speed | Higher (mature) | Lower (improving) |
| Energy density potential | Limited by coating/drying constraints | Enhanced (thicker electrodes) |

## Significance / LG Context

LG Energy Solution has been investing in dry electrode technology for over a decade. As of late 2024, the company completed a pilot line at the Ochang Energy Plant and is targeting mass production readiness by 2028, with sequential rollout to global manufacturing sites. LGES expects dry processing to reduce electrode manufacturing costs by **17%** and overall battery costs by up to **30%**.

Beyond cost reduction, dry electrode technology is a key enabler for next-generation batteries. It improves production efficiency for **sodium-ion cells** and is essential for **all-solid-state batteries**, where solvent-free processing is required. LGES is also researching dry process applications for high-nickel cathodes and silicon anodes, aiming to simultaneously reduce cost and enhance performance.

The technology aligns with global sustainability trends: eliminating toxic NMP simplifies regulatory compliance and reduces environmental burden. LGES’s roadmap includes continued R&D on advanced materials, process integration, and scaling up line speeds to match or exceed wet process throughput.

## Related Pages

- [[electrode-process|Electrode Process]]
- [[lg-energy-solution|LG Energy Solution]]
- [[sodium-ion-battery|Sodium-ion Battery]]
- [[battery-manufacturing|Battery Manufacturing Process Overview]]
- [[high-nickel-battery|High-Nickel Cathode]]
- [[solid-state-battery|Solid-State Battery]]
- [[dld|DLD (Double Layer Slot Die Coating)]]
- Battery Manufacturing Cost Analysis
