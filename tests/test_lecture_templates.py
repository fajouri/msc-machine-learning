"""AUTO-02 contract regressions; no Office libraries, network or authored lessons."""
import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
HERE = ROOT / 'templates/lecture'
spec = importlib.util.spec_from_file_location('lecture_contract', HERE / 'validate.py')
v = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v)


class LectureContractTests(unittest.TestCase):
    def setUp(self):
        self.source = v.read(HERE / 'lecture.template.json')

    def test_bundle_and_all_slide_types(self):
        v.check_bundle()

    def test_every_required_field_and_extra_field_rejected(self):
        # Walk every object in both actual templates, including nested figures/notes.
        def mutations(value, schema):
            if schema['type'] == 'object':
                for key in schema['required']:
                    bad = copy.deepcopy(value)
                    del bad[key]
                    with self.subTest(missing=key), self.assertRaises(ValueError):
                        v.schema_check(bad, schema)
                bad = copy.deepcopy(value)
                bad['unexpected'] = 'injected'
                with self.assertRaises(ValueError):
                    v.schema_check(bad, schema)
                for key, item in value.items():
                    mutations(item, schema['properties'][key])
            elif schema['type'] == 'array':
                for item in value:
                    mutations(item, schema['items'])
        for name, value in [('lecture', self.source), ('design', v.read(HERE / 'design.json'))]:
            mutations(value, v.read(HERE / f'{name}.schema.json'))

    def test_invalid_types_constants_and_blank_strings(self):
        for field, value in [('issue', True), ('issue', 0), ('audience', 'instructor'),
                             ('approval', 'approved'), ('session_title', '  '),
                             ('session_id', 'S17'), ('slides', [])]:
            data = copy.deepcopy(self.source)
            data[field] = value
            with self.subTest(field=field), self.assertRaises(ValueError):
                v.validate_source(data)

    def test_unknown_schema_keyword_rejected(self):
        with self.assertRaisesRegex(ValueError, 'unsupported'):
            v.schema_check('text', {'type': 'string', 'not': {}})

    def test_duplicate_keys_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / 'bad.json'
            path.write_text('{"issue":8,"issue":9}', encoding='utf-8')
            with self.assertRaisesRegex(ValueError, 'duplicate JSON'):
                v.read(path)

    def test_all_canonical_sessions_accepted(self):
        for session in v.read(ROOT / 'curriculum/curriculum.json')['sessions']:
            data = copy.deepcopy(self.source)
            data.update(session_id=session['id'], session_title=session['title'],
                        mode=session['proposed_mode'], learning_outcomes=session['learning_outcomes'])
            for slide in data['slides']:
                slide['learning_outcomes'] = session['learning_outcomes']
            v.validate_source(data)

    def test_canonical_session_drift_rejected(self):
        for key, value in [('session_title', 'Changed'), ('mode', 'campus'),
                           ('learning_outcomes', ['LO2'])]:
            data = copy.deepcopy(self.source)
            data[key] = value
            with self.assertRaises(ValueError):
                v.validate_source(data)

    def test_slide_identity_and_outcome_drift(self):
        self.source['slides'][1]['id'] = self.source['slides'][0]['id']
        with self.assertRaisesRegex(ValueError, 'duplicate slide'):
            v.validate_source(self.source)
        self.source['slides'][1]['id'] = 'SL02'
        self.source['slides'][1]['learning_outcomes'] = ['LO8']
        with self.assertRaisesRegex(ValueError, 'outside session'):
            v.validate_source(self.source)

    def test_equation_and_figure_records_required(self):
        for kind, field in [('equation', 'equations'), ('figure', 'figures')]:
            data = copy.deepcopy(self.source)
            next(s for s in data['slides'] if s['type'] == kind)[field] = []
            with self.subTest(kind=kind), self.assertRaisesRegex(ValueError, 'requires'):
                v.validate_source(data)

    def test_third_party_figure_needs_citation(self):
        figure = next(s for s in self.source['slides'] if s['type'] == 'figure')['figures'][0]
        figure.update(origin='third_party', source_id='geron2022')
        with self.assertRaisesRegex(ValueError, 'requires citation'):
            v.validate_source(self.source)

    def test_unknown_citation_rejected(self):
        self.source['slides'][0]['citations'] = [{'source_id': 'invented',
            'artifact': 'example.md', 'locator': 'TODO', 'attribution': 'TODO'}]
        with self.assertRaisesRegex(ValueError, 'bibliography registry'):
            v.validate_source(self.source)

    def test_citation_fields_required(self):
        schema = v.read(HERE / 'lecture.schema.json')['properties']['slides']['items']['properties']['citations']['items']
        record = dict(source_id='geron2022', artifact='example.md', locator='whole work', attribution='Test fixture')
        v.schema_check(record, schema)
        for field in record:
            bad = record.copy()
            del bad[field]
            with self.assertRaises(ValueError):
                v.schema_check(bad, schema)

    def completed_fixture(self):
        # Synthetic structural fixture, never a claim of completed academic content.
        return json.loads(json.dumps(self.source).replace('TODO:', 'Synthetic fixture:'))

    def test_completion_is_separate_from_draft(self):
        v.validate_source(self.source)
        with self.assertRaisesRegex(ValueError, 'placeholders'):
            v.validate_source(self.source, complete=True)
        data = self.completed_fixture()
        v.validate_source(data, complete=True)
        self.assertEqual('pending_professor_review', data['approval'])

    def test_complete_citation_requires_matching_existing_ledger(self):
        data = self.completed_fixture()
        citation = dict(source_id='geron2022', artifact='example.md', locator='whole work', attribution='Synthetic fixture')
        data['slides'][0]['citations'] = [citation]
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            for name in ['curriculum/curriculum.json', 'references/bibliography.json']:
                (root / name).parent.mkdir(parents=True, exist_ok=True)
                (root / name).write_bytes((ROOT / name).read_bytes())
            ledger = root / 'references/citation-usage.json'
            for uses, success in [([], False), ([citation], True),
                                  ([dict(citation, locator='wrong locator')], False)]:
                ledger.write_text(json.dumps({'uses': uses}), encoding='utf-8')
                if success:
                    v.validate_source(data, root, complete=True)
                else:
                    with self.assertRaisesRegex(ValueError, 'existing ledger'):
                        v.validate_source(data, root, complete=True)

    def test_markdown_preserves_notes_equations_and_metadata(self):
        self.source['slides'][0]['notes']['reasoning'] = 'Unique public reasoning α'
        self.source['slides'][3]['equations'][0]['latex'] = r'\sum_{i=1}^{n} x_i'
        output = v.markdown(self.source)
        self.assertIn('Unique public reasoning α', output)
        self.assertIn(json.dumps(r'\sum_{i=1}^{n} x_i'), output)
        self.assertIn('"audience": "public_student"', output)
        self.assertEqual(output, v.markdown(self.source))

    def test_design_geometry_contrast_and_drift(self):
        design = v.read(HERE / 'design.json')
        self.assertAlmostEqual(float(design['width_inches']) / float(design['height_inches']), 16/9, places=6)
        def luminance(hexcode):
            rgb = [int(hexcode[i:i+2], 16)/255 for i in (1, 3, 5)]
            rgb = [x/12.92 if x <= .04045 else ((x+.055)/1.055)**2.4 for x in rgb]
            return sum(a*b for a, b in zip(rgb, (.2126, .7152, .0722)))
        for colour in ('foreground', 'accent'):
            self.assertGreaterEqual((luminance(design['background'])+.05)/(luminance(design[colour])+.05), 4.5)
        for key, value in [('aspect_ratio', '4:3'), ('body_pt', 12), ('figure_editable', False)]:
            bad = dict(design, **{key: value})
            with self.assertRaises(ValueError):
                v.schema_check(bad, v.read(HERE / 'design.schema.json'))

    def test_cli_success_failure_and_no_binary_claim(self):
        def run(*args):
            return subprocess.run([sys.executable, '-s', str(HERE / 'validate.py'), *args],
                                  capture_output=True, text=True)
        good = run()
        self.assertEqual(0, good.returncode, good.stderr)
        self.assertIn('visual QA deferred', good.stdout)
        self.assertEqual(1, run('--complete').returncode)
        self.assertEqual(1, run('--source', 'missing-lecture-source.json').returncode)
        with tempfile.TemporaryDirectory() as temp:
            bad = Path(temp) / 'malformed.json'
            bad.write_text('{bad', encoding='utf-8')
            self.assertEqual(1, run('--source', str(bad)).returncode)


if __name__ == '__main__':
    unittest.main()
