---
title: Welding Process
created: 2026-06-05
updated: 2026-06-08
type: concept
tags: [welding, current-collector, ctp, thermal-management, safety]
sources:
  - raw/ko/tech/precise-connection-welding-process.md
  - raw/battery-inside-en/en/interview-en/incharge-jeong-hyun-park-of-the-platform-technology-for-welding-team-plans-to-set-global-9f81acd998.md
  - raw/ko/story/incharge-%ea%b8%80%eb%a1%9c%eb%b2%8c-%eb%b0%b0%ed%84%b0%eb%a6%ac-%ec%9a%a9%ec%a0%91-%ed%91%9c%ec%a4%80%ec%9d%84-%eb%a7%8c%eb%93%a4%ea%b8%b0-%ec%9c%84%ed%95%b4-%eb%85%b8%eb%a0%a5%ed%95%98%eb%8a%94.md
  - raw/battery-inside-en/en/news-en/lg-energy-solution-to-pioneer-battery-safety-diagnostics-software-business-exploring-unl-a59e221a94.md
  - raw/battery-inside-en/en/interview-en/incharge-chang-geun-ahn-of-the-environmental-safety-team-establishes-a-safe-infrastructu-a73bceea51.md
confidence: high
---
# Welding Process

## Overview and Introduction

Welding is one of the most critical and technically demanding processes in lithium‑ion battery manufacturing. Every cell, module, and pack depends on dozens to hundreds of precisely welded joints to create low‑resistance electrical pathways, maintain mechanical integrity, and guarantee long‑term safety. A single poor weld can generate a high‑resistance hot spot that wastes energy as heat, reduces cycle life, and creates a thermal runaway risk. In a modern electric vehicle battery pack, thousands of welds must each meet stringent conductivity and strength specifications.

The welding process in battery production encompasses several distinct joining operations: **tab welding** connects the exposed current‑collector foil (tab) to the cell terminal or busbar; **can welding** seals the cell enclosure for cylindrical and prismatic cells; **busbar welding** connects cells in series and parallel within modules and packs; and **module‑to‑pack connections** join module outputs to the pack’s main power terminals. Each operation faces unique material and geometry challenges.

## Technical Details

### Types of Welding Technologies

Three primary welding technologies are used in battery manufacturing, each with distinct advantages and limitations.

**Resistance Welding (Resistance Spot Welding, RSW)** uses electrical current to generate localized heat at the contact interface. Two metal sheets are pressed together between electrodes, and a high‑current pulse (typically several thousand amperes for milliseconds) causes resistive heating that melts the metals at the joint. This method is well‑suited for cylindrical battery can welding, where the negative tab is joined to the bottom of the can. Advantages include fast cycle times, minimal spatter, and suitability for automation. However, it requires high‑power electrical equipment, careful control of pressure and current, and limited non‑destructive inspection capability.

**Ultrasonic Welding** employs high‑frequency mechanical vibrations (typically 20–40 kHz) to create solid‑state bonds without bulk melting. The vibrating horn applies pressure and oscillatory motion, which breaks up surface oxides, generates frictional heat, and induces plastic deformation. This technique is ideal for joining dissimilar metals such as copper and aluminum, and for thin foils (6–20 μm) that would be damaged by high temperatures. Ultrasonic welding is widely used for tab‑to‑terminal connections in pouch cells. It produces no arc, minimal heat‑affected zone (HAZ), and excellent electrical conductivity.

**Laser Welding** uses a focused high‑density beam (typically from fiber or diode lasers) to melt and fuse materials. The beam’s narrow focus allows deep penetration with minimal HAZ, making it suitable for thick busbars and for joining different material thicknesses. Laser welding is non‑contact, so it avoids tool wear and can handle complex geometries. It is increasingly adopted across cell, module, and pack levels—from internal electrode connections to busbar joining and BMS wiring. Challenges include high reflectivity of aluminum and copper, which can damage optics if not managed, and the need for precise beam alignment and shielding gas.

### Material Challenges

Battery welding must join materials with vastly different physical properties. **Aluminum** (cathode) has a melting point of 660 °C, high thermal conductivity, and low electrical resistivity. **Copper** (anode) melts at 1085 °C and has even higher conductivity. When welding these two together, the thermal expansion mismatch can cause residual stress, and the different melting points require careful heat‑input control. The foils themselves are extremely thin—down to 6 μm for the current collector—so excessive heat can easily create burn‑through or weaken the adjacent material. Optimizing parameters (power, duration, pressure, frequency) for each material combination is a core engineering task.

### Quality and Inspection

Weld quality is verified through multiple methods. **Electrical resistance measurement** checks for high‑resistance joints that would cause inefficiency. **Pull testing** measures mechanical strength, while **visual inspection** identifies surface defects. For internal voids or cracks, **ultrasonic inspection (C‑scan)** is used. In production, **real‑time monitoring** of weld parameters—power, duration, displacement, acoustic signature—combined with statistical process control ensures consistent quality. LG Energy Solution is working to establish global battery welding standards through its **InCharge** initiative, aiming to bring the same rigor seen in aerospace and automotive structural welding to the battery industry.

## Significance in LG Context

LG Energy Solution has made welding a strategic focus area. The company operates a dedicated **Welding Core Technology Team** that develops welding mechanisms, solutions, and standards based on battery structure and material characteristics. This team works across all cell form factors—cylindrical, prismatic, and pouch—and collaborates closely with process development for [[cell-to-pack|Cell‑To‑Pack (CTP)]] technology.

In CTP architecture, welding becomes even more critical because individual cells are directly integrated into the pack without module‑level interconnects. This means more welds per pack, tighter positional tolerances, and less redundancy. A failure in a CTP weld cannot be easily repaired by replacing a module. LG Energy Solution has developed advanced techniques for **cell unit loading** and **compression pad bonding** to maintain dimensional stability during CTP assembly. The welding process must also accommodate **thermal resin** application for heat dissipation and **busbar connections** that handle high currents. These innovations reduce the number of process steps by approximately 26 % and investment costs by 19.2 % compared to conventional Module‑to‑Pack (MTP) approaches.

Furthermore, LG is actively working to make its battery welding processes a **global standard**. The company’s welding experts hold leadership positions in IEEE and other international bodies, and they are developing standardized testing and qualification protocols for battery welds—an area that currently lacks industry‑wide norms. This effort is crucial for scaling production safely and ensuring interoperability across the supply chain.

## Related Pages

- [[pack-process|Pack Process]]
- [[cell-to-pack|Cell‑To‑Pack (CTP)]]
- [[tp-prevention|TP Prevention Technology (Thermal Propagation Prevention)]]
- [[assembly-process|Assembly Process]]
- [[azs-stacking|AZS (Advanced Z‑Stacking)]]
- [[battery-management-system|BMS (Battery Management System)]]
- [[current-collector|Current Collector]]