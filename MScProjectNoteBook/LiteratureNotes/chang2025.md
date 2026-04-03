---
category: literaturenote
tags:
citekey: chang2025
status: unread
dateread:
---

> [!Cite]
> Chang, J.S. _et al._ (2025) “Continuous multimodal data supply chain and expandable clinical decision support for oncology,” _npj Digital Medicine_, 8(1), p. 128. Available at: [https://doi.org/10.1038/s41746-025-01508-2](https://doi.org/10.1038/s41746-025-01508-2).

>[!Synth]
>**Contribution**:: 
>
>**Related**:: 
>

>[!md]
> **FirstAuthor**:: Chang, Jee Suk  
> **Author**:: Kim, Hyunwook  
> **Author**:: Baek, Eun Sil  
> **Author**:: Choi, Jeong Eun  
> **Author**:: Lim, Joon Seok  
> **Author**:: Kim, Jin Sung  
> **Author**:: Shin, Sang Joon  
~    
> **Title**:: Continuous multimodal data supply chain and expandable clinical decision support for oncology  
> **Year**:: 2025   
> **Citekey**:: chang2025  
> **itemType**:: journalArticle  
> **Journal**:: *npj Digital Medicine*  
> **Volume**:: 8  
> **Issue**:: 1  
> **Publisher**:: Nature Publishing Group   
> **Pages**:: 128  
> **DOI**:: 10.1038/s41746-025-01508-2    

> [!LINK] 
>
>  [Full Text PDF](file:///home/mark/snap/zotero-snap/common/Zotero/storage/WE5E5DMG/Chang%20et%20al.%20-%202025%20-%20Continuous%20multimodal%20data%20supply%20chain%20and%20expandable%20clinical%20decision%20support%20for%20oncology.pdf).

> [!Abstract]
>
> The study introduces a clinical decision support system (CDSS) developed at a single academic cancer center, integrating real-time clinical, genomic, and imaging data for over 170,000 patients across 11 cancer types. We have developed the Yonsei Cancer Data Library (YCDL) data integration framework to continuously collect and update multimodal datasets comprising over 800 features per case. Quality control measures, using 143 logical comparisons, addressed missing data and outliers, achieving median accuracies of 92.6% for surgical and 98.7% for molecular pathology. An Extract-Transform-Load (ETL) process with natural language processing transformed unstructured data, enabling survival analyses stratified by tumor stage, which revealed significant stage-dependent differences. The CDSS dashboard visualizes patient trajectories and key milestones. User feedback from oncology professionals showed strong acceptance, with satisfaction scores exceeding 4 out of 5. This framework demonstrates the potential of multimodal data integration to enhance clinical decision-making and patient outcomes, with future research needed to validate its generalizability and scalability.
>.
> 
# Notes
>.

## **Summary**

- Describes a clinical decision support system (CDSS) integrating:
    - Real‑time clinical data
    - Genomic data
    - Imaging data
- Uses an ETL framework with **143 logical quality checks**.
- Provides clinicians with trajectory views and decision-support dashboards.
- Achieved **high user satisfaction (>4/5)** among oncology professionals.

## **Relevance**

- Strongly supportive of  system’s requirement for:
    - Multimodal integration
    - Automated QC checks
    - Operational dashboards tailored to oncology
- Demonstrates feasibility of large-scale, real-time clinical integration frameworks.



## **Critical Evaluation**

### **Strengths**

- One of the most directly relevant IDR/CDSS implementations in oncology literature.
- Includes operational evaluation via clinician feedback.

### **Weaknesses**

- Highly specialised environment; may not generalise to NHS Trusts.
- Heavy focus on genomics (secondary relevance to  operational scope).


## **Implications for Artefact**

- Reinforces the importance of user-centred dashboard evaluation (SUS + task-based tests).
- Supports the inclusion of QC rules in staging layers.



## **Contribution to Gap**

- Even advanced CDSS systems rarely map entire oncology pathways;  
    none focus on **post-MDT operational delays** — my contribution.



## Summary of Chang et al.

| Category      | Details                                                    |
| ------------- | ---------------------------------------------------------- |
| **Focus**     | Multimodal oncology data integration & CDSS                |
| **QC Rules**  | 143 logic‑based checks                                     |
| **Relevance** | Strong analogue for your ETL + dashboard                   |
| **Strength**  | Real-time integration; clinician evaluation                |
| **Gap**       | Not designed for operational cancer waiting time standards |
# Annotations%% begin annotations %%


%% end annotations %%

%% Import Date: 2026-03-28T19:55:39.238+00:00 %%
