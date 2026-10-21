"""Offline AUTO-02 source contracts. Python standard library; never builds Office files."""
import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
KEYWORDS = {'type', 'properties', 'required', 'additionalProperties', 'items',
            'minItems', 'uniqueItems', 'enum', 'const', 'minimum', 'pattern',
            '$schema', 'title', 'description'}


def read(path):
    def pairs(items):
        result = {}
        for key, value in items:
            if key in result:
                raise ValueError(f'duplicate JSON key: {key}')
            result[key] = value
        return result
    return json.loads(Path(path).read_text(encoding='utf-8'), object_pairs_hook=pairs)


def schema_check(value, schema, path='$'):
    """Validate the documented JSON Schema subset; reject unsupported keywords."""
    unknown = set(schema) - KEYWORDS
    if unknown:
        raise ValueError(f'{path}: unsupported schema keywords {sorted(unknown)}')
    types = {'object': dict, 'array': list, 'string': str, 'integer': int, 'boolean': bool}
    kind = schema.get('type')
    if kind not in types or type(value) is not types[kind]:
        raise ValueError(f'{path}: expected {kind}')
    if 'const' in schema and value != schema['const']:
        raise ValueError(f'{path}: incorrect constant')
    if 'enum' in schema and value not in schema['enum']:
        raise ValueError(f'{path}: invalid choice')
    if kind == 'object':
        props = schema['properties']
        if set(schema['required']) - set(value):
            raise ValueError(f'{path}: missing required fields')
        if schema['additionalProperties'] is not False or set(value) - set(props):
            raise ValueError(f'{path}: unknown fields')
        for key, item in value.items():
            schema_check(item, props[key], f'{path}.{key}')
    elif kind == 'array':
        if len(value) < schema.get('minItems', 0):
            raise ValueError(f'{path}: too few items')
        if schema.get('uniqueItems') and len({json.dumps(v, sort_keys=True) for v in value}) != len(value):
            raise ValueError(f'{path}: duplicate items')
        for index, item in enumerate(value):
            schema_check(item, schema['items'], f'{path}[{index}]')
    elif kind == 'string':
        if not value.strip() or ('pattern' in schema and not re.search(schema['pattern'], value)):
            raise ValueError(f'{path}: empty or malformed string')
    elif kind == 'integer' and value < schema.get('minimum', value):
        raise ValueError(f'{path}: below minimum')


def validate_source(source, root=ROOT, complete=False):
    schema_check(source, read(HERE / 'lecture.schema.json'))
    curriculum = read(root / 'curriculum/curriculum.json')
    session = next((s for s in curriculum['sessions'] if s['id'] == source['session_id']), None)
    if session is None:
        raise ValueError('unknown session')
    if source['learning_outcomes'] != session['learning_outcomes']:
        raise ValueError('learning outcomes differ from canonical session')
    if source['session_title'] != session['title'] or source['mode'] != session['proposed_mode']:
        raise ValueError('session title/mode differs from canonical session')
    ids = [s['id'] for s in source['slides']]
    if len(ids) != len(set(ids)):
        raise ValueError('duplicate slide IDs')
    covered = set()
    registry = {s['id'] for s in read(root / 'references/bibliography.json')['sources']}
    uses = read(root / 'references/citation-usage.json')['uses']
    for slide in source['slides']:
        if not set(slide['learning_outcomes']) <= set(source['learning_outcomes']):
            raise ValueError('slide outcome outside session')
        covered.update(slide['learning_outcomes'])
        if slide['type'] == 'equation' and not slide['equations']:
            raise ValueError('equation slide requires equation record')
        if slide['type'] == 'figure' and not slide['figures']:
            raise ValueError('figure slide requires figure record')
        citation_ids = {c['source_id'] for c in slide['citations']}
        for figure in slide['figures']:
            if figure['origin'] == 'third_party' and figure['source_id'] not in citation_ids:
                raise ValueError('third-party figure requires citation')
            if figure['origin'] == 'original' and figure['source_id'] != 'original':
                raise ValueError('original figure must declare original source')
        for citation in slide['citations']:
            if citation['source_id'] not in registry:
                raise ValueError('citation source missing from bibliography registry')
            if complete and not any(all(use.get(k) == citation[k] for k in
                                        ('source_id', 'artifact', 'locator', 'attribution')) for use in uses):
                raise ValueError('citation use missing from existing ledger')
    if covered != set(source['learning_outcomes']):
        raise ValueError('session outcomes not covered')
    if complete and re.search(r'TODO|TBD|FIXME|\{\{', json.dumps(source), re.I):
        raise ValueError('unresolved drafting placeholders')


def markdown(source):
    """Deterministic Word-ready Markdown view; all fields remain visible."""
    lines = [f"# {source['session_id']} {source['session_title']}", '',
             'Draft pending professor review. All notes are public student content.', '',
             '## Source metadata', '', '```json',
             json.dumps({k: v for k, v in source.items() if k not in ('framing', 'slides')},
                        indent=2, ensure_ascii=False), '```', '',
             '## Lecture framing', '']
    for key, value in source['framing'].items():
        lines += [f'### {key.replace("_", " ").title()}', '', value, '']
    for slide in source['slides']:
        lines += [f"## {slide['id']} {slide['title']}", '']
        for key, value in slide.items():
            if key in ('id', 'title'):
                continue
            lines += [f'### {key.replace("_", " ").title()}', '']
            if isinstance(value, (dict, list)):
                lines += ['```json', json.dumps(value, indent=2, ensure_ascii=False), '```', '']
            else:
                lines += [str(value), '']
    return '\n'.join(lines).rstrip() + '\n'


def check_bundle():
    design = read(HERE / 'design.json')
    schema_check(design, read(HERE / 'design.schema.json'))
    source = read(HERE / 'lecture.template.json')
    validate_source(source)
    if (HERE / 'lecture.template.md').read_text(encoding='utf-8') != markdown(source):
        raise ValueError('Markdown template differs from structured source')
    expected = set(read(HERE / 'lecture.schema.json')['properties']['slides']['items']['properties']['type']['enum'])
    if {s['type'] for s in source['slides']} != expected:
        raise ValueError('template must demonstrate every slide type')
    return source


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=Path, help='Validate a source JSON without writing files')
    parser.add_argument('--complete', action='store_true', help='Reject TODOs and require citation ledger matches; not release approval')
    parser.add_argument('--markdown', action='store_true', help='Print deterministic Markdown to stdout')
    args = parser.parse_args()
    try:
        source = check_bundle()
        if args.source:
            source = read(args.source)
        validate_source(source, complete=args.complete)
        print(markdown(source) if args.markdown else 'PASS: source contracts only; Office generation and visual QA deferred.', end='\n')
    except (ValueError, OSError, KeyError, TypeError) as error:
        parser.exit(1, f'FAIL: {error}\n')


if __name__ == '__main__':
    main()
