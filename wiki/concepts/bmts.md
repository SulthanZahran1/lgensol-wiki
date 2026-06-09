---
title: BMTS (B.around Total Solution)
created: 2026-06-05
updated: 2026-06-08
type: concept
tags: [bmts, bms, soc, soh]
sources:
  - raw/battery-inside-en/en/tech-en/battery-glossary-bmts-battery-management-total-solution.md
  - raw/ko/story/%eb%b0%b0%ed%84%b0%eb%a6%ac-%ec%a0%84-%ec%83%9d%ec%95%a0%ec%a3%bc%ea%b8%b0-%ea%b4%80%eb%a6%ac%ec%9d%98-%ec%83%88%eb%a1%9c%ec%9a%b4-%ed%98%81%ec%8b%a0-bmts%eb%b0%b0%ed%84%b0%eb%a6%ac.md
  - raw/battery-inside-en/en/interview-en/bmts-b-around-interview-part-1.md
  - raw/ko/tech/%eb%b0%b0%ed%84%b0%eb%a6%ac-%ec%9a%a9%ec%96%b4%ec%82%ac%ec%a0%84-bmts-battery-management-total-solution.md
  - raw/battery-inside-en/en/news-en/lg-energy-solution-launches-new-brand-b-around-for-battery-management-total-solution.md
confidence: high
---
# BMTS (B.around Total Solution)

## Overview

BMTS (Battery Management Total Solution) is LG Energy Solution's next-generation battery management platform that transcends the limitations of traditional BMS (Battery Management System). Announced in September 2024 under the brand name **B.around** (standing for "Battery around," "Be around," and "Better around"), BMTS integrates BMS hardware with cloud computing, artificial intelligence (AI), and advanced software services to manage batteries throughout their entire life cycle—from cell manufacturing through first use, second life, and eventual recycling.

While conventional BMS is an embedded circuit board confined to a battery pack with limited memory and computational resources, BMTS offloads complex algorithms and large-scale data analysis to the cloud and high-performance computing (HPC) platforms. This architecture enables real-time monitoring, predictive diagnostics, and proactive control at both the individual cell and fleet levels, delivering a step-change in accuracy, safety, and business model flexibility.

## Technical Details

The BMTS platform comprises four core layers: on-board BMS electronics, application-layer software, cloud-based data analytics, and user-facing services.

### Hardware and Sensing

At the hardware level, BMTS builds on LG Energy Solution's proven BMS electronics—capable of measuring voltage, current, and temperature per cell (or per module for large packs). Over two decades of development, LG has accumulated more than 8,000 BMS-related patents and analyzed over 130,000 individual cells and 1,000 modules. This empirical foundation feeds into the platform's diagnostic algorithms.

### Algorithms and Diagnostics

BMTS uses a suite of proprietary algorithms to estimate [[soc|State of Charge (SoC)]], [[soh|State of Health (SoH)]], and other [[sox|State of X (SoX)]] parameters with industry-leading accuracy. Key techniques include:

- **Coulomb counting with voltage correction** for real-time SoC estimation.
- **Impedance spectroscopy and capacity fade analysis** for SoH and degradation mechanism identification.
- **FRISM (Cell Data Free SOH Model)** – a model that estimates SoH without requiring cell-specific training data.
- **LLAZER (LAM LLI Analyzer)** – a diagnostic tool that separates capacity loss due to loss of active material (LAM) and loss of lithium inventory (LLI).
- **BLiS (Battery Life Simulator)** – a simulator that predicts remaining useful life (RUL) under user-specific driving and charging patterns.

For safety, BMTS introduces three novel AI-driven health diagnostics: **MAVD** (Moving Average Voltage Deviation), **RdV** (Relaxation Deviation Voltage), and **dSOH** (Delta State of Health). These algorithms detect subtle cell anomalies—like lithium plating, SEI growth, electrolyte dry-out, or current collector corrosion—before they manifest as performance loss. Validation against real vehicle data (from 12,000 EVs in 2023 alone) shows a detection rate exceeding 90%. The overall SoH estimation error margin is only 1–2%, among the best in the industry.

### Cloud and SDV Integration

BMTS leverages cloud connectivity to store and analyze massive datasets from individual vehicles and fleets. Collected via LG's **B-Checkup** OBD dongle (used in the [[baas|B-Lifecare]] service), the data feeds machine learning models that continuously tune diagnostic algorithms.

For [[sox|Software-Defined Vehicles (SDVs)]], BMTS provides an on-board solution: LG partnered with Qualcomm to develop a SoC (System on Chip) that embeds battery management algorithms directly on the vehicle's HPC. This chip delivers 80× the computing power of conventional BMS microcontrollers, enabling real-time SoX estimation and adaptive control without cloud dependency. For customers using existing chips, BMTS offers a software package that can be integrated into their HPC and updated over-the-air (OTA). This dual approach—dedicated SoC or standalone software—provides flexibility for OEMs.

### Service Ecosystem

BMTS powers a range of user-facing services, including **B-Lifecare**, a smartphone application that provides personalized battery health scores, driving habit analysis, and charging recommendations. The same platform enables [[baas|Battery-as-a-Service (BaaS)]] business models, where LG Energy Solution retains ownership of the battery, monitors its health continuously, and guarantees performance over its life. The platform also prepares batteries for second-life applications by certifying their condition for stationary storage.

## Significance and LG Energy Solution Context

BMTS marks LG Energy Solution's strategic transformation from a pure cell manufacturer into a total battery solution provider. By bridging hardware, software, cloud, and services, LG can offer performance-based warranties, battery leasing, and circular-economy initiatives—all underpinned by the deepest battery empirical dataset in the industry.

The platform directly addresses the growing need for battery life-cycle management. As vehicles become SDVs and energy storage systems become more distributed, the ability to monitor, diagnose, and optimize batteries remotely becomes critical. BMTS not only improves safety and extends useful life but also unlocks residual value through informed second-life decisions and recycling coordination.

LG's commitment to BMTS is reflected in its R&D investment: over 20 years of BMS development, 8,000+ patents, and partnerships with automotive OEMs and chipmakers. The B.around brand embodies this vision—"Be around your side"—promising that LG Energy Solution will remain close to customers (both OEMs and end users) throughout the battery's entire journey.

## Related Pages

- [[battery-management-system|BMS (Battery Management System)]]
- [[sox|SoX (State of X)]]
- [[cell-balancing|Cell Balancing]]
- [[soc|SoC (State of Charge)]]
- [[soh|SoH (State of Health)]]
- [[battery-recycling|End-of-Life Battery Reuse and Recycling]]
- [[baas|BaaS (Battery as a Service)]]