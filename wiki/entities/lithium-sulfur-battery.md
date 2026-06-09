---
title: Lithium-Sulfur Battery
created: 2026-06-05
updated: 2026-06-08
type: entity
tags: [lithium-sulfur, cathode, energy-density, aerospace, uam, lithium-metal]
sources:
  - raw/ko/tech/game-changer-battery-%eb%8d%94-%ea%b0%80%eb%b3%8d%ea%b2%8c-%eb%8d%94-%eb%a9%80%eb%a6%ac-%eb%82%a0%ec%95%84%ea%b0%88-%eb%a6%ac%ed%8a%ac%ed%99%a9%eb%b0%b0%ed%84%b0%eb%a6%ac.md
  - raw/ko/opinion/technology-trends-lithium-sulfur-batteries.md
  - raw/battery-inside-en/en/tech-en/lithium-sulfur-battery-the-soaring-next-gen-battery.md
  - raw/ko/tech/%ed%95%98%eb%8a%98%ec%9d%84-%eb%82%98%eb%8a%94-%ec%b0%a8%ec%84%b8%eb%8c%80-%eb%b0%b0%ed%84%b0%eb%a6%ac-%eb%a6%ac%ed%8a%ac%ed%99%a9%eb%b0%b0%ed%84%b0%eb%a6%ac.md
  - raw/battery-inside-en/en/tech-en/game-changer-battery-lighter-weight-and-longer-lasting-lithium-sultur-battery.md
confidence: high
---
# Lithium-Sulfur Battery

## Overview

Lithium-sulfur (Li-S) batteries represent a transformative chemistry for energy storage, pairing an elemental sulfur cathode with a lithium metal anode. Unlike conventional [[lithium-ion-battery|lithium-ion cells]] that rely on intercalation into metal oxide cathodes, Li-S batteries exploit a conversion reaction that yields a theoretical specific capacity of 1,675 mAh g⁻¹ for sulfur—roughly eight times that of NCM cathodes (~200 mAh g⁻¹). Combined with the lithium metal anode’s theoretical capacity of 3,860 mAh g⁻¹ (compared to 372 mAh g⁻¹ for graphite), the cell-level gravimetric energy density can reach 500–600 Wh kg⁻¹, approximately 1.5–2 times higher than today’s best lithium-ion batteries.

This exceptional weight-to-energy ratio makes Li-S a prime candidate for applications where mass is the overriding constraint: electric aviation, drones, [[uam-battery|Urban Air Mobility (UAM)]], satellites, and lightweight portable electronics. Sulfur is also the 17th most abundant element in Earth’s crust, inexpensive (<$0.10 kg⁻¹ versus >$30 kg⁻¹ for cobalt or nickel), and non-toxic, offering a path to lower-cost, more sustainable battery systems. However, the chemistry faces well-documented hurdles—chiefly the polysulfide shuttle effect, low sulfur conductivity, and lithium anode instability—that have so far limited cycle life to a few hundred cycles. Research by companies like LG Energy Solution (LGES) is steadily overcoming these challenges through advanced electrolyte design, carbon–sulfur composites, and pressure management, pushing Li-S toward commercial readiness.

## Technical Details

### Electrochemical Mechanism

During discharge, solid sulfur (S₈) at the cathode is reduced in a multi-step conversion sequence:

S₈ → Li₂S₈ → Li₂S₆ → Li₂S₄ → Li₂S₂ → Li₂S

The first stages generate long-chain lithium polysulfides (Li₂Sₓ, 4≤x≤8) that are soluble in typical organic electrolytes. As discharge proceeds, shorter-chain polysulfides (Li₂Sₓ, 2≤x≤4) form, and finally insoluble Li₂S precipitates. The theoretical capacity of 1,675 mAh g⁻¹ corresponds to the full two-electron conversion per sulfur atom. On charge, the reverse reaction occurs, regenerating sulfur.

### The Polysulfide Shuttle

The soluble long-chain polysulfides (especially Li₂S₈ and Li₂S₆) can diffuse through the electrolyte toward the lithium anode. At the anode, they are chemically reduced to shorter polysulfides, which then diffuse back to the cathode and are re-oxidized. This parasitic “shuttle” causes capacity fade, self-discharge, low coulombic efficiency, and rapid degradation of the lithium anode. Mitigation strategies include:

- **Electrolyte modification**: Using sparingly solvating electrolytes or mixtures with high donor numbers to reduce polysulfide solubility; adding LiNO₃ to form a protective passivation layer on the lithium anode.
- **Cathode architecture**: Encapsulating sulfur in porous carbon hosts (e.g., mesoporous carbon, carbon nanotubes, graphene) to physically confine polysulfides and provide electronic pathways.
- **Interlayers and separators**: Placing functional coatings (e.g., carbon, metal oxides, or polymers) on the separator to block polysulfide crossover.

### Low Conductivity and Volume Changes

Elemental sulfur has an electrical conductivity of ~5 × 10⁻³⁰ S cm⁻¹, requiring a substantial fraction of conductive carbon (typically 20–30 wt%) in the cathode. The conversion also involves a ~80% volume expansion upon full lithiation (S₈ to Li₂S), stressing the electrode structure. Advanced composite cathodes—such as sulfur–carbon nanotube mixtures or sulfur-impregnated porous carbons—mitigate both issues by providing intimate electron transport and accommodating swelling.

### Lithium Metal Anode Challenges

The lithium metal anode is essential for high energy density but suffers from dendritic electrodeposition, infinite volume change, and continuous solid–electrolyte interphase (SEI) formation. These lead to short circuits, low coulombic efficiency, and eventual cell failure. Solutions under development include:

- High-modulus artificial SEI layers (e.g., Li₃N, LiF, or polymer composites).
- 3D porous lithium hosts (e.g., carbon foam or copper mesh) to distribute plating/stripping.
- Pressure cells that apply external force to suppress dendrite growth and maintain contact.
- Electrolyte additives (e.g., LiNO₃, fluoroethylene carbonate) that promote stable SEI.

### LG Energy Solution’s Development

Since 2013, LGES’s Future Technology Center—co-located at LG Science Park in Seoul—has been a major industrial contributor to Li‑S R&D. The company focuses on pouch-type cells to maximize the weight benefit (avoiding heavy metal cans) and to manage the anode volume changes through controlled pressure. Key innovations include:

- **Specialized carbon–sulfur composites** that achieve >80% sulfur utilization and loadings up to 5 mg S cm⁻².
- **Novel electrolytes** with ether-based solvents and dual-salt systems (LiTFSI + LiNO₃) that suppress polysulfide dissolution and stabilize the lithium anode.
- **Pressure management technology** that maintains a uniform stack pressure of ~0.5–1 MPa, extending cycle life beyond 300 cycles while retaining >80% capacity.
- **Prototype cells** achieving 500 Wh kg⁻¹ at the cell level, with a path toward 600 Wh kg⁻¹ by 2028.

LGES targets aviation, drones, and UAM as initial market entries, where premium energy density outweighs cycle life constraints. The company also explores hybrid configurations (e.g., Li‑S + supercapacitor) for pulse-power applications like take‑off and landing.

## Market Significance

Li‑S batteries fill a unique niche in the next-gen battery landscape. Compared to [[solid-state-battery|all-solid-state batteries]], Li‑S offers practical energy densities that are already higher and at lower cost, though cycle life is lower. Versus [[sodium-ion-battery|sodium-ion]], Li‑S has a 3× energy density advantage but trades cost and sustainability. For [[next-gen-battery-overview|next-generation batteries]], Li‑S is the leading candidate for weight-critical aerospace applications where 500–600 Wh kg⁻¹ is achievable by 2030.

The global market for Li‑S is projected to exceed $2B by 2030, driven by eVTOL (electric vertical take‑off and landing) aircraft, high‑altitude pseudo‑satellites (HAPS), and military unmanned systems. In these sectors, batteries account for 20–40% of vehicle weight, and every kilogram of battery saved translates directly into increased payload or range. For example, a 10% reduction in battery mass in a UAM aircraft can increase range by 8–12%.

Challenges remain: achieving >500 cycles for aviation certification, scaling manufacturing from lab to pilot lines, and managing the safety of lithium metal anodes in abusive conditions. However, with sustained investment—LGES alone has filed over 400 Li‑S patents—and cross‑industry collaboration, these barriers are progressively being overcome. The first commercial Li‑S cells are expected to enter the UAM market around 2027–2028, with wider adoption in consumer drones and defense applications soon after.

## Related Pages

- [[lithium-metal-battery|Lithium Metal Battery]]
- [[uam-battery|Batteries for UAM]]
- [[solid-state-battery|All-Solid-State Battery]]
- [[next-gen-battery-overview|Next-Generation Battery Comprehensive Comparison]]
- [[sodium-ion-battery|Sodium-ion Battery]]
- Polysulfide Shuttle Effect
- Energy Density in Batteries
- [[lithium-ion-battery|Lithium-Ion Battery]]
