# Post-merge CSV physical-line audit: Van Cliburn 2025 v1

Date: 2026-07-05
Scope: fix and verify cleaned CSV physical formatting only. No new competition, statistical analysis, API, app, recommender, or architecture work was added.

## Fix applied

Every CSV under `data/cleaned/` was opened as bytes/CSV, every embedded `\r\n`, `\r`, or `\n` inside cells was replaced with a space, and every file was rewritten with Python `csv.writer(..., lineterminator="\n", quoting=csv.QUOTE_ALL)`.

No underlying data values were intentionally changed except newline-to-space normalization inside cells and CSV physical formatting.

## Required physical checks

```sh
$ wc -l data/cleaned/cliburn_2025_candidates.csv
29 data/cleaned/cliburn_2025_candidates.csv

$ wc -l data/cleaned/cliburn_2025_results.csv
29 data/cleaned/cliburn_2025_results.csv
```

## Raw visual inspection commands

```sh
$ cat -A data/cleaned/cliburn_2025_candidates.csv | head
"candidate_id","full_name","nationality","birth_year","source_url"$
"1","Piotr Alexewicz","Poland","","https://cliburn.org/competitions/2025-cliburn-competition/2025-competitors/piotr-alexewicz"$
"2","Jonas Aumiller","Germany","","https://cliburn.org/competitions/2025-cliburn-competition/2025-competitors/jonas-aumiller"$
"3","Alice Burla","Canada","","https://cliburn.org/competitions/2025-cliburn-competition/2025-competitors/alice-burla"$
"4","Yangrui Cai","China","","https://cliburn.org/competitions/2025-cliburn-competition/2025-competitors/yangrui-cai"$
"5","Elia Cecino","Italy","","https://cliburn.org/competitions/2025-cliburn-competition/2025-competitors/elia-cecino"$
"6","Yanjun Chen","China","","https://cliburn.org/competitions/2025-cliburn-competition/2025-competitors/yanjun-chen"$
"7","Jiarui Cheng","China","","https://cliburn.org/competitions/2025-cliburn-competition/2025-competitors/jiarui-cheng"$
"8","Federico Gad Crema","Italy","","https://cliburn.org/competitions/2025-cliburn-competition/2025-competitors/federico-gad-crema"$
"9","Shangru Du","China","","https://cliburn.org/competitions/2025-cliburn-competition/2025-competitors/shangru-du"$

$ cat -A data/cleaned/cliburn_2025_results.csv | head
"result_id","candidate_id","edition_id","reached_round","preliminary","quarterfinalist","semifinalist","finalist","laureate_rank","prize","result_source_url","notes"$
"1","1","1","Semifinal","1","1","1","0","","","https://cliburn.org/news/semifinalists-announced-2025-cliburn-competition",""$
"2","2","1","Semifinal","1","1","1","0","","Raymond E. Buck Jury Discretionary Award","https://cliburn.org/competitions/2025-cliburn-competition/prizes-and-awards",""$
"3","3","1","Quarterfinal","1","1","0","0","","Patricia and Neal Steffen Family Jury Discretionary Award","https://cliburn.org/competitions/2025-cliburn-competition/prizes-and-awards",""$
"4","4","1","Semifinal","1","1","1","0","","Beverley Taylor Smith Award for Best Performance of a New Work","https://cliburn.org/competitions/2025-cliburn-competition/prizes-and-awards",""$
"5","5","1","Semifinal","1","1","1","0","","","https://cliburn.org/news/semifinalists-announced-2025-cliburn-competition",""$
"6","6","1","Semifinal","1","1","1","0","","","https://cliburn.org/news/semifinalists-announced-2025-cliburn-competition",""$
"7","7","1","Preliminary","1","0","0","0","","","https://cliburn.org/competitions/2025-cliburn-competition/2025-competitors",""$
"8","8","1","Preliminary","1","0","0","0","","","https://cliburn.org/competitions/2025-cliburn-competition/2025-competitors",""$
"9","9","1","Quarterfinal","1","1","0","0","","","https://cliburn.org/news/quarterfinalists-announced-2025-cliburn-competition",""$
```

The disputed prize field `Raymond E. Buck Jury Discretionary Award` is on one physical line in the `cat -A` output above.

## Physical line count for every cleaned CSV

```sh
$ wc -l data/cleaned/*.csv
    29 data/cleaned/cliburn_2025_candidates.csv
   169 data/cleaned/cliburn_2025_performances.csv
    29 data/cleaned/cliburn_2025_repertoire_coverage.csv
    29 data/cleaned/cliburn_2025_results.csv
   234 data/cleaned/cliburn_2025_works.csv
    69 data/cleaned/composer_aliases.csv
   375 data/cleaned/performance_works.csv
   169 data/cleaned/program_features.csv
   234 data/cleaned/work_aliases.csv
  1337 total
```

## Embedded-newline and header/record checks

```text
data/cleaned/cliburn_2025_candidates.csv: physical_lines=29; records=28; headers=1; embedded_newline_cells=0; cr_bytes=0
data/cleaned/cliburn_2025_performances.csv: physical_lines=169; records=168; headers=1; embedded_newline_cells=0; cr_bytes=0
data/cleaned/cliburn_2025_repertoire_coverage.csv: physical_lines=29; records=28; headers=1; embedded_newline_cells=0; cr_bytes=0
data/cleaned/cliburn_2025_results.csv: physical_lines=29; records=28; headers=1; embedded_newline_cells=0; cr_bytes=0
data/cleaned/cliburn_2025_works.csv: physical_lines=234; records=233; headers=1; embedded_newline_cells=0; cr_bytes=0
data/cleaned/composer_aliases.csv: physical_lines=69; records=68; headers=1; embedded_newline_cells=0; cr_bytes=0
data/cleaned/performance_works.csv: physical_lines=375; records=374; headers=1; embedded_newline_cells=0; cr_bytes=0
data/cleaned/program_features.csv: physical_lines=169; records=168; headers=1; embedded_newline_cells=0; cr_bytes=0
data/cleaned/work_aliases.csv: physical_lines=234; records=233; headers=1; embedded_newline_cells=0; cr_bytes=0
```

## Raw GitHub review safety

Based on the committed file bytes verified locally and the `cat -A` physical-line view, the cleaned CSV files are safe for Raw GitHub review: LF line endings, one header line, one record per physical line, valid CSV quoting, and no embedded newline characters in cells.

## Final committed-file checks

```sh
$ git show HEAD:data/cleaned/cliburn_2025_candidates.csv | wc -l
29

$ git show HEAD:data/cleaned/cliburn_2025_results.csv | wc -l
29
```

## Recommendation

PASS. The working-tree physical checks and the exact committed-file checks both show 29 physical lines for `cliburn_2025_candidates.csv` and 29 physical lines for `cliburn_2025_results.csv`.
