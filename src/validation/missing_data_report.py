import csv
for path in ['data/cleaned/cliburn_2025_candidates.csv','data/cleaned/cliburn_2025_results.csv','data/cleaned/cliburn_2025_performances.csv','data/cleaned/cliburn_2025_works.csv']:
    rows=list(csv.DictReader(open(path,encoding='utf-8')))
    print(f'{path}: {len(rows)} rows')
    for field in rows[0] if rows else []:
        empty=sum(1 for r in rows if r.get(field,'')=='')
        if empty: print(f'  {field}: {empty} empty')
