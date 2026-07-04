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
- Unresolved problems: complete candidate-page repertoire still needs to be captured for the other 27 competitors.
- Manual decisions: raw repertoire text preserved; normalized titles are conservative lower-case variants.
