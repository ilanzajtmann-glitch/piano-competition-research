# Targeted CSV physical-line fix: Van Cliburn 2025

Date: 2026-07-05
Scope: targeted fix only for:

- `data/cleaned/cliburn_2025_candidates.csv`
- `data/cleaned/cliburn_2025_results.csv`

No new competition was added. No statistical analysis, API, web app, recommender, or architecture work was added.

## Fix applied

Only the two targeted CSV files were rewritten. Embedded `\r\n`, `\r`, and `\n` inside cells were replaced with spaces, and the files were written with Python `csv.writer(..., lineterminator="\n", quoting=csv.QUOTE_ALL)`.

The purpose of the rewrite is physical formatting only:

- header on physical line 1;
- one candidate/result per physical line;
- LF line endings;
- no embedded newline characters inside cells;
- valid CSV quoting.

## Required local physical checks

```sh
$ wc -l data/cleaned/cliburn_2025_candidates.csv data/cleaned/cliburn_2025_results.csv
  29 data/cleaned/cliburn_2025_candidates.csv
  29 data/cleaned/cliburn_2025_results.csv
  58 total
```

## Local raw visual checks

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

The `Raymond E. Buck Jury Discretionary Award` prize value is on one physical line in the local raw visual check.

## Embedded-newline check for targeted files

```text
data/cleaned/cliburn_2025_candidates.csv: physical_lines=29; records=28; headers=1; embedded_newline_cells=0; cr_bytes=0
data/cleaned/cliburn_2025_results.csv: physical_lines=29; records=28; headers=1; embedded_newline_cells=0; cr_bytes=0
```

## Committed-file checks

```sh
$ git show HEAD:data/cleaned/cliburn_2025_candidates.csv | python -c "import sys; print(sys.stdin.read().count('\n'))"
29

$ git show HEAD:data/cleaned/cliburn_2025_results.csv | python -c "import sys; print(sys.stdin.read().count('\n'))"
29
```

## Raw GitHub status

Not yet claimed. Success must not be claimed until the actual GitHub raw URLs for both targeted files show 29 physical lines.

## Recommendation

PENDING RAW GITHUB VERIFICATION.
