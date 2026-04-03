---
category: literaturenote
tags:
citekey: huser2017
status: unread
dateread:
---

> [!Cite]
> Huser, V. _et al._ (2017) “Methods for examining data quality in healthcare integrated data repositories,” _Biocomputing 2018_. _Pacific Symposium on Biocomputing 2018_, WORLD SCIENTIFIC, pp. 628–633. Available at: [https://doi.org/10.1142/9789813235533_0059](https://doi.org/10.1142/9789813235533_0059).

>[!Synth]
>**Contribution**:: 
>
>**Related**:: 
>

>[!md]
> **FirstAuthor**:: Huser, Vojtech  
> **Author**:: Kahn, Michael G.  
> **Author**:: Brown, Jeffrey S.  
> **Author**:: Gouripeddi, Ramkiran  
~    
> **Title**:: Methods for examining data quality in healthcare integrated data repositories  
> **Year**:: 2017   
> **Citekey**:: huser2017  
> **itemType**:: conferencePaper  
> **Publisher**:: WORLD SCIENTIFIC   
> **Pages**:: 628-633  
> **DOI**:: 10.1142/9789813235533_0059    

> [!LINK] 
>
>  [Full Text PDF](file:///home/mark/snap/zotero-snap/common/Zotero/storage/RJ783AUY/Huser%20et%20al.%20-%202017%20-%20Methods%20for%20examining%20data%20quality%20in%20healthcare%20integrated%20data%20repositories.pdf).

> [!Abstract]
>.
> 
# Notes
>.

## **Summary**

- Reviews data quality infrastructure across IDRs and multi-site research networks.
- Highlights key data quality challenges:
    - Missingness
    - Semantic heterogeneity
    - Lack of terminological alignment
- Describes tools like **Achilles Heel** (OHDSI) for automated quality checks.
- Presents evidence that **Common Data Models (CDMs)** (e.g., OMOP, Sentinel, i2b2) enable better syntactic and semantic integration. 



## **Relevance to  Study**

- Provides core justification for  IDR design’s emphasis on:
    - CDM alignment
    - Terminology mapping (SNOMED CT, ICD‑10, NCWTMDS)
    - Data quality pipelines
- Aligns with  proposal plan for:
    - Staging → warehouse → dashboard
    - QC workflows
    - Event/interval validation rules



## **Critical Evaluation**

### **Strengths**

- Offers practical, implementable data quality strategies.
- Demonstrates established best‑practice tools and industry patterns.

### **Weaknesses**

- Focuses more on research networks; less explicit on operational decision-making.
- Requires adaptation for NHS cancer pathways.



## **Implications for Artefact**

- System must incorporate:
    - **Automated QC checks**
    - **Event sequencing validation** (e.g., no MDT → clinic reversals)
    - **Terminology validation**
    - **Audit trails**



## **Contribution to Literature Gap**

- Confirms the absence of operational IDRs built for day‑to‑day decision support (most IDRs are research‑oriented).
- Supports building a new artefact.



## Summary of Huser et al.**

| Category                | Details                                            |
| ----------------------- | -------------------------------------------------- |
| **Focus**               | Data quality methods for IDRs                      |
| **Problems Identified** | Missingness, semantic mismatch, data heterogeneity |
| **Solutions Discussed** | CDMs, Achilles Heel, distributed quality checks    |
| **Relevance**           | Directly informs  IDR QC pipeline                  |
| **Gap**                 | Research-focused, not operational                  |
# Annotations%% begin annotations %%


%% end annotations %%

%% Import Date: 2026-03-28T19:46:48.990+00:00 %%
