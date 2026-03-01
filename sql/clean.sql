-- clean.sql
-- Purpose: placeholder transformation for the CLEAN layer.
-- Contract: read from the source configured in dataset.yml and keep the query portable.

with source_rows as (
    select
        year,
        entity_id,
        metric_value
    from raw_input
),
normalized as (
    select
        cast(year as integer) as year,
        cast(entity_id as varchar) as entity_id,
        cast(metric_value as double) as metric_value
    from source_rows
)
select
    year,
    entity_id,
    metric_value
from normalized;
