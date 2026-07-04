import subprocess, sys, pathlib
checks=['candidate_count_check.py','result_consistency_check.py','source_url_check.py','duplicate_work_check.py','missing_data_report.py']
out=['# Data Quality Report','']
failed=False
for c in checks:
    p=subprocess.run([sys.executable, 'src/validation/'+c],text=True,capture_output=True)
    status='PASS' if p.returncode==0 else 'FAIL'; failed |= p.returncode!=0
    out += [f'## {c}: {status}','```',p.stdout+p.stderr,'```','']
pathlib.Path('reports/data_quality_report.md').write_text('\n'.join(out),encoding='utf-8')
print('\n'.join(out))
sys.exit(1 if failed else 0)
