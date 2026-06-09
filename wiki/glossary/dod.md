---
title: DoD (Depth of Discharge)
created: 2026-06-05
updated: 2026-06-08
type: glossary
tags: [soc, cycle-life]
sources:
  - raw/battery-inside-en/en/tech-en/battery-glossary-dod-depth-of-discharge.md
  - raw/ko/tech/%eb%b0%b0%ed%84%b0%eb%a6%ac-%ec%9a%a9%ec%96%b4%ec%82%ac%ec%a0%84-dod-depth-of-discharge.md
  - raw/battery-inside-en/en/tech-en/battery-glossary-soc.md
  - raw/ko/tech/%eb%b0%b0%ed%84%b0%eb%a6%ac-%ec%9a%a9%ec%96%b4%ec%82%ac%ec%a0%84-soc-state-of-charge.md
  - raw/battery-inside-en/en/tech-en/battery-glossary-coulombic-efficiency-ce.md
confidence: high
---
# DoD (Depth of Discharge)

## Overview / Introduction

Depth of Discharge (DoD) is a fundamental metric that quantifies how much of a battery's rated capacity has been discharged at a given point in a cycle. Expressed as a percentage, it is the complement of [[soc|State of Charge (SoC)]]: DoD (%) = 100% – SoC (%). For example, a battery at 70% SoC has a DoD of 30%, meaning 30% of its total capacity has been drained. While SoC tells users what remains, DoD focuses on what has been consumed — and that consumption depth directly governs the electrochemical stress that drives capacity fade and cycle life.

In the LG Energy Solution ecosystem, DoD is not merely a readout; it is a key input into the [[sox|State of X (SoX)]] framework, influencing BMS logic, warranty terms, and application-level optimization. Understanding DoD is essential for anyone designing, operating, or maintaining lithium-ion battery systems, from consumer electronics to electric vehicles (EVs) and grid-scale [[energy-storage-system|Energy Storage Systems (ESS)]].

## Technical Details

### DoD and Cycle Life: The Inverse Relationship

The single most important relationship in battery aging is the inverse proportionality between DoD and cycle life. Deeper discharges impose greater physical and chemical strain on the electrode materials. During lithiation and delithiation, the active particles in the anode (typically graphite) and cathode (e.g., NMC, LFP) undergo volumetric expansion and contraction. At high DoD (e.g., 100%), the electrode is cycled through its full expansion range, which accelerates particle cracking, loss of electrical contact, and exposure of fresh surfaces to the electrolyte. This, in turn, promotes continual growth of the solid electrolyte interphase (SEI) on the anode, consuming cyclable lithium and increasing cell resistance.

Quantitatively, a typical lithium-ion cell rated for 3,000 cycles at 80% DoD may deliver 6,000 cycles at 40% DoD and over 10,000 cycles at 20% DoD. This is because the cumulative charge throughput (total energy delivered over life) often increases at moderate DoDs, even though the per-cycle energy decreases. The relationship is not strictly linear; rather, it follows a power-law or exponential model often parameterized in stress-factor models (SFM) as described in LG’s technical literature. The SFM combines cycle count, time, temperature, and DoD into a degradation function: `f = (N/N_ref)^α * (D/D_ref)^β * exp(γ*(T - T_ref))`, where `α`, `β`, `γ` are empirical coefficients.

### Mechanisms of Damage at High DoD

At the electrode level, deep discharge (low SoC) drives the cathode to a lithium-deficient state, which can destabilize its crystal structure, especially in layered oxides. Simultaneously, the anode experiences near-complete delithiation, causing severe contraction of graphite layers. These repeated mechanical stresses lead to microcracking and loss of active material. Additionally, during deep discharge, cell voltage can drop close to the cutoff limit, increasing the risk of copper dissolution from the anode current collector if the BMS fails. The electrolyte decomposition rates also accelerate at extreme potentials, further degrading performance.

### Relationship with Temperature and C-rate

DoD’s effect is further modulated by temperature and charge/discharge rate. At elevated temperatures, the SEI growth rate increases, and high DoD cycles cause faster capacity fade. In LG’s thermal chemistry studies, a cell cycled at 80% DoD and 45°C can lose 20% capacity in half the cycles compared to the same DoD at 25°C. Similarly, high C-rates (fast charging/discharging) compound the stress because diffusion limitations create lithium concentration gradients that amplify mechanical strain. Therefore, optimal battery life is achieved by *simultaneously* limiting DoD, temperature, and charge rates.

### Practical Implications for Usage

For consumer devices, the recommendation is clear: frequent top-up charging (shallow DoD) extends battery life far better than full discharge followed by full charge. This is why many manufacturers guide users to keep lithium-ion batteries between 20% and 80% SoC (i.e., 80% DoD down to 20% DoD). In EVs, the BMS typically implements a “buffer” zone at both extremes — for example, the usable SoC window might be 10–90% even though the actual cell chemistry could go to 0–100%. This buffer effectively limits DoD and protects cycle life.

### DoD in BMS and SoX Framework

Modern BMS, including LG’s [[battery-management-system|BMTS (B.around Total Solution)]], continuously estimate DoD using coulomb counting and state estimation algorithms. DoD is not directly measured but derived from SoC. The BMS uses DoD in real time to calculate remaining cycle life, adjust power limits ([[sox|SoP]]), and trigger cell balancing. DoD also feeds into State of Health ([[sox|SoH]]) models: a battery that has accumulated many deep-discharge cycles will show a faster decline in SoH, which can be predicted by the BMS.

## Significance and LG Energy Solution Context

DoD is a crucial parameter in warranty specifications. LG Energy Solution guarantees a minimum number of cycles at a defined DoD — for instance, typical ESS products are warranted for 10,000 cycles at 90% DoD or 15,000 cycles at 70% DoD. This reflects the trade-off between energy throughput per cycle and total lifetime energy delivered. In ESS, the economic value (levelized cost of storage) depends on optimizing DoD to maximize revenue from energy arbitrage while preserving battery longevity.

LG’s EMO (Energy Market Optimizer) platform takes DoD management a step further. It computes the Dynamic Marketable Energy (DME) — the amount of energy that can be safely sold to the market — based on real-time SoC, temperature, and battery degradation models that explicitly account for DoD. By avoiding deep discharges that would accelerate fade, EMO balances short-term profit with long-term system health. This is a key differentiator in LG’s AEROS™ software suite.

In EVs, LG’s BMS uses DoD as an input for adaptive charging strategies. For example, during DC fast charging, the system may lower the maximum allowable DoD to limit thermal and mechanical stress, especially in high-energy-density cells with NCM cathodes. This extends pack life without compromising usable range.

## Related Pages

- [[soc|SoC (State of Charge)]]
- [[sox|SoX (State of X) Framework]]
- [[battery-management-system|BMS (Battery Management System)]]
- [[bmts|BMTS (B.around Total Solution)]]
- [[energy-storage-system|ESS (Energy Storage System)]]
- [[anode-materials|Anode Materials]]
- [[coulombic-efficiency|Coulombic Efficiency (CE)]]