# AUTO-03 implementation and validation evidence

Task: [Issue #9](https://github.com/fajouri/msc-machine-learning/issues/9). Date: 2026-10-21. Executor: Codex, as requested. Status: implemented for professor review. The initial validation was completed locally before committing; the user subsequently authorised a commit, push and PR. This does not authorise issue closure or student release.

## Inputs and scope

Read AGENTS.md, production plan, working session map, course-builder skill and package contract, approved curriculum model, traceability matrix/gaps, delivery plan, public-output boundary, bibliography/usage conventions, existing lecture schema and all five existing test modules. GitHub Issue #9 and its empty comment list were checked through the API. AUTO-01 / Issue #7 was verified closed, with no comments; its implementation is present. `plan --session S01 --issue 9` passed without creating a session package. S01 was only a preflight representative, not a claim that this task authors that session.

The issue's original solution/private-storage wording is bounded by the explicit public-only contract and this user request. No instructor solutions, exam keys, completed independent answers, private records or private storage were generated. The worked constant baseline is explicitly public instructional material, separate from the unanswered seed-sensitivity investigation.

All activity choices, the synthetic demonstration, and template adaptation guidance are pedagogical proposals. Approved outcomes, topic blocks, workload budgets and 60/30/10 assessment rules are unchanged. No new reading assignment, invented citation or third-party dataset was added. The two tooling references in the README were checked against the official Colab FAQ and nbclient documentation; these are not additions to the approved bibliography. A manual inspection of the new notebook source found original prose/code, original synthetic rows and no third-party teaching assets; a future authored lesson still needs its own complete citation/rights review.

## Changed files

| File | Purpose |
| --- | --- |
| [student-lab.ipynb](../skills/msc-course-builder/assets/student-lab.ipynb) | Canonical AUTO-01 session template: expanded exact LO text, setup, synthetic data/hash/split, worked mathematical baseline, guided activity, independent TODO stubs, checks and reflection |
| [independent-practice.template.ipynb](../templates/notebook/independent-practice.template.ipynb) | Reusable independent investigation with data/setup but no fitted model or completed answers |
| [Notebook README](../templates/notebook/README.md) | Inputs, setup/recovery, exercise convention, source provenance, authoring integration, validation and review steps |
| [validate.py](../templates/notebook/validate.py) | Structural/public-stub checks and repeatability in fresh processes or real Jupyter kernels; outputs remain in memory |
| [requirements-validation.txt](../templates/notebook/requirements-validation.txt) | Exact direct versions for author/CI notebook tooling; student path needs no pip installs |
| [session_package.py](../skills/msc-course-builder/scripts/session_package.py) | Narrow readiness exception for explicit student TODOs; original metadata/output/inventory checks retained |
| [Package contract](../skills/msc-course-builder/references/package-contract.md) | Documents the student-marker exception and notebook integration |
| [test_notebook_templates.py](../tests/test_notebook_templates.py) | 12 new regressions covering determinism, data/splits, public stubs, metadata, syntax, failures, markers, all session substitutions and format checks |
| [test_course_builder.py](../tests/test_course_builder.py) | Updated runnable-template expectation plus readiness lifecycle regression |
| [notebooks.yml](../.github/workflows/notebooks.yml) | Read-only CI on PRs/master: full regression suite, validators and two fresh kernels per template across Python 3.10/3.12/3.13 |
| [Repository README](../README.md) | Discovery link to templates and evidence |
| This report | Evidence, limitations and review decisions |

No lecture schema, curriculum source, bibliography record, citation ledger or manifest version changed. Existing AUTO-01 source/full inventories remain intact. The separate practice template is reusable cell material, not an additional session package output.

## Actual local checks

Environment: Windows, CPython 3.13.2. A fresh project `.venv` installed `nbclient==0.10.2`, `nbformat==5.10.4`, `ipykernel==6.29.5`; `pip check` reported no broken requirements. Student code imports only standard-library modules. Direct tooling versions are pinned; transitive packages are pip-resolved, not a fully locked environment.

| Command (repository root) | Observed result |
| --- | --- |
| `python -s skills/msc-course-builder/scripts/session_package.py plan --session S01 --issue 9` | PASS, read-only preflight |
| `python -s -m unittest discover -s tests` | PASS: 83 tests, including 12 new notebook tests and the added package lifecycle test |
| `python -s templates/notebook/validate.py` | PASS: both templates, two fresh isolated Python processes each |
| `.venv/Scripts/python -m pip check` | PASS: no broken requirements |
| `.venv/Scripts/python -s templates/notebook/validate.py --execute` | PASS: both notebooks, two fresh Jupyter kernels each, identical outputs, no source notebook mutations |
| `python -s curriculum/validate_traceability.py` | PASS, including unchanged local descriptor identity |
| `python -s curriculum/validate_curriculum.py` | PASS: approved wording/mappings, assessments and 250-hour accounting |
| `python -s curriculum/validate_delivery.py` | PASS: session modes and schedules |
| `python -s references/validate_bibliography.py` | PASS in audit mode |
| `python -s templates/lecture/validate.py` | PASS: existing lecture source contracts |
| `git diff --check` | PASS; local Git emits informational LF/CRLF conversion warnings |

Fresh-kernel execution initially exposed a notebook source-list normalization bug; the loader now uses `nbformat.reads` and the actual kernel check passed after the correction. Local sandbox restrictions required approved network access for the tooling install and permission for Jupyter's profile/runtime directory access. These are validation-environment restrictions, not student notebook dependencies.

The existing test for bibliography release still confirms the expected failure on `ng2017` unresolved metadata. Audit success does not bypass that gate. Regression tests also confirm all 16 session substitutions preserve canonical titles and exact outcome text, while source authoring markers remain unresolved until session production.

## Limits and unresolved decisions

- Hosted Google Colab upload/run-all has **not** been exercised in an authenticated browser. Compatibility is supported by self-contained standard-library code and real Jupyter execution; a clean hosted Colab smoke test and practical accessibility check remain pre-delivery gates.
- The new Linux/Python matrix was not run during initial local validation; consult the PR checks for subsequent GitHub results. Local evidence is Python 3.13.2 on Windows only.
- These are reusable drafts, not completed session lessons. Session-specific prerequisites, mathematical depth, reading locators and author TODOs need professor review and completion. Blank student tasks are deliberately retained and report NOT ATTEMPTED; no independent results are claimed tested or correct.
- Seeded SHA-256 ordering and rational arithmetic make the small illustration repeatable. One designed dataset/split does not establish statistical reliability, real-world validity or fairness. Later numerical/accelerator labs need their own versions, deterministic settings, uncertainty evaluation and execution evidence.
- Automated checks detect specific structural/metadata/path/stub regressions. They cannot authenticate privacy, rights, originality, the absence of arbitrary answers in prose, or academic approval. Human inspection remains required.
- No private solution handling decision is introduced. The existing Ng metadata issue, future dataset/reading rights, RL environment choice and S10/S14 scope decisions remain with the professor. No release approval is claimed.

Implementation and local engineering validation are ready for review. Hosted Colab verification and academic/release gates remain explicit outstanding work before student delivery.
