# Targeted CSV physical-line fix: Van Cliburn 2025

Date: 2026-07-05
Scope: targeted fix only for:

- `data/cleaned/cliburn_2025_candidates.csv`
- `data/cleaned/cliburn_2025_results.csv`

No new competition was added. No statistical analysis, API, web app, recommender, or architecture work was added.

## Local fix applied

The two targeted CSV files were rewritten locally. Embedded `\r\n`, `\r`, and `\n` inside cells were replaced with spaces, and the files were written with Python `open(..., newline="")` and `csv.writer(..., lineterminator="\n", quoting=csv.QUOTE_ALL)`.

## Local committed-blob verification

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

The local commit could not be pushed from this environment because GitHub access through the shell failed with HTTP 403 from the CONNECT tunnel.

## Raw GitHub verification after failed push

Raw GitHub was checked after the failed push attempt:

- `https://raw.githubusercontent.com/ilanzajtmann-glitch/piano-competition-research/refs/pull/3/head/data/cleaned/cliburn_2025_candidates.csv?cb=afterpushattempt1`
  - Raw GitHub reported total lines: 1.
  - This still fails the required 29 physical lines.
- `https://raw.githubusercontent.com/ilanzajtmann-glitch/piano-competition-research/refs/pull/3/head/data/cleaned/cliburn_2025_results.csv?cb=afterpushattempt1`
  - Raw GitHub reported total lines: 3.
  - This still fails the required 29 physical lines.
  - The raw file still contains broken prize fields at `Raymond E. Buck` and `Nancy Lee and Perry R. Bass`.

## Verdict

FAIL.

The local committed blobs have 29 newline bytes for both targeted files, but the pushed PR branch on GitHub still shows the old malformed raw files. The reason is that the corrected local commit could not be pushed to the GitHub PR branch from this environment due to the 403 CONNECT tunnel failure.
