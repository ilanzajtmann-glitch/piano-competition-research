# piano-competition-research

Data-quality-first research database for repertoire performed in major international piano competitions, excluding the Chopin Competition.

## Current scope

The current dataset is limited to the 2025 Van Cliburn International Piano Competition. It stores competitors, verified round outcomes, official source URLs, performance occurrences by round, and a conservative subset of captured work-level repertoire.

## Rebuild / validate

```bash
python scripts/regenerate_database.py
python src/validation/run_all.py
```

Do not proceed to statistical modeling until the audit report says work-level repertoire is complete.
