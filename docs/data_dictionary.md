# Data Dictionary

Audience: Maintainers

Schema sintetico dei dataset gestiti dal progetto.

## Raw

| Column | Type | Description | Nullable | Notes |
| --- | --- | --- | --- | --- |
| year | int | Reference year | no | Example placeholder |
| entity_id | string | Stable entity identifier | no | Replace with project key |
| metric_value | float | Raw metric value | yes | Replace with actual meaning |

## Clean

| Column | Type | Description | Nullable | Validation |
| --- | --- | --- | --- | --- |
| year | int | Reference year | no | not_null |
| entity_id | string | Stable entity identifier | no | not_null, unique_key |
| metric_value | float | Normalized metric value | yes | range TBD |

## Mart

| Column | Type | Description | Nullable | Consumer |
| --- | --- | --- | --- | --- |
| year | int | Reference year | no | dashboard/report |
| entity_id | string | Stable entity identifier | no | dashboard/report |
| metric_value | float | Final metric | yes | dashboard/report |
| rows_in_year | int | Record count by year | no | QA/dashboard |
