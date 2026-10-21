"""AUTO-03 regression checks: reproducibility, public stubs and AUTO-01 integration."""
import copy
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('notebook_templates', ROOT / 'templates/notebook/validate.py')
v = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v)


class NotebookTemplateTests(unittest.TestCase):
    def setUp(self):
        self.value = v.read(v.TEMPLATES[0])

    def cell(self, name):
        return next(c for c in self.value['cells'] if c['id'] == name)

    def test_all_templates_execute_repeatably_without_answers(self):
        for path in v.TEMPLATES:
            with self.subTest(path=path.name):
                value = v.read(path)
                before = copy.deepcopy(value)
                output = v.repeat(value, v.execute_python)
                self.assertIn('NOT ATTEMPTED', output)
                self.assertNotIn('FORMAT CHECK PASSED', output)
                self.assertEqual(before, value)

    def test_data_and_split_contract(self):
        output = v.execute_python(self.value)
        records = output.splitlines()
        data = json.loads(records[1])
        self.assertEqual('m5-synthetic-v1', data['data_version'])
        self.assertEqual(18, len(data['train_ids']))
        self.assertEqual(6, len(data['validation_ids']))
        self.assertFalse(set(data['train_ids']) & set(data['validation_ids']))
        self.assertEqual(list(range(24)), sorted(data['train_ids'] + data['validation_ids']))
        # Independently reconstruct the canonical synthetic data identity.
        import hashlib
        rows = []
        for i in range(24):
            x = i - 12
            rows.append(dict(row_id=i, x=x, y=3*x + 2 + ((7*i) % 5 - 2)))
        payload = json.dumps(rows, sort_keys=True, separators=(',', ':')).encode()
        self.assertEqual(hashlib.sha256(payload).hexdigest(), data['sha256'])

    def test_stored_output_count_and_metadata_rejected(self):
        for field, value in [('outputs', [{'output_type': 'stream', 'name': 'stdout', 'text': 'private'}]),
                             ('execution_count', 1), ('metadata', {'collapsed': True})]:
            self.setUp()
            self.cell('environment')[field] = value
            with self.subTest(field=field), self.assertRaises(ValueError):
                v.validate(self.value)
        self.setUp()
        self.value['metadata']['colab'] = {'private': 'incidental metadata'}
        with self.assertRaises(ValueError):
            v.validate(self.value)

    def test_missing_sections_duplicate_ids_and_attachments_rejected(self):
        mutations = [lambda d: d['cells'].pop(1),
                     lambda d: d['cells'][1].update(id=d['cells'][0]['id']),
                     lambda d: d['cells'][0].update(attachments={'hidden': {}})]
        for mutate in mutations:
            value = copy.deepcopy(self.value)
            mutate(value)
            with self.assertRaises(ValueError):
                v.validate(value)

    def test_completed_student_code_is_not_public_template(self):
        for source in ['experiment_results = [{"seed": 42, "mse": 1.0}]',
                       'def answer():\n    return 1', 'pass']:
            self.cell('student-experiment')['source'] = [source]
            with self.assertRaisesRegex(ValueError, 'None stubs'):
                v.validate(self.value)

    def test_syntax_and_local_dependencies_fail(self):
        for source, error in [('if broken', SyntaxError),
                              ('path = "C:/Users/example/data.csv"', ValueError),
                              ('secret = userdata.get("TOKEN")', ValueError)]:
            self.cell('environment')['source'] = [source]
            with self.assertRaises(error):
                v.validate(self.value)

    def test_execution_errors_fail(self):
        self.cell('baseline')['source'] = ['raise RuntimeError("broken demonstration")']
        with self.assertRaisesRegex(ValueError, 'student path failed'):
            v.execute_python(self.value)

    def test_determinism_comparison_detects_drift(self):
        results = iter(['first', 'second'])
        with self.assertRaisesRegex(ValueError, 'non-deterministic'):
            v.repeat(self.value, lambda value: next(results))

    def test_readiness_exempts_only_explicit_student_markers(self):
        self.value['cells'] = [self.cell('student-experiment')]
        text = v.builder.notebook_authoring_text(self.value)
        self.assertNotIn('TODO', text)
        self.value['cells'][0]['source'] += ['\n# TODO: unfinished author work\n# FIXME: author work\n# {{unresolved}}']
        text = v.builder.notebook_authoring_text(self.value)
        for marker in ['TODO', 'FIXME', '{{']:
            self.assertIn(marker, text)
        self.value['cells'][0]['id'] = 'ordinary-cell'
        self.assertIn('STUDENT TODO:', v.builder.notebook_authoring_text(self.value))

    def test_exact_curriculum_injection_for_every_session(self):
        data = v.builder.read_json(ROOT / 'curriculum/curriculum.json')
        for session in data['sessions']:
            values = dict(session=session['id'], title=session['title'], issue='9',
                          mode=session['proposed_mode'], block=session['block_id'],
                          outcomes='\n'.join('- ' + lo['id'] + ': ' + lo['wording']
                                             for lo in data['approved']['learning_outcomes']
                                             if lo['id'] in session['learning_outcomes']))
            notebook = copy.deepcopy(self.value)
            for cell in notebook['cells']:
                cell['source'] = [v.builder.expand(line, values) for line in cell['source']]
            v.validate(notebook)
            text = v.builder.notebook_authoring_text(notebook)
            self.assertNotIn('{{', text)
            self.assertIn(session['title'], text)
            self.assertIn(values['outcomes'], text)

    def test_student_format_feedback_rejects_invalid_attempts(self):
        # Test the public format checker with generic fixtures, not exercise solutions.
        checker = ''.join(self.cell('exercise-checks')['source'])
        for invalid in [[], [{'seed': True, 'mse': 1}], [{'seed': 1, 'mse': float('nan')}],
                        [{'seed': 1, 'mse': -1}], [{'seed': 1}], 'not a list']:
            with self.subTest(value=invalid), self.assertRaises(AssertionError):
                exec(checker, {'experiment_results': invalid})

    def test_duplicate_json_keys_rejected(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / 'duplicate.json'
            path.write_text('{"cells": [], "cells": []}', encoding='utf-8')
            with self.assertRaisesRegex(ValueError, 'duplicate JSON key'):
                v.read(path)


if __name__ == '__main__':
    unittest.main()
