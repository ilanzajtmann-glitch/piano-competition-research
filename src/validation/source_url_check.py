import csv
for path, col in [('data/cleaned/cliburn_2025_candidates.csv','source_url'),('data/cleaned/cliburn_2025_results.csv','result_source_url'),('data/cleaned/cliburn_2025_performances.csv','source_url'),('data/cleaned/performance_works.csv','source_url')]:
    rows=list(csv.DictReader(open(path,encoding='utf-8')))
    missing=[i+2 for i,r in enumerate(rows) if not r.get(col,'').startswith('http')]
    assert not missing, f'{path} missing {col} at lines {missing[:10]}'
print('PASS source_url_check: required source URL columns are populated')
