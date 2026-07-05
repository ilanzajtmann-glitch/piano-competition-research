# Data Quality Report

This report was regenerated for the Van Cliburn 2025 cleaned dataset.

## Validation Summary

| Check | Status | Result |
|---|---|---|
| CSV integrity | PASS | Cleaned CSV files have headers, LF line endings, valid quoting, and one parsed record per physical line. |
| Candidate count | PASS | 28 candidates. |
| Result consistency | PASS | Reached-round and finalist/laureate fields are internally consistent. |
| Source URL presence | PASS | Required source URL fields are populated. |
| Duplicate work keys | PASS | No duplicate normalized composer/title work keys. |
| Repertoire completeness | PASS | All 28 candidates have six candidate-page program sections and at least one work per section. |
| Feature consistency | PASS | `program_features.csv` `num_works` matches `performance_works.csv`; zero zero-work rows. |
| Missing-data report | PASS | Known nulls are documented rather than guessed. |

## program_features.csv Formatting Audit

| Field | Value |
|---|---:|
| Header physical line | 1 |
| Physical lines | 169 |
| Parsed records | 169 |
| Data records | 168 |
| Notes rows with non-empty values | 0 |
| Embedded newline cells | 0 |
| CR bytes | 0 |

## Known Intentional Nulls

- `birth_year` is empty for 28 candidate rows because exact birth years were not source-confirmed.
- Work metadata fields such as catalog parsing, key, genre, period, and duration remain empty unless source-confirmed.
- These nulls are expected and should be resolved only through source-backed enrichment.
