import csv, collections
performances=list(csv.DictReader(open('data/cleaned/cliburn_2025_performances.csv',encoding='utf-8')))
performance_works=list(csv.DictReader(open('data/cleaned/performance_works.csv',encoding='utf-8')))
features=list(csv.DictReader(open('data/cleaned/program_features.csv',encoding='utf-8')))
perf_key={p['performance_id']:(p['candidate_id'],p['program_label']) for p in performances}
work_counts=collections.Counter(pw['performance_id'] for pw in performance_works)
expected={(p['candidate_id'],p['program_label']):work_counts[p['performance_id']] for p in performances}
actual={(f['candidate_id'],f['round_name']):int(f['num_works']) for f in features}
missing=set(expected)-set(actual)
extra=set(actual)-set(expected)
assert not missing, f'missing feature rows for performances: {sorted(missing)[:10]}'
assert not extra, f'extra feature rows without performance rows: {sorted(extra)[:10]}'
mismatched=[(key, expected[key], actual[key]) for key in expected if expected[key] != actual[key]]
assert not mismatched, f'feature num_works mismatches performance_works counts: {mismatched[:10]}'
zeros=[key for key,count in actual.items() if count == 0]
assert not zeros, f'program_features rows with zero num_works: {zeros[:10]}'
print('PASS feature_consistency_check: program_features num_works matches performance_works and has no zero-work rows')
