---
title: Active Material
created: 2026-06-05
updated: 2026-06-08
type: concept
tags: [active-material, cathode, anode, electrode]
sources:
  - raw/battery-inside-en/en/tech-en/infographics-22-slurry-components-and-their-roles-active-material-conductive-additive-and-binder.md
  - raw/battery-inside-en/en/tech-en/battery-glossary-active-materials.md
  - raw/battery-inside-en/en/tech-en/infographics-16-wet-electrode-process-dry-electrode-process.md
  - raw/battery-inside-en/en/tech-en/the-next-generation-anode-material-silicon.md
  - raw/battery-inside-en/en/tech-en/infographics-12-anode.md
confidence: high
---
# Active Material

## Overview

Active material is the electrochemically active powder in a battery electrode that directly participates in the charge–discharge reactions storing and releasing electrical energy. It is the substance that actually generates electric energy inside the cell. Every lithium-ion battery contains two types of active material: **cathode active material** and **anode active material**. Without active material, there would be no electrochemical energy storage—all other electrode components (binder, conductive additive, current collector) exist solely to support the active material's function.

## Technical Details

### Cathode Active Materials

Cathode active materials hold lithium ions and release them to the anode during charging, then accept them back during discharge. They largely determine a battery's voltage, capacity, and thermal behavior. Each chemistry offers a distinct trade-off among energy density, power capability, cost, and safety.

- **LCO (lithium cobalt oxide, LiCoO₂)** – The first commercial cathode; delivers high volumetric energy density (~550 Wh/L) and a practical capacity of ~140–160 mAh/g. Its layered structure allows stable lithium intercalation, but cobalt's high cost and thermal runaway risk above ~200 °C limit it to consumer electronics.
- **LMO (lithium manganese oxide, LiMn₂O₄)** – A spinel structure providing good safety and lower cost, with a capacity of ~120 mAh/g. Manganese dissolution at elevated temperatures reduces cycle life, so LMO is often blended with NCM to improve stability.
- **NCM (nickel‑cobalt‑manganese, LiNiₓCoᵧMn₁₋ₓ₋ᵧO₂)** – The dominant chemistry for EVs. Increasing nickel content (modern formulations exceed 80 % Ni) boosts specific capacity to 180–220 mAh/g while reducing cobalt for cost and ethical reasons. The trade‑off is increased reactivity and need for advanced electrolyte additives.
- **NCA (nickel‑cobalt‑aluminum, LiNiₓCoᵧAl₁₋ₓ₋ᵧO₂)** – Similar to NCM; used extensively in Tesla and other EV cells. Capacity ~200 mAh/g; the aluminum dopant improves structural stability at high voltage.
- **LFP (lithium iron phosphate, LiFePO₄)** – An olivine structure with a flat voltage plateau at 3.2‑3.3 V. Capacity is moderate (~160 mAh/g), but it offers exceptional thermal stability (decomposition >500 °C), long cycle life (2000+ cycles), and no cobalt. Now widely adopted for entry‑level EVs and energy storage systems.

The choice of cathode active material sets the fundamental voltage window (3.2–4.2 V), capacity (120–220 mAh/g), and cost envelope of the cell.

### Anode Active Materials

Anode active materials store lithium ions that have moved from the cathode during charging and release them during discharge. Their ability to repeatedly accept and release lithium ions determines cycle life and fast‑charging capability.

- **Graphite** (natural and synthetic) is the most widely used anode active material. Its well‑ordered layered structure allows lithium ions to intercalate reversibly between graphene planes. Natural graphite offers high lithium storage capacity at low cost, but its internal structure expands ~10 % during lithiation, which can degrade surface stability. Synthetic graphite is produced by heating carbon precursors above 2,500 °C in a graphitization step, yielding a more ordered structure with longer cycle life. The practical capacity of graphite is ~350–360 mAh/g, close to its theoretical limit of 372 mAh/g.

- **Silicon** is emerging as a next‑generation anode active material because it can alloy with up to **4.4 lithium ions per silicon atom** (vs. 1 Li per 6 carbon atoms in graphite), offering a theoretical capacity of 4,200 mAh/g. However, silicon undergoes **~300 % volume expansion** during lithiation, causing severe mechanical stress, particle pulverization, and continuous solid‑electrolyte interphase (SEI) formation. To mitigate this, silicon is often blended with graphite in small amounts (2–10 wt %) to boost capacity while maintaining structural integrity. Advanced approaches include nanostructured silicon (nanowires, porous particles) and silicon‑graphite composites with tailored binders.

- **Other anodes** under development include lithium titanate (LTO, Li₄Ti₅O₁₂) for high‑power applications (fast charging, long cycle life) and tin‑based alloys for high capacity (theoretical ~993 mAh/g for Sn).

### Role in the Electrode Manufacturing Process

Active material is the primary component of the **slurry** used in electrode manufacturing. The slurry is created by mixing active material with conductive additives, binder, and solvent in precise ratios. This mixture is then coated onto current collectors to form the cathode and anode. The quality and uniformity of the active material distribution directly affects electrode performance—capacity, resistance, adhesion, porosity, and electrolyte wetting behavior.

In the **mixing process**, a pre‑dispersion step is critical. Conductive additives such as carbon black or carbon nanotubes (CNTs) tend to form agglomerates due to strong van der Waals forces. A bead mill is used to break these agglomerates, ensuring active material particles are uniformly surrounded by conductive paths. If agglomerates remain, electrical resistance increases and battery performance degrades. The pre‑dispersion process typically involves mixing the conductive additive, dispersant, and solvent, followed by high‑energy milling with beads. Temperature and mixing speed must be carefully controlled—excessive heat can cause gelation and weaken dispersion, while overly high shear can damage sensitive active material particles.

A newer approach is the **dry electrode process**, where active material, binder (e.g., PTFE), and conductive additive are mixed as a dry powder without solvent. PTFE binder undergoes **fibrillation** under shear—the particles elongate into microfibers that form a continuous network holding the electrode together. This eliminates the need for solvent recovery and drying, reducing manufacturing cost by up to 40 % and enabling thicker, high‑loading electrodes for higher energy density. The dry process also avoids **binder migration** (where binder rises to the surface during drying in wet processes), resulting in a more uniform electrode structure.

## Significance in LG Energy Solution Context

LG Energy Solution prioritizes **responsible supply chain management** to ensure stable sourcing of active materials while meeting ESG commitments. This includes partnerships with mining companies, investment in recycling infrastructure, and development of low‑cobalt and cobalt‑free chemistries (e.g., LFP, NMx). The company's advanced NCM and NCA cathode materials are designed for high nickel content (Ni > 80 %) to maximize energy density in EVs.

For anode active materials, LG Energy Solution is developing **silicon‑graphite composites** and **silicon‑dominant anodes** to boost capacity while managing volume expansion through advanced binders and electrode architectures. The company's use of PTFE in dry electrode processing further enhances the viability of high‑silicon anodes by improving structural stability.

Active material innovation is central to LG’s technology roadmap, enabling improvements in energy density, fast charging, cycle life, and safety across its product lines—from IT cells to electric vehicle batteries and ESS.

## Related Pages

- [[anode-materials|Anode Material]]
- [[binder|Binder]]
- [[cathode-materials|Cathode Material]]
- [[current-collector|Current Collector]]
- [[lithium-ion-battery|Lithium-Ion Battery Structure & Operating Principle]]
- [[silicon-anode|Silicon Anode Material]]
- [[conductive-additive|Conductive Additive (CNT)]]
- [[electrode-process|Electrode Process]]
- [[dry-electrode-process|Dry Electrode Process]]
- [[pre-dispersion|Pre-dispersion Process]]