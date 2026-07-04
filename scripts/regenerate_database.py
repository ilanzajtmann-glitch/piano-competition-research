#!/usr/bin/env python3
"""Regenerate the SQLite database from cleaned CSV files.

The repository intentionally does not track generated binary database files.
Run this script after updating text-based CSV inputs under ``data/`` to rebuild
``data/database.sqlite`` locally.
"""

from __future__ import annotations

import argparse
import csv
import sqlite3
from pathlib import Path

DEFAULT_DATA_DIR = Path("data")
DEFAULT_OUTPUT = DEFAULT_DATA_DIR / "database.sqlite"


def table_name_for(csv_path: Path, data_dir: Path) -> str:
    """Return a stable SQLite table name for a CSV path."""
    relative = csv_path.relative_to(data_dir).with_suffix("")
    name = "__".join(relative.parts)
    return "".join(char if char.isalnum() or char == "_" else "_" for char in name)


def quote_identifier(identifier: str) -> str:
    """Safely quote a SQLite identifier."""
    return '"' + identifier.replace('"', '""') + '"'


def load_csv(conn: sqlite3.Connection, csv_path: Path, data_dir: Path) -> None:
    """Load one CSV file into a SQLite table with TEXT columns."""
    table_name = table_name_for(csv_path, data_dir)
    with csv_path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        if not reader.fieldnames:
            raise ValueError(f"CSV file has no header row: {csv_path}")

        columns = [column.strip() or f"column_{index + 1}" for index, column in enumerate(reader.fieldnames)]
        quoted_columns = [quote_identifier(column) for column in columns]
        conn.execute(f"DROP TABLE IF EXISTS {quote_identifier(table_name)}")
        conn.execute(
            f"CREATE TABLE {quote_identifier(table_name)} ("
            + ", ".join(f"{column} TEXT" for column in quoted_columns)
            + ")"
        )

        placeholders = ", ".join("?" for _ in columns)
        insert_sql = (
            f"INSERT INTO {quote_identifier(table_name)} ("
            + ", ".join(quoted_columns)
            + f") VALUES ({placeholders})"
        )
        rows = ([row.get(original, "") for original in reader.fieldnames] for row in reader)
        conn.executemany(insert_sql, rows)


def regenerate_database(data_dir: Path, output: Path) -> list[Path]:
    """Create a fresh SQLite database from all CSV files in data_dir."""
    csv_files = sorted(path for path in data_dir.rglob("*.csv") if path.is_file())
    if not csv_files:
        raise FileNotFoundError(f"No CSV files found under {data_dir}")

    output.parent.mkdir(parents=True, exist_ok=True)
    if output.exists():
        output.unlink()

    with sqlite3.connect(output) as conn:
        for csv_path in csv_files:
            load_csv(conn, csv_path, data_dir)
        conn.commit()
        conn.execute("VACUUM")

    return csv_files


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data-dir", type=Path, default=DEFAULT_DATA_DIR, help="Directory containing cleaned CSV files.")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT, help="SQLite database path to regenerate.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    csv_files = regenerate_database(args.data_dir, args.output)
    print(f"Regenerated {args.output} from {len(csv_files)} CSV file(s).")


if __name__ == "__main__":
    main()
