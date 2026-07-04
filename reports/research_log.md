# Research Log

## 2026-07-04 — Van Cliburn 2025 initial auditable dataset

### Official Cliburn 2025 competition page
- URL: https://cliburn.org/competitions/2025-cliburn-competition
- Extracted: edition dates, medalists, official competition context.
- Retrieved: 2026-07-04.
- Reliability: high; official organizer page.
- Unresolved problems: none for dates/medalists.
- Manual decisions: medal ranks encoded as laureate ranks 1–3.

### Official Cliburn 2025 competitors page
- URL: https://cliburn.org/competitions/2025-cliburn-competition/2025-competitors
- Extracted: exactly 28 competitors, nationality/representation text, candidate profile URLs.
- Retrieved: 2026-07-04.
- Reliability: high; official organizer page.
- Unresolved problems: birth years unavailable; left null.
- Manual decisions: listed age was not converted into birth_year because exact birth date is unknown.

### Quarterfinalists announcement
- URL: https://cliburn.org/news/quarterfinalists-announced-2025-cliburn-competition
- Extracted: 18 quarterfinalists.
- Retrieved: 2026-07-04.
- Reliability: high; official organizer announcement.
- Unresolved problems: none for quarterfinalist status.
- Manual decisions: candidates not in this list are marked preliminary-only reached_round=Preliminary.

### Semifinalists announcement
- URL: https://cliburn.org/news/semifinalists-announced-2025-cliburn-competition
- Extracted: 12 semifinalists.
- Retrieved: 2026-07-04.
- Reliability: high; official organizer announcement.
- Unresolved problems: none for semifinalist status.
- Manual decisions: quarterfinalists not in this list are marked reached_round=Quarterfinal.

### Official schedule page
- URL: https://cliburn.org/competitions/2025-cliburn-competition/schedule
- Extracted: performance rounds, dates, finalist concerto works, rule note distinguishing required/list repertoire.
- Retrieved: 2026-07-04.
- Reliability: high; official organizer schedule.
- Unresolved problems: schedule page did not expose all solo recital work lists in the captured text.
- Manual decisions: performance rows are marked performed when the source schedule says competitors performed in that round; work-level rows are only entered where captured from official text.

### Prizes and awards page
- URL: https://cliburn.org/competitions/2025-cliburn-competition/prizes-and-awards
- Extracted: medal prizes and special awards.
- Retrieved: 2026-07-04.
- Reliability: high; official organizer prize page.
- Unresolved problems: none for prize labels captured.
- Manual decisions: finalist/semifinalist/quarterfinalist participation awards are not duplicated into each candidate prize field unless individually named.

### Carter Johnson official candidate page
- URL: https://cliburn.org/competitions/2025-cliburn-competition/2025-competitors/carter-johnson
- Extracted: complete listed repertoire for Carter Johnson across rounds.
- Retrieved: 2026-07-04.
- Reliability: high; official candidate page.
- Unresolved problems: superseded by the complete candidate-page repertoire capture below.
- Manual decisions: raw repertoire text preserved; normalized titles are conservative lower-case variants.

## 2026-07-04 — Complete candidate-page repertoire capture

### Official candidate pages for all 28 competitors
- URL pattern: https://cliburn.org/competitions/2025-cliburn-competition/2025-competitors/{candidate-slug}
- Extracted: all published candidate-page repertoire items under Preliminary Round, Quarterfinal Round, Semifinal Round - Recital, Semifinal Round - Mozart Concerto, Final Round - Concerto 1, and Final Round - Concerto 2.
- Retrieved: 2026-07-04.
- Reliability: high; official organizer candidate pages.
- Unresolved problems: pages list later-round repertoire even for candidates who did not advance; these are retained as `planned` when not reached and `performed` when reached.
- Manual decisions made: compound composer/transcriber strings such as BACH–BUSONI and SAINT-SAËNS–LISZT–HOROWITZ are preserved as raw composer tokens pending authority normalization; raw repertoire text is preserved in `performance_works.csv`.

## 2026-07-04 — Derived feature/report consistency regeneration

- Regenerated `reports/data_quality_report.md` from current cleaned CSVs after confirming `cliburn_2025_works.csv` has 233 rows and `performance_works.csv` has 374 rows.
- Added a feature consistency validation that compares every `program_features.csv` row to `performance_works.csv` counts and rejects zero-work feature rows.
- Result: all 168 feature rows have nonzero `num_works`, and feature counts match the current performance-work table.

## 2026-07-04 — CSV integrity normalization

- Rewrote cleaned CSV files with LF line endings using Python `csv.writer` and added `csv_integrity_check.py`.
- Verification requires a header row, no NUL bytes, LF-only line endings, uniform column counts, one parsed CSV record per physical line, and valid CSV quoting.
- Re-ran feature generation and validation after normalization.
