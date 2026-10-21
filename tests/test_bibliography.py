"""Regression tests for unknown citations and unsafe publication claims."""
import copy
import importlib.util
import json
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
        self.use(kind='code', rights_status='cleared')
        self.assertTrue(self.errors())

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
