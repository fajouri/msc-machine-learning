# M5 student notebook templates (AUTO-03)

[Issue #9](https://github.com/fajouri/msc-machine-learning/issues/9), implemented with Codex. Draft pedagogical proposals pending professor review; no curriculum, assessment or workload changes.

## Choose and adapt a template

- [Session lab](../../skills/msc-course-builder/assets/student-lab.ipynb): canonical AUTO-01 asset, with setup, original synthetic data, a public worked baseline, guided discussion, blank independent experiment and reflection cells. `session_package.py init` expands its session/title/mode/block/exact approved outcome placeholders into `sessions/Sxx/student-lab.ipynb`.
- [Independent investigation](independent-practice.template.ipynb): standalone student worksheet with the same data/setup and unattempted experiment, without a fitted baseline. Copy its cells into the existing session notebook when desired; do not add an unlisted output to an AUTO-01 package. Author its session framing before delivery.

These are templates, not 16 authored lessons. Preserve required pandas/scikit-learn, TensorFlow/Keras and OpenAI Gym curriculum coverage in future labs; the standard-library illustration does not replace those requirements. Review RL environment selection and S10/S14 scope separately.

Start from the course-builder preflight and initialise only the session named by the later task. Keep `student-lab.ipynb` as the single notebook output. Complete ordinary author TODOs and verify outcome alignment before readiness. The lecture JSON schema remains unchanged: coordinate activities with `framing.independent_practice`, `framing.reproducibility`, `framing.ethical_evaluation` and activity-slide purposes, using the same curriculum session identity. Do not put notebook fields into that schema.

## Reusable exercise cell convention

Use stable, unique `student-<task>` cell IDs, empty cell metadata and the exact literal `STUDENT TODO:` for tasks intentionally left to students. A blank executable cell contains a `None` assignment:

```python
# STUDENT TODO: Implement the investigation described in the preceding Markdown.
experiment_results = None
```

Place checks in a separate ordinary code cell. If the value is `None`, print **NOT ATTEMPTED** and continue. If attempted, check documented types/shapes/ranges without supplying independent answers. A format check is neither methodological validation nor a grade. Keep reasoning prompts as Markdown with the same marker. Do not use `raise NotImplementedError`, invalid syntax, unconditional failure or completed reference answers as student placeholders.

AUTO-01 readiness ignores only that exact marker in `student-*` cells. Ordinary TODO/TBD/FIXME and `{{...}}` tokens still fail. Reviewers must inspect that marked tasks are actually student work. No tags, hidden cells, attachments, stored outputs or incidental Colab metadata are allowed in public sources.

## Student execution and reproducibility

Upload through Colab's File menu, save a personal copy, choose Python 3 on CPU and run all in a fresh runtime. A Google account/internet is needed for hosted execution, but no credentials in code, Drive mount, GPU, paid plan or external dataset is needed. Download your work before leaving and keep completed copies private. Setup/recovery and offline reasoning instructions appear inside each notebook. Google's [Colab FAQ](https://research.google.com/colaboratory/faq.html) documents notebook upload, sharing and runtime reset (checked 2026-10-21).

The runnable path uses only the standard library, Python >=3.10. No student dependencies need installing/pinning. Record the actual Python version. A fixed seed, versioned integer synthetic generator, canonical JSON SHA-256, explicit split IDs and exact rational baseline results support reproduction. Outputs are generated during execution and absent from public sources. The environment version line differs across Python versions; substantive results should not. No external data is downloaded or copied. `m5-synthetic-v1` is original non-personal teaching data, not a population dataset or fairness benchmark.

When a later session needs libraries, provide exact compatible versions and an installation cell before imports; record Python and hardware assumptions, restart after installation as needed, and test on fresh Colab. Record solver/random seeds, use fold-local preprocessing and distinguish multi-seed variability from repeatability. Do not assume seeds guarantee deterministic accelerator kernels. Record verified origin/version/hash/licence and permission evidence for replacement data.

## Validation

From the repository root:

```powershell
python -s templates/notebook/validate.py
python -s -m unittest discover -s tests -v
python -m venv .venv
.venv/Scripts/python -m pip install -r templates/notebook/requirements-validation.txt
.venv/Scripts/python -m pip check
.venv/Scripts/python -s templates/notebook/validate.py --execute
```

On Linux/macOS use `.venv/bin/python`. Pinned direct validation dependencies are author/CI tools only; transitive dependencies are resolved by pip, so this is not a full environment lock. [CI](../../.github/workflows/notebooks.yml) tests Python 3.10, 3.12 and 3.13 on Linux with the same direct pins and dependency consistency checks.

The default validator executes code in two fresh isolated Python processes with empty temporary working directories. `--execute` validates nbformat and runs all cells in two fresh Jupyter kernels, comparing outputs and failing on exceptions/timeouts. The [nbclient API](https://nbclient.readthedocs.io/en/latest/client.html) supports this approach (checked 2026-10-21). Neither route writes executed notebooks to the repository. `--notebook path` selects a template-compatible notebook; it expects unattempted `None` exercise stubs. It is not a grading tool.

These tools execute repository code, not sandboxed untrusted notebooks. Static path/metadata/stub checks catch specific regressions; they cannot establish privacy, originality, licensing, academic quality or absence of answers in arbitrary prose. Review the entire artifact and citation inventory before publication.

## References, private work and review

Templates contain original explanations/data and no external teaching readings or copied assets. The bibliography/usage ledger is unchanged. Register subsequent actual teaching uses under [bibliography conventions](../../references/README.md), with verified locators and visible attribution. The two links above document tooling rather than add course readings.

No instructor solution template, hidden answer, exam key or private storage is created. The [public-output boundary](../../docs/course-builder-boundary.md) governs the solution part of the original issue; separate private authoring requires a separate handling decision. Ignored paths and collapsed cells do not secure confidential material.

Before delivering an authored session: resolve author TODOs; run clean execution; clear outputs/counts and incidental metadata; run AUTO-01 snapshot/check; inspect academic depth, accessibility, rights and hidden content; test hosted Colab upload/run-all; record professor review. Structural success is not release approval. The existing Ng metadata TODO still blocks bibliography release. See [validation evidence and remaining decisions](../../docs/notebook-templates-validation.md).
