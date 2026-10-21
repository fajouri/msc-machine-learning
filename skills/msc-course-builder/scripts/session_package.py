"""Offline M5 student package preparation and integrity checks; no publication."""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[3]
SKILL = Path('skills/msc-course-builder')
SOURCES = (
    'AGENTS.md', 'docs/PRODUCTION_PLAN.md', 'curriculum/session-map.csv',
    'curriculum/curriculum.json', 'curriculum/traceability-matrix.md',
    'curriculum/traceability-gaps.md', 'docs/delivery-plan.md',
    'docs/course-builder-boundary.md', 'references/bibliography.json',
    'references/README.md',
)
TEXT_FILES = ('brief.md', 'lecture.md', 'exercises.md', 'references.md', 'completion.md')
SOURCE_FILES = (*TEXT_FILES, 'student-lab.ipynb')
BINARY_FILES = ('lecture.docx', 'slides.pptx')
NOTEBOOK_METADATA = {
    'kernelspec': {'display_name': 'Python 3', 'language': 'python', 'name': 'python3'},
    'language_info': {'name': 'python'},
}


def read_json(path):
    return json.loads(path.read_text(encoding='utf-8'))


def digest(path, text=False):
    content = path.read_text(encoding='utf-8').encode('utf-8') if text else path.read_bytes()
    return hashlib.sha256(content).hexdigest()


def module(root, relative, name):
    spec = importlib.util.spec_from_file_location(name, root / relative)
    loaded = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(loaded)
    return loaded


def preflight(root):
    """Reuse authoritative checks; never rewrite their approved baseline."""
    sources = {name: digest(root / name, text=True) for name in SOURCES}
    data = read_json(root / 'curriculum/curriculum.json')
    errors = module(root, 'curriculum/validate_curriculum.py', 'm5_curriculum').validate(data, root)
    errors += module(root, 'curriculum/validate_delivery.py', 'm5_delivery').validate(
        (root / 'docs/delivery-plan.md').read_text(encoding='utf-8'), root)
    errors += module(root, 'references/validate_bibliography.py', 'm5_bibliography').validate(
        read_json(root / 'references/bibliography.json'),
        read_json(root / 'references/citation-usage.json'), root)
    if errors:
        raise ValueError('prerequisite checks failed: ' + '; '.join(errors))
    return data, sources


def session_id(value):
    if not isinstance(value, str) or not re.fullmatch(r'S(?:0[1-9]|1[0-6])', value):
        raise ValueError('session must be exactly S01 through S16')
    return value


def destination(root, selected):
    """Only fixed paths; reject symlinks/junctions even when pointing inside root."""
    session_id(selected)
    root = root.resolve()
    target = root / 'sessions' / selected
    for path in (root / 'sessions', target):
        if path.is_symlink() or (hasattr(path, 'is_junction') and path.is_junction()):
            raise ValueError('redirected package directory is forbidden')
        if path.resolve() != path:
            raise ValueError('package path escapes its fixed destination')
    return target


def plan(root, selected, issue, package='source'):
    session_id(selected)
    if type(issue) is not int or issue <= 0:
        raise ValueError('issue must be a positive integer')
    if package not in ('source', 'full'):
        raise ValueError('package must be source or full')
    destination(root, selected)
    data, sources = preflight(root)
    session = next(s for s in data['sessions'] if s['id'] == selected)
    filenames = SOURCE_FILES + (BINARY_FILES if package == 'full' else ())
    return {
        'schema_version': 1, 'issue': issue, 'session': session, 'package': package,
        'audience': 'public_student', 'approval': 'pending_professor_review',
        'sources': sources,
        'outputs': [{'path': name, 'sha256': None} for name in filenames],
    }


def write_json(path, value):
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')


def initialise(root, selected, issue, package='source'):
    manifest = plan(root, selected, issue, package)
    target = destination(root, selected)
    if target.exists():
        raise ValueError('destination exists; review/edit it in place, never overwrite')
    session = manifest['session']
    data = read_json(root / 'curriculum/curriculum.json')
    outcomes = '\n'.join('- ' + lo['id'] + ': ' + lo['wording']
                         for lo in data['approved']['learning_outcomes']
                         if lo['id'] in session['learning_outcomes'])
    substitutions = {
        'session': selected, 'title': session['title'], 'issue': str(issue),
        'mode': session['proposed_mode'], 'topics': session['indicative_topics'],
        'outcomes': outcomes, 'block': session['block_id'],
        'self_study': str(session['self_study']['hours']),
    }
    # Load/expand everything before creating the destination, so missing templates
    # cannot leave a misleading partially initialised package.
    rendered = {}
    for name in SOURCE_FILES:
        text = (root / SKILL / 'assets' / name).read_text(encoding='utf-8')
        if name.endswith('.ipynb'):
            value = json.loads(text)
            for cell in value['cells']:
                cell['source'] = [expand(line, substitutions) for line in cell['source']]
            rendered[name] = json.dumps(value, indent=2, ensure_ascii=False) + '\n'
        else:
            rendered[name] = expand(text, substitutions)
    target.mkdir(parents=True)
    for name, content in rendered.items():
        (target / name).write_text(content, encoding='utf-8')
    update_hashes(target, manifest)
    write_json(target / 'manifest.json', manifest)
    return target


def expand(text, substitutions):
    for name, value in substitutions.items():
        text = text.replace('{{' + name + '}}', value)
    return text


def update_hashes(target, manifest):
    for record in manifest['outputs']:
        path = target / record['path']
        record['sha256'] = digest(path) if path.is_file() else None


def inventory(root, selected):
    target = destination(root, selected)
    # Reject all unexpected entries and redirected files before reading them.
    allowed = {*SOURCE_FILES, *BINARY_FILES, 'manifest.json'}
    for path in target.iterdir():
        if path.name not in allowed or path.is_symlink() or not path.is_file():
            raise ValueError('unexpected or redirected package entry: ' + path.name)
        if path.resolve() != path:
            raise ValueError('redirected package file: ' + path.name)
    actual = read_json(target / 'manifest.json')
    if type(actual['schema_version']) is not int:
        raise ValueError('schema_version must be an integer')
    expected = plan(root, selected, actual['issue'], actual['package'])
    if set(actual) != set(expected):
        raise ValueError('manifest fields differ from contract')
    for key in expected:
        if key != 'outputs' and actual[key] != expected[key]:
            raise ValueError('manifest/source drift: ' + key)
    records = actual['outputs']
    if not isinstance(records, list) or len(records) != len(expected['outputs']):
        raise ValueError('output inventory differs from requested package')
    for record, planned in zip(records, expected['outputs']):
        if set(record) != {'path', 'sha256'} or record['path'] != planned['path']:
            raise ValueError('output inventory differs from requested package')
        if record['sha256'] is not None and not re.fullmatch(r'[0-9a-f]{64}', record['sha256']):
            raise ValueError('invalid output hash')
    filenames = {r['path'] for r in records}
    if any(p.name not in filenames | {'manifest.json'} for p in target.iterdir()):
        raise ValueError('unlisted output file')
    if any(not (target / name).is_file() for name in SOURCE_FILES):
        raise ValueError('missing source artifact')
    return target, actual


def notebook_check(value):
    if (set(value) != {'nbformat', 'nbformat_minor', 'metadata', 'cells'}
            or value['nbformat'] != 4 or value['nbformat_minor'] != 5
            or value['metadata'] != NOTEBOOK_METADATA
            or not isinstance(value['cells'], list) or not value['cells']):
        raise ValueError('invalid notebook structure/metadata')
    ids = set()
    for cell in value['cells']:
        kind = cell['cell_type']
        keys = {'id', 'cell_type', 'metadata', 'source'}
        if kind == 'code':
            keys |= {'outputs', 'execution_count'}
            if cell['outputs'] != [] or cell['execution_count'] is not None:
                raise ValueError('notebook output/execution history must be cleared')
        elif kind != 'markdown':
            raise ValueError('only markdown and code cells are supported')
        if (set(cell) != keys or cell['metadata'] != {}
                or not isinstance(cell['source'], list)
                or not all(isinstance(line, str) for line in cell['source'])
                or not re.fullmatch(r'[A-Za-z0-9_-]{1,64}', cell['id']) or cell['id'] in ids):
            raise ValueError('invalid cell structure/metadata/id')
        ids.add(cell['id'])


def check(root, selected, ready=False, hashes=True):
    target, manifest = inventory(root, selected)
    for record in manifest['outputs']:
        path = target / record['path']
        if not path.exists():
            if ready or record['sha256'] is not None:
                raise ValueError('missing output: ' + path.name)
            continue
        if hashes and record['sha256'] != digest(path):
            raise ValueError('output hash drift; review then snapshot: ' + path.name)
        if not path.stat().st_size:
            raise ValueError('empty artifact: ' + path.name)
        if path.name == 'student-lab.ipynb':
            notebook_check(read_json(path))
        if ready and path.suffix in ('.md', '.ipynb'):
            text = path.read_text(encoding='utf-8')
            if path.suffix == '.ipynb':
                text = notebook_authoring_text(read_json(path))
            if re.search(r'\b(TODO|TBD|FIXME)\b|\{\{', text, re.I):
                raise ValueError('unresolved drafting marker: ' + path.name)
        if ready and path.name in BINARY_FILES:
            member = 'word/document.xml' if path.suffix == '.docx' else 'ppt/presentation.xml'
            with zipfile.ZipFile(path) as archive:
                if not {'[Content_Types].xml', member} <= set(archive.namelist()):
                    raise ValueError('invalid Office container: ' + path.name)
    return target, manifest


def notebook_authoring_text(value):
    """Only explicit student task markers in student-* cells are not drafting TODOs.

    This is a readiness distinction, never permission to hide arbitrary author work.
    All other markers (including template tokens) remain visible to the gate.
    """
    notebook_check(value)
    sources = []
    for cell in value['cells']:
        text = ''.join(cell['source'])
        if cell['id'].startswith('student-'):
            text = text.replace('STUDENT TODO:', 'Student task:')
        sources.append(text)
    return '\n'.join(sources)


def snapshot(root, selected):
    target, manifest = check(root, selected, hashes=False)
    update_hashes(target, manifest)
    write_json(target / 'manifest.json', manifest)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest='command', required=True)
    for name in ('plan', 'init', 'snapshot', 'check'):
        command = commands.add_parser(name)
        command.add_argument('--session', required=True)
        if name in ('plan', 'init'):
            command.add_argument('--issue', type=int, required=True)
            command.add_argument('--package', choices=('source', 'full'), default='source')
        if name == 'check':
            command.add_argument('--review-ready', action='store_true')
    args = parser.parse_args(argv)
    try:
        if args.command == 'plan':
            print(json.dumps(plan(ROOT, args.session, args.issue, args.package), indent=2))
        elif args.command == 'init':
            initialise(ROOT, args.session, args.issue, args.package)
            print('CREATED draft: sessions/' + args.session + '; not approved or released.')
        elif args.command == 'snapshot':
            snapshot(ROOT, args.session)
            print('RECORDED current hashes; no academic or release approval.')
        else:
            check(ROOT, args.session, args.review_ready)
            print('PASS: package structure/integrity; manual review and professor approval still required.')
    except (OSError, ValueError, KeyError, TypeError, AttributeError, StopIteration,
            zipfile.BadZipFile) as exc:
        print('FAIL:', exc, file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
