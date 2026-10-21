"""Exercise package lifecycle and fail-fast boundaries in disposable repositories."""
import copy
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = Path('skills/msc-course-builder/scripts/session_package.py')
spec = importlib.util.spec_from_file_location('course_builder', ROOT / SCRIPT)
builder = importlib.util.module_from_spec(spec)
spec.loader.exec_module(builder)


class CourseBuilderTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve() / 'repo'
        self.root.mkdir()
        for name in ('curriculum', 'docs', 'references', 'skills'):
            shutil.copytree(ROOT / name, self.root / name,
                            ignore=shutil.ignore_patterns('*.pdf', '__pycache__'))
        shutil.copy2(ROOT / 'AGENTS.md', self.root / 'AGENTS.md')

    def init(self, selected='S01', package='source'):
        return builder.initialise(self.root, selected, 13, package)

    def cli(self, *args):
        return subprocess.run([sys.executable, '-s', str(self.root / SCRIPT), *args],
                              capture_output=True, text=True, cwd=self.root)

    def test_all_sessions_plan_without_writes(self):
        curriculum = builder.read_json(self.root / 'curriculum/curriculum.json')
        for session in curriculum['sessions']:
            with self.subTest(session=session['id']):
                plan = builder.plan(self.root, session['id'], 13)
                self.assertEqual(session, plan['session'])
                self.assertEqual('pending_professor_review', plan['approval'])
                self.assertEqual(set(builder.SOURCE_FILES), {r['path'] for r in plan['outputs']})
        self.assertFalse((self.root / 'sessions').exists())

    def test_invalid_selection_issue_and_scope_do_not_write(self):
        for selected in ('S00', 'S17', '01', '../S01', 'S01/../S02', 's01', ''):
            with self.subTest(selected=selected), self.assertRaises(ValueError):
                self.init(selected)
        for issue in (True, 0, -1, '7'):
            with self.subTest(issue=issue), self.assertRaises(ValueError):
                builder.initialise(self.root, 'S01', issue)
        with self.assertRaises(ValueError):
            self.init(package='instructor')
        self.assertFalse((self.root / 'sessions').exists())

    def test_online_and_campus_drafts_preserve_inputs(self):
        for selected in ('S01', 'S02'):
            folder = self.init(selected)
            builder.check(self.root, selected)
            plan = builder.read_json(folder / 'manifest.json')
            brief = (folder / 'brief.md').read_text(encoding='utf-8')
            self.assertIn(plan['session']['proposed_mode'], brief)
            self.assertNotIn('{{', brief)
            self.assertTrue(all(r['sha256'] for r in plan['outputs']))
            with self.assertRaisesRegex(ValueError, 'drafting marker'):
                builder.check(self.root, selected, ready=True)

    def test_existing_destination_never_overwritten(self):
        folder = self.init()
        path = folder / 'lecture.md'
        path.write_text('Existing authored material', encoding='utf-8')
        with self.assertRaisesRegex(ValueError, 'destination exists'):
            self.init()
        self.assertEqual('Existing authored material', path.read_text(encoding='utf-8'))

    def test_missing_prerequisite_fails_before_writing(self):
        (self.root / 'docs/course-builder-boundary.md').unlink()
        with self.assertRaises(OSError):
            self.init()
        self.assertFalse((self.root / 'sessions').exists())

    def test_changed_approved_source_fails_before_writing(self):
        source = self.root / 'curriculum/session-map.csv'
        source.write_text(source.read_text(encoding='utf-8').replace('online', 'campus', 1),
                          encoding='utf-8')
        with self.assertRaisesRegex(ValueError, 'prerequisite'):
            self.init()
        self.assertFalse((self.root / 'sessions').exists())

    def test_missing_template_does_not_leave_partial_package(self):
        (self.root / builder.SKILL / 'assets/exercises.md').unlink()
        with self.assertRaises(OSError):
            self.init()
        self.assertFalse((self.root / 'sessions').exists())

    def test_hash_drift_and_explicit_snapshot(self):
        folder = self.init()
        (folder / 'lecture.md').write_text('Original synthetic teaching example.', encoding='utf-8')
        with self.assertRaisesRegex(ValueError, 'hash drift'):
            builder.check(self.root, 'S01')
        builder.snapshot(self.root, 'S01')
        builder.check(self.root, 'S01')

    def test_snapshot_cannot_reset_source_drift(self):
        self.init()
        path = self.root / 'docs/course-builder-boundary.md'
        path.write_text(path.read_text(encoding='utf-8') + '\nChanged decision.\n', encoding='utf-8')
        with self.assertRaisesRegex(ValueError, 'manifest/source drift'):
            builder.snapshot(self.root, 'S01')

    def test_manifest_tampering_rejected(self):
        folder = self.init()
        original = builder.read_json(folder / 'manifest.json')
        variants = []
        for field, value in [('approval', 'approved'), ('audience', 'instructor'),
                             ('issue', False), ('schema_version', 2),
                             ('schema_version', True), ('outputs', [])]:
            changed = copy.deepcopy(original)
            changed[field] = value
            variants.append(changed)
        changed = copy.deepcopy(original)
        changed['session']['learning_outcomes'] = ['LO8']
        variants.append(changed)
        changed = copy.deepcopy(original)
        changed['outputs'][0]['path'] = '../../AGENTS.md'
        variants.append(changed)
        changed = copy.deepcopy(original)
        changed['outputs'].append(changed['outputs'][0])
        variants.append(changed)
        changed = copy.deepcopy(original)
        changed['extra'] = 'unrecognised'
        variants.append(changed)
        for index, changed in enumerate(variants):
            with self.subTest(index=index):
                builder.write_json(folder / 'manifest.json', changed)
                with self.assertRaises(ValueError):
                    builder.snapshot(self.root, 'S01')

    def test_unlisted_files_and_directories_rejected(self):
        folder = self.init()
        for name in ('answer-key.md', 'notes.txt', 'slides.pptx'):
            path = folder / name
            path.write_text('Synthetic fixture only.', encoding='utf-8')
            with self.subTest(name=name), self.assertRaises(ValueError):
                builder.snapshot(self.root, 'S01')
            path.unlink()
        (folder / 'extra').mkdir()
        with self.assertRaises(ValueError):
            builder.check(self.root, 'S01')

    def test_missing_and_empty_source_rejected(self):
        folder = self.init()
        (folder / 'lecture.md').unlink()
        with self.assertRaisesRegex(ValueError, 'missing source'):
            builder.snapshot(self.root, 'S01')
        (folder / 'lecture.md').touch()
        with self.assertRaisesRegex(ValueError, 'empty artifact'):
            builder.snapshot(self.root, 'S01')

    def test_notebook_output_and_metadata_rejected(self):
        folder = self.init()
        path = folder / 'student-lab.ipynb'
        original = builder.read_json(path)
        variants = []
        for field, value in [('outputs', [{'output_type': 'stream', 'text': ['fixture']}]),
                             ('execution_count', 1), ('metadata', {'hidden': 'fixture'})]:
            changed = copy.deepcopy(original)
            changed['cells'][2][field] = value
            variants.append(changed)
        changed = copy.deepcopy(original)
        changed['metadata']['student'] = 'synthetic fixture'
        variants.append(changed)
        changed = copy.deepcopy(original)
        changed['cells'][1]['id'] = changed['cells'][0]['id']
        variants.append(changed)
        for changed in variants:
            builder.write_json(path, changed)
            with self.assertRaises(ValueError):
                builder.snapshot(self.root, 'S01')

    def test_notebook_scaffold_executes_without_solutions(self):
        folder = self.init()
        notebook = builder.read_json(folder / 'student-lab.ipynb')
        source = '\n'.join(''.join(c['source']) for c in notebook['cells'] if c['cell_type'] == 'code')
        result = subprocess.run([sys.executable, '-I', '-c', source], capture_output=True, text=True)
        self.assertEqual(0, result.returncode, result.stderr)
        self.assertEqual('', result.stdout)

    def remove_drafting_markers(self, folder):
        # Synthetic structural candidates only, never academic approval fixtures.
        for name in builder.SOURCE_FILES:
            path = folder / name
            path.write_text(path.read_text(encoding='utf-8').replace('TODO', 'Review'), encoding='utf-8')

    def test_review_candidate_does_not_promote_approval(self):
        folder = self.init()
        self.remove_drafting_markers(folder)
        builder.snapshot(self.root, 'S01')
        builder.check(self.root, 'S01', ready=True)
        self.assertEqual('pending_professor_review', builder.read_json(folder / 'manifest.json')['approval'])

    def test_full_package_requires_real_office_containers(self):
        folder = self.init(package='full')
        self.remove_drafting_markers(folder)
        builder.snapshot(self.root, 'S01')
        builder.check(self.root, 'S01')
        with self.assertRaisesRegex(ValueError, 'missing output'):
            builder.check(self.root, 'S01', ready=True)
        for name in builder.BINARY_FILES:
            (folder / name).write_text('Not an Office file.', encoding='utf-8')
        builder.snapshot(self.root, 'S01')
        with self.assertRaises(zipfile.BadZipFile):
            builder.check(self.root, 'S01', ready=True)

    def test_redirected_session_directory_rejected(self):
        outside = Path(self.temp.name) / 'outside'
        outside.mkdir()
        sessions = self.root / 'sessions'
        try:
            sessions.symlink_to(outside, target_is_directory=True)
        except OSError:
            if sys.platform != 'win32':
                self.skipTest('directory symlinks unavailable')
            result = subprocess.run(['cmd', '/c', 'mklink', '/J', str(sessions), str(outside)],
                                    capture_output=True, text=True)
            self.assertEqual(0, result.returncode, result.stderr)
        try:
            with self.assertRaisesRegex(ValueError, 'redirected'):
                self.init()
            self.assertEqual([], list(outside.iterdir()))
        finally:
            if sessions.is_symlink():
                sessions.unlink()
            else:
                sessions.rmdir()  # Removes the junction itself, never its target.

    def test_cli_lifecycle_and_failures(self):
        for args in [('plan', '--session', 'S02', '--issue', '15'),
                     ('init', '--session', 'S02', '--issue', '15'),
                     ('snapshot', '--session', 'S02'), ('check', '--session', 'S02')]:
            result = self.cli(*args)
            self.assertEqual(0, result.returncode, result.stderr)
        for args in [('init', '--session', 'S02', '--issue', '15'),
                     ('check', '--session', 'S02', '--review-ready'),
                     ('plan', '--session', '../S01', '--issue', '15')]:
            result = self.cli(*args)
            self.assertEqual(1, result.returncode, result.stderr)
            self.assertNotIn('Traceback', result.stderr)
        result = self.cli('plan', '--session', 'S01')
        self.assertEqual(2, result.returncode)

    def test_malformed_manifest_fails_cleanly(self):
        folder = self.init()
        (folder / 'manifest.json').write_text('{broken', encoding='utf-8')
        result = self.cli('check', '--session', 'S01')
        self.assertEqual(1, result.returncode)
        self.assertNotIn('Traceback', result.stderr)


if __name__ == '__main__':
    unittest.main()
