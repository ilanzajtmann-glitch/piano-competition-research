import csv
from pathlib import Path

ROOT=Path('.')
CANDIDATES=ROOT/'data/cleaned/cliburn_2025_candidates.csv'
RESULTS=ROOT/'data/cleaned/cliburn_2025_results.csv'
PERFORMANCES=ROOT/'data/cleaned/cliburn_2025_performances.csv'
WORKS=ROOT/'data/cleaned/cliburn_2025_works.csv'
PERFORMANCE_WORKS=ROOT/'data/cleaned/performance_works.csv'
OUT=ROOT/'data/cleaned/program_features.csv'

FRENCH=('debussy','ravel','fauré','faure','messiaen','dutilleux','saint-saëns','saint-saens')
RUSSIAN_SLAVIC=('rachmaninov','scriabin','prokofiev','shostakovich','medtner','mussorgsky','tchaikovsky','balakirev','bartók','bartok','janáček','janacek','smetana','dvořák','dvorak')
MODERNISM=('bartók','bartok','prokofiev','stravinsky','ligeti','shostakovich','messiaen','schoenberg','adès','ades','bolcom','chin','barber','ginastera','gubaidulina','hindemith')
CONTEMPORARY=('montero','adès','ades','chin','onaç','on̈aç','bolcom')
TRANSCRIPTION_MARKERS=('–','-busoni','-liszt','-horowitz','-hess','-agosti','-grainger')
LATE_BEETHOVEN=('op. 101','op. 106','op. 109','op. 110','op. 111','hammerklavier')


def read(path):
    return list(csv.DictReader(open(path, encoding='utf-8')))

candidates={r['candidate_id']:r for r in read(CANDIDATES)}
results={r['candidate_id']:r for r in read(RESULTS)}
performances=read(PERFORMANCES)
works={r['work_id']:r for r in read(WORKS)}
pworks=read(PERFORMANCE_WORKS)
by_perf={}
for pw in pworks:
    by_perf.setdefault(pw['performance_id'], []).append(pw)

header=['candidate_id','full_name','edition','round_name','reached_round','qualified_to_next_round','finalist','laureate_rank','num_works','num_composers','num_periods','has_bach','has_classical_sonata','has_beethoven','has_late_beethoven','has_french_color','has_russian_slavic','has_modernism','has_contemporary','has_transcription','has_large_form','has_etude','has_variations','has_concerto','stylistic_breadth_score','program_diversity_score','notes']
round_order={'Preliminary Round':1,'Quarterfinal Round':2,'Semifinal Round - Recital':3,'Semifinal Round - Mozart Concerto':4,'Final Round - Concerto 1':5,'Final Round - Concerto 2':6}
reached_rank={'Preliminary':1,'Quarterfinal':2,'Semifinal':4,'Final':6}
rows=[]
for perf in performances:
    cid=perf['candidate_id']
    result=results[cid]
    items=by_perf.get(perf['performance_id'], [])
    linked=[works[pw['work_id']] for pw in items]
    raw_blob=' '.join((pw['raw_text']+' '+works[pw['work_id']]['raw_title']).lower() for pw in items)
    composer_ids={w['composer_id'] for w in linked}
    periods={w['period'] for w in linked if w.get('period')}
    qualified=''
    if not perf['program_label'].startswith('Final'):
        qualified=int(perf['performance_status']=='performed' and round_order[perf['program_label']] < reached_rank[result['reached_round']])
    feature_flags=[
        int('bach' in raw_blob),
        int('sonata' in raw_blob and any(k in raw_blob for k in ['beethoven','mozart','haydn','clementi'])),
        int('beethoven' in raw_blob),
        int(any(k in raw_blob for k in LATE_BEETHOVEN)),
        int(any(k in raw_blob for k in FRENCH)),
        int(any(k in raw_blob for k in RUSSIAN_SLAVIC)),
        int(any(k in raw_blob for k in MODERNISM)),
        int(any(k in raw_blob for k in CONTEMPORARY)),
        int(any(k in raw_blob for k in TRANSCRIPTION_MARKERS)),
        int(any(k in raw_blob for k in ['concerto','sonata','variations','pictures at an exhibition','gaspard','chaconne','fantasie','fantasy','kreisleriana','davidsbündler'])),
        int('etude' in raw_blob or 'étude' in raw_blob),
        int('variation' in raw_blob),
        int('concerto' in raw_blob),
    ]
    rows.append([cid,candidates[cid]['full_name'],'Van Cliburn 2025',perf['program_label'],result['reached_round'],qualified,result['finalist'],result['laureate_rank'],len(items),len(composer_ids),len(periods),*feature_flags,len(composer_ids)+len(periods),len(items),'Regenerated from cliburn_2025_performances.csv, performance_works.csv, and cliburn_2025_works.csv. Categories are heuristic, not conclusions.'])

with open(OUT,'w',newline='',encoding='utf-8') as f:
    csv.writer(f).writerows([header]+rows)

zeros=[r for r in rows if r[8]==0]
if zeros:
    raise SystemExit(f'program feature rows with zero num_works: {zeros[:5]}')
print(f'wrote {OUT} with {len(rows)} rows; zero-work rows: 0')
