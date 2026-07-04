# Van Cliburn 2025 Audit

## 1. What was collected
- 28 official competitors with nationality/representation text and profile source URLs.
- Verified advancement flags: preliminary, quarterfinalist, semifinalist, finalist.
- Medal ranks and named special prizes from official Cliburn sources.
- Complete candidate-page repertoire listings for all 28 competitors across all six published program sections: Preliminary Round, Quarterfinal Round, Semifinal Round - Recital, Semifinal Round - Mozart Concerto, Final Round - Concerto 1, and Final Round - Concerto 2.
- 168 sourced program/performance rows: 28 candidates × 6 candidate-page program sections.
- 374 sourced performance-work rows and 233 normalized work rows.

## 2. Source list
- Official competition page: https://cliburn.org/competitions/2025-cliburn-competition
- Competitors index: https://cliburn.org/competitions/2025-cliburn-competition/2025-competitors
- Official candidate pages for all 28 competitors under: https://cliburn.org/competitions/2025-cliburn-competition/2025-competitors/
- Quarterfinalists announcement: https://cliburn.org/news/quarterfinalists-announced-2025-cliburn-competition
- Semifinalists announcement: https://cliburn.org/news/semifinalists-announced-2025-cliburn-competition
- Finalists announcement: https://cliburn.org/news/finalists-announced-2025-cliburn-competition
- Prizes and awards: https://cliburn.org/competitions/2025-cliburn-competition/prizes-and-awards

## 3. Number of candidates
- 28 candidates.

## 4. Number of performances/programs
- 168 candidate-page program rows.
- `performance_status` is `performed` only for rounds the competitor reached and `planned` for later candidate-page program listings that were published but not performed because the candidate did not advance.

## 5. Number of works
- 233 normalized work rows.
- 374 performance-work rows preserving the candidate-page raw text.

## 6. Completeness percentage
- Candidate/results completeness: 100% for expected count, candidate source URLs, result source URLs, and reached-round flags.
- Candidate-page repertoire capture: 100% for the six published candidate-page program sections for all 28 candidates.
- Work metadata enrichment completeness: incomplete by design for composer birth/death dates, work catalog parsing, key parsing, genre, period, and approximate duration. These fields remain null rather than guessed.

## 7. Known missing data
- Birth years are null because exact birth dates were not captured from official sources.
- Work metadata authority enrichment remains incomplete; raw title and conservative normalized title are preserved.
- Performance status is inferred from verified reached-round results and candidate-page listing structure; the Cliburn pages list repertoire for future rounds for non-advancing competitors, so those rows are marked `planned` rather than `performed`.
- Xiaofu Ju's page states withdrawal for medical reasons; the candidate-page repertoire is still captured because it is officially published.

## 8. Validation results
- Candidate count check: passed.
- Result consistency check: passed.
- Source URL check: passed.
- Duplicate work check: passed.
- Repertoire completeness check: passed for all 28 candidates × six candidate-page program sections, with at least one work row per program section.
- Feature consistency check: passed; `program_features.csv` `num_works` matches `performance_works.csv` counts and has no zero-work rows.
- Missing data report: passed as a report, with known nulls documented.

## 9. Whether the dataset is ready for statistical analysis
Not yet. Candidate-page repertoire and results are now complete enough for source review, but statistical analysis should wait until a human audit confirms the `planned` versus `performed` interpretation and the work/composer normalization choices.

## 10. Next recommended competition/edition
Do not move to another competition yet. The next recommended step is human review of Van Cliburn 2025 work normalization and planned/performed status, then rerun validation and only then consider minimal descriptive analysis.
