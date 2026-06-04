Using AURA (Aria Unified Reporting Application), the following reports are made:

## RT_Referral

**Data Sources**
- `RTReferral = dwActivityModel`
	- Filter:  `[ActivityName] Like *Registration*`
- `Patient = dwPatientModel`

**Fields**
- `PatientID = [RTReferral].[PatientID]`
- `DateRegistered = [RTReferral].[ScheduledEndTime]`
- `PrimaryOncologist = [RTReferral].[PrimaryOncologistFullName]`
- `ActivityName = [RTReferral].[ActivityName]`
- `RegisteredBy = [RTReferral].[ActivityCreatedBy`]
- `NHSNumber = Lookup(Fields!ctrPatientSer.Value,Fields!ctrPatientSer.Value,Fields!UniversalPatientID.Value, "Patient")`
- `PASNumber = Lookup(Fields!ctrPatientSer.Value,Fields!ctrPatientSer.Value,Fields!PatientSSN.Value, "Patient")`
- `Diagnosis_ICD10 = Lookup(Fields!ctrPatientSer.Value,Fields!ctrPatientSer.Value,Fields!UniversalPatientDiagnosisCode.Value, "Patient")`

## Initial Run
`StartDate = 2026-04-01` (This is when the SharePoint list was first implemented)
`EndDate = 2026-06-01`
Manual export to `\\Rhu-d090232\idr`

### Scheduled run
`StartDate = Today()`
`EndDate = Today()`
Frequency = Every Day @ 23:00
Output = `\\Rhu-d090232\idr`\RT_Referral
Increment File Name

## RT_CT

**Data Sources**
- `CT = dwActivityModel`
	- Filter:  `[ResourceName] Like *CT*`
	- `[AppointmentStatus] <> *Cancelled*`
- `Patient = dwPatientModel`

**Fields**
- `r_number = [CT].[PatientID]`
- `CT_Date = [CT].[AppointmentDateTime]`
- `AppointmentStatus = [CT].[AppointmentStatus]` (Sanity check the filter is working)
- `PrimaryOncologist = [CT].[PrimaryOncologistFullName]`
- `ActivityName = [CT].[ActivityName]`
- `ResourceName = [CT}.[ResourceName]` (Sanity check that Filter is working)
- `RegisteredBy = [RTReferral].[ActivityCreatedBy`]
- `NHSNumber = Lookup(Fields!ctrPatientSer.Value,Fields!ctrPatientSer.Value,Fields!UniversalPatientID.Value, "Patient")`
- `PASNumber = Lookup(Fields!ctrPatientSer.Value,Fields!ctrPatientSer.Value,Fields!PatientSSN.Value, "Patient")`


## Initial Run
`StartDate = 2026-04-01` (This is when the SharePoint list was first implemented)
`EndDate = 2026-09-01` (three months from now)
Manual export to `\\Rhu-d090232\idr\RT_CT.csv`

### Scheduled run
`StartDate = Today()` (capture any emergency/urgent patients)
`EndDate = DateAdd(Today(), 90)` (find those booked in advance)
Frequency = Every Day @ 23:00
Output = `\\Rhu-d090232\idr\RT_CTxx.csv` 
Increment File Name