# Data Quality Report

## csv_integrity_check.py: PASS
```
PASS csv_integrity_check: 9 cleaned CSV files have headers, LF line endings, one record per line, and consistent quoting

```

## candidate_count_check.py: PASS
```
PASS candidate_count_check: 28 candidates

```

## result_consistency_check.py: PASS
```
PASS result_consistency_check: finalists, laureates, and reached_round flags consistent

```

## source_url_check.py: PASS
```
PASS source_url_check: required source URL columns are populated

```

## duplicate_work_check.py: PASS
```
PASS duplicate_work_check: no duplicate composer/title normalized work keys

```

## repertoire_completeness_check.py: PASS
```
PASS repertoire_completeness_check: all 28 candidates have six candidate-page program sections and at least one work per section

```

## feature_consistency_check.py: PASS
```
PASS feature_consistency_check: program_features num_works matches performance_works and has no zero-work rows

```

## missing_data_report.py: PASS
```
data/cleaned/cliburn_2025_candidates.csv: 28 rows
  birth_year: 28 empty
data/cleaned/cliburn_2025_results.csv: 28 rows
  laureate_rank: 25 empty
  prize: 21 empty
  notes: 28 empty
data/cleaned/cliburn_2025_performances.csv: 168 rows
data/cleaned/cliburn_2025_works.csv: 233 rows
  catalog_number: 233 empty
  key: 233 empty
  genre: 233 empty
  period: 233 empty
  approximate_duration: 233 empty
  notes: 233 empty

```
