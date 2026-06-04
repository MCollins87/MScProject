DROP TABLE IF EXISTS warehouse.fact_oncology_pathway;

CREATE TABLE warehouse.fact_oncology_pathway AS
SELECT
    s.nhs_number,
    s.r_number,
    s.tumour_site,
    s.oncologist,

    s.date_referred,
    s.clinic_date,
    ct.ct_date,
    t.first_treat_date,

    (s.clinic_date::DATE - s.date_referred::DATE) AS days_referral_to_clinic,
    (ct.ct_date::DATE - s.clinic_date::DATE) AS days_clinic_to_ct,
    (t.first_treat_date::DATE - ct.ct_date::DATE) AS days_ct_to_treat,
    (t.first_treat_date::DATE - s.date_referred::DATE) AS total_pathway_days,

    CURRENT_TIMESTAMP AS load_timestamp

FROM staging.stg_oncology_intake s

LEFT JOIN staging.stg_aria_ct ct
    ON s.nhs_number = ct.nhs_number
    AND ct.ct_date >= s.clinic_date

LEFT JOIN staging.stg_aria_treat t
    ON ct.nhs_number = t.nhs_number
    AND t.first_treat_date >= ct.ct_date;
