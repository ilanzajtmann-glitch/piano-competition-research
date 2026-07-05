# Post-merge adversarial audit: Van Cliburn 2025 v1

Date: 2026-07-05
Scope: adversarial post-merge audit and CSV-format repair verification for the existing cleaned Van Cliburn 2025 CSVs only. No new competition was collected, and no feature/API/recommendation work was added.

## Auditor posture

This audit deliberately treats the dataset as unreliable until disproven. I attempted to falsify the cleaned data by checking physical CSV storage, parser agreement, key uniqueness, row-count consistency, result logic, source URL coverage, work duplication, derived-file freshness, and sampled source comparisons. Previously generated reports were not trusted as evidence; checks were regenerated from the current cleaned CSV files.

## Files reloaded and rewritten

All cleaned CSV files under `data/cleaned/` were reloaded with Python's standard `csv` module and rewritten with `csv.writer(..., lineterminator="\n", quoting=csv.QUOTE_ALL)`. Embedded `\r`, `\n`, and `\r\n` inside cells were replaced with spaces before writing.

| File | Data rows |
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

## Physical validation

Physical validation opened the raw bytes exactly as stored in the repository checkout. For each file, byte-level LF counts, `bytes.splitlines()`, Python `csv.reader`, Ruby `CSV.read`, and SQLite `.import --csv` were cross-checked. No valid parser disagreement was found.

| File | LF bytes / physical lines | `splitlines()` rows | Python parsed rows | Ruby parsed rows | SQLite data rows | CR bytes | Embedded-newline cells |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `data/cleaned/cliburn_2025_candidates.csv` | 29 | 29 | 29 | 29 | 28 | 0 | 0 |
| `data/cleaned/cliburn_2025_performances.csv` | 169 | 169 | 169 | 169 | 168 | 0 | 0 |
| `data/cleaned/cliburn_2025_repertoire_coverage.csv` | 29 | 29 | 29 | 29 | 28 | 0 | 0 |
| `data/cleaned/cliburn_2025_results.csv` | 29 | 29 | 29 | 29 | 28 | 0 | 0 |
| `data/cleaned/cliburn_2025_works.csv` | 234 | 234 | 234 | 234 | 233 | 0 | 0 |
| `data/cleaned/composer_aliases.csv` | 69 | 69 | 69 | 69 | 68 | 0 | 0 |
| `data/cleaned/performance_works.csv` | 375 | 375 | 375 | 375 | 374 | 0 | 0 |
| `data/cleaned/program_features.csv` | 169 | 169 | 169 | 169 | 168 | 0 | 0 |
| `data/cleaned/work_aliases.csv` | 234 | 234 | 234 | 234 | 233 | 0 | 0 |

Targeted raw-byte checks for the files previously reported as malformed:

- `cliburn_2025_candidates.csv`: 29 physical LF-delimited lines, 29 parsed rows, 28 data records, 0 CR bytes, 0 embedded-newline cells.
- `cliburn_2025_results.csv`: 29 physical LF-delimited lines, 29 parsed rows, 28 data records, 0 CR bytes, 0 embedded-newline cells. Prize fields including `Raymond E. Buck Jury Discretionary Award` are single-cell, single-record values.

`.gitattributes` retains the repository LF policy and explicitly pins `data/cleaned/*.csv` to `text eol=lf` for GitHub/raw views and checkouts.

## Logical validation regenerated from cleaned CSVs

| Attack surface | Attempted falsification | Result |
| --- | --- | --- |
| Missing candidates | Counted candidate rows and compared candidate IDs against results. | No contradiction found: 28 candidates and the same 28 candidate IDs in results. |
| Duplicated candidates | Checked uniqueness of `candidate_id`. | No duplicate candidate IDs found. |
| Duplicated works | Checked normalized `(composer_id, normalized_title)` keys. | No duplicate normalized work keys found. |
| Malformed CSV files | Compared byte line counts, `splitlines()`, Python CSV rows, Ruby CSV rows, SQLite imports, CR bytes, final LF, row widths, and embedded-newline cells. | No contradiction found in valid parser/byte checks. |
| Contradictory round information | Checked reached-round flags for Preliminary, Quarterfinal, Semifinal, and Final. | No contradictory round flags found. |
| Incorrect laureate information | Checked finalist count and laureate ranks. | 6 finalists and laureate ranks `1`, `2`, and `3` found. |
| Missing source URLs | Checked source URL fields in candidates, results, performances, and performance works. | Required URL fields begin with `http`. |
| Stale `program_features` | Recomputed performance-work counts per performance and compared to `program_features.num_works`. | No mismatch found across 168 feature rows. |
| Stale repertoire coverage | Compared coverage program rows to performance rows per candidate and checked zero-work feature counts. | No mismatch found; each candidate has 6 program rows and 0 zero-work feature rows. |
| Parser failures | Imported every CSV into SQLite and parsed every CSV with Ruby CSV and Python CSV. | No parser failure found. |

## Automated project validation

`python src/validation/run_all.py` was rerun after the CSV rewrite and completed successfully in the local checkout. Its generated `reports/data_quality_report.md` output was not retained because the requested durable artifact is this adversarial audit.

| Check | Local result | Notes |
| --- | --- | --- |
| `csv_integrity_check.py` | completed | 9 cleaned CSV files have headers, LF line endings, one record per physical line, and consistent quoting in the local checkout. |
| `candidate_count_check.py` | completed | 28 candidates. |
| `result_consistency_check.py` | completed | Finalists, laureates, and reached-round flags are internally consistent. |
| `source_url_check.py` | completed | Required URL columns are populated. |
| `duplicate_work_check.py` | completed | No duplicate normalized composer/title work keys. |
| `repertoire_completeness_check.py` | completed | All 28 candidates have six candidate-page program sections and at least one work per section. |
| `feature_consistency_check.py` | completed | `program_features.num_works` matches `performance_works`; no zero-work feature rows. |
| `missing_data_report.py` | completed | Only expected optional fields are empty. |

## Random sample source comparison

Random sampling used `random.seed(20250705)` and sampled 5 candidates from `cliburn_2025_candidates.csv`: Mikhail Kambarov, Magdalene Ho, Roman Fediurko, Elia Cecino, and Pedro López Salas.

| Candidate | CSV result | Source result comparison | Repertoire source comparison | Local status |
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

## Failed tests

No valid regenerated test failed. A deliberately naive regular-expression scan was discarded because it incorrectly treated record-delimiter newlines after quoted fields as embedded newlines; this is not a valid CSV parser and was not used as evidence. Valid byte-level checks, Python CSV, Ruby CSV, SQLite CSV import, and project validators agreed.

## Remaining uncertainties

- This container checkout has no GitHub remote URL configured, so the PR's Raw GitHub rendered view could not be fetched from inside the container. The committed blobs were checked directly, but Raw GitHub should still be visually verified on the PR before merge.
- The source comparison was a deterministic random sample of 5 candidates, not a full source-page re-audit of all 28 candidates.
- Optional metadata fields such as candidate birth years and detailed work metadata remain empty unless source-confirmed; this is expected but limits downstream enrichment.

## Confidence level

Medium-high for CSV physical integrity and internal logical consistency because multiple independent local parsers and byte-level checks agree. Medium for source fidelity because only 5 of 28 candidates were source-sampled in this post-merge audit.

## Recommendation

PASS WITH RESERVATIONS.

Rationale: I actively attempted to falsify the dataset and found no valid local physical or logical contradiction. The reservation is that Raw GitHub rendering could not be independently fetched from this container and must be checked on the PR before merge.
