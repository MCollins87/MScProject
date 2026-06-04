# Automate the export of Oncology Referral intake register

``` mermaid
flowchart TD
A[SharePoint List] --> B[Power Automate Flow]
B --> C[Create CSV Table]
C --> D["Save to Folder C:\IDR\raw (via sync)"]
D --> E[Python ETL Pipeline]
```


## Flow Design

**Power Automate:**
1. Trigger:
	- "Recurrence" - everyday at 06:00
2. Get Items
	- Connect to SharePoint List
3. Select 
	- Rename columns to match ETL Schema
4. Create CSV Table
	- Converts list -> flat CSV
5. Create file
	- Save to:
		- SharePoint document library 
		- or OneDrive (autosync to local machine)

## Key points
### Control schema consistency
Use Select step to enforce column names:
``` JSON
{
"nhs_number": item()?['NHSNumber'],
"referral_data": item()?['ReferralDate']
}
```

### Add timestamp to filename
```
oncology_intake_2026-06-01.csv
```

### handle large lists
- Enable pagination
- SharePoint export has limit (~30k rows for csv UI export)
- Power Automate handles larger datasets better. 

# MSc-Level Justification 

*To ensure consistency across heterogeneous clinical systems, all data sources were standardised to a CSV ingestion format. SharePoint list extraction was automated using Microsoft Power Automate, enabling scheduled, reproducible exports into a secure data landing zone. This approach reduces manual intervention, improves reliability, and aligns with enterprise ETL design principles by enforcing a consistent ingestion interface across disparate operational systems.*


# Plans change 
This was the plan, but unfortunately, the Power Automate option has hit an issue. I am unable to build in the default  NHS Mail workspace. I have requested access to a locally managed environment, but until then, the workflow is manual. 