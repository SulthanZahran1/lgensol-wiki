---
title: Activation Process (Formation & Aging)
created: 2026-06-05
updated: 2026-06-08
type: concept
tags: [formation, aging, safety, cycle-life]
sources:
  - raw/battery-inside-en/en/tech-en/a-better-life-with-batteries-how-to-make-a-battery-step3-formation.md
  - raw/battery-inside-en/en/news-en/lg-energy-solution-to-pioneer-battery-safety-diagnostics-software-business-exploring-unl-a59e221a94.md
  - raw/battery-inside-en/en/interview-en/incharge-chang-geun-ahn-of-the-environmental-safety-team-establishes-a-safe-infrastructu-a73bceea51.md
  - raw/battery-inside-en/en/interview-en/can-ai-also-determine-the-safety-of-car-batteries.md
  - raw/battery-inside-en/en/tech-en/infographics-7-how-to-make-a-battery-step-3-formation.md
confidence: high
---
# Activation Process (Formation & Aging)

## Overview

The activation process is the third major stage of lithium-ion battery manufacturing, following electrode fabrication and cell assembly. Although the cell is physically complete after assembly, it lacks the electrochemical properties required to store and deliver energy. Activation transforms the inert assembly into a functional battery through precisely controlled charging, aging, and testing sequences. This stage is both time-intensive (typically several days) and capital-intensive, yet it is critical for determining the cell’s cycle life, safety, and overall quality. LG Energy Solution (LGES) employs proprietary techniques in this process, including advanced degassing and multi-stage aging protocols, to ensure high reliability and performance.

## Technical Details

### Step 1: Electrolyte Wetting (Aging)

After cell assembly, the injected electrolyte must fully penetrate the porous electrode structure to enable uniform ion transport. The cell is stored at controlled temperature and humidity for a period that varies by cell format. LGES literature indicates that typical aging times range from 1.5 to 3 days for pouch cells, while some formats may require only 30 minutes to 3 hours at room temperature. Incomplete wetting leads to “dry spots” that do not participate in electrochemical reactions, reducing usable capacity and creating localized stress during cycling. The aging step ensures that the electrolyte uniformly wets both the anode and cathode, allowing lithium ions to move freely between electrodes during subsequent charge.

### Step 2: Formation – SEI Creation

The most critical step is the first controlled charge. During charging, lithium ions migrate from the cathode to the anode. At the anode surface, the electrolyte decomposes to form a thin solid layer called the Solid Electrolyte Interphase (SEI). The SEI is a passivation layer that conducts lithium ions but blocks electrons, preventing further electrolyte breakdown. The quality of this initial SEI directly governs the cell’s long-term cycle life, self-discharge rate, and safety characteristics.

Formation protocols must be optimized for each cell chemistry (e.g., NCM, LFP). Parameters such as charge rate, temperature, voltage limits, and rest periods are precisely controlled. Too-rapid formation can produce a non-uniform SEI with poor coverage, while overly slow formation reduces manufacturing throughput. Typically, formation involves one or more slow charge-discharge cycles to build a stable, uniform SEI. LGES emphasizes that this step is the core of the activation process, as it “gives life” to the battery.

### Step 3: Degassing

During formation, side reactions (particularly electrolyte decomposition at the anode) generate gaseous byproducts. In pouch cells, these gases accumulate and must be removed to prevent internal pressure buildup and maintain electrode contact. Degassing is performed after the first charge cycle, when most gas generation occurs. The cell is opened in a dry, controlled environment, the gas is extracted, and the cell is resealed.

LGES has developed a proprietary vertical degassing technology, in which the pouch is held upright during gas removal. This approach minimizes electrolyte loss, reduces equipment footprint, and improves process efficiency. For cylindrical or prismatic cells, gas is often removed via built-in venting mechanisms, but pouch cells require this dedicated step.

### Step 4: Secondary Aging and Testing

After degassing, the cell undergoes additional aging at elevated temperatures (60–70 °C) for one or two more cycles. This high-temperature aging stabilizes the SEI, promotes uniform thickness, and allows latent defects (e.g., micro-shorts, internal leaks) to manifest. The cell’s capacity, internal resistance, and open-circuit voltage (OCV) are measured. Cells exhibiting low voltage, high self-discharge, or abnormal resistance are rejected.

The final quality checks include an End of Line (EOL) test that verifies performance against specifications and conducts a visual inspection. Before shipping, the cell is discharged to a specified state of charge (typically 30% of rated capacity) using a controlled discharge rate of 0.1–1 C-rate. This ensures safe handling and long shelf life.

## Significance and LG Context

The activation process directly impacts every performance metric that matters to end users: energy density achievable in practice, cycle life, and safety. LGES’s approach incorporates several innovations:

- **Optimized formation protocols** tailored to high-nickel NCM cathodes and advanced anodes (e.g., silicon‑graphite composites), ensuring robust SEI formation even under aggressive charging conditions.
- **Vertical degassing** reduces electrolyte waste and minimizes contamination risk, contributing to higher yield and lower cost.
- **Integrated aging and testing** sequences are fully automated, enabling high throughput while maintaining strict quality gates. LGES’s Michigan plant, for example, operates at a 5 GWh annual capacity using such advanced processes.

The company also invests in region-specific activation knowledge: its Michigan workforce engages with local universities (e.g., Grand Valley State University, Michigan State University) to develop future talent for battery manufacturing, including the critical activation steps. This reflects LGES’s commitment to both technical excellence and community engagement.

## Related Pages

- [[battery-manufacturing|Battery Manufacturing Process Overview]]
- [[sei|SEI (Solid Electrolyte Interphase)]]
- [[dendrite|Dendrite Formation and Prevention]]
- [[lfp-vs-ncm|LFP vs NCM Comparison]]
- [[srs|SRS® Safety Reinforced Separator]]