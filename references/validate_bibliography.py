"""Offline SETUP-05 provenance and citation-release checks (standard library)."""
import argparse
import json
from datetime import date
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {'geron2022', 'goodfellow2016', 'hastie2009', 'provost2013', 'ng2017'}


def web_url(value):
    return isinstance(value, str) and urlparse(value).scheme in {'http', 'https'} and bool(urlparse(value).netloc)


def validate(bibliography, ledger, root=ROOT, release=False):
    errors = []
    def require(condition, message):
        if not condition:
            errors.append(message)

    require(bibliography.get('issue') == 5 and ledger.get('issue') == 5, 'Issue must be 5')
    try:
        date.fromisoformat(bibliography.get('checked_on', ''))
    except (ValueError, TypeError):
        errors.append('Invalid audit date')
    sources = bibliography.get('sources', [])
    ids = [s.get('id') for s in sources]
    require(len(ids) == len(set(ids)) and set(ids) == EXPECTED, 'Exactly five unique descriptor sources required')
    by_id = {s.get('id'): s for s in sources}
    for source in sources:
        key = source.get('id')
        for field in ('descriptor_citation', 'title', 'authors', 'metadata_evidence', 'access', 'rights_evidence'):
            require(bool(source.get(field)), f'{key}: missing {field}')
        require(source.get('descriptor_role') == ('Supplementary' if key in {'ng2017', 'provost2013'} else 'Core'), f'{key}: descriptor role changed')
        for field in ('metadata_url', 'rights_url'):
            require(web_url(source.get(field)), f'{key}: invalid {field}')
        require(source.get('reuse_status') == 'link_only', f'{key}: book-wide clearance not established')
        status = source.get('metadata_status')
        require(status in {'verified', 'TODO'}, f'{key}: invalid metadata status')
        if status == 'verified':
            require(type(source.get('year')) is int and bool(source.get('publisher')), f'{key}: verified metadata incomplete')
        else:
            require(bool(source.get('todos')), f'{key}: unresolved metadata requires TODO explanation')
        if release:
            require(status == 'verified' and not source.get('todos'), f'{key}: unresolved metadata/TODO prevents release')
    for index, use in enumerate(ledger.get('uses', [])):
        label = f'use {index}'
        require(use.get('source_id') in by_id, f'{label}: unknown source')
        for field in ('artifact', 'locator', 'attribution', 'review_note'):
            require(bool(use.get(field)), f'{label}: missing {field}')
        raw = use.get('artifact', '')
        path = (root / raw).resolve()
        require(not Path(raw).is_absolute() and path.is_relative_to(root.resolve()) and path.is_file(), f'{label}: artifact must exist inside repository')
        require(not any(part.lower() in {'private', 'instructor-private', 'exam-keys', 'student-data', 'secrets'} for part in Path(raw).parts), f'{label}: private artifact prohibited')
        kind = use.get('kind')
        status = use.get('rights_status')
        require(kind in {'link', 'paraphrase', 'quotation', 'figure', 'code'}, f'{label}: invalid kind')
        require(status in {'link_only', 'TODO', 'cleared'}, f'{label}: invalid rights status')
        require(status != 'link_only' or kind == 'link', f'{label}: link-only cannot clear reused content')
        if status == 'cleared':
            require(web_url(use.get('permission_evidence')), f'{label}: clearance needs evidence URL')
        if release:
            require(status in {'cleared', 'link_only'}, f'{label}: pending rights prevent release')
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--release', action='store_true')
    args = parser.parse_args()
    folder = Path(__file__).resolve().parent
    bibliography = json.loads((folder / 'bibliography.json').read_text(encoding='utf-8'))
    ledger = json.loads((folder / 'citation-usage.json').read_text(encoding='utf-8'))
    errors = validate(bibliography, ledger, release=args.release)
    for error in errors:
        print('FAIL:', error)
    if errors:
        return 1
    print('PASS: five source records, provenance, roles and citation usage validated offline.')
    print('Audit mode permits documented TODOs; no legal clearance or professor approval is inferred.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
