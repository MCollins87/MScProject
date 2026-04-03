# Introduction

Delivering timely cancer care remains a critical priority within the NHS, where delays at any stage of the diagnostic and treatment pathway can negatively affect patient outcomes, experience, and service performance. Recent policy reforms have consolidated the NHS Cancer Waiting Time (CWT) framework into three outcome-focused standards: 28-day Faster Diagnosis Standard (FDS); 31-day decision-to-treat to treatment (DTT); and 62-day referral to treatment (RTT) - implemented nationally from October 2023 [@johnson2024; @NHSDigital2026]. These standards place an increased emphasis on the need for operational viability, rapid decision-making, and efficient progression of patients through the post-MDT (multidisciplinary team) stages of the oncology pathway. However, many Trusts continue to face systemic challenges in generating timely, accurate, and actionable insights from fragmented data sources. 

Within Portsmouth Hospitals University NHS Trust, as in many NHS institutions, key operational data concerning MDT outcomes, clinic scheduling, booking practices, and treatment initiation remain dispersed across siloed systems. Although these systems individually support MDT coordination, outpatient clinic management, and treatment delivery, they lack a consolidated view of pathway performance. This fragmentation makes it difficult for operational managers to detect bottlenecks, identify emerging breach risks, or allocate clinical capacity efficiently. As a result, delays between **MDT outcomes, first oncology clinic, decision-to-treat** and **first definitive treatment** remain insufficiently visible, impairing the Trust's ability to monitor compliance with the 31 and 62 day standards and respond rapidly to operational pressures. 

## Problem Statement

The central problem addressed in this research is the absence of an integrated, operationally focused data infrastructure and decision-support interface to illuminate post-MDT workflow delays and guide timely interventions within an NHS oncology service. Despite the availability of relevant data, the lack of integration and harmonisation across MDT, clinic, and treatment systems results in manual workarounds, inconsistent performance monitoring, and delayed insights. This gap diminishes the ability of operational teams to identify patients at risk of breaching national cancer standards, understand the factors driving variability in pathway intervals, and proactively manage capacity constrained environments. 

Moreover, existing reporting solutions tend to focus on aggregate compliance metrics rather than providing real-time or near real-time visibility of operational bottlenecks. Without a unified source of truth that aligns event definitions, timestamps, and clinical coding standards [@NHSDigital2026], it becomes difficult to execute performance analysis or support day-to-day decision-making. Literature on Integrated Data Repositories (IDRs) similarly highlights that many institutions struggle with data harmonisation, terminological alignment, and the creation of analytics-ready architectures capable of supporting both research and operational use cases [@gagalova2020]. 

This study therefore seeks to design, develop, and evaluate a **lightweight Integrated Data Repository (IDR)** and accompanying **decision-support dashboard** tailored specifically to the Post-MDT oncology workflow. By integrating key pathway events, clinic capacity information, and national standard definitions, the artefact aims o surface bottlenecks, highlight breach risks, and support operational teams in prioritising actions that improve pathway performance. 

## Research Aim and Objectives

The overarching aim of this research is to apply Design Science Research (DSR) methods to create and evaluate an IDR-backed dashboard that enhances operational decision-making in post-MDT oncology pathways. The study seeks to generate both a practical artefact - an integrated warehouse plus a usable dashboard - and generalised design knowledge concerning IDR architectures and decision-support principles suitable for NHS operational analytics. 

The specific objectives are to:

1. identify, quantify, and interpret delays within the MDT-to-treatment pathway. 
2. Design and implement an IDR architecture that consolidates and harmonises data from MDT, clinic scheduling and treatment systems. 
3. Develop a decision-support dashboard aligned with ISO 9241-110 usability principles to surface actionable operational insights. 
4. Evaluate the artefacts usibality, utility, and technical validity through task-based experiments, heuristic analysis, and metric reconciliation.
5. Derive transferable design principles and architecture guidance for NHS oncology operational analytics. 

## Design Science Methodology

This dissertation adopts the Design Science Research (DSR) paradigm, a well-established approach for solving complex, real-world problems through the creation and evaluation of innovative artefacts [@hevner2004]. DSR is especially suited to healthcare informatics contexts where organisational, data and process challenges intersect, and where practical solutions must be both rigorously designed and empirically evaluated.

The research follows the six-activity Design Science Research Methodology (DSRM) proposed by @Peffers2007 :

1. **Problem identification and motivation** - identifying post-MDT workflow delays and the need for integrated information. 
2. **Define objectives for the solution** - specifying analytic, architectural, and usability requirements for an IDR-backed dashboard.
3. **Design and development** - constructing the IDR, data transformation pipelines, and dashboard view.
4. **Demonstration** - deploying the artefact with real Trust data to show how it addresses operational problems. 
5. **Evaluation** - measuring usability, utility, and technical accuracy using multi-method evaluation. 
6. **Communication** - producing a dissertation delivering both artefact and design knowledge contributions.

This structured methodology ensures that the work moves beyond a local service-improvement project to make a scholarly contribution to the fields of operational analytics, IDR design, and health informatics within NHS settings. 

## Academic and Practical Significance

Academically, the research contributes to the limited body of DSR-grounded studies focussing on NHS operational analytics, offering:
- an IDR reference architecture for oncology operations;
- a set of design principles for NHS-appropriate decision-support dashboards;
- an evaluation protocol combining usability metrics, decision-quality testing, and technical verification. 

Practically, the artefact provides operational teams with a tool that can:
- reduce time-to-insight;
- support rapid identification and bottlenecks and breach risks;
- align capacity planning with demand; 
- improve pathway monitoring in line with the 28/31/62-day standards.

Ultimately, the study aims to support faster, more reliable progression from MDT decision to treatment initiation - directly contributing to improved patient care and more effective management of oncology services. 