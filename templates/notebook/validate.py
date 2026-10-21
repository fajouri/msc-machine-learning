"""Validate public templates; optionally execute twice in fresh Jupyter kernels."""
import argparse
import ast
import importlib.util
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[2]
TEMPLATES = (
    ROOT / 'skills/msc-course-builder/assets/student-lab.ipynb',
    ROOT / 'templates/notebook/independent-practice.template.ipynb',
)
spec = importlib.util.spec_from_file_location(
    'notebook_package_contract', ROOT / 'skills/msc-course-builder/scripts/session_package.py')
builder = importlib.util.module_from_spec(spec)
spec.loader.exec_module(builder)


def read(path):
    def unique(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError('duplicate JSON key: ' + key)
            result[key] = value
        return result
    return json.loads(path.read_text(encoding='utf-8'), object_pairs_hook=unique)


def validate(value):
    builder.notebook_check(value)
    cells = {cell['id']: cell for cell in value['cells']}
    required = {'overview', 'setup', 'environment', 'data-provenance', 'data',
                'student-practice', 'student-experiment', 'exercise-checks', 'student-reflection'}
    if not required <= cells.keys():
        raise ValueError('missing required notebook sections')
    for cell in value['cells']:
        source = ''.join(cell['source'])
        if not source.strip():
            raise ValueError('empty cell: ' + cell['id'])
        if re.search(r'[A-Za-z]:[\\/]|/content/drive|/Users/|/home/|drive\.mount|userdata\.get|os\.environ', source):
            raise ValueError('local path or credential/storage dependency')
        if cell['cell_type'] == 'code':
            tree = ast.parse(source)
            # Public reusable exercise cells contain stubs, never completed answers.
            if cell['id'].startswith('student-'):
                if not tree.body or any(
                    not isinstance(node, ast.Assign)
                    or not isinstance(node.value, ast.Constant)
                    or node.value.value is not None
                    for node in tree.body
                ):
                    raise ValueError('student code must contain only unattempted None stubs')
    if not any('STUDENT TODO:' in ''.join(c['source']) for c in value['cells']):
        raise ValueError('missing explicit student tasks')


def execute_python(value):
    """Dependency-free smoke check, distinct from real notebook execution."""
    validate(value)
    source = '\n'.join(''.join(c['source']) for c in value['cells'] if c['cell_type'] == 'code')
    with tempfile.TemporaryDirectory() as folder:
        result = subprocess.run([sys.executable, '-I', '-c', source], cwd=folder,
                                capture_output=True, text=True, timeout=60)
    if result.returncode:
        raise ValueError('student path failed: ' + result.stderr)
    return result.stdout


def execute_kernel(value):
    """Never persist executed notebooks or kernel metadata into public sources."""
    import nbformat
    from nbclient import NotebookClient
    from jupyter_client import KernelManager

    validate(value)
    notebook = nbformat.reads(json.dumps(value), as_version=4)
    nbformat.validate(notebook)
    manager = KernelManager(kernel_name='python3')
    manager.kernel_spec.argv = [sys.executable, '-I', '-m', 'ipykernel_launcher',
                                '-f', '{connection_file}']
    with tempfile.TemporaryDirectory() as folder:
        client = NotebookClient(notebook, km=manager, timeout=60, allow_errors=False,
                                resources={'metadata': {'path': folder}}, record_timing=False)
        try:
            client.execute()
        finally:
            # A supplied manager is caller-owned, including on execution failure.
            if manager.has_kernel:
                manager.shutdown_kernel(now=True)
    return [[{k: output[k] for k in ('output_type', 'name', 'text', 'data') if k in output}
             for output in cell.get('outputs', [])]
            for cell in notebook.cells if cell.cell_type == 'code']


def repeat(value, executor):
    first, second = executor(value), executor(value)
    if first != second:
        raise ValueError('non-deterministic outputs across fresh executions')
    return first


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--execute', action='store_true', help='require pinned Jupyter tools; two fresh kernels')
    parser.add_argument('--notebook', type=Path, action='append')
    args = parser.parse_args(argv)
    try:
        for path in args.notebook or TEMPLATES:
            value = read(path)
            repeat(value, execute_kernel if args.execute else execute_python)
            print('PASS:', path.name, '- two fresh ' + ('Jupyter kernels' if args.execute else 'Python processes'))
    except Exception as exc:
        print('FAIL:', exc, file=sys.stderr)
        return 1
    print('Unattempted exercises remain unattempted; professor review and hosted Colab smoke test required.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
