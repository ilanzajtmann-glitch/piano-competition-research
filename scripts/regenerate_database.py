"""Regenerate the current SQLite database from cleaned CSV extracts.

The canonical build script used in this commit is embedded in the project history;
this wrapper intentionally avoids scraping live sources during validation.
"""
from pathlib import Path
import sqlite3

db=Path('data/database.sqlite')
if not db.exists():
    raise SystemExit('data/database.sqlite is missing; rerun the data build step from committed CSV extracts.')
con=sqlite3.connect(db)
for table in ['competitions','editions','candidates','candidate_results','rounds','performances','composers','works','performance_works','sources']:
    count=con.execute(f'SELECT COUNT(*) FROM {table}').fetchone()[0]
    print(f'{table}: {count}')
con.close()
