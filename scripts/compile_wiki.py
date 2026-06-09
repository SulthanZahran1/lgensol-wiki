#!/usr/bin/env python3
"""Compile the 95-page LG Energy Solution LLM wiki.

This script intentionally keeps the large Korean corpus out of the agent
context. It reads raw posts locally, scores sources for each page, and writes
compact English wiki pages with YAML frontmatter and wikilinks.
"""
from __future__ import annotations

import argparse
import html
import re
import subprocess
from collections import Counter
from datetime import date
from pathlib import Path
from urllib.parse import unquote


ROOT = Path("/home/dev/lgensol-wiki")
WIKI = ROOT / "wiki"
RAW = ROOT / "raw"
TODAY = date.today().isoformat()
CONTENT_DIRS = ("entities", "concepts", "comparisons", "glossary")


STOP_TERMS = {
    "battery",
    "batteries",
    "cell",
    "cells",
    "energy",
    "solution",
    "comparison",
    "process",
    "technology",
    "material",
    "materials",
    "system",
    "systems",
    "current",
    "state",
}


TITLE_OVERRIDES = {
    "bbu": "BBU (Battery Backup Unit)",
    "bi-cell": "Bi-Cell",
    "battery-passport": "Battery Passport",
    "c-rate": "C-rate (Current Rate / Charge-Discharge Rate)",
    "srs": "SRS (Safety Reinforced Separator)",
}


ALLOWED_TAGS = set(
    """
    lfp ncm nca ncma lmrp lithium-sulfur sodium-ion lithium-metal solid-state lmo high-nickel mid-nickel
    cathode anode electrolyte separator binder conductive-additive current-collector active-material
    energy-density power-density cycle-life fast-charging safety thermal-stability voltage
    electrode slurry mixing coating drying calendering slitting-notching stacking winding lamination welding formation aging eol dry-electrode wet-electrode
    ev ess uam aerospace mobility battery-swapping humanoid commercial-vehicle
    earnings partnership joint-venture investment plant supply-chain recycling esg open-innovation mineral
    bms bmts ctp ccb azs lpm bipolar cell-balancing thermal-management srs soc soh
    cylindrical pouch prismatic mono-cell bi-cell 46-series 18650 21700
    comparison glossary interview news opinion timeline meta fundamentals
    """.split()
)


TAG_REPLACEMENTS = {
    "assembly": ["stacking", "lamination"],
    "c-rate": ["fast-charging", "power-density"],
    "electrolyte-additive": ["electrolyte"],
    "ionic-conductivity": ["electrolyte"],
    "pack": ["ctp", "thermal-management"],
}


NOTES = {
    "46-series-battery": {
        "summary": "Large cylindrical lithium-ion cells with a 46 mm diameter, represented by formats such as 4680 and 4695.",
        "facts": [
            "The larger diameter raises cell-level energy and can reduce pack complexity when thermal and current paths are engineered correctly.",
            "LG Energy Solution's corpus links 46-series cells to EV programs, Arizona production plans, and the Rivian 4695 supply story.",
            "The format competes with pouch and prismatic cells on manufacturing speed, mechanical rigidity, fast charging, and pack integration.",
        ],
    },
    "avel": {
        "summary": "AVEL is an LG Energy Solution in-house venture focused on energy aggregation, ESS operation, and renewable-grid integration.",
        "facts": [
            "Its role is less about cell chemistry and more about dispatching batteries as controllable grid assets.",
            "The raw posts connect AVEL to Jeju power-market pilots, distribution-grid ESS plants, and virtual power plant logic.",
            "AVEL sits on the business side of ESS, where forecasting, grid constraints, energy-market optimization, and operating software decide battery value.",
        ],
    },
    "azs-stacking": {
        "summary": "Advanced Z-Stacking is LG Energy Solution's pouch-cell assembly method that combines Z-stacking with lamination and heat pressing.",
        "facts": [
            "AZS aligns electrodes and separator sheets before they are inserted into the pouch case.",
            "Heat and pressure bond layers so electrode movement and overhang risk are reduced during transfer and later operation.",
            "The technology belongs to the assembly-process layer and is closely tied to mono-cell, bi-cell, separator, and pouch-cell design.",
        ],
    },
    "bipolar-technology": {
        "summary": "Bipolar battery architecture connects cells internally in series through shared current collectors.",
        "facts": [
            "The appeal is lower inactive material and shorter current paths at module or pack level.",
            "The engineering difficulty is sealing, isolation, and uniform pressure across stacked electrochemical units.",
            "LG Energy Solution discusses bipolar and semi-solid concepts as part of a broader next-generation portfolio.",
        ],
    },
    "ford": {
        "summary": "Ford appears in the corpus as a global automaker customer and partner for EV battery supply.",
        "facts": [
            "Ford-related entries are best read as part of LG Energy Solution's customer diversification, not as a chemistry by itself.",
            "The technical connection is high-performance EV cells, pack requirements, quality consistency, and regional manufacturing.",
            "Ford sits near other OEM pages such as GM, Stellantis, Hyundai Motor Group, Honda, Toyota, Tesla, and Rivian.",
        ],
    },
    "gm": {
        "summary": "General Motors is a central LG Energy Solution partner through Ultium Cells and related North American EV battery programs.",
        "facts": [
            "The corpus links GM to Ultium Cells, pouch-cell manufacturing, LFP ESS conversion plans, prismatic development, and LMR work.",
            "GM's page is mainly a partnership and manufacturing node, while the chemistry details live on NCM, LFP, NCMA, and LMR pages.",
            "The relationship illustrates how cell makers and OEMs coordinate chemistry, form factor, plant location, and pack architecture.",
        ],
    },
    "high-nickel-battery": {
        "summary": "High-nickel batteries use nickel-rich layered cathodes to raise energy density for long-range EVs.",
        "facts": [
            "More nickel increases cathode capacity but can lower thermal and structural stability if coating, doping, and electrolyte design are weak.",
            "LG Energy Solution sources discuss high-nickel NCMA and high-nickel cylindrical products as premium-performance options.",
            "The key tradeoff is energy density versus cost, safety margin, and process control.",
        ],
    },
    "honda": {
        "summary": "Honda is an LG Energy Solution joint-venture partner for North American EV battery manufacturing.",
        "facts": [
            "The business relevance is localized battery production, supply assurance, and dedicated cells for Honda EV programs.",
            "The technical relevance is less a named chemistry than repeatable manufacturing quality across electrode, assembly, and formation processes.",
            "Honda belongs with GM, Stellantis, Hyundai Motor Group, Toyota, Ford, and Rivian in the OEM ecosystem.",
        ],
    },
    "hyundai-motor-group": {
        "summary": "Hyundai Motor Group appears as an LG Energy Solution automotive partner in the EV battery supply chain.",
        "facts": [
            "Its page represents OEM requirements: high energy, fast charging, safety validation, and stable regional supply.",
            "The chemistry and form-factor choices connect outward to NCM, NCMA, LFP, pouch cells, cylindrical cells, and pack integration.",
            "Hyundai's partnership context fits the broader move from simple cell supply toward joint production and long-term platform planning.",
        ],
    },
    "kooroo": {
        "summary": "KooRoo is an LG Energy Solution in-house venture building battery swapping stations for electric two-wheelers.",
        "facts": [
            "KooRoo separates charging time from vehicle use by swapping depleted packs for charged packs.",
            "The sources connect KooRoo to BSS infrastructure, electric delivery culture, pack standards, and battery-life management.",
            "It is a service model where battery management, pack safety, station density, and user convenience matter as much as cell chemistry.",
        ],
    },
    "lfp-battery": {
        "summary": "LFP batteries use lithium iron phosphate cathodes, prioritizing thermal stability, cycle life, and cost over maximum energy density.",
        "facts": [
            "The olivine phosphate structure is intrinsically stable, which makes LFP attractive for ESS and affordable EV segments.",
            "The tradeoff is lower cell-level energy density than nickel-rich NCM or NCMA, although pack design can close some of the gap.",
            "LG Energy Solution sources discuss LFP for ESS, pouch-type LFP, and the strategic shift toward diversified chemistries.",
        ],
    },
    "lg-energy-solution": {
        "summary": "LG Energy Solution is the central company in the corpus, spanning EV batteries, ESS, next-generation chemistry, manufacturing, services, and ESG.",
        "facts": [
            "The wiki treats the company as a hub that links chemistries, cell formats, OEM partnerships, ESS projects, recycling, BMTS, and software services.",
            "Its technical portfolio includes pouch, cylindrical, and prismatic directions as well as NCM, NCMA, LFP, LMR, lithium-sulfur, sodium-ion, lithium-metal, and solid-state research.",
            "The raw posts also cover global plants, joint ventures, smart-factory quality systems, critical minerals, carbon reduction, water and waste management, and circular-economy programs.",
        ],
    },
    "lithium-metal-battery": {
        "summary": "Lithium-metal batteries replace graphite or silicon-host anodes with metallic lithium to raise theoretical energy density.",
        "facts": [
            "The benefit is a very high specific capacity anode, useful for aviation, UAM, and next-generation high-energy cells.",
            "The central risk is dendrite growth and unstable interfaces, which must be handled through electrolyte, separator, pressure, and charging control.",
            "Lithium metal is a bridge concept for lithium-sulfur, solid-state, and anodeless battery research.",
        ],
    },
    "lithium-sulfur-battery": {
        "summary": "Lithium-sulfur batteries pair a sulfur-based cathode with a lithium-metal anode for lightweight, high-energy applications.",
        "facts": [
            "Sulfur is abundant and light, so the chemistry is attractive for aviation, drones, UAM, and aerospace use cases.",
            "The hard problems are polysulfide shuttle, low electronic conductivity of sulfur, lithium-metal stability, and cycle life.",
            "LG Energy Solution sources frame lithium-sulfur as a next-generation route where weight matters more than conventional EV packaging.",
        ],
    },
    "lmr-battery": {
        "summary": "LMR batteries use lithium- and manganese-rich cathode chemistry to balance cost and performance.",
        "facts": [
            "Manganese can reduce dependence on expensive nickel and cobalt while supporting high-voltage cathode design.",
            "The engineering questions are voltage fade, cycle stability, gas generation, and electrolyte compatibility.",
            "The corpus links LMR to future product diversification and GM-related development work.",
        ],
    },
    "mid-nickel-battery": {
        "summary": "High-voltage mid-nickel batteries use a moderate nickel content and higher operating voltage to balance cost, range, and safety.",
        "facts": [
            "Mid-nickel reduces exposure to high nickel cost and stability penalties while retaining better energy density than low-nickel options.",
            "High-voltage operation needs electrolyte additives, surface coating, and cathode design to suppress side reactions.",
            "LG Energy Solution presents this as a standard-segment EV option beside high-nickel NCMA and LFP.",
        ],
    },
    "nca-battery": {
        "summary": "NCA batteries use nickel, cobalt, and aluminum layered cathode chemistry for high-energy lithium-ion cells.",
        "facts": [
            "Nickel contributes capacity, cobalt helps structural stability, and aluminum improves stability at small addition levels.",
            "NCA is usually discussed alongside NCM and NCMA as a nickel-rich cathode family.",
            "The key design issues are high energy density, safety control, and stable interfaces with electrolyte.",
        ],
    },
    "ncm-battery": {
        "summary": "NCM batteries use nickel, cobalt, and manganese cathodes and are a mainstream EV lithium-ion chemistry.",
        "facts": [
            "Nickel raises capacity, cobalt supports structural order, and manganese improves stability and cost balance.",
            "As nickel content rises, energy density improves but thermal stability and surface reactivity require stronger materials engineering.",
            "NCM is the baseline comparison point for LFP, NCMA, high-nickel, and mid-nickel pages.",
        ],
    },
    "ncma-battery": {
        "summary": "NCMA batteries extend NCM cathodes by adding aluminum to a nickel-cobalt-manganese system.",
        "facts": [
            "The aluminum addition is used to improve structural and thermal stability in nickel-rich layered cathodes.",
            "LG Energy Solution sources connect NCMA to premium EV cells and high-energy product strategy.",
            "NCMA should be read with NCM, NCA, high-nickel batteries, electrolyte additives, and safety management.",
        ],
    },
    "qualcomm": {
        "summary": "Qualcomm appears as a technology partner for advanced BMS diagnostics and connected EV platforms.",
        "facts": [
            "The LG Energy Solution partnership links BMS diagnostic software with Snapdragon Digital Chassis capabilities.",
            "This page is about compute and diagnostics rather than cell chemistry.",
            "It belongs near BMTS, BMS, SoC, SoH, and battery safety because diagnostics convert battery data into operating decisions.",
        ],
    },
    "rivian": {
        "summary": "Rivian appears in LG Energy Solution sources as an EV customer for next-generation cylindrical 4695 batteries.",
        "facts": [
            "The technical signal is the move toward 46-series cylindrical cells for high-energy EV platforms.",
            "Rivian links cell format, fast charging, pack design, and North American supply strategy.",
            "Read it with 46-series battery, cylindrical formats, fast charging, and LG Energy Solution's customer portfolio.",
        ],
    },
    "sodium-ion-battery": {
        "summary": "Sodium-ion batteries replace lithium-ion charge carriers with sodium ions to reduce material cost and supply pressure.",
        "facts": [
            "Sodium is abundant and can perform well at low temperature, but its larger ion size generally lowers energy density versus lithium-ion.",
            "The chemistry is attractive for low-cost, high-power, and stationary applications where maximum range is not the first priority.",
            "LG Energy Solution discusses sodium-ion as part of a diversified next-generation battery portfolio.",
        ],
    },
    "solid-state-battery": {
        "summary": "Solid-state batteries replace flammable liquid electrolyte with solid electrolyte to pursue higher safety and energy density.",
        "facts": [
            "Solid electrolyte can also act as a separator, enabling thinner designs and possible lithium-metal or anodeless anodes.",
            "The hard problems are interface resistance, dendrites, pressure management, manufacturability, and room-temperature performance.",
            "LG Energy Solution sources include UCSD work on room-temperature, long-life solid-state battery technology.",
        ],
    },
    "stellantis": {
        "summary": "Stellantis appears through LG Energy Solution's North American joint-venture and EV battery manufacturing context.",
        "facts": [
            "The main technical relevance is localized cell manufacturing and production ramp for EV platforms.",
            "Stellantis connects to NextStar Energy, pouch-cell production, quality systems, and regional supply-chain design.",
            "It is best read alongside GM, Honda, Hyundai Motor Group, Toyota, and Ultium Cells.",
        ],
    },
    "tesla": {
        "summary": "Tesla appears in the corpus as an ESS partner/customer for LG Energy Solution battery supply.",
        "facts": [
            "The raw posts emphasize ESS, where cell performance, LFP chemistry, system safety, and manufacturing scale all matter.",
            "Tesla's Megapack context makes this page a bridge between LFP battery, ESS, BMS, pack process, and LG Energy Solution's North American production network.",
            "The page is a customer/market node, not a claim that Tesla uses a single chemistry everywhere.",
        ],
    },
    "toyota": {
        "summary": "Toyota appears as an automaker customer in LG Energy Solution's EV battery supply ecosystem.",
        "facts": [
            "The relevance is long-term EV platform supply, manufacturing reliability, and chemistry/form-factor selection.",
            "Toyota should be linked to high-energy lithium-ion cells, pack-level safety, fast charging, and regional production.",
            "The page sits in the OEM group with GM, Honda, Hyundai Motor Group, Ford, Stellantis, Tesla, and Rivian.",
        ],
    },
    "ultium-cells": {
        "summary": "Ultium Cells is the LG Energy Solution-GM joint venture for North American battery manufacturing.",
        "facts": [
            "The sources cover Ohio and Tennessee plants, production ramp, smart-factory systems, recycling links, and ESS LFP conversion.",
            "Ultium Cells is a manufacturing and partnership node connecting GM, LG Energy Solution, LFP, NCM-class cells, and recycling.",
            "It demonstrates how joint ventures combine local production, OEM platform demand, and cell-maker process know-how.",
        ],
    },
    "active-material": {
        "summary": "Active material is the electrochemically active powder in an electrode that stores and releases lithium ions.",
        "facts": [
            "Cathode active materials largely determine voltage and capacity; anode active materials control lithium storage and fast-charge behavior.",
            "Conductive additives, binders, solvent, coating, drying, and calendering turn active material into a usable electrode.",
            "For LG Energy Solution topics, active material links directly to NCM, LFP, NCMA, silicon anode, and LMR.",
        ],
    },
    "anode-materials": {
        "summary": "Anode materials host lithium during charging and release it during discharge.",
        "facts": [
            "Graphite is the commercial baseline; silicon and silicon oxide raise capacity but swell during lithiation.",
            "Lithium-metal and anodeless designs pursue higher energy density but are limited by dendrites and interface control.",
            "The anode is tightly coupled to SEI formation, electrolyte additives, fast charging, and formation-aging.",
        ],
    },
    "assembly-process": {
        "summary": "The assembly process turns finished electrodes and separator into a physical cell stack, jelly roll, or pouch structure.",
        "facts": [
            "Cylindrical and many prismatic cells use winding; pouch cells often use stacking or lamination-and-stacking.",
            "Assembly quality controls alignment, short-circuit risk, electrolyte wetting, tab placement, and later swelling behavior.",
            "LG Energy Solution sources discuss pouch assembly, mono-cell, bi-cell, AZS, welding, and electrolyte injection.",
        ],
    },
    "battery-management-system": {
        "summary": "A BMS monitors and controls battery operation so cells stay inside safe voltage, current, temperature, and health limits.",
        "facts": [
            "Core functions include SoC estimation, SoH estimation, cell balancing, thermal control, fault diagnosis, and charge/discharge limits.",
            "Advanced BMS is becoming software-defined through diagnostics, cloud services, and chip-level integration.",
            "LG Energy Solution connects BMS to BMTS and partnerships such as Qualcomm for advanced diagnostics.",
        ],
    },
    "battery-manufacturing": {
        "summary": "Battery manufacturing converts powders, foils, separator, electrolyte, and cases into tested cells and packs.",
        "facts": [
            "A practical process map is electrode making, assembly, formation-aging, inspection, module/pack build, and end-of-line testing.",
            "Yield, safety, cost, and energy density are decided as much by process capability as by chemistry.",
            "LG Energy Solution sources explain wet electrode lines, dry electrode development, AZS, welding, digital-twin style stabilization, AI/DX initiatives, and smart-factory quality systems.",
        ],
    },
    "battery-recycling": {
        "summary": "Battery recycling recovers valuable metals and materials from production scrap and end-of-life batteries.",
        "facts": [
            "Nickel, cobalt, lithium, manganese, copper, aluminum, and graphite can be routed back into a circular supply chain.",
            "Reuse extends battery life in second-life applications; recycling handles material recovery when reuse is no longer practical.",
            "LG Energy Solution sources connect recycling to closed-loop strategy, Ultium Cells, Li-Cycle, and critical mineral security.",
        ],
    },
    "battery-safety": {
        "summary": "Battery safety is the combined control of electrochemistry, materials, design, manufacturing, BMS, and pack-level protection.",
        "facts": [
            "Thermal runaway risk rises when abuse, internal short, overcharge, contamination, or poor heat removal creates self-heating reactions.",
            "Safety is engineered through separator design, electrolyte additives, cathode stability, cell balancing, thermal propagation barriers, and diagnostics.",
            "LG Energy Solution sources cover SRS, TP prevention, ESS fire standards, BMS, EOL inspection, diagnostics, and process quality.",
        ],
    },
    "binder": {
        "summary": "Binder holds active material and conductive additive together and anchors the coating to the current collector.",
        "facts": [
            "A good binder must maintain adhesion through swelling, cycling, drying, calendering, and electrolyte exposure.",
            "Binder choice is especially important for silicon anodes because silicon expands strongly during lithiation.",
            "Binder belongs to the slurry and electrode-process layer, together with active material, conductive additive, and current collector.",
        ],
    },
    "bmts": {
        "summary": "BMTS is LG Energy Solution's broader battery-management total solution, extending BMS into diagnosis, service, and life-cycle data.",
        "facts": [
            "BMTS treats battery management as a platform rather than only an embedded circuit board.",
            "The idea links cell data, impedance or health diagnosis, software, cloud services, BaaS, and customer operations.",
            "BMTS is a bridge between BMS, SoC, SoH, B-Lifecare-style services, ESS operation, and safety management.",
        ],
    },
    "cathode-materials": {
        "summary": "Cathode materials determine much of a lithium-ion cell's voltage, capacity, cost, and thermal behavior.",
        "facts": [
            "NCM, NCA, NCMA, LFP, and LMR represent different compromises among energy density, cost, safety, and mineral exposure.",
            "Nickel raises capacity, cobalt improves layered-oxide stability, manganese supports stability and cost, and iron-phosphate improves thermal robustness.",
            "Cathode engineering depends on coating, doping, particle design, electrolyte additives, and formation conditions.",
        ],
    },
    "cell-balancing": {
        "summary": "Cell balancing reduces imbalance among series-connected cells so usable pack capacity and safety are not limited by the weakest cell.",
        "facts": [
            "Passive balancing burns excess energy as heat; active balancing moves charge between cells but adds circuit complexity.",
            "Balancing works with SoC estimation, voltage sensing, temperature sensing, and BMS control logic.",
            "It is essential in EV and ESS packs because small cell differences become pack-level constraints over many cycles.",
        ],
    },
    "cell-to-pack": {
        "summary": "Cell-to-pack removes or reduces module-level structure so cells integrate more directly into the battery pack.",
        "facts": [
            "CTP can raise pack-level energy density by reducing inactive components, but it raises demands on safety, serviceability, and structural design.",
            "The concept is chemistry-neutral and can apply to LFP, NCM, pouch, prismatic, or cylindrical strategies depending on platform needs.",
            "LG Energy Solution sources describe CTP as a pack architecture topic connected to BMS and thermal management.",
        ],
    },
    "conductive-additive": {
        "summary": "Conductive additive creates electron pathways through an electrode coating whose active material may be poorly conductive.",
        "facts": [
            "Carbon black, CNTs, and related carbon networks reduce resistance and improve power performance.",
            "Too little additive limits rate capability; too much displaces active material and lowers energy density.",
            "Conductive additive is co-designed with binder, active material, slurry mixing, coating, and calendering.",
        ],
    },
    "critical-minerals": {
        "summary": "Critical minerals are the lithium, nickel, cobalt, manganese, graphite, copper, aluminum, and related inputs that shape battery cost and resilience.",
        "facts": [
            "Supply-chain strategy includes long-term sourcing, recycling, regional processing, traceability, and chemistry diversification.",
            "The LG Energy Solution corpus connects minerals to responsible sourcing, ESG, closed-loop recycling, and cathode strategy.",
            "Chemistry choices such as LFP, LMR, high-nickel, sodium-ion, and lithium-sulfur shift exposure to different mineral, human-rights, carbon, and supplier-management risks.",
        ],
    },
    "current-collector": {
        "summary": "Current collectors are metal foils that collect electrons from electrode coatings and connect them to tabs or terminals.",
        "facts": [
            "Aluminum foil is commonly used on cathodes, while copper foil is commonly used on graphite or silicon anodes.",
            "Foil thickness, surface treatment, adhesion, and mechanical strength affect resistance, safety, and manufacturing yield.",
            "Current collectors link electrode design to welding, tab design, bipolar architectures, and pack-level current paths.",
        ],
    },
    "dry-electrode-process": {
        "summary": "Dry electrode processing makes electrodes without the solvent-heavy wet slurry route.",
        "facts": [
            "The main promise is lower drying energy, lower solvent recovery burden, lower cost, and potential compatibility with next-generation materials.",
            "The hard part is forming a uniform, well-adhered electrode with correct porosity and conductivity at production speed.",
            "LG Energy Solution sources discuss dry electrode as a cost and sustainability lever with pilot and commercialization roadmaps.",
        ],
    },
    "electrode-process": {
        "summary": "The electrode process makes coated cathode and anode rolls through mixing, coating, drying, calendering, and slitting/notching.",
        "facts": [
            "Electrode quality decides capacity uniformity, resistance, adhesion, porosity, and later electrolyte wetting.",
            "Wet electrodes dominate commercial production; dry electrodes are a strategic alternative for cost and energy reduction.",
            "This page links materials chemistry to manufacturing controls before assembly begins.",
        ],
    },
    "electrolyte": {
        "summary": "Electrolyte transports lithium ions between cathode and anode while electrons travel through the external circuit.",
        "facts": [
            "Commercial lithium-ion electrolytes usually combine lithium salt, organic solvent, and additives.",
            "Electrolyte must balance ionic conductivity, voltage stability, wetting, low-temperature behavior, gas control, SEI/CEI formation, and safety.",
            "It is central to fast charging, high-voltage cathodes, silicon anodes, lithium metal, and solid-state comparisons.",
        ],
    },
    "electrolyte-additive": {
        "summary": "Electrolyte additives are small-formulation ingredients that tune interphases, gas generation, safety, and lifetime.",
        "facts": [
            "Additives can help form stable SEI on the anode or CEI on the cathode, reducing continued electrolyte decomposition.",
            "High-voltage cathodes, silicon anodes, and fast-charging cells depend heavily on additive packages.",
            "Additive design is a precision lever: too little may be ineffective, while too much can hurt conductivity or side reactions.",
        ],
    },
    "energy-storage-system": {
        "summary": "An ESS stores electricity for later use, usually at grid, commercial, data-center, renewable, or home scale.",
        "facts": [
            "A battery ESS includes cells, modules, racks, BMS, PCS, EMS, thermal controls, fire protection, and operating software.",
            "LFP is attractive for many ESS projects because safety, life, and cost matter more than maximum vehicle range.",
            "LG Energy Solution sources cover TR1300, Tesla ESS supply, North American ESS production, AVEL, EMO-style energy-market optimization, and grid integration.",
        ],
    },
    "fast-charging": {
        "summary": "Fast charging raises charging power while trying to avoid lithium plating, overheating, excessive SEI growth, and accelerated aging.",
        "facts": [
            "The limiting factors include anode diffusion, electrolyte transport, internal resistance, heat removal, BMS estimation, and cell balancing.",
            "Silicon anodes, electrode porosity, electrolyte additives, and thermal management can improve fast-charge capability.",
            "Fast charging is a system-level result, not a single material property.",
        ],
    },
    "formation-aging": {
        "summary": "Formation and aging activate a new cell, form stable interphases, and screen early defects before shipment.",
        "facts": [
            "Formation applies controlled first charge-discharge profiles so SEI and CEI layers form in a reproducible way.",
            "Aging gives time for voltage drift, gas generation, self-discharge, and defects to appear before final grading.",
            "This step is slow and capital-intensive but critical for lifetime, safety, and quality assurance.",
        ],
    },
    "humanoid-robot-battery": {
        "summary": "Humanoid robot batteries must combine high energy, high power, safety, compact packaging, and long cycle life.",
        "facts": [
            "Robots draw pulsed power for actuation while also needing all-day operating time and safe operation near people.",
            "The corpus connects robot use cases to solid-state batteries, high-power lithium-ion cells, and software diagnosis.",
            "This application sits between EV, ESS, UAM, and next-generation battery topics.",
        ],
    },
    "lithium-ion-battery": {
        "summary": "A lithium-ion battery stores energy by shuttling lithium ions between cathode and anode through electrolyte while electrons flow externally.",
        "facts": [
            "The four core cell components are cathode, anode, electrolyte, and separator.",
            "Charging moves lithium ions into the anode; discharging moves them back to the cathode while delivering electrical work.",
            "Most pages in this wiki are refinements of this basic architecture: materials, processes, form factors, BMS, safety, and recycling.",
        ],
    },
    "pack-process": {
        "summary": "The pack process integrates cells into modules or packs with structure, sensing, thermal control, high-voltage paths, and protection.",
        "facts": [
            "Pack design converts cell performance into usable EV or ESS performance.",
            "Key issues include crash safety, thermal propagation prevention, serviceability, current distribution, cooling, and BMS integration.",
            "CTP reduces module overhead but raises the importance of pack-level safety and diagnostics.",
        ],
    },
    "pre-dispersion": {
        "summary": "Pre-dispersion prepares hard-to-disperse conductive materials or powders before final slurry mixing.",
        "facts": [
            "CNTs and other conductive additives can agglomerate, so pre-dispersion helps create a uniform conductive network.",
            "Uniform dispersion improves electrode resistance, coating quality, and process repeatability.",
            "The topic belongs to slurry preparation and electrode manufacturing rather than finished-cell operation.",
        ],
    },
    "separator": {
        "summary": "The separator is a porous membrane that prevents cathode and anode contact while letting ions pass through electrolyte-filled pores.",
        "facts": [
            "Separator failure can create internal short circuits, so thickness, porosity, shutdown behavior, coating, and puncture resistance are safety critical.",
            "LG Energy Solution's SRS concept reinforces separator safety through ceramic coating technology.",
            "In solid-state batteries, the solid electrolyte can partly replace the separator function.",
        ],
    },
    "silicon-anode": {
        "summary": "Silicon anode material can store far more lithium than graphite but expands strongly during charging.",
        "facts": [
            "Silicon improves energy density and fast-charge potential when combined with the right binder, conductive network, electrolyte additives, and formation protocol.",
            "Volume expansion can crack particles, break SEI, consume lithium, and raise resistance.",
            "LG Energy Solution sources connect silicon to high-performance EV cells and solid-state research.",
        ],
    },
    "uam-battery": {
        "summary": "UAM batteries serve urban air mobility aircraft, where weight, power, safety, and reliability dominate design choices.",
        "facts": [
            "Aviation batteries need high specific energy for range and high power for takeoff and climb.",
            "Lithium-sulfur and lithium-metal are attractive because weight reduction is valuable, but cycle life and safety remain hard problems.",
            "UAM links aerospace, lithium-sulfur, lithium-metal, solid-state, fast charging, and BMS.",
        ],
    },
    "welding-process": {
        "summary": "Welding connects electrode tabs, current collectors, cans, modules, and busbars into low-resistance electrical paths.",
        "facts": [
            "Poor welds create heat, resistance variation, mechanical weakness, and safety risk.",
            "Battery welding must control material combinations such as aluminum and copper, thin foils, tabs, and busbars.",
            "It sits between assembly, pack process, current collectors, and end-of-line inspection.",
        ],
    },
    "cathode-tier-comparison": {
        "summary": "A comparison of high-nickel, mid-nickel, and LFP cathode strategies for EV and ESS applications.",
        "facts": [
            "High-nickel prioritizes energy density; mid-nickel balances cost and voltage; LFP prioritizes safety, cost, and life.",
            "No tier is universally best: vehicle segment, pack design, mineral exposure, and safety margin decide fit.",
            "LG Energy Solution's product strategy uses multiple cathode tiers rather than a single chemistry answer.",
        ],
    },
    "cell-format-comparison": {
        "summary": "A comparison of cylindrical, pouch, and prismatic cell formats and the manufacturing/pack tradeoffs behind them.",
        "facts": [
            "Cylindrical cells benefit from mature high-speed winding and rigid cans.",
            "Pouch cells offer high packaging efficiency and flexible shapes but need external mechanical support.",
            "Prismatic cells integrate well into modules or packs but require precise case and swelling management.",
        ],
    },
    "lfp-vs-ncm": {
        "summary": "A direct comparison of LFP and NCM battery chemistry for cost, safety, energy density, cycle life, and application fit.",
        "facts": [
            "LFP generally wins on thermal stability, cost, and life; NCM generally wins on cell-level energy density.",
            "Pack architecture and vehicle segment can move the decision more than cell chemistry alone.",
            "ESS and affordable EVs often favor LFP, while long-range or performance EVs often favor NCM-family cathodes.",
        ],
    },
    "liquid-vs-solid-electrolyte": {
        "summary": "A comparison of conventional liquid electrolyte cells and solid-state cells.",
        "facts": [
            "Liquid electrolyte is mature, manufacturable, and high-conductivity but flammable and interface-limited.",
            "Solid electrolyte can improve safety and enable lithium-metal or anodeless designs, but interfaces and manufacturing remain difficult.",
            "The comparison links electrolyte, separator, solid-state battery, lithium-metal, dendrite, and ionic conductivity.",
        ],
    },
    "next-gen-battery-overview": {
        "summary": "A map of next-generation battery routes including solid-state, lithium-sulfur, lithium-metal, sodium-ion, LMR, and bipolar designs.",
        "facts": [
            "Next-generation does not mean one chemistry replaces all lithium-ion cells.",
            "Each route solves a different bottleneck: energy density, cost, weight, safety, mineral exposure, or manufacturability.",
            "LG Energy Solution's corpus frames the future as a portfolio of chemistry, form-factor, software, and process innovations.",
        ],
    },
    "wet-vs-dry-electrode": {
        "summary": "A comparison of conventional wet electrode manufacturing and emerging dry electrode processing.",
        "facts": [
            "Wet processing is mature and uniform but solvent drying and recovery add cost, energy use, and floor space.",
            "Dry processing can lower cost and emissions, but uniform mixing, adhesion, porosity, and line speed are difficult.",
            "The comparison is central to manufacturing cost and next-generation process strategy.",
        ],
    },
}


GLOSSARY = {
    "anodeless-battery": ("An anodeless battery starts without a host anode layer; lithium plates onto the anode current collector during charging.", "It can raise energy density but requires extremely stable plating, stripping, pressure, and electrolyte interfaces."),
    "baas": ("BaaS means Battery as a Service: battery value sold through diagnostics, leasing, swapping, life management, or data services.", "It shifts the business focus from selling cells once to managing usable battery performance over time."),
    "battery-passport": ("A battery passport is a digital record of a battery's materials, manufacturing, performance, carbon footprint, and life-cycle history.", "It supports traceability, regulation, second-life decisions, and recycling."),
    "bbu": ("A BBU, or Battery Backup Unit, supplies backup power when the primary power source fails.", "It is critical for data centers, telecom, factories, and grid-connected infrastructure."),
    "bi-cell": ("A bi-cell is a laminated sub-unit used in stacked pouch-cell construction.", "It helps build repeatable electrode-separator units before final stacking."),
    "c-rate": ("C-rate expresses charge or discharge current relative to nominal capacity.", "A 1C discharge empties an ideal cell in about one hour, while higher C-rates increase heat and degradation stress."),
    "cc-cv-charging": ("CC/CV charging uses a constant-current phase followed by a constant-voltage phase.", "It is common for lithium-ion cells because it charges quickly early while limiting overvoltage near full charge."),
    "cei": ("CEI means Cathode Electrolyte Interphase, the interphase that forms on cathode surfaces.", "A stable CEI reduces electrolyte oxidation, gas generation, and transition-metal dissolution."),
    "coin-cell": ("A coin cell is a small button-like cell format widely used for material screening and small electronics.", "In R&D, it provides a fast way to test electrode and electrolyte combinations before scale-up."),
    "coulombic-efficiency": ("Coulombic efficiency is the ratio of discharge capacity to charge capacity in a cycle.", "Small losses accumulate over many cycles, making high efficiency essential for long battery life."),
    "dendrite": ("A dendrite is a needle-like metal deposit that can grow during uneven lithium plating.", "Dendrites can consume lithium, raise resistance, or pierce separators and trigger internal shorts."),
    "dld": ("DLD means Double Layer Slot Die coating, a method that coats two layers with slot-die equipment.", "It can tune electrode architecture and improve manufacturing efficiency or performance."),
    "dod": ("DoD, or Depth of Discharge, indicates how much of a battery's capacity has been used.", "Lower average DoD usually improves cycle life, while deeper cycling extracts more usable energy per cycle."),
    "eaas": ("EaaS means Energy as a Service: customers buy energy outcomes rather than owning every asset directly.", "In battery markets it can combine ESS, software, financing, and operation."),
    "ems": ("EMS means Energy Management System, software that supervises power generation, storage, and load.", "In ESS it coordinates battery dispatch with PCS, BMS, grid rules, and market signals."),
    "gas-free-solvent": ("Gas-free solvent refers to electrolyte solvent design intended to suppress gas generation during cell operation.", "Gas control matters for swelling, safety, lifetime, and high-voltage cathode stability."),
    "internal-resistance": ("Internal resistance is the effective resistance inside a cell that causes voltage drop and heat generation under current.", "It rises with aging, poor contacts, low temperature, and degraded interfaces."),
    "ionic-conductivity": ("Ionic conductivity measures how easily ions move through electrolyte or solid electrolyte.", "High ionic conductivity supports power and fast charging, especially at low temperature."),
    "mah": ("mAh, or milliampere-hour, is a capacity unit equal to current in milliamps multiplied by time in hours.", "It is useful for small cells but must be paired with voltage to compare energy."),
    "mono-cell": ("A mono-cell is a basic laminated electrode-separator unit in stacked pouch-cell assembly.", "It improves handling and alignment before repeated stacking."),
    "pcm": ("PCM means Protection Circuit Module, electronics that protect a battery from overcharge, overdischarge, overcurrent, and short circuits.", "It is common in small packs and complements broader BMS logic."),
    "pcs": ("PCS means Power Conversion System, the inverter/converter hardware that moves power between batteries and AC or DC grids.", "In ESS, PCS translates battery energy into usable grid power."),
    "potential-window": ("The potential window is the voltage range over which an electrolyte or material remains electrochemically stable.", "Exceeding it causes decomposition, gas, interphase growth, or safety problems."),
    "quaternary-battery": ("A quaternary battery commonly refers to a four-element cathode family such as NCMA.", "Adding a fourth element can tune stability, cost, and energy density."),
    "sei": ("SEI means Solid Electrolyte Interphase, the thin layer formed mainly on the anode during early charging.", "A stable SEI passes lithium ions but suppresses continuous electrolyte decomposition."),
    "soc": ("SoC means State of Charge, the estimated remaining charge as a percentage of usable capacity.", "It is a core BMS value for range, power limits, and user display."),
    "soh": ("SoH means State of Health, an estimate of how much battery capability remains compared with a fresh cell.", "It combines capacity fade, resistance growth, power capability, and safety margins."),
    "sox": ("SoX is a family term for state estimators such as SoC, SoH, state of power, and state of safety.", "It reflects the move from simple voltage monitoring to model-based battery diagnosis."),
    "srs": ("SRS is Safety Reinforced Separator, LG Energy Solution's ceramic-coated separator safety technology.", "It strengthens separator heat resistance and helps reduce internal short risk."),
    "ternary-battery": ("A ternary battery uses a three-metal cathode system, usually NCM or NCA-type layered oxides.", "It is associated with higher energy density EV batteries but requires careful safety and cost control."),
    "tp-prevention": ("TP prevention means thermal propagation prevention: design measures that stop one failing cell from spreading heat to neighbors.", "It is a pack-level safety topic involving barriers, vents, cooling, spacing, and detection."),
    "ups": ("UPS means Uninterruptible Power Supply, a system that provides immediate backup power during outages.", "Battery UPS applications value reliability, fast response, BMS control, and periodic health checks."),
}


KEYWORDS = {
    "46-series-battery": ["46시리즈", "4680", "4695", "46120", "cylindrical", "원통형", "Rivian"],
    "avel": ["AVEL", "에이블", "전력망", "재생에너지", "ESS", "VPP", "제주"],
    "azs-stacking": ["AZS", "Advanced Z-Stacking", "Z-Stacking", "스태킹", "라미네이션"],
    "bipolar-technology": ["bipolar", "바이폴라", "반고체"],
    "ford": ["Ford", "포드"],
    "gm": ["GM", "General Motors", "제너럴모터스", "얼티엄셀즈", "Ultium"],
    "high-nickel-battery": ["하이니켈", "high-nickel", "high nickel", "니켈", "NCMA"],
    "honda": ["Honda", "혼다"],
    "hyundai-motor-group": ["Hyundai", "현대", "현대자동차", "현대차"],
    "kooroo": ["KooRoo", "쿠루", "BSS", "Battery Swapping", "교환형", "이륜차"],
    "lfp-battery": ["LFP", "리튬인산철", "인산철", "ESS"],
    "lg-energy-solution": ["LG에너지솔루션", "LG Energy Solution", "LG엔솔"],
    "lithium-metal-battery": ["리튬메탈", "lithium metal", "리튬 금속"],
    "lithium-sulfur-battery": ["리튬황", "Lithium-sulfur", "황", "UAM", "드론"],
    "lmr-battery": ["LMR", "리튬망간리치", "망간리치"],
    "mid-nickel-battery": ["미드니켈", "mid-nickel", "Mid-Ni", "고전압 미드"],
    "nca-battery": ["NCA", "니켈", "코발트", "알루미늄"],
    "ncm-battery": ["NCM", "삼원계", "니켈", "코발트", "망간"],
    "ncma-battery": ["NCMA", "쿼터너리", "사원계", "알루미늄"],
    "qualcomm": ["Qualcomm", "퀄컴", "Snapdragon", "BMS"],
    "rivian": ["Rivian", "리비안", "4695"],
    "sodium-ion-battery": ["소듐", "sodium", "나트륨"],
    "solid-state-battery": ["전고체", "solid-state", "고체전해질", "UCSD"],
    "stellantis": ["Stellantis", "스텔란티스", "NextStar", "넥스트스타"],
    "tesla": ["Tesla", "테슬라", "Megapack", "메가팩", "ESS"],
    "toyota": ["Toyota", "토요타", "도요타"],
    "ultium-cells": ["Ultium", "얼티엄셀즈", "GM", "Ohio", "Tennessee", "테네시", "오하이오"],
    "active-material": ["활물질", "active material", "양극 활물질", "음극 활물질"],
    "anode-materials": ["음극재", "음극", "graphite", "흑연", "silicon", "실리콘"],
    "assembly-process": ["조립 공정", "assembly", "스태킹", "와인딩", "파우치"],
    "battery-management-system": ["BMS", "Battery Management System", "배터리 관리 시스템"],
    "battery-manufacturing": ["제조 공정", "만들기", "공정", "manufacturing"],
    "battery-recycling": ["recycle", "recycling", "재활용", "reuse", "리사이클", "순환"],
    "battery-safety": ["safety", "안전", "열폭주", "thermal runaway", "화재", "TP"],
    "binder": ["binder", "바인더", "결착재"],
    "bmts": ["BMTS", "B.around", "비어라운드", "Battery Management Total Solution"],
    "cathode-materials": ["양극재", "양극", "cathode", "NCM", "LFP", "니켈"],
    "cell-balancing": ["cell balancing", "셀 밸런싱", "balancing"],
    "cell-to-pack": ["CTP", "Cell-To-Pack", "셀투팩"],
    "conductive-additive": ["conductive additive", "도전재", "CNT", "전도성"],
    "critical-minerals": ["광물", "mineral", "니켈", "코발트", "리튬", "망간", "흑연"],
    "current-collector": ["current collector", "집전체", "동박", "알루미늄박"],
    "dry-electrode-process": ["dry electrode", "건식 전극", "건식전극"],
    "electrode-process": ["전극 공정", "electrode", "mixing", "coating", "calendering", "slitting"],
    "electrolyte": ["전해질", "전해액", "electrolyte", "이온전도도"],
    "electrolyte-additive": ["전해액 첨가제", "첨가제", "electrolyte additive"],
    "energy-storage-system": ["ESS", "Energy Storage System", "에너지저장", "전력망", "TR1300"],
    "fast-charging": ["fast charging", "급속충전", "고속충전", "충전"],
    "formation-aging": ["formation", "aging", "활성화", "에이징"],
    "humanoid-robot-battery": ["휴머노이드", "robot", "로봇"],
    "lithium-ion-battery": ["리튬이온", "lithium-ion", "작동 원리", "구조"],
    "pack-process": ["pack", "팩 공정", "모듈", "배터리 팩"],
    "pre-dispersion": ["pre-dispersion", "predispersion", "프리디스퍼전", "분산"],
    "separator": ["separator", "분리막", "SRS"],
    "silicon-anode": ["silicon anode", "실리콘 음극", "실리콘음극", "Si"],
    "uam-battery": ["UAM", "도심항공", "항공", "드론"],
    "welding-process": ["welding", "용접", "tab", "탭"],
    "cathode-tier-comparison": ["하이니켈", "미드니켈", "LFP", "양극재", "cathode"],
    "cell-format-comparison": ["원통형", "파우치", "각형", "cylindrical", "prismatic"],
    "lfp-vs-ncm": ["LFP", "NCM", "리튬인산철", "삼원계"],
    "liquid-vs-solid-electrolyte": ["전해질", "전해액", "고체전해질", "전고체"],
    "next-gen-battery-overview": ["차세대", "전고체", "리튬황", "소듐", "리튬메탈", "LMR"],
    "wet-vs-dry-electrode": ["습식", "wet electrode", "건식 전극", "dry electrode", "전극 공정"],
}


RELATED_SEEDS = {
    "chemistry": ["cathode-materials", "electrolyte", "separator", "battery-safety", "battery-management-system"],
    "manufacturing": ["battery-manufacturing", "electrode-process", "assembly-process", "formation-aging", "pack-process"],
    "ess": ["energy-storage-system", "battery-management-system", "bmts", "lfp-battery", "cell-balancing"],
    "oem": ["lg-energy-solution", "battery-manufacturing", "cell-format-comparison", "ncm-battery", "lfp-battery"],
    "glossary": ["lithium-ion-battery", "battery-management-system", "electrolyte", "battery-safety", "battery-manufacturing"],
}


SPECIAL_RELATED = {
    "lg-energy-solution": ["gm", "ultium-cells", "tesla", "lfp-battery", "solid-state-battery", "battery-manufacturing"],
    "gm": ["lg-energy-solution", "ultium-cells", "lmr-battery", "lfp-battery", "battery-recycling"],
    "ultium-cells": ["gm", "lg-energy-solution", "lfp-battery", "energy-storage-system", "battery-manufacturing"],
    "tesla": ["lg-energy-solution", "energy-storage-system", "lfp-battery", "battery-management-system", "pack-process"],
    "kooroo": ["baas", "bmts", "battery-management-system", "battery-safety", "energy-storage-system"],
    "avel": ["energy-storage-system", "eaas", "ems", "pcs", "lg-energy-solution"],
    "azs-stacking": ["assembly-process", "separator", "mono-cell", "bi-cell", "battery-safety"],
    "solid-state-battery": ["liquid-vs-solid-electrolyte", "lithium-metal-battery", "anodeless-battery", "separator", "dendrite"],
    "lithium-sulfur-battery": ["lithium-metal-battery", "uam-battery", "dendrite", "solid-state-battery", "next-gen-battery-overview"],
    "lfp-battery": ["lfp-vs-ncm", "energy-storage-system", "battery-safety", "cathode-materials", "cell-to-pack"],
    "ncm-battery": ["lfp-vs-ncm", "high-nickel-battery", "ncma-battery", "cathode-materials", "electrolyte-additive"],
    "battery-management-system": ["bmts", "soc", "soh", "cell-balancing", "battery-safety"],
    "energy-storage-system": ["lfp-battery", "pcs", "ems", "bms", "avel", "tesla"],
    "electrolyte": ["electrolyte-additive", "sei", "cei", "ionic-conductivity", "liquid-vs-solid-electrolyte"],
    "battery-safety": ["separator", "srs", "tp-prevention", "battery-management-system", "cell-balancing"],
    "cathode-tier-comparison": ["high-nickel-battery", "mid-nickel-battery", "lfp-battery", "ncm-battery", "cathode-materials", "lfp-vs-ncm"],
    "cell-format-comparison": ["46-series-battery", "azs-stacking", "assembly-process", "cell-to-pack", "pack-process", "battery-safety"],
    "lfp-vs-ncm": ["lfp-battery", "ncm-battery", "cathode-materials", "cathode-tier-comparison", "battery-safety", "energy-storage-system"],
    "liquid-vs-solid-electrolyte": ["electrolyte", "solid-state-battery", "separator", "lithium-metal-battery", "ionic-conductivity", "dendrite"],
    "next-gen-battery-overview": ["solid-state-battery", "lithium-sulfur-battery", "lithium-metal-battery", "sodium-ion-battery", "lmr-battery", "bipolar-technology"],
    "wet-vs-dry-electrode": ["electrode-process", "dry-electrode-process", "battery-manufacturing", "binder", "conductive-additive", "current-collector"],
}


def parse_frontmatter(text: str) -> tuple[dict[str, object], str]:
    match = re.match(r"^---\n(.*?)\n---\n?(.*)$", text, re.S)
    if not match:
        return {}, text
    fm_text, body = match.groups()
    fm: dict[str, object] = {}
    current = None
    for line in fm_text.splitlines():
        if line.startswith("  - ") and current:
            fm.setdefault(current, [])
            assert isinstance(fm[current], list)
            fm[current].append(line[4:].strip())
            continue
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        current = key
        if value == "":
            fm[key] = []
        else:
            fm[key] = value
    return fm, body


def parse_tags(raw: object) -> list[str]:
    if isinstance(raw, list):
        return [str(x) for x in raw]
    value = str(raw or "").strip()
    if value.startswith("[") and value.endswith("]"):
        return [x.strip() for x in value[1:-1].split(",") if x.strip()]
    return [value] if value else []


def sanitize_tags(tags: list[str]) -> list[str]:
    sanitized: list[str] = []
    for tag in tags:
        replacements = TAG_REPLACEMENTS.get(tag, [tag])
        for replacement in replacements:
            if replacement in ALLOWED_TAGS and replacement not in sanitized:
                sanitized.append(replacement)
    return sanitized


def read_raw_posts() -> list[dict[str, str]]:
    posts = []
    for path in sorted(RAW.glob("**/*.md")):
        text = path.read_text(encoding="utf-8")
        fm, body = parse_frontmatter(text)
        rel = path.relative_to(ROOT).as_posix()
        title = html.unescape(str(fm.get("title", "")))
        category = html.unescape(str(fm.get("category", path.parent.name)))
        decoded_path = unquote(rel)
        haystack = f"{title}\n{decoded_path}\n{body[:12000]}"
        posts.append(
            {
                "path": rel,
                "title": title,
                "category": category,
                "text": haystack,
                "title_text": f"{title}\n{decoded_path}",
            }
        )
    return posts


def page_files() -> list[Path]:
    files = []
    for directory in CONTENT_DIRS:
        files.extend(sorted((WIKI / directory).glob("*.md")))
    return files


def slug_for(path: Path) -> str:
    return path.stem


def score_term(text: str, title_text: str, term: str) -> int:
    if not term:
        return 0
    flags = re.I
    escaped = re.escape(term)
    if re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9.+/-]*", term):
        pattern = rf"(?<![A-Za-z0-9]){escaped}(?![A-Za-z0-9])"
    else:
        pattern = escaped
    title_hits = len(re.findall(pattern, title_text, flags))
    body_hits = len(re.findall(pattern, text, flags))
    return title_hits * 12 + body_hits * 2


def terms_for(slug: str, title: str, tags: list[str]) -> list[str]:
    terms = list(KEYWORDS.get(slug, []))
    raw_words = re.split(r"[^A-Za-z0-9+/-]+", f"{slug} {title} {' '.join(tags)}")
    for word in raw_words:
        word = word.strip()
        if len(word) >= 3 and word.lower() not in STOP_TERMS:
            terms.append(word)
    deduped = []
    seen = set()
    for term in terms:
        key = term.lower()
        if key not in seen:
            seen.add(key)
            deduped.append(term)
    return deduped


def select_sources(slug: str, title: str, tags: list[str], posts: list[dict[str, str]], page_type: str) -> list[str]:
    terms = terms_for(slug, title, tags)
    scored = []
    for post in posts:
        score = sum(score_term(post["text"], post["title_text"], term) for term in terms)
        if page_type == "glossary" and "용어사전" in post["title"]:
            score += 4
        if slug in unquote(post["path"]).lower():
            score += 20
        if score > 0:
            scored.append((score, post["path"]))
    scored.sort(key=lambda item: (-item[0], item[1]))

    selected = []
    for _score, path in scored:
        if path not in selected:
            selected.append(path)
        if len(selected) >= 5:
            break

    if selected:
        return selected

    fallback_terms = ["배터리 용어사전"] if page_type == "glossary" else ["LG에너지솔루션", "배터리"]
    for post in posts:
        if any(term in post["text"] for term in fallback_terms):
            selected.append(post["path"])
        if len(selected) >= 3:
            break
    return selected


def choose_related(slug: str, tags: list[str], page_type: str, all_pages: dict[str, dict[str, object]]) -> list[str]:
    chosen = []
    for item in SPECIAL_RELATED.get(slug, []):
        if item in all_pages and item != slug:
            chosen.append(item)

    tag_set = set(tags)
    scored = []
    for other, meta in all_pages.items():
        if other == slug or other in chosen:
            continue
        other_tags = set(meta["tags"])
        score = len(tag_set & other_tags)
        if score:
            scored.append((score, other))
    scored.sort(key=lambda item: (-item[0], item[1]))
    chosen.extend(other for _score, other in scored[:8])

    if page_type == "glossary":
        chosen.extend(x for x in RELATED_SEEDS["glossary"] if x in all_pages and x != slug)
    if "ess" in tag_set:
        chosen.extend(x for x in RELATED_SEEDS["ess"] if x in all_pages and x != slug)
    if any(t in tag_set for t in ("electrode", "assembly", "formation", "aging", "welding", "dry-electrode")):
        chosen.extend(x for x in RELATED_SEEDS["manufacturing"] if x in all_pages and x != slug)
    if page_type == "entity" and not any(t in tag_set for t in ("lfp", "ncm", "nca", "ncma", "solid-state")):
        chosen.extend(x for x in RELATED_SEEDS["oem"] if x in all_pages and x != slug)
    chosen.extend(x for x in RELATED_SEEDS["chemistry"] if x in all_pages and x != slug)

    deduped = []
    seen = set()
    for item in chosen:
        if item != slug and item in all_pages and item not in seen:
            seen.add(item)
            deduped.append(item)
    for other in sorted(all_pages):
        if len(deduped) >= 6:
            break
        if other != slug and other not in seen:
            deduped.append(other)
            seen.add(other)
    return deduped[:6]


def wiki_link(slug: str, all_pages: dict[str, dict[str, object]]) -> str:
    title = str(all_pages[slug]["title"])
    return f"[[{slug}|{title}]]"


def sentence_list(items: list[str]) -> str:
    if len(items) == 1:
        return items[0]
    if len(items) == 2:
        return f"{items[0]} and {items[1]}"
    return f"{', '.join(items[:-1])}, and {items[-1]}"


def body_for(slug: str, title: str, page_type: str, tags: list[str], related: list[str], sources: list[str], all_pages: dict[str, dict[str, object]]) -> str:
    note = NOTES.get(slug)
    if page_type == "glossary" and slug in GLOSSARY:
        definition, why = GLOSSARY[slug]
        note = {
            "summary": definition,
            "facts": [
                why,
                "In practical battery work, the term is useful because it connects a measurable behavior to design decisions in materials, manufacturing, BMS, or pack operation.",
                "Use it as a compact handle, then follow the related concept pages for the deeper electrochemistry or system design.",
            ],
        }
    if not note:
        note = {
            "summary": f"{title} is a wiki node in the LG Energy Solution battery knowledge base.",
            "facts": [
                "It is included because the raw corpus repeatedly connects the topic to battery materials, manufacturing, applications, or business strategy.",
                "Read it through the neighboring pages rather than as an isolated definition.",
                "The page is intentionally compact so an LLM can use it as a high-signal retrieval unit.",
            ],
        }

    related_links = [wiki_link(item, all_pages) for item in related[:5]]
    nearby = sentence_list(related_links[:3])
    source_note = sentence_list([f"`{Path(src).name}`" for src in sources[:3]]) if sources else "the raw LG Energy Solution posts"

    if page_type == "comparison":
        rows = "\n".join(f"- {fact}" for fact in note["facts"])
        body = f"""# {title}

## Core Idea
{note["summary"]} The useful way to read this comparison is through {nearby}.

## Decision Frame
{rows}

## How To Use This Page
Use this page as a routing node. If the question is about chemistry fundamentals, continue to {wiki_link(related[0], all_pages)} or {wiki_link(related[1], all_pages)}. If the question is about commercialization, check {wiki_link(related[2], all_pages)} and {wiki_link(related[3], all_pages)}. The source set includes {source_note}.

## Related
"""
    elif page_type == "glossary":
        rows = "\n".join(f"- {fact}" for fact in note["facts"])
        body = f"""# {title}

## Definition
{note["summary"]}

## Why It Matters
{rows}

## In The LG Energy Solution Corpus
The term is used as a precise retrieval handle for posts about {nearby}. The source set includes {source_note}.

## Related
"""
    elif page_type == "entity":
        rows = "\n".join(f"- {fact}" for fact in note["facts"])
        body = f"""# {title}

## Snapshot
{note["summary"]} In this wiki, it is cross-referenced with {nearby}.

## What To Remember
{rows}

## LG Energy Solution Context
The source set treats this page as part of LG Energy Solution's battery ecosystem: products, partners, chemistries, process capability, software, and life-cycle management. The most relevant raw posts selected for this page include {source_note}.

## Related
"""
    else:
        rows = "\n".join(f"- {fact}" for fact in note["facts"])
        body = f"""# {title}

## Core Idea
{note["summary"]} It connects directly to {nearby}.

## Technical Notes
{rows}

## LG Energy Solution Context
In the raw corpus, this concept appears as a practical engineering lever rather than a standalone textbook term. It affects how LG Energy Solution balances performance, safety, manufacturability, cost, and customer requirements. The source set includes {source_note}.

## Related
"""

    for item in related[:6]:
        body += f"- {wiki_link(item, all_pages)}\n"
    return body.rstrip() + "\n"


def serialize_frontmatter(
    title: str,
    page_type: str,
    tags: list[str],
    sources: list[str],
    confidence: str,
    *,
    created: str | None = None,
) -> str:
    lines = [
        "---",
        f"title: {title}",
        f"created: {created or TODAY}",
        f"updated: {TODAY}",
        f"type: {page_type}",
        f"tags: [{', '.join(tags)}]",
        "sources:",
    ]
    for src in sources:
        lines.append(f"  - {src}")
    lines.append(f"confidence: {confidence}")
    lines.append("---")
    return "\n".join(lines) + "\n"


def build_page_registry(files: list[Path]) -> dict[str, dict[str, object]]:
    pages: dict[str, dict[str, object]] = {}
    for path in files:
        text = path.read_text(encoding="utf-8")
        fm, _body = parse_frontmatter(text)
        slug = slug_for(path)
        title = str(fm.get("title") or slug.replace("-", " ").title())
        title = TITLE_OVERRIDES.get(slug, title)
        tags = sanitize_tags(parse_tags(fm.get("tags")))
        page_type = str(fm.get("type") or path.parent.name[:-1])
        pages[slug] = {"path": path, "title": title, "tags": tags, "type": page_type}
    return pages


def write_pages(*, preserve_body: bool = False) -> None:
    posts = read_raw_posts()
    files = page_files()
    pages = build_page_registry(files)
    for slug, meta in sorted(pages.items()):
        title = str(meta["title"])
        tags = list(meta["tags"])
        page_type = str(meta["type"])
        sources = select_sources(slug, title, tags, posts, page_type)
        confidence = "high" if len(sources) >= 2 else "medium"
        path = Path(meta["path"])
        created = None
        if preserve_body:
            existing_frontmatter, body = parse_frontmatter(path.read_text(encoding="utf-8"))
            created = str(existing_frontmatter.get("created") or TODAY)
            body = body.lstrip("\n")
        else:
            related = choose_related(slug, tags, page_type, pages)
            body = body_for(slug, title, page_type, tags, related, sources, pages)
        text = serialize_frontmatter(
            title,
            page_type,
            tags,
            sources,
            confidence,
            created=created,
        ) + body
        Path(meta["path"]).write_text(text, encoding="utf-8")


def write_index_and_log(*, preserve_body: bool = False) -> None:
    files = page_files()
    pages = build_page_registry(files)
    raw_count = len(list(RAW.glob("**/*.md")))
    by_type: dict[str, list[str]] = {"entity": [], "concept": [], "comparison": [], "glossary": []}
    for slug, meta in pages.items():
        by_type[str(meta["type"])].append(slug)
    for slugs in by_type.values():
        slugs.sort()

    lines = [
        "---",
        "title: Index",
        f"created: {TODAY}",
        f"updated: {TODAY}",
        "type: meta",
        "tags: [meta]",
        "---",
        "",
        "# Index - LG Energy Solution Battery Wiki",
        "",
        f"Compiled from {raw_count} official-source markdown records into 95 English wiki pages. See [[SCHEMA]] for schema rules and [[log]] for the compilation log.",
        "",
        "| Category | Count |",
        "|---|---:|",
        f"| Entities | {len(by_type['entity'])} |",
        f"| Concepts | {len(by_type['concept'])} |",
        f"| Comparisons | {len(by_type['comparison'])} |",
        f"| Glossary | {len(by_type['glossary'])} |",
        f"| Total | {sum(len(v) for v in by_type.values())} |",
        "",
    ]
    headings = {
        "entity": "Entities",
        "concept": "Concepts",
        "comparison": "Comparisons",
        "glossary": "Glossary",
    }
    for page_type, heading in headings.items():
        lines.append(f"## {heading}")
        lines.append("")
        for slug in by_type[page_type]:
            meta = pages[slug]
            note = NOTES.get(slug)
            if page_type == "glossary" and slug in GLOSSARY:
                summary = GLOSSARY[slug][0]
            elif note:
                summary = str(note["summary"])
            else:
                summary = f"{meta['title']} in the LG Energy Solution battery knowledge base."
            lines.append(f"- [[{slug}|{meta['title']}]] - {summary}")
        lines.append("")
    (WIKI / "index.md").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")

    final_log_line = (
        "- Preserved existing long-form page bodies while updating their source selections."
        if preserve_body
        else "- Replaced page bodies with the compiler's compact generated summaries."
    )
    log_text = f"""---
title: Compilation Log
created: {TODAY}
updated: {TODAY}
type: meta
tags: [meta]
---

# Compilation Log

## {TODAY}

- Read {raw_count} raw markdown records under `raw/` for local source matching.
- {"Refreshed source lists on" if preserve_body else "Rebuilt"} 95 English wiki pages under `entities/`, `concepts/`, `comparisons/`, and `glossary/`.
- Added YAML frontmatter with title, type, tags, sources, and confidence on every content page.
- Added at least five outbound `[[wikilinks]]` per content page and regenerated [[index]].
- Rebuilt `server/data/graph.json` after page population.
{final_log_line}
"""
    (WIKI / "log.md").write_text(log_text, encoding="utf-8")


def validate() -> int:
    files = page_files()
    pages = build_page_registry(files)
    all_slugs = set(pages)
    errors = []
    if len(files) != 95:
        errors.append(f"expected 95 content pages, found {len(files)}")
    type_counts = Counter(str(meta["type"]) for meta in pages.values())
    expected = Counter({"entity": 27, "concept": 30, "comparison": 6, "glossary": 32})
    if type_counts != expected:
        errors.append(f"type counts differ: {dict(type_counts)}")

    for slug, meta in pages.items():
        path = Path(meta["path"])
        text = path.read_text(encoding="utf-8")
        fm, body = parse_frontmatter(text)
        for key in ("title", "type", "tags", "sources"):
            if key not in fm or fm.get(key) in ("", []):
                errors.append(f"{path}: missing {key}")
        sources = fm.get("sources", [])
        if not isinstance(sources, list) or not sources:
            errors.append(f"{path}: no sources list")
        else:
            for src in sources:
                if not (ROOT / str(src)).exists():
                    errors.append(f"{path}: missing source {src}")
        links = re.findall(r"\[\[([^\]|#]+)", body)
        distinct = {link for link in links if link in all_slugs and link != slug}
        if len(distinct) < 5:
            errors.append(f"{path}: only {len(distinct)} distinct outbound page links")
        if len(body.strip()) < 500:
            errors.append(f"{path}: body too short")
        if re.search(r"[\uac00-\ud7af\u1100-\u11ff\u3130-\u318f]", body):
            errors.append(f"{path}: Korean text remains in body")

    index = (WIKI / "index.md").read_text(encoding="utf-8")
    for slug in sorted(all_slugs):
        if f"[[{slug}|" not in index and f"[[{slug}]]" not in index:
            errors.append(f"index missing {slug}")
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(f"OK: {len(files)} pages, counts {dict(type_counts)}, all sources and wikilinks validated")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--preserve-body",
        action="store_true",
        help="Refresh source frontmatter without replacing existing wiki bodies",
    )
    args = parser.parse_args()
    write_pages(preserve_body=args.preserve_body)
    write_index_and_log(preserve_body=args.preserve_body)
    result = validate()
    if result == 0:
        subprocess.run(["python3", str(ROOT / "scripts" / "build_graph.py")], check=True)
    return result


if __name__ == "__main__":
    raise SystemExit(main())
