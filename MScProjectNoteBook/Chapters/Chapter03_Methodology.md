## Overview of Research Design

This research adopts a Design Science Research (DSR) methodology to address an operational problem in NHS oncology services: the lack of integrated, actionable visibility of delays between MDT outcomes and treatment initiation. DSR is particuarly suitable for this study because it explicitly focuses on the design, construction, and evaluation of an artefact intended to improve a real-world organisational context, while generating transferable design knowledge [@hevner2004]. 

The primary artefact developed in this study is a lightweight integrated data repository (IDR) ad decision-support dashboard, designed to consolidate post-MDT pathway data and support operational decision-making. In addition to the artefact itself, the research produces a set of evaluated design principles for oncology operational analytics, constituting a contribution to knowledge beyond the local implementation. 

## Design Science Research Framework

The study follows the Design Science Research Methodology (DSRM) proposed by @Peffers2007, which structures DSR into six interrelated activities. These activities are applied iteratively rather than strictly linearly. 

### Problem Identification and Motivation
The problem was identified through:
- analysis of NHS cancer waiting time standards and performance pressures [@johnson2024; @NHSDigital2026],
- review of literature on MDT operational inefficiencies and pathway delays,
- practical experience with Portsmouth Hospitals University NHS Trust.
The central problem is the absence of an integrated, operationally focused data infrastructure that aligns MDT outcome, clinic scheduling, and treatment delivery data into a single, trusted view capable of supporting proactive action. 

### Objectives of a Solution
The objectives of the solution were derived from both literature synthesis and stakeholder needs, and include:
- consolidating post-MDT pathway events into a harmonised, analytics-ready data model;
- enabling early identification of patients at risk of breaching the 31- and 62-day standards;
- aligning operational risk signals with actionable capacity information;
- supporting rapid, routine decision-making through a usable dashboard interface;
- complying with NHS data governance and national metric definitions.
These objectives directly inform the design principles articulated in Section ==3.4== and implemented in the artefact.

### Design and Development
The design and development activity involved two tightly coupled components:
1. Integrated Data Repository (IDR)
2. Decision-Support Dashboard
The IDR adopts a general-model architecture consisting of a staging layer for ETL and harmonisation, a central warehouse, and an application layer for analytics and visualisation, consistent with IDR literature for single-institution deployments [@gagalova2020].

The dashboard is designed to support operational tasks rather than retrospective reporting, aligning with the role of operational dashboards in healthcare performance management [@buttigieg2017]. 

Both components were developed iteratively, guided by explicit design principles derived from prior research and refined during prototyping. 

### Demonstration
The artefact is demonstrated using:
- retrospective Trust data covering MDT decisions, clinic appointments, and treatment initiation;
- realistic operational scenarios reflecting common management tasks (e.g., identifying upcoming breach risks, assessing clinic capacity).
Demonstration focuses on illustrating how the artefact supports decision-making that was previously manual, fragmented, or retrospective.

### Evaluation
Evaluation is multi-method and aligned with @hevner2004's guidance that DSR artefacts must be assessed for utility, quality, and efficacy. Evaluation methods are detailed in Section ==3.5==.

### Communication
The final activity consists of communicating:
- the artefact,
- its measured effects, and
- the derived design principles,
through this dissertation, targeting both academic and and practitioner audiences. 

## Research Questions and Method Alignment
| Research Question                                                   | DSR Activity           | Primary Methods                               |
| ------------------------------------------------------------------- | ---------------------- | --------------------------------------------- |
| RQ1: Where do delays occur between MDT outcome and treatment?       | Problem identification | Descriptive statistics, interval analysis     |
| RQ2: What operational factors predict extended delays?              | Problem analysis       | Regression and capacity analysis              |
| RQ3: Does the artefact improve operational decision-making?         | Evaluation             | Task-based testing, time-to-answer, accuracy  |
| RQ4: What design principles support post-MDT operational analytics? | Design knowledge       | Literature synthesis and evaluation synthesis |
This mapping ensures methodological coherence between the research questions, artefact, and evaluation. 

## Design Principles
Design principles represent the design knowledge contribution of this study. They are formulated using a standard DSR structure: _context_, _intervention_, and _rationale_. These initial principles are refined following evaluation.

### DP1: Surface Breach Risks as a Leading Indicator
If operational teams must prioritise actions in time-constrained cancer pathways, then dashboards should surface leading indicators of breach risk (e.g. days remaining to breach thresholds), because prospective visibility enables earlier and more effective intervention than retrospective compliance metrics. 

### DP2: Pair Risk Information with Actionable Capacity Data
If users are expected to act on identified risks, then risk indicators should be presented alongside relevant capacity and demand information, because risk awareness without visible operational levers does not support decision-making.

### DP3: Use Canonical, Standard-Aligned Pathway Events
If pathway metrics are to be trusted and comparable, then all intervals should be derived from canonical event definitions aligned to NCWTMDS rules, because inconsistent definitions undermine credibility and evaluation validity. 

### DP4: Match Data Refresh Cadence to the Action Horizon
If decisions depend on short operational windows, then data refresh frequency should be aligned to the decision horizon (e.g. daily or near–real-time where feasible), because stale information degrades decision quality.

### DP5: Preserve Data Provenance and Auditability
If analytics are deployed in regulated healthcare environments, then all derived metrics must maintain transparent provenance to source systems, because trust, governance, and reconciliation are essential for adoption.

### DP6: Align Interaction Design with Real Operational Tasks
If dashboards are intended to support complex operational work, then interaction design should reflect users’ real task sequences, because task-aligned interfaces reduce cognitive load and improve decision quality [@ISO9241-2020].

These principles directly inform both the IDR architecture and the dashboard design, and serve as evaluation criteria in Section 3.5.

## Evaluation Strategy

Evaluation combines formative and summative methods across four dimensions.

### Usability Evaluation
- System Usability Scale (SUS)
- Heuristic review grounded in ISO 9241‑110
- Think-aloud walkthroughs

### Utility and Effectiveness
- Task-based experiment with operational users
- Primary measures:
    - time-to-answer key operational questions,
    - accuracy of breach-risk identification,
    - decision quality in constrained scheduling scenarios

### Technical Validity
- Reconciliation of dashboard metrics with source SQL queries
- Validation of interval derivations against NCWTMDS rules

### Design Knowledge Evaluation
- Synthesis of user feedback and performance outcomes
- Refinement and confirmation of final design principles

## Ethical and Governance Considerations
The study operates within UK GDPR and NHS data governance requirements. All data are de-identified or pseudonymised, with access controls and separation between operational and research use. The project follows university ethics procedures and local Trust information governance guidance.

## Summary
This chapter has outlined a rigorous, design-science-based methodology that supports both artefact creation and theory-driven knowledge contribution. By embedding explicit design principles within the DSR framework and evaluating the artefact using multiple complementary methods, the study ensures methodological robustness, practical relevance, and academic contribution.

## Table 3.X: Design Principles for Post‑MDT Operational Analytics in NHS Oncology

|ID|Design Principle|Context|Prescriptive Design Rule|Rationale / Intended Mechanism|Artefact Instantiation|Evaluation Link|
|---|---|---|---|---|---|---|
|**DP1**|Breach risk as a first‑class signal|NHS oncology pathways are governed by strict time‑bound standards (31‑ and 62‑day), requiring proactive intervention before breaches occur|If operational managers must prioritise actions in post‑MDT pathways, **then dashboards should surface leading indicators of breach risk**, not only retrospective compliance metrics|Prospective breach visibility enables earlier intervention, prioritisation of high‑risk patients, and improved decision quality under time constraints|Post‑MDT tracker displaying elapsed days and days‑to‑breach counters, colour‑coded against 31‑/62‑day thresholds|Task‑based testing: accuracy of breach‑risk identification; time‑to‑answer metrics|
|**DP2**|Couple risk with actionable capacity information|Operational users require not only awareness of risk but insight into what actions are feasible within capacity constraints|If users are expected to act on identified risks, **then risk indicators must be paired with relevant capacity and demand information** (e.g. clinic slots, utilisation)|Risk awareness without visible operational levers limits the ability to translate insight into action|Risk panels displayed alongside clinic capacity, utilisation heatmaps, and next‑available slot indicators|Decision‑quality scoring in constrained scheduling scenarios|
|**DP3**|Canonical pathway event definitions|Oncology pathway data originate from heterogeneous systems with inconsistent timestamps and definitions|If pathway metrics are to be trusted and comparable, **then all intervals must be derived from canonical event definitions aligned to NCWTMDS**|Standardised event derivation ensures metric credibility, governance compliance, and evaluation validity|Harmonised MDT date, first oncology clinic, DTT, and first definitive treatment events in the IDR schema|Technical validation through reconciliation with NCWTMDS‑aligned SQL|
|**DP4**|Data refresh cadence aligned to action horizon|Operational decisions are time‑sensitive, particularly in the MDT‑to‑clinic window|If decisions depend on short operational windows, **then data refresh frequency should match the decision horizon** (daily or near‑real‑time where feasible)|Timely data reduces decision latency and avoids actions based on stale information|Daily baseline refresh with optional higher‑frequency sync for MDT‑to‑clinic tracking|User feedback on timeliness; qualitative utility assessment|
|**DP5**|Transparent data provenance and auditability|NHS operational analytics operate within regulated, high‑scrutiny environments|If analytics are used for operational management and compliance monitoring, **then all derived metrics must retain traceable provenance to source systems**|Transparent lineage builds trust, supports governance, and enables dispute resolution when metrics are challenged|Per‑metric lineage metadata; auditable ETL transformations; reproducible SQL definitions|Metric reconciliation success rate; user trust feedback|
|**DP6**|Task‑aligned interaction design|Operational users perform sequential, goal‑oriented tasks under cognitive load|If dashboards are intended to support complex operational decision‑making, **then interaction design should align with real user task structures**, consistent with ISO 9241‑110|Task‑aligned interfaces reduce cognitive burden, improve learnability, and enhance decision accuracy|Task‑driven dashboard layout reflecting identify‑risk → assess‑capacity → decide‑action workflow|SUS score; heuristic evaluation mapped to ISO 9241‑110 principles|

---