---
title: Qualcomm
created: 2026-06-05
updated: 2026-06-08
type: entity
tags: [partnership, bms, open-innovation]
sources:
  - raw/battery-inside-en/en/news-en/lg-energy-solution-intends-to-work-with-qualcomm-to-develop-advanced-battery-management-c00e1bd079.md
  - raw/corporate/kr/newsroom/8649-lg에너지솔루션-퀄컴과-첨단-bms-솔루션-본격-상용화-나선다.md
  - raw/lg-energy-solution-poland/pl/pages/lg-energy-solution-rozpoczyna-wspolprace-z-qualcomm-by-opracowac-zaawansowane-rozwiazani-9a41d107d5.md
  - raw/ko/news/lg%ec%97%90%eb%84%88%ec%a7%80%ec%86%94%eb%a3%a8%ec%85%98-%ed%80%84%ec%bb%b4-%ec%b2%a8%eb%8b%a8-bms-%ec%86%94%eb%a3%a8%ec%85%98-%ea%b0%9c%eb%b0%9c-%eb%82%98%ec%84%a0%eb%8b%a4.md
  - raw/battery-inside-en/en/interview-en/lg-energy-solutions-bms-the-doctor-ensuring-battery-safety-and-efficiency.md
confidence: high
---
# Qualcomm

## Overview
Qualcomm Incorporated is a global leader in wireless technology and semiconductor design, headquartered in San Diego, California. Its Snapdragon portfolio powers a vast ecosystem of mobile, automotive, IoT, and edge computing devices. In the battery industry, Qualcomm is best known for a strategic partnership with [[lg-energy-solution|LG Energy Solution]] (LGES) to co-develop next-generation battery management system (BMS) solutions. The collaboration marries LGES’s decades of battery electrochemistry expertise — spanning lithium-ion, NCMA, and solid-state chemistries — with Qualcomm’s high-performance Snapdragon Digital Chassis compute platform. The result is a software-defined BMS that moves beyond conventional rule-based algorithms to real-time, AI-driven cell diagnostics, predictive health monitoring, and adaptive control. This partnership positions Qualcomm as a key enabler of intelligent battery platforms for electric vehicles (EVs), energy storage systems (ESS), and other high-power applications.

## Technical Details
### Snapdragon Digital Chassis as a BMS Compute Backbone
Traditional BMS microcontrollers typically offer modest processing power (e.g., 200–400 MHz ARM Cortex cores) with limited memory (a few megabytes of flash). In contrast, Qualcomm’s Snapdragon Digital Chassis integrates multiple system-on-chips (SoCs) such as the Snapdragon Ride and Snapdragon Cockpit. For BMS applications, the platform leverages automotive-grade processors like the SA8295P and SA8650P, delivering up to 30 TOPS of AI performance. This compute headroom — over 80 times greater than conventional BMS hardware — enables algorithms previously impractical in embedded microcontrollers, such as physics-informed neural networks for electrochemical modeling, real-time Kalman filters for 200+ cell state estimation, and multi-physics thermal runaway prediction models.

### Advanced Battery State Estimation and Diagnostics
The joint LGES–Qualcomm system improves [[soc|state of charge (SoC)]] and [[soh|state of health (SoH)]] estimation accuracy to within ±1% and ±2%, respectively, under dynamic driving conditions. This is achieved by fusing voltage, current, temperature, and impedance data from every cell at sampling rates exceeding 100 Hz. The BMS employs a dual-extended Kalman filter (DEKF) running on the Snapdragon AI engine to simultaneously estimate SoC and internal resistance. Additionally, a long short-term memory (LSTM) neural network trained on LGES’s proprietary aging database — covering over 100,000 EVs and more than 10,000 disassembled batteries — predicts capacity fade and power fade with a mean absolute percentage error of less than 3% over the battery’s full lifetime. LGES holds over 8,000 BMS-related patents, and its safety diagnostic algorithms achieve detection rates exceeding 90%, with degradation error rates at industry-leading 1%.

### Predictive Diagnostics and Early Warning
A key capability is early detection of anomalous cell behavior that can lead to thermal runaway. The system uses edge-based anomaly detection models such as Moving Average Voltage Deviation (MAVD), Relaxation Deviation Voltage (RdV), and Delta State of Health (dSOH). If any cell deviates more than 50 mV from its pack-average voltage under load, the BMS triggers a predictive maintenance alert. The Snapdragon platform also supports over-the-air (OTA) firmware updates, allowing continuous improvement of diagnostic models without hardware changes. For example, a model update can add new failure modes (e.g., lithium plating detection during fast charging) based on field data aggregated from thousands of vehicles.

### System Integration and Communication
The BMS hardware integrates Qualcomm’s QCX216 Ethernet switch and Snapdragon X55 5G modem for high-bandwidth data transmission to cloud analytics platforms, enabling remote fleet monitoring and digital twin creation. The system supports ISO 26262 ASIL-D functional safety requirements with redundant processing cores and fail-safe mechanisms. On the cell monitoring side, the BMS communicates via isolated daisy-chain UART to cell monitoring ICs (e.g., Analog Devices LTC6813 or Texas Instruments BQ79616), reading up to 18 cell voltages per chip at 1 mV resolution. The entire stack is designed for scalability from small 48V mild-hybrid packs to large 800V EV battery packs exceeding 100 kWh.

## Significance and LG Context
### Shift from Hardware- to Software-Defined Batteries
The Qualcomm–LGES partnership exemplifies the industry trend toward [[battery-management-system|software-defined battery management]]. By decoupling BMS intelligence from low-cost microcontrollers and placing it on a high-performance compute platform, automakers can extend battery life by 10–15%, increase usable energy by 5%, and reduce warranty costs through predictive diagnostics. This is particularly valuable for fleet operators where each percentage point of SoH savings translates into millions of dollars in avoided battery replacement.

### Open Innovation and Ecosystem Integration
Qualcomm’s approach is part of a broader open-innovation strategy. The Snapdragon Digital Chassis supports AUTOSAR Adaptive, ROS 2, and Android Automotive, allowing third-party battery algorithm developers to deploy their models. This contrasts with proprietary BMS solutions from companies like NXP, Infineon, or Tesla. The partnership also positions LGES to sell BMS software as a service (BMSaaS) alongside its cells, transforming its business model from a pure component supplier to a solution provider. LGES has launched the B.around brand and BMTS (Battery Management Total Solution) initiative, integrating cloud and AI technologies. Related programs include the [[kooroo|KooRoo]] portable power platform and [[avel|AVEL]] aviation batteries, both of which could adopt the same BMS platform.

### Impact on EV and ESS Scalability
With 5G connectivity, the BMS can offload heavy computations to the cloud when needed, but the Snapdragon edge capability ensures low-latency decisions even in dead zones. For energy storage systems, the platform enables virtual power plant (VPP) optimization, where thousands of residential ESS units coordinate via Qualcomm’s mesh networking technology. The scalability from consumer to grid-scale is a unique selling point, and early adopters include GM (for Ultium-based EVs) and unnamed ESS integrators. LGES and Qualcomm signed a formal joint promotion agreement in late 2024 to commercialize this SoC-based BMS solution for global OEMs.

## Related Pages
- [[battery-management-system|BMS (Battery Management System)]]
- [[lg-energy-solution|LG Energy Solution]]
- [[soc|State of Charge (SoC)]]
- [[soh|State of Health (SoH)]]
- Thermal Runaway
- Electric Vehicle (EV)
- [[energy-storage-system|ESS (Energy Storage System)]]
- [[kooroo|KooRoo Portable Power]]
- [[avel|AVEL Aviation Batteries]]