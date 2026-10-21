"""Validate SETUP-02 structure and unchanged inputs using only the standard library."""
import csv
import hashlib
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CUR = ROOT / 'curriculum'
matrix = (CUR / 'traceability-matrix.md').read_text(encoding='utf-8')
gaps = (CUR / 'traceability-gaps.md').read_text(encoding='utf-8')


def check(condition, label):
    if not condition:
        raise SystemExit('FAIL: ' + label)
    print('PASS: ' + label)


baseline = ROOT / 'curriculum/session-map.csv'
check(hashlib.sha256(baseline.read_bytes()).hexdigest().upper() ==
      'A60B0336DE9801C95A9ED082FF082E52CFA9B8DAAFF07EFBA4F9C855440E4F10',
      'working session map unchanged from audit baseline')
with baseline.open(encoding='utf-8-sig', newline='') as source:
    sessions = list(csv.DictReader(source))
check([s['session'] for s in sessions] == [f'{i:02}' for i in range(1, 17)],
      '16 unique ordered source sessions')

crosswalk = matrix.split('## Full session crosswalk')[1].split('## Session evidence')[0]
rows = [[c.strip() for c in line.strip('|').split('|')]
        for line in crosswalk.splitlines() if re.match(r'^\| S\d{2} \|', line)]
check(len(rows) == 16 and all(len(r) == 10 for r in rows),
      '128 LO/session intersections present')
for row, source in zip(rows, sessions):
    check(row[0] == 'S' + source['session'] and row[1] == source['proposed_mode']
          and all(v in {'M', 'P', '—'} for v in row[2:])
          and {f'LO{i}' for i, value in enumerate(row[2:], 1) if value == 'M'}
          == set(source['learning_outcomes'].split(';')),
          row[0] + ' baseline LO links and mode preserved')
check(sum(r[1] == 'online' for r in rows) == 9 and
      sum(r[1] == 'campus' for r in rows) == 7, '9 online / 7 campus modes')
outcomes = matrix.split('## Approved outcomes')[1].split('## Full session')[0]
assessment = matrix.split('## Approved assessments')[1].split('## Review')[0]
for section, columns, label in [(outcomes, 3, '8 source outcomes'),
                                (assessment, 4, '24 LO/assessment intersections')]:
    entries = [[c.strip() for c in line.strip('|').split('|')]
               for line in section.splitlines() if re.match(r'^\| LO\d \|', line)]
    check([r[0] for r in entries] == [f'LO{i}' for i in range(1, 9)]
          and all(len(r) == columns and all(r) for r in entries), label)
activities = matrix.split('## Session evidence')[1].split('## Approved assessments')[0]
check(re.findall(r'^\| (S\d{2}) ', activities, re.M) ==
      [f'S{i:02}' for i in range(1, 17)], 'all sessions have activity/evidence audit rows')
check(all(t in assessment for t in ['60%', '30%', '10%', '3 hours', '10 minutes',
                                    'leaderboard', 'technical report']),
      'approved assessment constraints recorded (manual source comparison also required)')
check(len(re.findall(r'^\| G\d{2} \|', gaps, re.M)) == 11 and
      len(re.findall(r'^\| R\d{2} \|', gaps, re.M)) == 9,
      '11 findings and 9 separate recommendations')
for doc in CUR.glob('traceability-*.md'):
    for target in re.findall(r'\]\(([^)]+)\)', doc.read_text(encoding='utf-8')):
        if not target.startswith('https://'):
            check((doc.parent / target).is_file(), doc.name + ' local link: ' + target)
descriptor = ROOT / 'docs/Machine Learning.pdf'
if descriptor.exists():
    check(hashlib.sha256(descriptor.read_bytes()).hexdigest().upper() ==
          'BDC82A68602E666E13B869DE83279241C85D81A307A7F770742F245690F40660',
          'local descriptor unchanged from audit baseline')
else:
    print('SKIP: local descriptor absent; source identity cannot be rechecked')
print('Structural validation complete. Academic validity and approval require professor review.')
