import csv, collections
rows=list(csv.DictReader(open('data/cleaned/cliburn_2025_works.csv',encoding='utf-8')))
keys=collections.Counter((r['composer_id'],r['normalized_title']) for r in rows)
dups=[k for k,v in keys.items() if v>1]
assert not dups, f'duplicate normalized work keys: {dups[:10]}'
print('PASS duplicate_work_check: no duplicate composer/title normalized work keys')
