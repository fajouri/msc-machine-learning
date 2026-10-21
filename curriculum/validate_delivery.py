"""Check the SETUP-04 Markdown planning contract; standard library only."""
import csv
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
SCHEDULES = (
    'Online (S01, S03, S05, S07, S09, S11, S13, S14, S15)',
    'Campus labs (S02, S04, S06, S08, S10, S12)',
    'Campus presentations (S16)',
)


def section(text, heading, level):
    marker = '#' * level + ' ' + heading + '\n'
    if text.count(marker) != 1:
        raise ValueError('missing or duplicate section: ' + heading)
    return re.split(r'^#{1,' + str(level) + r'} ', text.split(marker)[1],
                    maxsplit=1, flags=re.M)[0]


def rows(text):
    return [[cell.strip() for cell in line.strip().strip('|').split('|')]
            for line in text.splitlines() if line.startswith('| ')
            and not line.startswith('| ---')]


def validate(text, root=ROOT):
    errors = []

    def check(condition, message):
        if not condition:
            errors.append(message)

    try:
        check('**Draft pending professor review.**' in text, 'proposal status missing')
        with (root / 'curriculum/session-map.csv').open(encoding='utf-8-sig', newline='') as f:
            baseline = list(csv.DictReader(f))
        table = rows(section(text, 'Per-session delivery matrix', 2))
        check(table[0] == ['Session', 'Mode', 'Engagement / practical activity',
                          'Formative evidence', 'Offline or service fallback',
                          'Specific accessibility provision', 'Logistics / preparation'],
              'session table contract')
        sessions = table[1:]
        check([r[:2] for r in sessions] ==
              [['S' + r['session'], r['proposed_mode']] for r in baseline],
              'session order, coverage or mode differs from working map')
        check(len(sessions) == 16 and sum(r[1] == 'online' for r in sessions) == 9
              and sum(r[1] == 'campus' for r in sessions) == 7, '16 sessions / 9 online / 7 campus')
        for row in sessions:
            check(len(row) == 7 and all(cell.strip() and cell.strip().lower() not in
                  ('todo', 'tbd', '-') for cell in row), 'incomplete planning row: ' + row[0])
        for heading in SCHEDULES:
            schedule = rows(section(text, heading, 3))
            check(schedule[0] == ['Start', 'End', 'Activity'], 'schedule table contract: ' + heading)
            previous = 0
            slots = 0
            for start, end, activity in schedule[1:]:
                start, end = int(start), int(end)
                check(start == previous and end > start and bool(activity),
                      'schedule gap, overlap or invalid interval: ' + heading)
                previous = end
                if heading == SCHEDULES[2] and 'slots:' in activity:
                    match = re.fullmatch(
                        r'(\w+) slots: (\d+)-minute presentation \+ (\d+)-minute Q&A '
                        r'\+ (\d+)-minute changeover each', activity)
                    if not match:
                        raise ValueError('invalid S16 presentation slot format')
                    count = {'Five': 5}.get(match[1], 0)
                    duration, questions, transition = map(int, match.groups()[1:])
                    check(count > 0 and duration == 10 and questions > 0 and transition > 0
                          and count * (duration + questions + transition) == end - start,
                          'S16 slot capacity or ten-minute presentation constraint')
                    slots += count
            check(previous == 180, 'schedule must end at 180 minutes: ' + heading)
            if heading == SCHEDULES[2]:
                check(slots == 10, 'S16 must provide ten presentation slots')
        # Check that locally linked inputs and evidence remain navigable.
        for link in re.findall(r'\]\(([^)]+)\)', text):
            if not link.startswith(('https://', 'http://', '#')):
                check((root / 'docs' / link.split('#')[0]).is_file(), 'broken local link: ' + link)
    except (ValueError, TypeError, IndexError, KeyError, OSError) as exc:
        errors.append('invalid delivery plan: ' + str(exc))
    return errors


def main():
    try:
        errors = validate((ROOT / 'docs/delivery-plan.md').read_text(encoding='utf-8'))
    except OSError as exc:
        errors = [str(exc)]
    if errors:
        for error in errors:
            print('FAIL: ' + error)
        return 1
    print('PASS: 16 ordered sessions, 9 online / 7 campus, complete planning fields.')
    print('PASS: three continuous 180-minute schedules; ten 10-minute presentations fit S16.')
    print('Professor review and pre-delivery rehearsal remain required.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
