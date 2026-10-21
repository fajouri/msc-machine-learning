"""Reject curriculum drift and workload double-counting; no third-party packages."""
import copy
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('curriculum_validator', ROOT / 'curriculum/validate_curriculum.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class CurriculumTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads((ROOT / 'curriculum/curriculum.json').read_text(encoding='utf-8'))

    def test_baseline(self):
        self.assertEqual([], module.validate(self.data))

    def test_invalid_hours(self):
        for value in (-1, True, '10', None, float('nan'), float('inf')):
            for category in ('study', 'assessment'):
                with self.subTest(value=value, category=category):
                    data = copy.deepcopy(self.data)
                    row = (data['sessions'][0]['self_study'] if category == 'study'
                           else data['assessment_workload']['allocations'][0])
                    row['hours'] = value
                    self.assertTrue(module.validate(data))

    def test_totals_and_descriptor_drift(self):
        mutations = [
            lambda d: d['approved']['hours'].update(total=252),
            lambda d: d['sessions'][0]['self_study'].update(hours=9),
            lambda d: d['assessment_workload']['allocations'][0].update(hours=10),
            lambda d: d['approved']['learning_outcomes'][0].update(wording='Changed'),
            lambda d: d['approved']['assessments'][0].update(weight_percent=50),
            lambda d: d['approved']['assessments'][0].update(duration_minutes=120),
            lambda d: d['approved']['topic_blocks'][0].update(sessions=['S03', 'S04']),
            lambda d: d['sessions'][0].update(proposed_mode='campus'),
            lambda d: d['sessions'][0].update(learning_outcomes=['LO8']),
            lambda d: d['sessions'].pop(),
            lambda d: d['sessions'].append(copy.deepcopy(d['sessions'][0])),
            lambda d: d['sources'][0].update(sha256='0' * 64),
            lambda d: d.update(status='approved'),
            lambda d: d['assessment_workload'].update(status='approved'),
        ]
        for index, mutate in enumerate(mutations):
            with self.subTest(index=index):
                data = copy.deepcopy(self.data)
                mutate(data)
                self.assertTrue(module.validate(data))

    def test_certification_and_presentation_cannot_be_recounted(self):
        self.data['assessment_workload']['allocations'][0]['assessment_id'] = 'CERT'
        self.assertTrue(module.validate(self.data))
        self.setUp()
        self.data['contact_reconciliation']['additional_activity']['lecturer_deliverable'] = True
        self.assertTrue(module.validate(self.data))
        self.setUp()
        self.data['assessment_workload']['presentation_delivery']['additional_assessment_hours'] = 1 / 6
        self.assertTrue(module.validate(self.data))

    def test_duplicate_allocation(self):
        self.data['assessment_workload']['allocations'][1]['id'] = 'E_PREP'
        self.assertTrue(module.validate(self.data))

    def test_missing_or_malformed_data(self):
        for data in ({}, [], None, {'schema_version': 1}):
            with self.subTest(data=data):
                self.assertTrue(module.validate(data))

    def test_public_checkout_without_pdf_and_source_drift(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for source in self.data['sources']:
                if source['path'].endswith('.pdf'):
                    continue
                target = root / source['path']
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes((ROOT / source['path']).read_bytes().replace(b'\r\n', b'\n'))
            self.assertEqual([], module.validate(self.data, root))
            with (root / 'docs/PRODUCTION_PLAN.md').open('a', encoding='utf-8') as f:
                f.write('\nChanged decision\n')
            self.assertIn('source drift: docs/PRODUCTION_PLAN.md', module.validate(self.data, root))


if __name__ == '__main__':
    unittest.main()
