# Data Quality Report

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

## missing_data_report.py: PASS
```
data/cleaned/cliburn_2025_candidates.csv: 28 rows
  birth_year: 28 empty
data/cleaned/cliburn_2025_results.csv: 28 rows
  laureate_rank: 25 empty
  prize: 21 empty
  notes: 28 empty
data/cleaned/cliburn_2025_performances.csv: 82 rows
data/cleaned/cliburn_2025_works.csv: 24 rows
  catalog_number: 24 empty
  key: 24 empty
  genre: 24 empty
  period: 24 empty
  approximate_duration: 24 empty
  notes: 24 empty

```
