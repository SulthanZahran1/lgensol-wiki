---
title: Potential Window
created: 2026-06-05
updated: 2026-06-08
type: glossary
tags: [voltage, electrolyte, energy-density]
sources:
  - raw/corporate/de/pages/career-career-recruit-overseas.md
  - raw/ko/tech/%eb%b0%b0%ed%84%b0%eb%a6%ac-%ec%9a%a9%ec%96%b4%ec%82%ac%ec%a0%84-%ec%a0%84%ec%9c%84%ec%b0%bd-potential-window.md
  - raw/battery-inside-en/en/tech-en/game-changer-battery-high-voltage-mid-nickel-batteries-securing-both-energy-density-and-ea70153231.md
  - raw/battery-inside-en/en/tech-en/a-better-life-with-batteries-the-electrolyte-additives-for-ev-batteries.md
  - raw/battery-inside-en/en/tech-en/a-better-life-with-batteries-solid-electrolyte.md
confidence: high
---
# Potential Window

## Overview / Introduction

The **potential window** (also called the electrochemical stability window) defines the voltage range over which a battery electrolyte remains electrochemically stable—neither oxidized at the cathode nor reduced at the anode. It is a fundamental constraint in lithium-ion battery design: operating within this window preserves electrolyte integrity and cell performance, while exceeding it triggers parasitic decomposition reactions that degrade capacity, generate gas, and shorten cycle life.

For commercial lithium-ion batteries using carbonate-based electrolytes (e.g., EC, DMC, EMC, DEC), the practical potential window is approximately **4.2–4.3 V** vs. Li/Li⁺. This relatively narrow window limits the maximum operating voltage—and thus the achievable energy density—of conventional cells. Pushing beyond 4.3 V requires advanced electrolytes, electrode coatings, or protective interphases that kinetically inhibit decomposition even though the thermodynamic stability limit has been surpassed.

## Technical Details

### The two limits of the potential window

The potential window is bounded by two characteristic potentials:

- **Oxidation potential (anodic limit):** The voltage at which the electrolyte begins to lose electrons and undergo oxidation at the cathode surface. This sets the *upper* voltage boundary.
- **Reduction potential (cathodic limit):** The voltage at which the electrolyte begins to gain electrons and undergo reduction at the anode surface. This sets the *lower* voltage boundary.

Both limits are measured in volts (V) relative to a reference electrode, typically Li/Li⁺. The window width is the difference between these two values, but in a full cell the anode potential varies during cycling, so the practical window is often narrower than the thermodynamic limits.

### Consequences of exceeding the window

When cell voltage surpasses the anodic limit, the electrolyte oxidizes at the cathode. Carbonate solvents decompose to produce gases such as **CO₂ and CO**, which accumulate inside the cell, increasing internal pressure and causing **swelling** (physical bulging). Simultaneously, parasitic oxidation drives the formation and continuous growth of the **[[cei|CEI]] (Cathode Electrolyte Interphase)**—a solid layer on the cathode surface. While a thin, stable CEI can protect the cathode, excessive growth creates a thick, resistive barrier that increases internal resistance and accelerates capacity fade.

On the anode side, reduction of the electrolyte below the cathodic limit leads to excessive growth of the **[[sei|SEI]] (Solid Electrolyte Interphase)**. The SEI normally forms during the first charge and acts as a protective film that allows Li⁺ transport while blocking further electrolyte reduction. However, when the potential window is violated, the SEI grows uncontrollably, consuming lithium and electrolyte, raising impedance, and contributing to swelling via hydrocarbon gas generation (e.g., methane, ethane).

Additionally, transition metals (Ni, Mn, Co) from the cathode can dissolve into the electrolyte, especially under high-voltage stress. These metal ions migrate to the anode, deposit there, and catalyze further SEI breakdown—a feedback loop that progressively destroys cell performance.

### Factors influencing the effective window

The potential window is not a fixed material property. It depends on:

- **Electrolyte composition** – solvents (carbonates vs. novel structures), lithium salts (LiPF₆, LiFSI, etc.), and additives (VC, PS, FEC).
- **Electrode materials** – the catalytic activity of cathode surfaces (e.g., NCM vs. LFP) and the anode (graphite vs. silicon) shifts decomposition onset potentials.
- **Temperature** – higher temperatures accelerate decomposition kinetics, effectively narrowing the stable window.
- **Interphase formation** – additive-derived SEI/CEI layers can *extend* the effective window by passivating the electrode surfaces. For example, vinylene carbonate (VC) forms a robust SEI that suppresses further reduction, while certain cathode coatings inhibit oxidation.

Modern electrolyte engineering uses **functional additives** (0.5–5 wt%) to create protective interphases that push the practical operating voltage well beyond the thermodynamic limit—often to 4.4 V, 4.5 V, or higher.

## Significance / LG Energy Solution Context

Widening the potential window is a direct route to **higher energy density**. Battery energy (Wh) = capacity (Ah) × operating voltage (V). For a cell with a given capacity, increasing the voltage yields more stored energy without increasing volume or weight. This is why high-voltage designs are a strategic priority for automakers and battery makers alike.

**LG Energy Solution**’s development of [[gas-free-solvent|Gas Free Solvent]] technology exemplifies this pursuit. Conventional carbonate solvents inherently contain carbonate groups that readily decompose into CO₂ or CO. LG’s approach is to **redesign the solvent molecule** from the ground up—moving away from carbonate structures to a new architecture inspired by the LiFSI anion. This novel solvent exhibits superior oxidation stability while simultaneously forming a durable SEI that resists gas evolution. The goal is to maintain long-term stability at elevated voltages (≥4.4 V) with minimal gas generation.

The company’s [[mid-nickel-battery|High-Voltage Mid-Nickel Battery]] program directly relies on an extended potential window. By combining a mid‑nickel cathode (e.g., NCM613, with 60% Ni, 10% Co, 30% Mn) with single-crystal cathode particles, LG achieves operation at 4.4–4.5 V while avoiding microcracking and excessive CEI growth. This yields an energy density of ~670 Wh/L, with cell safety improved by over 30% and cost reduced by about 8% compared to high‑nickel alternatives.

Furthermore, LG’s [[bipolar-technology|Bipolar Technology]] and next-generation [[solid-state-battery|all-solid-state batteries]] also demand a stable potential window at high voltages (often >4.5 V for solid electrolytes). Understanding and engineering this window is therefore central to LG’s roadmap for cell voltage escalation, from 4.2 V legacy cells toward 4.5 V+ high‑energy systems.

## Related Pages

- [[gas-free-solvent|Gas Free Solvent]]
- [[mid-nickel-battery|High-Voltage Mid-Nickel Battery]]
- [[bipolar-technology|Bipolar Technology]]
- [[solid-state-battery|All-Solid-State Battery]]
- [[sei|SEI (Solid Electrolyte Interphase)]]
- [[cei|CEI (Cathode Electrolyte Interphase)]]