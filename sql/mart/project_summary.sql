-- project_summary.sql
-- Purpose: placeholder MART query aligned with the toolkit `mart.tables[]` contract.
-- Contract: consume `clean_input` and expose a dashboard-ready table.

with clean_rows as (
    select
        year,
        entity_id,
        metric_value
    from clean_input
),
project_summary as (
    select
        year,
        count(*) as rows_in_year,
        sum(metric_value) as total_metric_value
    from clean_rows
    group by year
)
select
    year,
    rows_in_year,
    total_metric_value
from project_summary
order by year;
