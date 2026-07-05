# Post-merge audit: Van Cliburn 2025 v1

Date: 2026-07-05
Scope: post-merge audit and CSV-format repair of existing cleaned Van Cliburn 2025 CSVs only. No new competition was collected, and no feature/API/recommendation work was added.

## Files reloaded

All cleaned CSV files under `data/cleaned/` were reloaded with Python's standard `csv` module because `pandas` is not installed in the environment. Each file was then rewritten through `csv.writer(..., lineterminator="\n", quoting=csv.QUOTE_ALL)` after replacing any embedded `\r`, `\n`, or `\r\n` inside cells with spaces.

| File | Rows |
| --- | ---: |
| `data/cleaned/cliburn_2025_candidates.csv` | 28 |
| `data/cleaned/cliburn_2025_results.csv` | 28 |
| `data/cleaned/cliburn_2025_repertoire_coverage.csv` | 28 |
| `data/cleaned/cliburn_2025_performances.csv` | 168 |
| `data/cleaned/cliburn_2025_works.csv` | 233 |
| `data/cleaned/performance_works.csv` | 374 |
| `data/cleaned/program_features.csv` | 168 |
| `data/cleaned/composer_aliases.csv` | 68 |
| `data/cleaned/work_aliases.csv` | 233 |

## Physical line-count check

Physical line counts were checked directly from file bytes after rewriting. Each cleaned CSV blob in the local commit has LF-only line endings, zero CR bytes, zero embedded-newline cells, and physical line counts equal to parsed CSV rows. The existing `.gitattributes` LF policy is retained and `data/cleaned/*.csv` is explicitly pinned to `text eol=lf` for GitHub/raw views and checkouts.

| File | Physical lines | Parsed rows | CR bytes | Embedded-newline cells |
| --- | ---: | ---: | ---: | ---: |
| `data/cleaned/cliburn_2025_candidates.csv` | 29 | 29 | 0 | 0 |
| `data/cleaned/cliburn_2025_performances.csv` | 169 | 169 | 0 | 0 |
| `data/cleaned/cliburn_2025_repertoire_coverage.csv` | 29 | 29 | 0 | 0 |
| `data/cleaned/cliburn_2025_results.csv` | 29 | 29 | 0 | 0 |
| `data/cleaned/cliburn_2025_works.csv` | 234 | 234 | 0 | 0 |
| `data/cleaned/composer_aliases.csv` | 69 | 69 | 0 | 0 |
| `data/cleaned/performance_works.csv` | 375 | 375 | 0 | 0 |
| `data/cleaned/program_features.csv` | 169 | 169 | 0 | 0 |
| `data/cleaned/work_aliases.csv` | 234 | 234 | 0 | 0 |

## Automated checks

`python src/validation/run_all.py` was rerun after the CSV rewrite and completed successfully in the local checkout; its generated `reports/data_quality_report.md` output was not retained because the requested durable audit artifact is this post-merge report.

| Check | Local result | Notes |
| --- | --- | --- |
| CSV integrity | completed | 9 cleaned CSV files have headers, LF line endings, one record per line, and consistent quoting in the local commit. |
| Candidate count | completed | 28 candidates. |
| Result consistency | completed | 6 finalists; laureate and reached-round flags are consistent. |
| Source URLs | completed | Required source URL columns are populated and start with `http`. |
| Duplicate works | completed | No duplicate normalized composer/title work keys. |
| Repertoire completeness | completed | All 28 candidates have six candidate-page program sections and at least one work per section. |
| Feature consistency | completed | `program_features.num_works` matches `performance_works`; no zero-work feature rows. |
| Missing-data report | completed | Only expected optional fields are empty. |

## Targeted audit findings

- Candidate count is consistent across candidates and results: 28 rows in each file.
- Result flags are internally consistent for preliminary, quarterfinal, semifinal, finalist, laureate rank, and prize fields.
- Source URL fields are populated in candidate, result, performance, and performance-work files.
- Duplicate-work validation did not find duplicate normalized composer/title keys in `cliburn_2025_works.csv`.
- `program_features.csv` has 168 rows, matching the 28 candidates × 6 program sections represented in `cliburn_2025_performances.csv`; each row has at least one work and the work counts match `performance_works.csv`.
- CSV formatting was repaired by rewriting every cleaned CSV with `csv.writer`, LF line terminators, and `csv.QUOTE_ALL`, forcing the actual cleaned CSV files into a consistent one-record-per-physical-line representation in the tracked diff.

## Random sample source comparison

Random sampling used `random.seed(20250705)` and sampled 5 candidates from `cliburn_2025_candidates.csv`: Mikhail Kambarov, Magdalene Ho, Roman Fediurko, Elia Cecino, and Pedro López Salas.

| Candidate | CSV result | Source result comparison | Repertoire source comparison | Status |
| --- | --- | --- | --- | --- |
| Mikhail Kambarov | Quarterfinal; John Giordano Jury Chairman Discretionary Award | Prize confirmed on the official Prizes and Awards page. | Candidate page lists the same six program sections and works, including Chopin Ballade No. 3, Montero `Rachtime`, Scarlatti K. 213, Rachmaninov Corelli Variations, Messiaen, Beethoven op. 111, Scriabin, Haydn, Chopin Sonata No. 3, Mozart K. 450, Chopin Concerto No. 1, and Tchaikovsky Concerto No. 1. | matched locally |
| Magdalene Ho | Preliminary | Not listed among official semifinalists; CSV preliminary-only status is consistent. | Candidate page lists the same six program sections and works, including Bach BWV 912, Franck, Montero, Saint-Saëns, Liszt Dante Sonata, Sweelinck, Scriabin White Mass, Mozart K. 475, Adès, Schumann, Mozart K. 459, Beethoven Concerto No. 4, and Brahms Concerto No. 1. | matched locally |
| Roman Fediurko | Preliminary | Not listed among official semifinalists; CSV preliminary-only status is consistent. | Candidate page lists the same six program sections and works, including Bach BWV 887, Montero, Rachmaninov `Élégie`, Rachmaninov Sonata No. 2, Scriabin Sonata-Fantasy, Schumann Sonata No. 2, Hofmann, Schumann Presto passionato, Rachmaninov Moments musicaux, Chopin Sonata No. 3, Mozart K. 491, Beethoven Concerto No. 5, and Rachmaninov Concerto No. 3. | matched locally |
| Elia Cecino | Semifinal | Listed among official semifinalists; CSV semifinal status is consistent. | Candidate page lists the same six program sections and works, including Shostakovich op. 87 no. 21, Montero, Beethoven op. 31 no. 1, Gounod–Liszt, Haydn Hob. XVI:34, Mendelssohn, Scriabin, Tchaikovsky, Schumann, Gubaidulina, Prokofiev, Mozart K. 491, Beethoven Concerto No. 3, and Tchaikovsky Concerto No. 1. | matched locally |
| Pedro López Salas | Preliminary | Not listed among official semifinalists; CSV preliminary-only status is consistent. | Candidate page lists the same six program sections and works, including Mozart K. 330, Montero, Ginastera, Soler R. 87, Soler R. 84, Mussorgsky, Haydn Hob. XVI:12, Schumann Kreisleriana, de Falla, Mozart K. 467, Beethoven Concerto No. 3, and Prokofiev Concerto No. 3. | matched locally |

## Source URLs consulted for the random sample

- https://cliburn.org/competitions/2025-cliburn-competition/2025-competitors/mikhail-kambarov
- https://cliburn.org/competitions/2025-cliburn-competition/2025-competitors/magdalene-ho
- https://cliburn.org/competitions/2025-cliburn-competition/2025-competitors/roman-fediurko
- https://cliburn.org/competitions/2025-cliburn-competition/2025-competitors/elia-cecino
- https://cliburn.org/competitions/2025-cliburn-competition/2025-competitors/pedro-lopez-salas
- https://cliburn.org/news/semifinalists-announced-2025-cliburn-competition
- https://cliburn.org/competitions/2025-cliburn-competition/prizes-and-awards

## Issues and fixes

Issue found: the audit needed to verify raw CSV physical line formatting directly, not only logical CSV parsing. Fix applied: every cleaned CSV was rewritten with Python `csv.writer` using `lineterminator="\n"` and `quoting=csv.QUOTE_ALL`, embedded newlines were stripped from all cells, and direct byte-level physical line counts now match parsed CSV rows for every cleaned CSV.


## Raw GitHub display verification

This repository checkout has no GitHub remote URL available to fetch a PR raw-file URL from inside the container, so this audit does not claim that GitHub raw display has been independently verified here. The committed CSV blobs themselves were checked directly with byte counts, and `.gitattributes` pins cleaned CSV checkout/rendering to LF line endings. Raw GitHub should be verified on the opened PR before merge.
