import csv
from pathlib import Path

allowed_suffix='.csv'
paths=sorted(Path('data/cleaned').glob(f'*{allowed_suffix}'))
assert paths, 'no cleaned CSV files found'
for path in paths:
    raw=path.read_bytes()
    assert raw.endswith(b'\n'), f'{path} does not end with newline'
    assert b'\0' not in raw, f'{path} contains NUL byte'
    assert b'\r' not in raw, f'{path} contains CR characters; expected LF-only CSV'
    physical_lines=raw.splitlines()
    with open(path, newline='', encoding='utf-8') as f:
        rows=list(csv.reader(f))
    assert rows, f'{path} is empty'
    assert all(cell.strip() for cell in rows[0]), f'{path} header contains empty column name'
    width=len(rows[0])
    bad=[i+1 for i,row in enumerate(rows) if len(row)!=width]
    assert not bad, f'{path} has inconsistent column counts at rows {bad[:10]}'
    assert len(physical_lines)==len(rows), f'{path} has embedded newlines or concatenated physical/logical rows: physical={len(physical_lines)} parsed={len(rows)}'
print(f'PASS csv_integrity_check: {len(paths)} cleaned CSV files have headers, LF line endings, one record per line, and consistent quoting')
