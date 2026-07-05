import csv, collections
candidates=list(csv.DictReader(open('data/cleaned/cliburn_2025_candidates.csv',encoding='utf-8')))
performances=list(csv.DictReader(open('data/cleaned/cliburn_2025_performances.csv',encoding='utf-8')))
pworks=list(csv.DictReader(open('data/cleaned/performance_works.csv',encoding='utf-8')))
expected_rounds={
    'Preliminary Round','Quarterfinal Round','Semifinal Round - Recital',
    'Semifinal Round - Mozart Concerto','Final Round - Concerto 1','Final Round - Concerto 2'
}
by_candidate=collections.defaultdict(set)
for p in performances:
    by_candidate[p['candidate_id']].add(p['program_label'])
missing=[]
for c in candidates:
    have=by_candidate[c['candidate_id']]
    if have != expected_rounds:
        missing.append((c['full_name'], sorted(expected_rounds-have), sorted(have-expected_rounds)))
assert not missing, f'candidate-page round coverage errors: {missing[:5]}'
work_counts=collections.Counter(pw['performance_id'] for pw in pworks)
empty=[p['performance_id'] for p in performances if work_counts[p['performance_id']]==0]
assert not empty, f'performances without work rows: {empty[:10]}'
assert len(performances)==len(candidates)*len(expected_rounds), f'expected {len(candidates)*len(expected_rounds)} program rows, found {len(performances)}'
print('PASS repertoire_completeness_check: all 28 candidates have six candidate-page program sections and at least one work per section')
