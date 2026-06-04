Having spent some time creating a simple ETL pipeline based on referral spreadsheet, the following has been developed:

## Integrated Data Repository for Oncology Pathways

#### Key capabilities:
- Ingests operational data from SharePoint (CSV export)
- Cleans and standardises inconsistent NHS data
- Stores data in structured PostgreSQL environment
- Enables derivation of pathway metrics
- Supports real-time operational insight (e.g. delay, risk)

``` mermaid
flowchart TB
%% SOURCE LAYER
S1["Oncology Intake Register
(SharePoint List)"]
S2["ARIA RT Referral
(CSV Extract)"]
S3["ARIA CT Planning
(CSV Extract)"]
S4["ARIA RT Treatment
(CSV Extract)"]
%% STAGING LAYER
ST1["stg_oncology_intake
(Raw SharePoint data
+ Modified timestamp)"]
ST2["stg_aria_rt_referral
(RT decision events
+ course_id)"]
ST3["stg_aria_ct_planning

(CT planning events

+ course_id)"]

  

ST4["stg_aria_rt_treatment

(Treatment events

+ course_id)"]

  

%% TRANSFORMATION LAYER

T["Integration & Transformation Layer

- Join on NHS Number / course_id

- Deduplication (MERGE logic)

- Event alignment

- Interval calculations"]

  

%% WAREHOUSE

F["fact_oncology_pathway

(One row per patient pathway)

- Canonical event dates

- Derived intervals

- Breach risk metrics"]

  

%% FLOWS

S1 --> ST1

S2 --> ST2

S3 --> ST3

S4 --> ST4

  

ST1 --> T

ST2 --> T

ST3 --> T

ST4 --> T

  

T --> F
```


```mermaid
flowchart LR

  

%% ENTITIES

SP["SharePoint Intake Register"]

ARIA1["ARIA RT Referral CSV"]

ARIA2["ARIA CT Planning CSV"]

ARIA3["ARIA RT Treatment CSV"]

P1["Incremental Extract

(Modified Timestamp)"]

P2["CSV Load & Validation"]

P3["Staging Load (MERGE / UPSERT)"]

P4["Integration & Harmonisation"]

P5["Metric Calculation

(Intervals + Risk)"]

  

%% DATA STORES

D1["stg_oncology_intake"]

D2["stg_aria_rt_referral"]

D3["stg_aria_ct_planning"]

D4["stg_aria_rt_treatment"]

D5["fact_oncology_pathway"]

SP --> P1

P1 --> P3

P3 --> D1

  

ARIA1 --> P2

ARIA2 --> P2

ARIA3 --> P2

  

P2 --> P3

P3 --> D2

P3 --> D3

P3 --> D4

  

D1 --> P4

D2 --> P4

D3 --> P4

D4 --> P4

  

P4 --> P5

P5 --> D5
C["etl_control

(last load timestamps)"]

C --> P1
```


## Core Components Built:
### 1. ETL Pipeline (Python)
- Reads CSV from secure location (PID separated)
- Cleans column names and data types
- Handles: 
	- missing values (NaT -> NULL)
	- encoding issues (BOM fix)
	- inconsistent naming
- Loads into PostgreSQL using bulk insert

### 2. Staging layer (PostgreSQL)

Schema:
``` SQL
staging.stg_oncology_intake
```

Purpose:
- raw but structured data
- Minimal transformation
- Data quality nprmalisation

### 3. Transformation Layer (SQL)
Derived metrics:
- referral -> triage time
- triage ->  clinic time
- Total pathway duration
- days since referral

### Analytical Model (Warehouse)

Begun building:
``` SQL
warehouse.fact_oncology_pathway
```
Purpose:
- Clean, analysis-ready dataset
- Supports dashboards and decision making

## Design Justification
### 1. Separation of Concerns
- ETL (Python) handles ingestion + cleaning
- PostgreSQL handles storage + querying
Improves maintainability
Reflects enterprise data architecture

### 2. Data Governance

Code and data kept on separate partitions:
- Code, syncing with GitHub on P:\ drive
- PID data on local hard drive C:\
This prevents accidental data leakage
Aligns with IG / GDPR principles


### 3. Robust ETL Design
Real-world data issues have been encountered and resolved:
- Missing identifiers -> surrogate keys
- NaT/NaN handling
- BOM encoding issue
- Column inconsistencies

### 4 IDR Architecture Choice
Built layers architecture:
- staging -> transformation -> analytics
Allows: 
- scalability
- reuse
- incremental updates

## Alignment to Research Objectives

### RQ1: Where delays occur
- Pathway decomposition:
	- triage
	- Clinic

### RQ2: Drivers of delay
- grouped by tumour site / clinician

### RQ3: Decision support
- risk flags and prioritisation

## Archetecture Diagram

``` mermaid
flowchart TD

  

    A[SharePoint List] -->|Export CSV| B[Secure Data Storage C:\\IDR]

  

    B --> C[Python ETL Script]

  

    C -->|Read CSV| D[Data Cleaning]

    D -->|Standardise Columns| E[Transform Dates]

    E -->|Handle NULLs/NaT| F[Generate Surrogate Key]

  

    F -->|Bulk Insert| G[PostgreSQL Staging]

  

    G --> H[staging.stg_oncology_intake]

  

    H -->|SQL Transformations| I[Derived Metrics]

  

    I --> J[warehouse.fact_oncology_pathway]

  

    J --> K[Power BI Dashboard]

  

    K --> L[Operational Insight]
```

## Data Flow
1. Data exported from SharePoint
2. Stored securely outside Git
3. ETL script:
	1. cleans + standardises data
	2. resolves quality issues
4. Data loaded into staging table
5. SQL transforms create metrics
6. Warehouse table supports analytics
7. Power BI visualises patient pathways & risk


