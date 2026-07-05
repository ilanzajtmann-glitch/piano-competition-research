import csv
rows=list(csv.DictReader(open('data/cleaned/cliburn_2025_results.csv',encoding='utf-8')))
finalists=[r for r in rows if r['finalist']=='1']; laureates=[r for r in rows if r['laureate_rank']]
assert len(finalists)==6, f'expected 6 finalists, found {len(finalists)}'
assert laureates, 'expected at least one laureate'
assert not all(r['reached_round']=='Preliminary' for r in rows), 'all candidates preliminary only'
for r in rows:
    rr=r['reached_round']; flags={k:r[k]=='1' for k in ['quarterfinalist','semifinalist','finalist']}
    if rr=='Final': assert flags['finalist'] and flags['semifinalist'] and flags['quarterfinalist'], r
    if rr=='Semifinal': assert flags['semifinalist'] and flags['quarterfinalist'] and not flags['finalist'], r
    if rr=='Quarterfinal': assert flags['quarterfinalist'] and not flags['semifinalist'], r
print('PASS result_consistency_check: finalists, laureates, and reached_round flags consistent')
