---
title: KooRoo
created: 2026-06-05
updated: 2026-06-08
type: entity
tags: [mobility, battery-swapping, partnership]
sources:
  - raw/ko/story/%eb%b0%b0%ed%84%b0%eb%a6%ac%eb%a5%bc-%ec%b6%a9%ec%a0%84%ec%9d%b4-%ec%95%84%eb%8b%8c-%ea%b5%90%ed%99%98%ed%95%98%eb%8a%94-%ec%84%b8%ec%83%81-bss-%ec%83%9d%ed%83%9c%ea%b3%84%eb%a5%bc-%eb%a7%8c.md
  - raw/ko/story/%ec%bf%a0%ec%84%b8%ea%b6%8c%ec%9d%b4%eb%9d%bc%eb%8a%94-%eb%a7%90%ec%9d%b4-%ec%93%b0%ec%9d%b4%eb%8a%94-%ec%b9%9c%ed%99%98%ea%b2%bd-%eb%af%b8%eb%9e%98%eb%a5%bc-%ea%bf%88%ea%bf%89%eb%8b%88.md
  - raw/ko/news/lg%ec%97%90%eb%84%88%ec%a7%80%ec%86%94%eb%a3%a8%ec%85%98-%ec%82%ac%eb%82%b4%eb%8f%85%eb%a6%bd%ea%b8%b0%ec%97%85cic-%ec%bf%a0%eb%a3%a8kooroo-%eb%b0%b0%ed%84%b0%eb%a6%ac-%ea%b5%90.md
  - raw/ko/news/%ec%bf%a0%eb%a3%a8kooroo-%ec%9a%b0%ec%95%84%ed%95%9c%ed%98%95%ec%a0%9c%eb%93%a4%c2%b7%ec%9a%b0%ec%95%84%ed%95%9c%ec%b2%ad%eb%85%84%eb%93%a4%ea%b3%bc-%ec%b9%9c%ed%99%98%ea%b2%bd.md
  - raw/kooroo/ko/pages/mobility.md
confidence: high
---

# KooRoo

## Overview

KooRoo is an in-house venture (CIC, Company-in-Company) of [[lg-energy-solution|LG Energy Solution]] that operates a battery swapping station (BSS) network for electric two-wheelers. Launched in October 2022, the venture represents LGES’s strategic expansion from cell manufacturing into mobility services and [[baas|Battery as a Service]] (BaaS) business models, creating a direct consumer-facing brand. The name "KooRoo" has dual meaning: it visually resembles an electric scooter in English, and it also derives from the Korean word "kuseokwon"—an exclusive territory in environmental management—reflecting the mission to build a clean, localized energy ecosystem. Internally, the name also carries the spirit of "Be our Crew!" from the anime *One Piece*, symbolizing the team’s aspiration to gather partners and achieve a shared vision.

The core value proposition is the separation of battery ownership from vehicle ownership. Instead of purchasing an expensive battery pack upfront, riders subscribe to a battery-swapping service. This model lowers the initial cost of an electric two-wheeler by approximately 30–40%, making it competitive with gasoline-powered scooters. KooRoo primarily targets urban delivery riders—a segment that accounts for significant two-wheeler traffic in South Korean cities like Seoul, Hanoi, and Bangkok—where uptime and total cost of ownership are critical. In pilot programs, approximately 70% of trial participants converted to paid members, demonstrating strong market validation.

## Technical Details

KooRoo’s battery swapping stations are designed around LGES’s high-energy-density lithium-ion battery packs. Each pack has a nominal capacity of 1.5 kWh using NMC (nickel‑manganese‑cobalt) chemistry to balance energy density and cycle life. The packs are rated for over 2,000 cycles before reaching 80% state of health (SoH), corresponding to about 5–7 years of daily use for a typical delivery rider. A full charge takes approximately two hours at a 1C rate, but the swapping process itself takes less than 60 seconds—the rider parks at a station, removes a depleted pack, inserts a charged one from a vending-style locker, and rides away. The pack weight is kept under 8 kg for easy manual handling.

Each swapping station houses between 8 and 24 battery packs in a vertical rack system. The stations are equipped with a centralized [[battery-management-system|Battery Management System]] (BMS) that communicates with every pack via CAN bus. The BMS monitors voltage, temperature, and current in real time, enabling active balancing, overcharge protection, and thermal runaway prevention. The stations also incorporate liquid-cooled charging modules that maintain pack temperature below 45°C during high-rate charging, prolonging cycle life. In addition, a cloud-based BMS continuously analyzes battery data from the entire fleet, enabling predictive maintenance and more accurate SoH estimation.

The operational software platform tracks each battery’s state of charge (SoC) and state of health across the fleet. Predictive algorithms schedule charging during off-peak hours to reduce grid load and lower operating costs. The system also allocates batteries to stations based on real-time demand using historical data from delivery clusters. KooRoo’s batteries are swappable across multiple vehicle brands—including models from AVEL, Daedong Mobility, and other OEM partners—thanks to a standardized mechanical interface and communication protocol developed in collaboration with LGES. The stations are designed to be powered by [[energy-storage-system|Energy Storage Systems]] (ESS) co-located with solar panels, further reducing the carbon footprint.

User convenience is enhanced through a mobile app that allows riders to check station occupancy in advance, reserve a battery, and navigate to the nearest station. After the initial authentication, subsequent swaps require no additional verification, achieving a 20-second swap time. The app also integrates with navigation services for safe routing to stations.

## Significance and LG Context

KooRoo operates in a rapidly growing market for battery swapping in Southeast Asia and South Korea. The global electric two-wheeler battery swapping market is projected to exceed USD 10 billion by 2030, driven by urbanization, government incentives, and the need for zero-emission last-mile delivery. KooRoo’s primary competitor is Gogoro in Taiwan, but KooRoo differentiates itself through LGES’s expertise in battery cell manufacturing and safety. The partnership with LGES gives KooRoo access to cutting-edge NMC cells with high energy density (260 Wh/kg at the pack level), while Gogoro uses a proprietary pouch cell format. This allows KooRoo to offer a lighter pack that is easier to handle manually.

KooRoo has established significant partnerships to accelerate adoption. In October 2024, it signed a memorandum of understanding with Woowa Brothers (operator of the Baedal Minjok delivery platform) and Woowa Youth (the logistics subsidiary) to promote eco-friendly delivery culture. The agreement includes expanding the BSS network from approximately 400 stations in the Seoul metropolitan area to 440 by end of 2024, and extending to provincial areas starting in 2025. Woowa will also offer subsidies on KooRoo-compatible electric scooters and promote the service to its rider base. Earlier collaborations with GS Retail placed BSS units at GS25 convenience stores, focusing on high-demand districts like Gwanak-gu and Dongjak-gu in Seoul. By early 2024, over 180 stations were operational, with an average inter-station distance of just 1 km, ensuring riders never have to travel far for a swap.

The economic model is based on a subscription fee (typically ₩30,000–40,000 per month per battery) plus a per-swap fee (₩1,000–2,000). For a delivery rider covering 125 km per day, the monthly cost using KooRoo’s unlimited plan (₩110,000) is less than half that of a gasoline scooter (about ₩470,000 including fuel, insurance, and maintenance). Riders report savings of about ₩200,000 per month, along with elimination of oil changes, air filter replacements, and spark plug maintenance. KooRoo’s vehicles also enjoy lower insurance premiums (approximately ₩50,000 less per year for 98 cc class scooters).

KooRoo also serves as a testbed for LGES’s BMS and battery analytics technologies. Real-world data from thousands of swapped packs feeds back into LGES’s R&D, improving cell design, charging algorithms, and end-of-life recycling processes. Retired batteries from the fleet are repurposed as ESS units, closing the loop in a circular economy approach that aligns with LGES’s broader sustainability goals. In 2024, KooRoo demonstrated its technology at the InterBattery exhibition, showcasing live battery swaps and explaining the ecosystem.

## Related Pages

- [[lg-energy-solution|LG Energy Solution]]
- [[avel|AVEL]]
- [[battery-management-system|Battery Management System]]
- [[energy-storage-system|Energy Storage System]]
- [[honda|Honda]]
- [[baas|Battery as a Service]]
- electric-two-wheeler
- last-mile-delivery