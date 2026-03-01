# Project Working Title

Post-MDT Oncology Workflow Bottlenecks: A Design-Science Study of an NHS Integrated Data Repository and Decision-Support Dashboard to Reduce Delays from MDT Outcome to Treatment Start.

# Problem and Significance

Timely progression from multidisciplinary team (MDT) decision to first Oncology clinic and treatment start is central to the three NHS Cancer Waiting Time Standards implemented from 1st October 2023: 1. 28-day Faster Diagnosis Standard (FDS); 2. 31-day decision-to-treat (DTT) to treatment; and 3. 62-day referral-to-treatment. The updated framework prioritises outcomes over process targets and explicitly emphasises rapid diagnosis and starts for the referral routes  [@johnson2024; @NHSDigital2026]. 

Within this context, many Trusts still lack a consolidated, actionable view of post-MDT delays (MDT outcome -> first oncology clinic -> DTT -> first definitive treatment). Data exists in siloed systems (MDT coordination, clinic scheduling, treatment), but are rarely integrated for operational decision support. 

This study addresses that gap by designing, implementing and evaluating a lightweight Integrated Data Repository (IDR) pus a decision-support dashboard tailored to the post-MDT pathway. The IDR is scoped to the Trust setting and informed by contemporary IDR architecture reviews and NHS-proven integration patterns (e.g. CogStack's "right data, right place, right time") [@gagalova2020; @jackson2018]

# Academic Contribution

The project is framed as Design Science Research (DSR). It contributes:

1. An IDR reference design for NHS oncology operations (a general IDR with a staging layer and central warehouse), including practical choices for terminology mapping, updates cadence, privacy/pseudonymisation, and and an evaluation-ready data model aligned to post-MDT events [@gagalova2020]. 
2. A set of actionable design principles for operational cancer dashboards in NHS settings (e.g. breach-risk surfacing; capacity-demand alignment; time-to-action information architecture), explicitly grounded in ISO 9241-110 interaction principles for usability and decision support [@ISO9241-2020].
3. An evaluation protocol that measures utility (task performance and decision quality), usibility (SUS/heuristics), and technical validity (metric reconciliation to source SQL/NCWTMDS rules), providing empirical evidence of improvement over current practice [@johnson2024]. 
4. A synthesis of DSR guidance applied to NHS operational analytics (Henver's DSR guidelines; Peffers' six-activity DSRM) demonstrating a rigorous and replicable pathway from problem to artefact to evaluation [@hevner2004; @Peffers2007].

Collectively, these elevate the work from a service-improvement project to a research contribution: (a) design knowledge (principles), (b) an evaluated instantiation (IDR+dashboard), and (c) evidence of effects on task and decision outcomes. 

# Research Questions (RQs)

**Primary RQ (descriptive/associative):**

Where do delays occur between MDT outcome and first oncology clinic appointment, and how strongly are these intervals associated with 31‑day and 62‑day performance? [@johnson2024]

**RQ2 (explanatory):**

Which operational factors (e.g., clinic slot availability, consultant caseload distribution, booking intervals) most strongly predict extended MDT->clinic waits and increased breach risk?

**RQ3 (intervention / measurable):**

To what extent does the IDR‑backed dashboard improve managers’ ability to (a) identify bottlenecks, (b) prioritise actions, and (c) monitor impact—measured by **time‑to‑answer** key pathway questions, **accuracy** of breach‑risk identification, and **decision quality** in task‑based testing versus current practice?

**RQ4 (design knowledge):**

What design principles and IDR architectural choices (data model, update cadence, privacy controls) are necessary and sufficient to support post‑MDT operational decision‑making in an NHS Trust?

# Theoretical and Methodological Framing

## Design Science Research (DSR) anchor

The project follows @hevner2004 (design-science guidance) and @Peffers2007 (six-activity DSRM: problem identification; objectives; design/development; demonstration; evaluation; communication).

## Operational analytics and IDR foundations

- **IDR architecture models:** general (centralised with staging), biobank‑driven, user‑controlled application layer, federated; small/medium institutions typically succeed with the general model plus a staging layer for ETL and harmonisation [@gagalova2020].
- **Terminologies & CDMs:** widespread use of ICD‑10, SNOMED CT, LOINC, CPT/RxNorm; common data models include i2b2 and OMOP (emerging adoption), aiding interoperability and queryability [@gagalova2020].
- **Update cadence:** varies from daily to near real‑time depending on use case (near real‑time for CDSS; 15‑minute syncs observed in some i2b2 deployments) [@gagalova2020].
- **Governance and privacy:** honest‑broker patterns, de‑identification/pseudonymisation with parallel identifiable stores where appropriate; strong data‑flow controls in federated settings [@gagalova2020].

## NHS-proven integration patterns for unstructured/operational data

CogStack [@jackson2018] demonstrates cost‑effective ingestion of structured and unstructured clinical data with de‑identification and Elasticsearch/Kibana for rapid retrieval and dashboards—the “3R” principle: right data, right place, right time. Lessons include batch/near‑real‑time synchronisation, OCR limits, and governance tiers (identifiable/pseudonymised/anonymised).

# Scope, Setting and Participant Involvement

-  **Setting:** Portsmouth Hospitals University NHS Trust (post‑MDT oncology pathways).
- **Stakeholders:** oncology service managers, MDT coordinators, booking teams; an interested Clinical Oncologist (informal interview plus task‑based evaluation).
- **Systems landscape:** MDT coordination, clinic scheduling/diary, treatment systems; scope to consider **Oracle EBS** (where relevant) at a high level for integration boundaries (master data; resource/rota interfaces).

# Artefact: IDR-Backed Post-MDT Dashboard

## IDR architecture (target state)

Adopt the general IDR model with staging/ETL → central warehouse → application layer (dashboard/API). This matches the study’s single‑institution scope, supports terminologies, and enables controlled sync frequencies [@gagalova2020].

- **Data types:** timestamped pathway events (MDT date & outcome, first oncology clinic, DTT, first treatment), clinic session/slot capacity and utilisation, basic demographics (de‑identified).
- **Terminology & definitions:** align event definitions and codes to **NCWTMDS** and national guidance for consistency with the 28/31/62‑day standards [@NHSDigital2026].
- **CDM options:** pragmatic star schema for the dissertation, with mapping “stubs” to i2b2/OMOP to support portability (documented as design principle rather than full migration) [@gagalova2020].
- **Update cadence:** daily baseline; capability to prototype **hourly** sync for the MDT→clinic tracker page if feasible [@gagalova2020]
- **Privacy & governance:** de‑identification/pseudonymisation at source with unique pathway IDs; honest‑broker pattern separating research/operational access; per‑role access control [@gagalova2020].
- **Unstructured data (optional extension):** if useful, apply CogStack‑style ingestion for free‑text MDT notes (de‑identified) to surface reasons for deferment/case complexity (time permitting) [@jackson2018].

## Dashboard design (views and principles)

- **Post‑MDT tracker:** live cohort of patients with **MDT→clinic** elapsed days, colour‑coded risk against 31/62‑day clocks [@johnson2024].
- **Capacity pane:** slot supply vs demand; **utilisation** by clinic/consultant; **next available** capacity for post‑MDT bookings.
- **Interval heatmaps/control charts:** MDT→clinic, clinic→DTT, DTT→treatment by tumour site/consultant/time.
- **Standards panel:** run charts for 31/62‑day performance.  
    Design adheres to **ISO 9241‑110** (task appropriateness, self‑descriptiveness, controllability, error tolerance, expectation conformity, customisability, learnability) [@ISO9241-2020].


# Data, variables, and Data Quality

## Key intervals and KPI's

- **Intervals:** MDT→Clinic; Clinic→DTT; DTT→Treatment; Referral→Treatment (where available).
- **KPIs:** 31‑day and 62‑day standards; proportion near breach thresholds.[@johnson2024]

### 7.2 Data quality strategy (explicit)

- **Conformance:** enforce NCWTMDS event rules; reject/flag invalid date orders; derive canonical event per pathway [@NHSDigital2026].
- **Completeness:** quantify % missing per field/event; escalate >X% missing for a tumour group; no silent imputation for regulatory events [@NHSDigital2026].
- **Consistency & de‑duplication:** deterministic rules to reconcile duplicates across booking/treatment systems; audit trail of resolution steps.
- **Timestamp reliability:** sensitivity analyses excluding incomplete timestamp subsets; report effect sizes with/without exclusions.
- **Provenance:** per‑record data lineage to source table/refresh cycle.

# Analysis Plan (specific and measurable)

1.  **Descriptive and SPC:** medians/IQRs; XmR/p‑charts of interval stability by tumour group/consultant/time.
2. **Variation & capacity:** funnel plots (clinic/session‑level) and utilisation heatmaps to find under/over‑capacity and demand‑slot mismatch.
3. **Associations:**
    - **Predictors of long MDT->clinic waits:** GLM/quantile regression with clinic capacity, caseload dispersion, tumour site, MDT load, week effects.
    - **Impact on breaches:** logistic or time‑to‑event models for 31/62‑day breach risk given observed intervals.
4. **Exploratory scenario testing (clearly labelled):** booking rules (e.g., auto‑prioritise post‑MDT within N days), or add X clinic sessions → simulated change in breach risk; results framed as **what‑if** not causal claims.

(Standards backdrop supplies cohort definitions and performance context for all analyses [@johnson2024].)

# Evaluation (multi-method, beyond heuristics)

**E1. Usability (formative):** heuristic review and SUS anchored in **ISO 9241‑110**; think‑aloud with 3–5 users to fix issues early [@ISO9241-2020].

**E2. Utility & effectiveness (summative):** ask‑based experiment with operational users (within‑subjects: current tools -> dashboard).

- **Primary endpoints:**
    - **Time‑to‑answer** (e.g., “Which clinics next week risk ≥X% breaches for tumour group Y?”),
    - **Accuracy** of breach‑risk identification,
    - **Decision quality** in a constrained scheduling scenario (measured against a gold‑standard rule set).
- **Secondary endpoints:** perceived usefulness and intention to use (short TAM items).

**E3. Technical validity:** reconcile a stratified sample of dashboard metrics with underlying SQL/warehouse tables; cross‑check event derivations against NCWTMDS [@NHSDigital2026].

**E4. Contribution capture:** extract design principles from artefact and user feedback (e.g., “surface lead time to breach” as a first‑class signal; “pair risk with capacity actionability”).  
(This evaluation framing responds to MSc‑level rigour requirements for measurable utility, not just usability.)

# Ethical, IG and Risk Management

- **Ethics route:** University submission via supervisor; local classification as service evaluation where applicable; DPIA and data sharing agreements appended.
- **IG & privacy:** UK GDPR/DPA 2018; de‑identification/pseudonymisation at source; honest‑broker access separation; role‑based controls. (Patterns align with IDR literature on privacy for clinical data reuse.) [@gagalova2020]
- **Risks & mitigations:**
    - _Data access/quality_: early availability check; staged pull with profiling; clear event definitions. [@NHSDigital2026]
    - _Scope creep:_ start with 1–2 high‑volume tumour groups; extend only after model stability.
    - _Adoption risk:_ co‑design sessions; map outputs directly to rostering/slot release/booking rules.

# Method Roadmap (DSR Activities)

1. **Problem identification & objectives** (Weeks 1‑4) – confirm pathway scope; articulate evaluation metrics. [@Peffers2007] 
2. **Design & development** (Weeks 5‑14) – build IDR (staging+warehouse), data transforms, definitions, and dashboard v1. [@gagalova2020]
3. **Demonstration** (Weeks 15‑16) – run with retrospective data and live incremental refresh; stakeholder walk‑through.[@Peffers2007]
4. **Evaluation** (Weeks 17‑20) – usability+task‑based study; technical reconciliation.
5. **Communication** (Weeks 21‑24) – write‑up of design principles, results, and implications.

(DSR framing per @Peffers2007; design‑science evaluation stance per @hevner2004.) 

# Timeline (aligned to module dates)

- **By 9th March:** Finalise literature review; ethics/DPIA; confirm data items and availability.
- **March - April:** ETL build; de-ID pipeline, warehouse schema, data profiling/QC [@gagalova2020].
- **April - May:** Analysis (descriptives, regression), scenario exploration; dashboard v1 -> v2.
- **May - July:** Evaluation (E1-E3); extract/compile design principles.
- **July - August:** Final analysis; dissertation writing; artefact packing.
# Expected Outcomes

1. **Evaluated artefact:** IDR+dashboard that measurably reduces time‑to‑insight and improves decision quality for post‑MDT actions (compared to current practice).
- **Design knowledge:** documented design principles and an IDR reference design for NHS oncology operations (transferable within Trusts) [@gagalova2020].
- **Method exemplar:** a DSR‑rigorous case study compliant with Hevner/Peffers, suitable for MSc grading and dissemination [@hevner2004; @Peffers2007]. 

# References

Gagalova, K.K. _et al._ (2020) ‘What You Need to Know Before Implementing a Clinical Research Data Warehouse: Comparative Review of Integrated Data Repositories in Health Care Institutions’, _JMIR Formative Research_, 4(8), p. e17687. Available at: [https://doi.org/10.2196/17687](https://doi.org/10.2196/17687).

Hevner, A.R. _et al._ (2004) ‘Design Science in Information Systems Research’, _MIS Quarterly_, 28(1).

ISO 9241 (2020) _ISO 9241-110:2020_, _ISO_. International Standards Organisation. Available at: [https://www.iso.org/standard/75258.html](https://www.iso.org/standard/75258.html) (Accessed: 1 March 2026).

Jackson, R. _et al._ (2018) ‘CogStack - experiences of deploying integrated information retrieval and extraction services in a large National Health Service Foundation Trust hospital’, _BMC Medical Informatics and Decision Making_, 18(1), p. 47. Available at: [https://doi.org/10.1186/s12911-018-0623-9](https://doi.org/10.1186/s12911-018-0623-9).

Johnson, P. (2024) ‘Updating the NHS cancer waiting time standards’, _BMJ Oncology_, 3(1). Available at: [https://doi.org/10.1136/bmjonc-2024-000337](https://doi.org/10.1136/bmjonc-2024-000337).

NHS Digital (2026) _Cancer Waiting Times Data Collection (CWT)_, _NHS England Digital_. Available at: [https://digital.nhs.uk/data-and-information/data-collections-and-data-sets/data-collections/cancerwaitingtimescwt](https://digital.nhs.uk/data-and-information/data-collections-and-data-sets/data-collections/cancerwaitingtimescwt) (Accessed: 1 March 2026).

Peffers, K. _et al._ (2007) ‘A design science research methodology for information systems research’, _Journal of Management Information Systems_, 24(3), pp. 45–77. Available at: [https://doi.org/10.2753/MIS0742-1222240302](https://doi.org/10.2753/MIS0742-1222240302).

# Appendix A - Data Items and Mapping (Summary)

- **Core events:** MDT date & outcome -> first oncology clinic -> DTT (or earliest clinically appropriate date) -> first definitive treatment (SACT/RT/surgery).
- **Operational:** clinic session calendar, planned slots, slot utilisation, consultant/rota, cancellation reasons.
- **Derived metrics:** days per interval; risk‑to‑breach counters; lead‑time‑to‑breach; capacity vs demand ratios.

(Aligned to NCWTMDS where applicable; mappings documented for transparency and replication.) [@NHSDigital2026] 