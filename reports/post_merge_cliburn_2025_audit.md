# Targeted CSV physical-line fix: Van Cliburn 2025

Date: 2026-07-05
Pull request: https://github.com/ilanzajtmann-glitch/piano-competition-research/pull/3
Branch checked locally: `codex/effectuer-un-audit-post-fusion-van-cliburn-2025`

## Scope

Targeted fix only for:

- `data/cleaned/cliburn_2025_candidates.csv`
- `data/cleaned/cliburn_2025_results.csv`

No `.gitattributes` change was made in this update. No new competition, statistical analysis, API, web app, recommender, or architecture work was added.

## Local rewrite performed

The two targeted CSV files were read as CSV rows. Every cell was sanitized by replacing `\r`, `\n`, and `\r\n` runs with a single space and stripping repeated spaces. The files were then written as UTF-8 text with `open(..., newline="")` and `csv.writer(..., lineterminator="\n", quoting=csv.QUOTE_ALL)`.

## Local branch and status commands

```sh
$ git status
On branch codex/effectuer-un-audit-post-fusion-van-cliburn-2025
nothing to commit, working tree clean

$ git branch --show-current
codex/effectuer-un-audit-post-fusion-van-cliburn-2025
```

## Local working-tree line counts

```sh
$ wc -l data/cleaned/cliburn_2025_candidates.csv
29 data/cleaned/cliburn_2025_candidates.csv

$ wc -l data/cleaned/cliburn_2025_results.csv
29 data/cleaned/cliburn_2025_results.csv
```

## Local embedded-newline checks

```text
data/cleaned/cliburn_2025_candidates.csv: rows=29 physical_lf=29 embedded_newline_cells=0 cr_bytes=0
data/cleaned/cliburn_2025_results.csv: rows=29 physical_lf=29 embedded_newline_cells=0 cr_bytes=0
```

## Local committed-blob checks

```sh
$ git show HEAD:data/cleaned/cliburn_2025_candidates.csv | python -c "import sys; print(sys.stdin.read().count('\\n'))"
29

$ git show HEAD:data/cleaned/cliburn_2025_results.csv | python -c "import sys; print(sys.stdin.read().count('\\n'))"
29
```

## Push attempt

```sh
$ git remote -v
origin  https://github.com/ilanzajtmann-glitch/piano-competition-research (fetch)
origin  https://github.com/ilanzajtmann-glitch/piano-competition-research (push)

$ git push origin HEAD:refs/heads/codex/effectuer-un-audit-post-fusion-van-cliburn-2025
fatal: unable to access 'https://github.com/ilanzajtmann-glitch/piano-competition-research/': CONNECT tunnel failed, response 403
```

No commit hash was pushed because the push failed before updating GitHub.

## Remote Raw GitHub verification after failed push

Raw GitHub PR #3 was checked after the failed push attempt:

- `https://raw.githubusercontent.com/ilanzajtmann-glitch/piano-competition-research/refs/pull/3/head/data/cleaned/cliburn_2025_candidates.csv?cb=20260705final`
  - Raw GitHub total lines: 1
  - Required total lines: 29
  - Status: FAIL
- `https://raw.githubusercontent.com/ilanzajtmann-glitch/piano-competition-research/refs/pull/3/head/data/cleaned/cliburn_2025_results.csv?cb=20260705final`
  - Raw GitHub total lines: 3
  - Required total lines: 29
  - Status: FAIL
  - Remaining remote issue: the raw file still breaks `Raymond E. Buck Jury Discretionary Award` and `Nancy Lee and Perry R. Bass Gold Medal; Audience Award` across physical lines.

## Final status

FAIL.

Local working-tree checks and local committed-blob checks report 29 lines for both targeted files, but the remote GitHub PR branch still reports 1 line for candidates and 3 lines for results. The pushed branch does not match the locally validated commit because the push to GitHub failed with a CONNECT tunnel 403.
