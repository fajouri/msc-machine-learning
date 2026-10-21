"""Regression checks for delivery coverage and feasible scheduled time."""
import importlib.util
from pathlib import Path
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('delivery', ROOT / 'curriculum/validate_delivery.py')
delivery = importlib.util.module_from_spec(spec)
spec.loader.exec_module(delivery)


class DeliveryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = (ROOT / 'docs/delivery-plan.md').read_text(encoding='utf-8')

    def test_baseline_and_cli(self):
        self.assertEqual([], delivery.validate(self.text))
        result = subprocess.run([sys.executable, '-s', str(ROOT / 'curriculum/validate_delivery.py')],
                                capture_output=True, text=True)
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)

    def test_missing_duplicate_reordered_or_changed_mode(self):
        row = next(line for line in self.text.splitlines() if line.startswith('| S03 |'))
        other = next(line for line in self.text.splitlines() if line.startswith('| S04 |'))
        for changed in (self.text.replace(row, ''), self.text.replace(row, row + '\n' + row),
                        self.text.replace(row, 'ROW').replace(other, row).replace('ROW', other),
                        self.text.replace('| S03 | online |', '| S03 | campus |')):
            with self.subTest(changed=changed != self.text):
                self.assertIn('session order, coverage or mode differs from working map',
                              delivery.validate(changed))

    def test_missing_each_planning_dimension(self):
        row = next(line for line in self.text.splitlines() if line.startswith('| S08 |'))
        cells = row.split('|')
        for index in range(3, 8):
            changed = cells.copy()
            changed[index] = ' '
            with self.subTest(column=index):
                self.assertIn('incomplete planning row: S08',
                              delivery.validate(self.text.replace(row, '|'.join(changed))))

    def test_timing_and_capacity_failures(self):
        replacements = [
            ('| 10 | 40 |', '| 11 | 40 |'),  # gap
            ('| 40 | 65 |', '| 39 | 65 |'),  # overlap
            ('| 40 | 65 |', '| 40 | 40 |'),  # zero duration
            ('| 165 | 180 |', '| 165 | 181 |'),
            ('Five slots:', 'Four slots:'),
            ('10-minute presentation +', '9-minute presentation +'),
            ('2-minute Q&A +', '3-minute Q&A +'),
            ('| 10 | 75 |', '| 10 | 74 |'),
        ]
        for old, new in replacements:
            with self.subTest(replacement=new):
                self.assertTrue(delivery.validate(self.text.replace(old, new)))

    def test_missing_structure_status_and_links(self):
        for old, new in [('**Draft pending professor review.**', 'Approved.'),
                         ('### Online (', '### Removed ('),
                         ('../curriculum/curriculum.json', '../curriculum/missing.json')]:
            with self.subTest(old=old):
                self.assertTrue(delivery.validate(self.text.replace(old, new)))
        self.assertTrue(delivery.validate(''))


if __name__ == '__main__':
    unittest.main()
