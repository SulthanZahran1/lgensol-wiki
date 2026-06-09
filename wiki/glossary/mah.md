---
title: mAh (milliampere-hour)
created: 2026-06-05
updated: 2026-06-08
type: glossary
tags: [energy-density, voltage]
sources:
  - raw/battery-inside-en/en/tech-en/battery-glossary-mah-milliampere-hour.md
  - raw/battery-inside-en/en/tech-en/game-changer-battery-high-voltage-mid-nickel-batteries-securing-both-energy-density-and-ea70153231.md
  - raw/ko/tech/%eb%b0%b0%ed%84%b0%eb%a6%ac-%ec%9a%a9%ec%96%b4%ec%82%ac%ec%a0%84-mah-milliampere-hour.md
  - raw/battery-inside-en/en/tech-en/a-better-life-with-batteries-lithium-manganese-rich-batteries-with-high-energy-density-s-7fe5607452.md
  - raw/lg-ess-battery/en/pages/eu-grid-news-view-lg.md
confidence: high
---
# mAh (milliampere-hour)

## Overview / Introduction

mAh (milliampere-hour) is a unit of electrical charge capacity, representing the amount of charge transferred by a steady current of one milliampere flowing for one hour. It is the most widely used metric for specifying the capacity of small to medium-sized batteries—smartphones, power banks, laptops, and portable electronics. One thousand mAh equals one ampere-hour (Ah). While mAh provides a convenient measure of charge-holding capability, it must be interpreted together with operating voltage to understand actual energy content. For example, a 3,000 mAh cell at 3.7 V stores 11.1 Wh, whereas the same mAh rating at 7.4 V yields 22.2 Wh. This distinction is critical when comparing batteries of different chemistries or configurations, especially as cell voltages rise in next-generation designs such as LG Energy Solution’s high-voltage mid-nickel batteries.

## Technical Details

The mAh rating indicates the total charge a battery can deliver under specified discharge conditions. In theory, a 3,000 mAh battery can supply 3,000 mA (3 A) for one hour, 1,500 mA for two hours, or 300 mA for ten hours before reaching its discharge cutoff voltage. However, practical runtime depends on discharge rate, temperature, and internal resistance. The fundamental relationship between capacity and energy is:

**Energy (Wh) = Capacity (Ah) × Voltage (V)**.

Thus, mAh alone does not capture energy density. To compare batteries of different voltages, engineers use Wh or specific energy (Wh/kg). For instance, a high-voltage mid-nickel battery (e.g., NCM613 with 3.7 V nominal) can achieve 670 Wh/L while offering improved safety and cost, as described in LG Energy Solution’s mid-nickel roadmap.

In real-world use, **usable capacity** is always less than the rated value due to several factors:

- **C‑rate dependence**: Higher discharge currents increase ohmic losses (I²R heating) and cause the voltage to drop faster to the cutoff, reducing delivered capacity. At low temperatures, electrolyte conductivity decreases, further limiting extractable charge.
- **Internal resistance**: Increases with aging and cycling; the voltage drop across the internal resistance reduces the available terminal voltage, forcing earlier cutoff.
- **Voltage cutoff**: The battery management system (BMS) stops discharge before complete depletion to protect cell health, leaving a safety margin. This margin is typically several percent of the rated mAh.
- **Coulombic inefficiency**: During charge-discharge cycles, side reactions (e.g., electrolyte decomposition, SEI growth) consume some charge, reducing the fraction that can be recovered. This is quantified by **Coulombic Efficiency (CE)** , typically >99 % for lithium‑ion cells, but lower initial CE (ICE) occurs during formation. LG’s BMTS platform (B.around) continuously tracks capacity retention as a key health indicator using AI‑driven diagnostics.

The **potential window** of the electrolyte (typically 4.2–4.3 V for Li‑ion) sets an upper bound on operating voltage. Exceeding this window causes electrolyte oxidation at the cathode (forming CEI) or reduction at the anode (thickening SEI), accelerating capacity fade. This is why mAh ratings are always specified at a defined voltage range (e.g., 3.0–4.2 V). Operating outside this window not only reduces usable mAh but also damages the cell.

**Example calculation**: A 10,000 mAh power bank (3.7 V) has an energy capacity of 37 Wh. Charging a smartphone with a 3,000 mAh cell (3.7 V) would theoretically yield about 3.3 full charges, but due to conversion losses (typically 80–90 % efficiency in the power bank’s DC‑DC converter and USB cable resistance), the practical number is closer to 2.5–3 charges. This conversion loss is a well-known consumer electronics issue and is one reason why OEMs like LG Energy Solution emphasize energy density (Wh/L) over raw mAh when evaluating cell performance.

## Significance / LG Energy Solution Context

Understanding mAh is essential for both consumers and battery engineers. For consumers, it allows comparison of power bank capacity and estimation of daily charging needs. For engineers, mAh is the fundamental unit for **Coulombic Efficiency** calculations, cycle‑life testing, and cell matching for pack assembly. In lithium‑ion cells, CE is calculated as (Discharge mAh) / (Charge mAh) × 100 %. A CE near 100 % indicates highly reversible chemistry; deviations signal parasitic side reactions that degrade capacity over time. LG’s high‑voltage mid‑nickel batteries (NCM613) exhibit excellent CE due to single‑crystal cathode technology, which minimizes particle cracking and electrolyte decomposition.

At LG Energy Solution, mAh is the unit for capacity specification across all product lines—from small coin cells used in R&D to large‑format prismatic and cylindrical cells for EVs and ESS. For example, the **46‑Series Cylindrical Battery (4680/4695)** and **mid‑nickel NCM613** cells are rated in Ah (thousands of mAh) with voltage‑dependent energy densities. The company’s **B.around (BMTS)** platform leverages continuous capacity (mAh) measurements from field data to estimate State of Health (SoH) with <2 % error. AI algorithms such as MAVD, RdV, and dSOH analyze capacity fade patterns to predict remaining useful life. This data‑driven approach is critical for optimizing battery performance in applications ranging from SDV (Software‑Defined Vehicles) to stationary ESS.

**Key relationships**:

- **Energy density = Voltage × Capacity / Weight or Volume** → explains why high‑voltage mid‑nickel batteries (≈3.7 V) can rival high‑nickel chemistries despite lower mAh per gram. LG’s mid‑nickel road map targets 670 Wh/L by 2025.
- **Coulombic Efficiency** = (Discharge mAh) / (Charge mAh) × 100 % → a key metric for assessing reversibility and aging. First‑cycle ICE is particularly important for evaluating new materials.
- **Potential window** defines the safe voltage range within which mAh capacity can be fully utilized without degradation. LG’s NCM613 operates within a 3.0–4.2 V window, balancing energy and longevity.

## Related Pages

- [[coulombic-efficiency|Coulombic Efficiency (CE)]]
- [[potential-window|Potential Window]]
- [[bmts|BMTS (B.around Total Solution)]]
- [[mid-nickel-battery|High-Voltage Mid-Nickel Battery]]
- [[46-series-battery|46-Series Cylindrical Battery (4680/4695)]]
- [[coin-cell|Coin-Cell Battery]]
- [[ncm-battery|NCM (Ternary) Battery]]