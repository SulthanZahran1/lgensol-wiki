---
title: Cell-To-Pack (CTP)
created: 2026-06-05
updated: 2026-06-08
type: concept
tags: [ctp, thermal-management, energy-density, pouch]
sources:
  - raw/battery-inside-en/en/interview-en/lg-energy-solution-innovates-pouch-type-batteries-with-the-cell-to-pack-process.md
  - raw/battery-inside-en/en/tech-en/game-changer-battery-innovative-cell-to-pack-technology-that-eliminates-modules.md
  - raw/battery-inside-en/en/tech-en/battery-glossary-cell-to-pack.md
  - raw/ko/tech/game-changer-battery-%eb%aa%a8%eb%93%88%ed%99%94-%ea%b3%bc%ec%a0%95%ec%9d%84-%ec%97%86%ec%95%a4-%ed%98%81%ec%8b%a0%ec%a0%81%ec%9d%b8-%ec%85%80%ed%88%ac%ed%8c%a9cell-to-pack-%ea%b3%b5.md
  - raw/battery-inside-en/en/interview-en/incharge-areum-lee-of-the-pouch-type-big-data-team-manages-the-quality-of-pouch-type-bat-250b116575.md
confidence: high
---
# Cell-To-Pack (CTP)

## Overview / Introduction

Cell-to-Pack (CTP) is a battery pack architecture that eliminates the conventional module assembly step, integrating cells directly into the pack enclosure. In traditional Module-to-Pack (MTP) design, cells are grouped into modules—each with its own frame, cooling plates, wiring harnesses, and busbars—and then multiple modules are assembled into a pack. This modular approach consumes significant volume and mass: module frames alone can account for 10–20% of total pack weight, and space utilization (the fraction of pack interior occupied by active cell volume) is typically only 40–50%. CTP removes the module layer entirely, boosting pack-level energy density by 10–20% and improving space utilization to 65–72% by replacing module structural components with additional cells.

The concept is chemistry- and form-factor-neutral and has been adopted by multiple manufacturers. BYD’s Blade Battery employs CTP with LFP prismatic cells, while Tesla’s structural battery pack uses CTP with 4680 cylindrical cells bonded with structural adhesive. LG Energy Solution demonstrated one of the first CTP implementations specifically for pouch cells, leveraging its Advanced Z-Stacking (AZS) technology and comprehensive battery management system (BMS) platform to achieve high energy density and safety.

## Technical Details

### Architecture and Process

LG Energy Solution’s pouch-based CTP process begins by arranging one or more stacked pouch cells in a precise array. Compression pads are attached to the sides of each cell to maintain uniform spacing and absorb swelling over the battery’s lifetime. The cells are then electrically connected via busbars, and a protective cell cover is applied to form a **cell unit**—a subassembly that provides structural integrity and protects the pouch cells from external shock. These cell units are loaded into the pack housing, which has been pre-coated with a thermally conductive resin (thermal resin) to enhance heat transfer from the cell bottoms to the pack floor. The final step integrates the BMS (Battery Management System) to monitor voltage, temperature, and current across the entire pack.

This process reduces the number of process steps by approximately 26% compared to MTP, and investment costs by 19.2%. A key enabling innovation is the **cell unit loading** process: vacuum suction adsorbs the cell stack, and a robot presses the entire block into the pack housing while maintaining dimensional accuracy. Without modules to hold cells in place, precise alignment and compression are critical to prevent misalignment and internal shorts.

### Space Utilization and Energy Density

CTP’s primary advantage is packing more active material into the same footprint. In MTP, the module frame, wiring harnesses, and internal cooling plates consume approximately 50–60% of the pack volume (space utilization 40–50%). CTP raises that to 65–72%—a 30–50% relative improvement. For LFP cells, which have inherently lower cell-level energy density (about 160 Wh/kg for LFP vs. 250–300 Wh/kg for NCM), CTP can make LFP packs competitive with mid-range NCM packs on a system level. LG Energy Solution’s pouch CTP achieves approximately 5% higher gravimetric energy density than an equivalent prismatic CTP design, because pouch cells have no rigid metal casing and dead space is minimized during stacking.

### Thermal Management and Safety

Removing the module layer eliminates the dedicated cooling plates that are often integrated within each module. In CTP, thermal management relies on the pack-level cooling system. LG applies a thermal resin between the cell units and the pack case bottom, increasing the heat transfer coefficient significantly. The resin also provides mechanical bonding and vibration damping. For safety, LG has validated its thermal propagation prevention solutions to ensure that a single cell failure does not cascade through the tightly packed cells. The combination of compression pads, cell covers, and resin helps contain any thermal event and delays propagation for several minutes, allowing the vehicle’s safety systems to respond.

### Serviceability and Manufacturing Challenges

A notable trade-off of CTP is reduced serviceability. In MTP, a faulty module can be replaced without disturbing the entire pack; in CTP, individual cells cannot be easily accessed. The entire pack must be replaced if a critical failure occurs. This places higher reliability demands on the cells, welding, and BMS. From a manufacturing standpoint, maintaining tight dimensional tolerances for hundreds or thousands of cells loaded directly into the pack requires advanced automation, precise compression fixtures, and robust alignment verification—all of which LG has addressed in its pilot lines and production scale-up.

## Significance and LG Energy Solution Context

LG Energy Solution publicly demonstrated its pouch-type CTP technology for the first time at InterBattery 2024 in Seoul. The company positioned CTP as a key enabler for its emerging LFP product line, which targets entry-level electric vehicles (EVs) and stationary energy storage (ESS). In July 2024, LG signed a major contract with Renault’s EV division, Ampere, to supply approximately 39 GWh of pouch LFP cells with CTP from 2025 to 2030—the first large-scale LFP supply deal by a Korean battery maker. The cells are to be produced at LG’s plant in Poland and will power Renault’s next-generation EVs.

LG’s CTP design is tightly integrated with its Advanced Z-Stacking (AZS) technology, which aligns multiple pouch electrodes precisely to maximize packing density and minimize dead space. The pack-level BMS, part of the Battery Management Total Solution (BMTS) platform, monitors every cell unit individually and employs advanced algorithms for state-of-charge estimation and cell balancing. This holistic approach—cell design, stacking, pack assembly, and intelligent management—allows LG to deliver a CTP solution that is both cost-competitive and safe.

The significance of LG’s CTP extends beyond passenger EVs. Its high space utilization makes it attractive for commercial vehicles (e.g., electric trucks) and ESS applications where floor space is limited. LG has also applied CTP to 46-series cylindrical cells (4680/4695) in its structural battery pack developments, though the pouch CTP remains the company’s flagship offering due to its lighter weight and higher volumetric efficiency.

## Related Pages
- [[azs-stacking|AZS (Advanced Z-Stacking)]]
- [[cell-format-comparison|Cell Form Factor Comparison]]
- [[pack-process|Pack Process]]
- [[welding-process|Welding Process]]
- [[46-series-battery|46-Series Cylindrical Battery]]
- [[energy-storage-system|ESS (Energy Storage System)]]
- [[battery-management-system|BMS (Battery Management System)]]