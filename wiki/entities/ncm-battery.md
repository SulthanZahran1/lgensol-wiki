---
title: NCM (Ternary) Battery
created: 2026-06-05
updated: 2026-06-08
type: entity
tags: [ncm, cathode, energy-density, voltage, ev]
sources:
  - raw/battery-inside-en/en/tech-en/infographics-9-ncm-cathode.md
  - raw/battery-inside-en/en/tech-en/battery-glossary-ternary-battery.md
  - raw/ko/tech/energy-density-price-competitiveness-%ea%b3%a0%ec%a0%84%ec%95%95-%eb%af%b8%eb%93%9c%eb%8b%88%ec%bc%88-%eb%b0%b0%ed%84%b0%eb%a6%ac.md
  - raw/battery-inside-en/en/tech-en/infographics-cathode-materials.md
  - raw/battery-inside-en/en/tech-en/infographics-11-ncma-cathode.md
confidence: high
---
# NCM (Ternary) Battery

## Overview

NCM (Nickel Cobalt Manganese) batteries, also known as ternary lithium-ion batteries, employ a layered oxide cathode of the form LiNiₓCoᵧMn₁₋ₓ₋ᵧO₂. By varying the molar ratios of nickel, cobalt, and manganese, manufacturers can tailor the cathode for specific trade-offs among energy density, power capability, cycle life, thermal stability, and cost. Common formulations include NCM111 (1:1:1), NCM523, NCM622, NCM712, and NCM811, where the digits represent the relative percentages of Ni, Co, and Mn, respectively. Since their commercial debut in the early 2010s, NCM cathodes have become the dominant chemistry for electric vehicle (EV) batteries, offering gravimetric energy densities of 200–300 Wh/kg at the cell level—significantly higher than lithium iron phosphate (LFP) cells (typically 140–180 Wh/kg). The nominal cell voltage of NCM is approximately 3.6–3.7 V, enabling high pack-level energy without excessive cell counts. Despite these advantages, NCM batteries face challenges related to cobalt price volatility, ethical sourcing concerns, and thermal stability degradation at high nickel contents. The industry trend is therefore shifting toward higher nickel ratios and lower cobalt, culminating in next-generation chemistries such as NCMA (with aluminum substitution) and ultra-high-nickel cathodes (Ni ≥ 90%).

## Technical Details

The electrochemical performance of NCM cathodes stems from their α-NaFeO₂-type layered crystal structure (space group R-3m). During charging, lithium ions deintercalate from octahedral sites between transition-metal–oxygen slabs, and nickel (Ni²⁺/Ni³⁺/Ni⁴⁺) undergoes redox reactions that provide the majority of reversible capacity. Cobalt (Co³⁺) partially participates in redox but primarily stabilizes the layered structure by suppressing unwanted cation mixing and improving lithium-ion diffusion kinetics. Manganese (Mn⁴⁺) remains electrochemically inactive in the typical 3.0–4.2 V window, acting as a structural pillar that enhances thermal robustness and reduces oxygen evolution at high states of charge.

**Composition–performance trade-offs:** In low-nickel formulations like NCM111, reversible capacity is limited (~160 mAh/g) but thermal runaway onset exceeds 250 °C, making cells safer. Increasing nickel content to NCM523 (~170 mAh/g) and NCM622 (~180 mAh/g) raises energy density while moderately reducing thermal stability. NCM811, with 80% nickel, achieves capacities of 200–210 mAh/g but exhibits a thermal runaway onset below 220 °C and accelerated surface reactivity with LiPF₆-based electrolytes. To mitigate these issues, manufacturers employ particle coatings (e.g., Al₂O₃, TiO₂), bulk doping with elements such as Zr, Al, or Mg, and advanced electrolyte additives like vinylene carbonate (VC) and prop-1-ene-1,3-sultone (PES). The latest high-nickel NCM (Ni ≥ 88%) incorporates single-crystal particle morphology to reduce grain boundary cracking and gas evolution, extending cycle life to over 1,500 cycles under standard EV usage.

**Degradation mechanisms:** Repeated cycling of high-nickel NCM induces H2–H3 phase transitions that cause anisotropic lattice contraction and expansion, generating microcracks within polycrystalline secondary particles. These cracks provide pathways for electrolyte penetration, leading to widespread side reactions and capacity fade. Additionally, Ni⁴⁺ ions at the particle surface are highly reactive, promoting oxygen loss and the formation of a spinel or rock-salt surface layer, which increases impedance. Cation mixing—where Ni²⁺ (ionic radius ~0.69 Å) occupies lithium sites (~0.76 Å)—further hinders lithium diffusion. Strategies to counter these effects include concentration-gradient designs (Ni-rich core, Mn-rich shell) that reduce surface reactivity and disperse internal stress, as well as bulk doping that strengthens metal–oxygen bonds and suppresses phase transitions.

**Manufacturing considerations:** NCM cathode active material is synthesized via co-precipitation of mixed hydroxides followed by calcination with a lithium source (typically LiOH or Li₂CO₃) at 800–950 °C. Particle size distribution (10–15 µm for polycrystalline aggregates; 3–6 µm for single crystals) directly affects electrode density and rate performance. Because NCM is moisture-sensitive, the drying and assembly process must occur in dry rooms (dew point ≤ –50 °C) to prevent LiOH formation and performance loss. Electrode fabrication requires precise slurry rheology and coating uniformity to avoid localized hotspots that could trigger thermal runaway.

## Significance and LG Energy Solution Context

NCM batteries currently represent approximately 60–70% of global EV battery demand by capacity, with the remainder largely held by LFP. In 2025, average NCM cell prices fell to around $80–90/kWh, approaching cost parity with LFP ($55–65/kWh) when considering total cost of ownership—namely pack energy density and vehicle range. Automakers such as Tesla, BMW, Mercedes-Benz, Hyundai, and General Motors favor high-nickel NCM for premium long-range vehicles. The industry trend toward reducing cobalt is driven by both cost and geopolitical factors: over 70% of global cobalt supply originates from the Democratic Republic of Congo, raising price volatility and ethical concerns. Consequently, formulations have evolved rapidly—NCM523 has largely given way to NCM712 and NCM811, and next-generation cells target Ni ≥ 90% with ≤5% Co, often reinforced with aluminum in NCMA.

LG Energy Solution is a leading producer of NCM-based batteries. The company mass-produces NCMA cells (Ni 89–90%, Co ≤5%, Mn + Al balance), which have been integrated into the Tesla Model Y (Made in China) and General Motors’ Ultium platform. LG’s development roadmap includes a high-voltage mid-nickel NCM (NCM613) for entry-level EVs and stationary storage, offering energy densities comparable to NCM811 while maintaining safer thermal profiles and lower cost. For premium segments, LG is advancing single-crystal NCMA technology with medium-sized primary particles to increase electrode packing density and energy density. To secure raw materials, LG has invested in Chinese refiner Greatpower (₩35 billion for 4.8% equity, securing 20,000 tonnes of nickel over six years) and Australian Mines (71,000 tonnes of nickel and 7,000 tonnes of cobalt over six years), emphasizing ethical mining practices such as dry stacking tailings and IRMA certification.

Safety remains a central focus: NCM cells require sophisticated battery management systems (BMS), ceramic separators, and thermal propagation barriers. While intrinsically less stable than LFP, modern pack-level designs achieve comparable fire incident rates. Future outlook points to ultra-high-nickel NCMA and lithium-rich manganese (LRM) cathodes, though commercialization is challenged by oxygen release and voltage fade. Parallel development of high-voltage mid-nickel (e.g., NCM613, NMx) offers a bridge between cost, safety, and performance for mass-market EVs.

## Related Pages

- [[lfp-vs-ncm|LFP vs NCM Comparison]]
- [[high-nickel-battery|High-Nickel Battery]]
- [[ncma-battery|NCMA (Quaternary) Battery]]
- [[mid-nickel-battery|High-Voltage Mid-Nickel Battery]]
- [[cathode-tier-comparison|High-Nickel vs Mid-Nickel vs LFP]]
- [[nca-battery|NCA Battery]]
- Cobalt Supply Chain and Ethics
- [[solid-state-battery|Solid-State Battery]]