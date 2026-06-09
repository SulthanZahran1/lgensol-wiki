---
title: Pack Process
created: 2026-06-05
updated: 2026-06-08
type: concept
tags: [ctp, thermal-management, welding, bms, ev]
sources:
  - raw/battery-inside-en/en/interview-en/lg-energy-solution-innovates-pouch-type-batteries-with-the-cell-to-pack-process.md
  - raw/battery-inside-en/en/tech-en/battery-glossary-cell-to-pack.md
  - raw/battery-inside-en/en/tech-en/game-changer-battery-innovative-cell-to-pack-technology-that-eliminates-modules.md
  - raw/ko/tech/game-changer-battery-%eb%aa%a8%eb%93%88%ed%99%94-%ea%b3%bc%ec%a0%95%ec%9d%84-%ec%97%86%ec%95%a4-%ed%98%81%ec%8b%a0%ec%a0%81%ec%9d%b8-%ec%85%80%ed%88%ac%ed%8c%a9cell-to-pack-%ea%b3%b5.md
  - raw/battery-inside-en/en/tech-en/a-better-life-with-batteries-how-to-make-a-battery-step3-pack-process.md
confidence: high
---
# Pack Process

## Overview / Introduction

The pack process is the final assembly stage in battery manufacturing, where individual cells are integrated into a complete system that delivers usable power. While a cell stores electrochemical energy, the pack makes that energy accessible and safe for electric vehicles (EVs), energy storage systems (ESS), and other applications. Pack assembly converts cell-level performance into system-level performance; a well-engineered pack can extract maximum capability from its cells, while poor pack design can negate even the best cell chemistry.

Conventionally, the pack process follows a cell→module→pack (MTP) hierarchy. Cells are first grouped into modules—each with its own frame, cooling plate, and monitoring board—and then multiple modules are assembled into a pack. This modular approach provides mechanical protection, thermal management, and serviceability: a failed module can be replaced without disturbing the entire pack. However, the module layer consumes space and adds cost. LG Energy Solution has pioneered a **cell-to-pack (CTP)** architecture that eliminates the module step, stacking cells directly into the pack enclosure to improve energy density and simplify manufacturing.

## Technical Details

### Conventional Module Assembly (MTP)

In the MTP process, cells are arranged and connected using busbars or wiring harnesses, then inserted into a module frame coated with adhesive. An upper cover seals the module. Modules are grouped, connected in series or parallel to reach the target voltage (typically 400 V or 800 V), and placed into a pack housing. The pack housing integrates structural beams, cooling channels, and high-voltage components such as fuses, contactors, and pre-charge circuits. Finally, the Battery Management System (BMS) is installed for monitoring and control. Module-level assembly enables easier repair and second-life reuse because modules can be swapped individually.

### Cell-to-Pack (CTP) Architecture

CTP bypasses the module layer entirely. The process begins by arraying one or more stacked pouch cells together, attaching compression pads to their sides, connecting them electrically with busbars, and enclosing the group in a cell cover to form a **cell unit**. Thermal resin is applied to the pack case to enhance heat transfer between the cells and the cooling structure. Cell units are placed into the case, and the BMS is mounted on top. By eliminating module frames and interconnects, CTP increases pack-level space utilization from approximately 40–50 % (MTP) to 65–72 %. This directly boosts energy density by 10–20 % and reduces the number of parts, shortening process steps by about 26 % and lowering investment costs by 19.2 %.

### Key Engineering Challenges

- **Structural integrity:** Without module frames, cells must be precisely aligned and dimensionally stable during assembly and in service. LG developed a cell unit loading process using vacuum suction and automated pressing to maintain consistent cell spacing and geometry.
- **Thermal management:** All cells must stay within 15–35 °C under fast charging and high-power discharge. Thermal resin improves cooling efficiency, and CTP packs require careful design of cooling plates and compression pads to prevent hot spots.
- **Safety and thermal runaway propagation:** Denser cell packing demands robust barriers and venting systems. LG’s CTP design integrates thermal propagation prevention technologies, including high-insulation materials and optimized vent channels.
- **BMS integration:** A modern BMS monitors voltage, current, and temperature for every cell or parallel group, performs cell balancing, and diagnoses faults with over 90 % detection accuracy. LG’s BMS uses patented MAVD (Moving Average Voltage Deviation), RdV (Relaxation Deviation Voltage), and dSOH (Delta State of Health) algorithms to detect anomalies early. The system also communicates with vehicle controllers and can interface with cloud-based services like B-Lifecare for remote health monitoring.

## Significance / LG Context

LG Energy Solution was the first in the industry to apply CTP to **pouch cells**. Pouch cells are lightweight and have minimal dead space when stacked, making them ideal for CTP. By combining the inherent advantages of pouch format with CTP’s space-saving approach, LG achieves approximately 5 % higher gravimetric energy density compared to prismatic CTP solutions. This translates into better vehicle range and efficiency.

LG’s CTP pilot line, established in 2024, continuously develops innovations in assembly, welding, resin dispensing, and inspection. The company targets 2025 for mass production of pouch CTP packs. Beyond EVs, CTP is under study for high-energy ESS where space and weight are critical.

The BMS, described in one of LG’s source articles as the “conductor of a choir,” is central to pack quality. LG holds over 8,000 BMS patents and, in 2024, launched BMTS (Battery Management Total Solution), adding AI-driven software for predictive diagnostics and adaptive charging control. In partnership with Qualcomm, LG is commercializing SoC-based BMS hardware that delivers 80 times the computing power of conventional controllers, enabling faster and more accurate state estimation.

## Related Pages

- [[cell-to-pack|Cell-To-Pack (CTP)]]
- [[battery-management-system|BMS (Battery Management System)]]
- [[welding-process|Welding Process]]
- [[assembly-process|Assembly Process]]
- Thermal Management
- [[46-series-battery|46-Series Cylindrical Battery (4680/4695)]]
- [[bmts|BMTS (B.around Total Solution)]]
- [[battery-safety|Battery Safety and Thermal Runaway]]