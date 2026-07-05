import csv, sys
rows=list(csv.DictReader(open('data/cleaned/cliburn_2025_candidates.csv',encoding='utf-8')))
assert len(rows)==28, f'expected 28 candidates, found {len(rows)}'
print('PASS candidate_count_check: 28 candidates')
