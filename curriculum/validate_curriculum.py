"""Validate SETUP-03 data and accounting using Python's standard library."""
import csv
import hashlib
import json
import math
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


def validate(data, root=ROOT):
    """Return validation errors; source checks work without the private PDF."""
    errors = []

    def check(ok, message):
        if not ok:
            errors.append(message)

    def hours(value):
        return type(value) in (int, float) and math.isfinite(value) and value >= 0

    try:
        check(data['schema_version'] == 1 and data['issue'] == 3, 'schema version / issue')
        check(data['status'] == 'draft_pending_professor_review', 'academic review status')
        check(data['dependencies'] == [
            {'issue': n, 'status': 'closed_verified_2026-10-21'} for n in (1, 2)],
            'dependency evidence')
        expected_sources = {
            'docs/Machine Learning.pdf': 'local_descriptor_do_not_publish',
            'curriculum/traceability-matrix.md': 'audited_descriptor_transcription_and_proposals',
            'curriculum/session-map.csv': 'working_map',
            'docs/PRODUCTION_PLAN.md': 'lecturer_report_2026-10-21',
        }
        check(len(data['sources']) == 4 and
              {s['path']: s['status'] for s in data['sources']} == expected_sources,
              'source inventory and authority')
        for source in data['sources']:
            if source['path'] not in expected_sources:
                continue
            path = root / source['path']
            if source['path'] == 'docs/Machine Learning.pdf':
                check(source['sha256'] ==
                      'bdc82a68602e666e13b869de83279241c85d81a307a7f770742f245690f40660',
                      'descriptor baseline identity')
                if not path.exists():
                    continue
            payload = path.read_bytes()
            if path.suffix != '.pdf':
                payload = payload.replace(b'\r\n', b'\n')
            check(source['hash_mode'] == ('raw_bytes' if path.suffix == '.pdf' else 'utf8_lf'),
                  'explicit source hash convention')
            check(hashlib.sha256(payload).hexdigest() == source['sha256'],
                  'source drift: ' + source['path'])
        approved = data['approved']
        check((approved['module'], approved['mqf_level'], approved['ects']) ==
              ('M5: Machine Learning', 7, 10), 'approved module identity')
        check(approved['hours'] == dict(total=250, contact=50, self_study=160, assessment=40),
              'approved 250-hour budgets')
        matrix = (root / 'curriculum/traceability-matrix.md').read_text(encoding='utf-8')
        outcomes = [dict(id=code, wording=wording, descriptor_page=int(page))
                    for code, wording, page in re.findall(
                        r'^\| (LO\d) \| (.*?) \| p\. (\d) \|$', matrix, re.M)]
        check(len(outcomes) == 8 and approved['learning_outcomes'] == outcomes,
              'exact audited LO1-LO8 wording')
        blocks = approved['topic_blocks']
        ranges = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10), (11, 12), (13, 14), (15,), (16,)]
        check([b['id'] for b in blocks] == [f'B{i:02}' for i in range(1, 10)] and
              [b['sessions'] for b in blocks] == [[f'S{i:02}' for i in r] for r in ranges],
              'approved topic-block sequence')
        check('OpenAI Gym' in blocks[5]['content_summary'], 'approved named RL environment retained')
        for b in blocks:
            check(b['descriptor_page'] == 2 and bool(b['title'].strip()) and
                  bool(b['content_summary'].strip()), 'block source and description')
        with (root / 'curriculum/session-map.csv').open(encoding='utf-8-sig', newline='') as f:
            baseline = list(csv.DictReader(f))
        sessions = data['sessions']
        check(len(sessions) == 16, '16 sessions required')
        for session, row in zip(sessions, baseline):
            check(session['id'] == 'S' + row['session'] and
                  all(session[key] == row[key] for key in ('title', 'proposed_mode', 'indicative_topics')) and
                  session['learning_outcomes'] == row['learning_outcomes'].split(';'),
                  'working session map preserved: ' + row['session'])
            check(session['block_id'] in {b['id'] for b in blocks if session['id'] in b['sessions']},
                  'session block membership')
            check(session['contact_hours'] == 3, 'three contact hours per session')
            study = session['self_study']
            check(hours(study['hours']) and study['hours'] > 0 and
                  study['status'] == 'proposed' and bool(study['activity'].strip()),
                  'positive proposed self-study allocation and activity')
        check(sum(s['self_study']['hours'] for s in sessions) == 160, 'self-study totals 160')
        check(sum(s['contact_hours'] for s in sessions) == 48, 'teaching totals 48')
        check(sum(s['proposed_mode'] == 'online' for s in sessions) == 9 and
              sum(s['proposed_mode'] == 'campus' for s in sessions) == 7, '9 online / 7 campus')
        reconciliation = data['contact_reconciliation']
        check(reconciliation == dict(
            status='lecturer_report_2026-10-21', scheduled_teaching_hours=48,
            descriptor_contact_hours=50, gap_hours=2,
            additional_activity=dict(id='CERT', title='University-administered certification exam',
                                     hours=2, category='contact', owner='university',
                                     lecturer_deliverable=False, m5_assessment=False),
            online_sessions=9, campus_sessions=7), '48 + 2 contact reconciliation and responsibility')
        assessments = approved['assessments']
        check([(a['id'], a['weight_percent']) for a in assessments] ==
              [('E', 60), ('K', 30), ('P', 10)], 'three approved assessments / 60-30-10 weights')
        check(assessments[0]['duration_minutes'] == 180 and
              assessments[2]['duration_minutes'] == 10, 'approved assessment durations')
        check(assessments[1]['evidence'] == ['Final model/leaderboard performance',
              'Technical report on methodology, experiments and findings'], 'both capstone evidence components')
        workload = data['assessment_workload']
        check(workload['status'] == 'proposed', 'assessment allocation remains proposed')
        allocations = workload['allocations']
        check(len({a['id'] for a in allocations}) == len(allocations), 'unique workload identifiers')
        for a in allocations:
            check(a['assessment_id'] in {'E', 'K', 'P'} and hours(a['hours']) and
                  bool(a['activity'].strip()), 'valid assessment allocation (no certification)')
        check({a['assessment_id'] for a in allocations} == {'E', 'K', 'P'}, 'all assessments allocated')
        check(sum(a['hours'] for a in allocations) == 40, 'assessment totals 40')
        check([a['hours'] for a in allocations if a['id'] == 'E_SIT' and a['assessment_id'] == 'E'] == [3],
              'M5 exam sitting counted once for three hours')
        check(workload['presentation_delivery'] == dict(session_id='S16', minutes_per_student=10,
              counted_in='contact', additional_assessment_hours=0), 'presentation delivery not double-counted')
        check(bool(data['decisions_pending']) and all(isinstance(x, str) and x.strip()
              for x in data['decisions_pending']), 'unresolved decisions recorded')
    except (KeyError, TypeError, ValueError, IndexError, AttributeError, OSError) as exc:
        errors.append('invalid or missing data/source: ' + str(exc))
    return errors


def main():
    try:
        data = json.loads((ROOT / 'curriculum/curriculum.json').read_text(encoding='utf-8'))
    except (OSError, ValueError) as exc:
        print('FAIL:', exc)
        return 1
    errors = validate(data)
    for error in errors:
        print('FAIL:', error)
    if errors:
        return 1
    if not (ROOT / 'docs/Machine Learning.pdf').exists():
        print('SKIP: private descriptor absent; using hash-pinned SETUP-02 transcription.')
    print('PASS: 16 sessions; 48 + 2 contact; 160 self-study; 40 assessment; 250 total.')
    print('PASS: source provenance, LO wording, mappings and assessment constraints.')
    print('Professor approval remains pending; structural validation is not academic approval.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
