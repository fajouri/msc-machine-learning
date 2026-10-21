"""Regression tests for unknown citations and unsafe publication claims."""
import copy
import importlib.util
import json
import subprocess
import sys
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('bibliography_validator', ROOT / 'references/validate_bibliography.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class BibliographyTests(unittest.TestCase):
    def setUp(self):
        self.bib = json.loads((ROOT / 'references/bibliography.json').read_text(encoding='utf-8'))
        self.ledger = {'issue': 5, 'uses': []}

    def errors(self, release=False):
        return module.validate(self.bib, self.ledger, release=release)

    def use(self, **changes):
        row = dict(source_id='geron2022', artifact='references/README.md',
                   locator='whole work', kind='link', attribution='Géron (2022)',
                   rights_status='link_only', permission_evidence='', review_note='Test fixture only')
        row.update(changes)
        self.ledger['uses'] = [row]

    def test_audit_accepts_explicit_unknowns(self):
        self.assertEqual([], self.errors())

    def test_release_blocks_unverified_ng(self):
        self.assertTrue(any('ng2017' in e for e in self.errors(release=True)))

    def test_duplicate_or_missing_source_rejected(self):
        self.bib['sources'][-1] = copy.deepcopy(self.bib['sources'][0])
        self.assertTrue(self.errors())

    def test_unexplained_unknown_rejected(self):
        self.bib['sources'][-1]['todos'] = []
        self.assertTrue(self.errors())

    def test_false_verified_metadata_rejected(self):
        self.bib['sources'][-1]['metadata_status'] = 'verified'
        self.assertTrue(self.errors())

    def test_unknown_citation_rejected(self):
        self.use(source_id='invented')
        self.assertTrue(self.errors())

    def test_link_allowed(self):
        self.use()
        self.assertEqual([], self.errors())

    def test_link_status_cannot_clear_figure(self):
        self.use(kind='figure')
        self.assertTrue(self.errors())

    def test_clearance_requires_evidence(self):
        self.cleared_use()
        del self.ledger['uses'][0]['permission_evidence']
        self.assertEqual(['use 0: clearance needs evidence URL'], self.errors())

    def test_release_cli_fails_only_for_documented_ng_metadata(self):
        result = subprocess.run(
            [sys.executable, '-s', str(ROOT / 'references/validate_bibliography.py'), '--release'],
            cwd=ROOT, capture_output=True, text=True, check=False)
        self.assertEqual(1, result.returncode)
        self.assertEqual('FAIL: ng2017: unresolved metadata/TODO prevents release', result.stdout.strip())
        self.assertEqual('', result.stderr)

    def cleared_use(self, **changes):
        # Synthetic approval fixture: does not grant rights to any real material.
        clearance = dict(permission_source='Fixture rights holder',
                         permitted_use='Fixture figure in a public teaching artifact',
                         conditions='Retain fixture attribution; no other uses permitted',
                         reviewer='Fixture academic reviewer', review_date='2026-10-21',
                         approval_status='approved')
        clearance.update(changes)
        self.use(kind='figure', rights_status='cleared',
                 permission_evidence='https://example.org/fixture-permission', clearance=clearance)

    def test_structured_clearance_accepted(self):
        self.cleared_use()
        self.assertEqual([], self.errors())
        self.assertFalse(any('use 0:' in e for e in self.errors(release=True)))

    def test_url_alone_does_not_clear_use(self):
        self.use(kind='figure', rights_status='cleared', permission_evidence='https://example.org/permission')
        self.assertTrue(any('structured approval' in e for e in self.errors()))

    def test_clearance_fields_required(self):
        for field in ('permission_source', 'permitted_use', 'conditions', 'reviewer', 'review_date', 'approval_status'):
            with self.subTest(field=field):
                self.cleared_use()
                del self.ledger['uses'][0]['clearance'][field]
                self.assertTrue(any(field in e for e in self.errors()))

    def test_clearance_text_must_be_nonblank_string(self):
        for field in ('permission_source', 'permitted_use', 'conditions', 'reviewer'):
            for value in ('', '   ', None, 42, ['reviewer']):
                with self.subTest(field=field, value=value):
                    self.cleared_use(**{field: value})
                    self.assertTrue(any(field in e for e in self.errors()))

    def test_clearance_date_format_and_calendar(self):
        for value in ('20261021', '2026-02-30', '2026-1-1', '2026-10-21T12:00:00', None, 20261021):
            with self.subTest(value=value):
                self.cleared_use(review_date=value)
                self.assertTrue(any('review_date' in e for e in self.errors()))

    def test_clearance_requires_explicit_approval(self):
        for value in ('pending', 'rejected', 'Approved', '', True, None):
            with self.subTest(value=value):
                self.cleared_use(approval_status=value)
                self.assertTrue(any('approval_status' in e for e in self.errors()))

    def test_clearance_record_must_be_object(self):
        for value in (None, [], 'approved', True):
            with self.subTest(value=value):
                self.cleared_use()
                self.ledger['uses'][0]['clearance'] = value
                self.assertTrue(any('structured approval' in e for e in self.errors()))

    def test_pending_reuse_not_releasable(self):
        self.use(kind='quotation', rights_status='TODO')
        self.assertEqual([], self.errors())
        self.assertTrue(any('pending rights' in e for e in self.errors(release=True)))

    def test_path_escape_rejected(self):
        self.use(artifact='../outside.md')
        self.assertTrue(self.errors())

    def test_private_reference_rejected(self):
        self.use(artifact='instructor-private/solutions.md')
        self.assertTrue(any('private artifact' in e for e in self.errors()))

    def test_missing_locator_rejected(self):
        self.use(locator='')
        self.assertTrue(self.errors())

    def test_invalid_provenance_url_rejected(self):
        self.bib['sources'][0]['metadata_url'] = 'not a URL'
        self.assertTrue(self.errors())


if __name__ == '__main__':
    unittest.main()
