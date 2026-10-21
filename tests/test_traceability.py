"""Keep SETUP-02's original CRLF audit identity; tolerate only LF/CRLF transport."""
import hashlib
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
AUDIT_SHA256 = 'a60b0336de9801c95a9ed082ff082e52cfa9b8daaff07efba4f9c855440e4f10'
GIT_LF_SHA256 = '92b4f9665a376bcca52d08401d974e81e3e1b69c2910367c1a773964f0424b6d'


class TraceabilityBytesTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.cur = self.root / 'curriculum'
        self.cur.mkdir()
        for name in ['validate_traceability.py', 'traceability-matrix.md',
                     'traceability-gaps.md', 'traceability-validation.md']:
            shutil.copyfile(ROOT / 'curriculum' / name, self.cur / name)
        self.lf = (ROOT / 'curriculum/session-map.csv').read_bytes().replace(b'\r\n', b'\n')

    def run_validator(self, payload):
        (self.cur / 'session-map.csv').write_bytes(payload)
        return subprocess.run([sys.executable, '-s', str(self.cur / 'validate_traceability.py')],
                              cwd=self.root, capture_output=True, text=True)

    def rejected(self, payload):
        result = self.run_validator(payload)
        self.assertEqual(1, result.returncode, result.stdout + result.stderr)
        self.assertIn('FAIL: working session map unchanged from audit baseline', result.stderr)

    def test_historical_hashes_and_encoding(self):
        # Fixed identities established from scaffold and original SETUP-02 Git history.
        self.assertEqual(GIT_LF_SHA256, hashlib.sha256(self.lf).hexdigest())
        crlf = self.lf.replace(b'\n', b'\r\n')
        self.assertEqual(AUDIT_SHA256, hashlib.sha256(crlf).hexdigest())
        self.assertEqual((1527, 1544, 17), (len(self.lf), len(crlf), self.lf.count(b'\n')))
        self.assertTrue(self.lf.isascii())
        self.assertFalse(self.lf.startswith(b'\xef\xbb\xbf'))

    def test_lf_crlf_and_mixed_endings_pass_full_validator(self):
        for payload in [self.lf, self.lf.replace(b'\n', b'\r\n'),
                        self.lf.replace(b'\n', b'\r\n', 1)]:
            with self.subTest(crlf=payload.count(b'\r\n')):
                result = self.run_validator(payload)
                self.assertEqual(0, result.returncode, result.stdout + result.stderr)
                self.assertIn('9 online / 7 campus modes', result.stdout)
                self.assertIn(hashlib.sha256(payload).hexdigest(), result.stdout)

    def test_content_changes_fail_in_both_line_endings(self):
        changes = [(b'"online"', b'"campus"'), (b'"LO1"', b'"LO8"'),
                   (b'Regression I', b'Regression X'), (b'"01"', b'"17"'),
                   (b'Python stack', b'Python  stack')]
        for old, new in changes:
            for crlf in [False, True]:
                with self.subTest(change=new, crlf=crlf):
                    changed = self.lf.replace(old, new, 1)
                    self.rejected(changed.replace(b'\n', b'\r\n') if crlf else changed)

    def test_encoding_and_bom_changes_are_not_normalised(self):
        for payload in [b'\xef\xbb\xbf' + self.lf, self.lf.decode('ascii').encode('utf-16'),
                        self.lf.replace(b'Python stack', 'Python st\u00e4ck'.encode('utf-8')),
                        self.lf.replace(b'Python stack', b'Python st\xe4ck')]:
            with self.subTest(prefix=payload[:8]):
                self.rejected(payload)

    def test_bare_cr_and_whitespace_changes_are_not_normalised(self):
        for payload in [self.lf.replace(b'\n', b'\r'), self.lf.replace(b'\n', b'\r', 1),
                        self.lf.rstrip(b'\n'), self.lf + b'\n', self.lf + b' ',
                        self.lf.replace(b'\n', b' \n', 1)]:
            with self.subTest(length=len(payload)):
                self.rejected(payload)


if __name__ == '__main__':
    unittest.main()
