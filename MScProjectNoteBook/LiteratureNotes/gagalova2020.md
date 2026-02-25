---
category: literaturenote
tags:
citekey: gagalova2020
status: read
dateread: 2026-02-22
---

> [!Cite]
> Gagalova, K.K. _et al._ (2020) “What You Need to Know Before Implementing a Clinical Research Data Warehouse: Comparative Review of Integrated Data Repositories in Health Care Institutions,” _JMIR Formative Research_, 4(8), p. e17687. Available at: [https://doi.org/10.2196/17687](https://doi.org/10.2196/17687).

>[!Synth]
>**Contribution**:: 
> This paper introduces the concept of a Integrated Data Repository (IDR) used in healthcare. This is exactly what I intend to produce as my artefact . 
> The most common architectures are discussed, which align with my initial ideas. 
> They provide some guiding principles I can use when developing my IDR. They also highlight challenges which should not be underestimated. 
>**Related**:: 
>

>[!md]
> **FirstAuthor**:: Gagalova, Kristina K.  
> **Author**:: Elizalde, M. Angelica Leon  
> **Author**:: Portales-Casamar, Elodie  
> **Author**:: Görges, Matthias  
~    
> **Title**:: What You Need to Know Before Implementing a Clinical Research Data Warehouse: Comparative Review of Integrated Data Repositories in Health Care Institutions  
> **Year**:: 2020   
> **Citekey**:: gagalova2020  
> **itemType**:: journalArticle  
> **Journal**:: *JMIR Formative Research*  
> **Volume**:: 4  
> **Issue**:: 8  
> **Publisher**:: JMIR Publications Inc., Toronto, Canada   
> **Pages**:: e17687  
> **DOI**:: 10.2196/17687    

> [!LINK] 
>
>  [Full Text](file:///home/mark/snap/zotero-snap/common/Zotero/storage/DW7CCNSQ/Gagalova%20et%20al.%20-%202020%20-%20What%20You%20Need%20to%20Know%20Before%20Implementing%20a%20Clinical%20Research%20Data%20Warehouse%20Comparative%20Review%20of.pdf)
>  [PDF](file:///home/mark/snap/zotero-snap/common/Zotero/storage/6AHPZKNB/Gagalova%20et%20al.%20-%202020%20-%20What%20You%20Need%20to%20Know%20Before%20Implementing%20a%20Clinical%20Research%20Data%20Warehouse%20Comparative%20Review%20of.pdf).

> [!Abstract]
>
> Background: Integrated data repositories (IDRs), also referred to as clinical data warehouses, are platforms used for the integration of several data sources through specialized analytical tools that facilitate data processing and analysis. IDRs offer several opportunities for clinical data reuse, and the number of institutions implementing an IDR has grown steadily in the past decade.
Objective: The architectural choices of major IDRs are highly diverse and determining their differences can be overwhelming. This review aims to explore the underlying models and common features of IDRs, provide a high-level overview for those entering the field, and propose a set of guiding principles for small- to medium-sized health institutions embarking on IDR implementation.
Methods: We reviewed manuscripts published in peer-reviewed scientific literature between 2008 and 2020, and selected those that specifically describe IDR architectures. Of 255 shortlisted articles, we found 34 articles describing 29 different architectures. The different IDRs were analyzed for common features and classified according to their data processing and integration solution choices.
Results: Despite common trends in the selection of standard terminologies and data models, the IDRs examined showed heterogeneity in the underlying architecture design. We identified 4 common architecture models that use different approaches for data processing and integration. These different approaches were driven by a variety of features such as data sources, whether the IDR was for a single institution or a collaborative project, the intended primary data user, and purpose (research-only or including clinical or operational decision making).
Conclusions: IDR implementations are diverse and complex undertakings, which benefit from being preceded by an evaluation of requirements and definition of scope in the early planning stage. Factors such as data source diversity and intended users of the IDR influence data flow and synchronization, both of which are crucial factors in IDR architecture planning.
>.
> 
# Notes
>.


# Annotations%% begin annotations %%



### Imported: 2026-02-22 3:16 pm



<mark style="background-color: #ffd400">Quote</mark>
> Integrated data repositories (IDRs), also referred to as clinical data warehouses, are platforms used for the integration of several data sources through specialized analytical tools that facilitate data processing and analysis. IDRs offer several opportunities for clinical data reuse, and the number of institutions implementing an IDR has grown steadily in the past decade.

<mark style="background-color: #ffd400">Quote</mark>
> An EHR is typically organized in a patient-centric manner and has become a powerful tool to store data in a time-dependent and longitudinal structure. EHR data can also be integrated into an enterprise data warehouse or integrated data repository (IDR). IDRs collect heterogeneous data from multiple sources and present them to the user through a comprehensive view [4]. Unlike EHRs, IDRs offer specialized analytical tools for researchers or analysts to perform data analyses.

<mark style="background-color: #ffd400">Quote</mark>
> the purpose of an IDR is to produce generalized knowledge that can be extended to future patients. Typical applications of IDRs include retrospective analysis and hypothesis generation [7]. Some IDRs also support clinical applications, such as clinical decision support systems (CDSSs), that work alongside clinical practice to estimate risk factors or predictive scores associated with clinical treatments.

<mark style="background-color: #ffd400">Quote</mark>
> Different institutions can implement multiple architectures for different purposes;

<mark style="background-color: #ffd400">Quote</mark>
> The general architecture model is the most common model,

<mark style="background-color: #ffd400">Quote</mark>
> n outline, different data marts are transferred to a staging layer that harmonizes the input to a common data view; data are loaded into a common data warehouse and queried through an application layer that communicates with the user

<mark style="background-color: #ffd400">Quote</mark>
> ach data source is originally stored in an independent data mart, collecting data from a separate research or clinical source within the same institution. Data are processed in the staging layer, which reshapes the input to an integrated view through several steps of data linkage, transformation, and harmonization. The next stage of processing is loading the data into a single database connected to an application layer that provides the tools for end users, typically researchers, to access and analyze the data securely with different services.

<mark style="background-color: #ff6666">Quote</mark>
> An example of an IDR providing multiple services is the STRIDE architecture stack [18], which includes several services for data analysis or research data management

<mark style="background-color: #5fb236">Quote</mark>
> The user-controlled application layer architecture model does not have a specific staging layer

<mark style="background-color: #ff6666">Quote</mark>
> The data processing involved in extraction, transformation, and loading (ETL) is described in detail in the articles of biomedical translational research information system (BTRIS) [14], HaMSTR [24], Mayo Translational Research Center (TRC) [38], CARPEM [28], onco-i2b2, Vanderbilt’s Synthetic Derivative [39] and BioVU [40], and BRP [41]. These IDRs represent the general and biobank-driven architecture models, which implement a staging layer for the ETL process.

<mark style="background-color: #ffd400">Quote</mark>
> The most common types of data are those extracted from EHR that include patient demographics, diagnoses, procedures, laboratory tests, and medications.

<mark style="background-color: #ffd400">Quote</mark>
> The most broadly used were International Classification of Diseases (ICD)-9 and 10 for the classification of diseases, systematized nomenclature of medicine-clinical terms (SNOMED-CT) for a variety of medical domains

<mark style="background-color: #ffd400">Quote</mark>
> A common data model (CDM) is a standard data schema that enables data interoperability and sharing. Contemporary data warehouses propose an analytical platform built around the CDM that provides all the software components to construct and manage the data in a CDM

<mark style="background-color: #ff6666">Quote</mark>
> A few different CDMs have been developed and adopted by the wider clinical research community, although some institutions still favor using a custom data schema tailored to their specific needs. In our study, a standard CDM was adopted by 18 of the 29 IDRs. The most frequently applied CDM, found in 16 instances, is Informatics for Integrating Biology and the Bedside (i2b2) [277].

<mark style="background-color: #ff6666">Quote</mark>
> Another popular CDM that has been used more frequently in recent years is the Observational Medical Outcomes Partnership (OMOP) [279],

<mark style="background-color: #ffd400">Quote</mark>
> The most common architecture model employs a staging layer implemented before the data are loaded into the data warehouse.

<mark style="background-color: #ffd400">Quote</mark>
> A set of common features are applied across most IDRs: IDRs commonly use standard terminologies such as ICD-9/10 and SNOMED-CT, which are often already part of the EHR data.

<mark style="background-color: #ffd400">Quote</mark>
> To safeguard the data in the IDR, data security and privacy need to be ensured from the initial steps of development.

<mark style="background-color: #5fb236">Quote</mark>
> The implementation of an IDR is subject to several factors that must be considered before development. We identified 2 major factors: (1) the data stored in the IDR and (2) the scope of the IDR, either being exclusively used for research purposes or in combination with clinical or operational purposes

<mark style="background-color: #5fb236">Quote</mark>
> The scope of the IDR influences its primary end users, researchers, clinical users, or operational users, who have different needs and, thus, need access to different sets of tools to extract, analyze, and visualize the data.

<mark style="background-color: #ffd400">Quote</mark>
> Among the set of selected IDRs, we observed a number of collaborative projects that work within specialized medical domains, such as cancer or pediatrics.

<mark style="background-color: #5fb236">Quote</mark>
> On the basis of our analysis, we highlight the following guiding principles for small- to medium-sized institutions planning to implement an IDR:  1. The general architecture model, with or without CDSS, is the most straightforward to implement; the data staging layer facilitates ETL and data processing before loading into the data warehouse. 2. Select a standard CDM already in use by other institutions; both i2b2 and OMOP provide server and client services in a single unique platform that serves the user with all the necessary tools to set up a structured IDR. 3. Wherever possible, adopt standard terminologies; we listed the most common terminologies derived from the integration with EHR data (Table 1). One promising approach is that common terminologies are applied in the first phases of the IDR development with other, more specialized terminologies, added later as the project scope expands. 4. Finally, the data update requirements and ETL process design should be carefully considered, the level of automation, as these are the limiting stages in data integration and update.

<mark style="background-color: #ffd400">Quote</mark>
> However, although some information about how to query underlying databases and application programming interfaces to communicate with these systems are available, little information on transforming such data into IDR is available in the literature, most likely because of their proprietary nature.

<mark style="background-color: #ffd400">Quote</mark>
> In their review, Hamoud et al [13] provided general requirements for building a successful clinical data warehouse, recommending a top-down approach to the initial stages of development. They recommended considering all the individual components of the final system to decrease integration obstacles when dealing with heterogeneous data sources.

<mark style="background-color: #5fb236">Quote</mark>
> Three major factors contributing to the success of IDRs were identified by Baghal [231] when developing their in-house IDR: (1) organizational, enhancing the collaboration between different departments and researchers; (2) behavioral, building new professional relationships through frequent meetings and communication between departments; and (3) technical improvements to deploy new self-service tools that empower  researchers. Collectively, these factors increase the utility and adoption of IDRs in clinical research.

<mark style="background-color: #5fb236">Quote</mark>
> the report by Rizi and Roudsari [282] on lessons and barriers from their development of a public health data warehouse, which IDR developers might want to consider, specifically, not to underestimate technical challenges such as those related to extracting data from other systems, difficulties in modeling and mapping of data, as well as data security and privacy.

<mark style="background-color: #2ea8e5">Quote</mark>
> Other considerations include leveraging the IDR to improve data quality at the source, implementing a data governance framework from the beginning, and ensuring that key organizational stakeholders endorse the project early and strongly [282].


%% end annotations %%

%% Import Date: 2026-02-22T15:16:50.504+00:00 %%

## References worth following up on

- 26 - Prostate Cancer 
- 28 - Cancer
- 30, 31 - Cancer
- 36-38 - Mayo Clinic Cancer
- 