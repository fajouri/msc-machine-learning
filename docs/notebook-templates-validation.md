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

## PR #64 correction: preserve the audit hash across checkout line endings

The initial [Linux run 39624086098](https://github.com/fajouri/msc-machine-learning/actions/runs/39624086098) failed on Python 3.13 at `working session map unchanged from audit baseline`; fail-fast cancelled the 3.10/3.12 jobs. The traceability validator hashed raw bytes, unlike the later curriculum validator's explicit CRLF-to-LF source convention. Windows `core.autocrlf=true` produced CRLF in the working tree, while Git stored LF (`git ls-files --eol`: `i/lf w/crlf`).

Exact byte comparison on 2026-10-21:

| Form | Bytes | CRLF pairs / LF bytes | SHA-256 |
| --- | --- | --- | --- |
| Windows working CSV / original CRLF audit form | 1544 | 17 / 17 | `a60b0336de9801c95a9ed082ff082e52cfa9b8daaff07efba4f9c855440e4f10` |
| Git blob / LF checkout form | 1527 | 0 / 17 | `92b4f9665a376bcca52d08401d974e81e3e1b69c2910367c1a773964f0424b6d` |

Both are ASCII-compatible UTF-8, without a BOM or bare carriage returns; only the 17 CR bytes differ. Binary reads via `Path.read_bytes()` and `subprocess.check_output(['git', 'show', revision + ':curriculum/session-map.csv'])` avoid shell decoding/newline conversion. The Git blobs at scaffold `deb702d`, original audit `fec7671` and PR head `100c072` are byte-identical LF content. Converting that historical blob to CRLF reproduces exactly the `a60b...` hash recorded by **both** the original audit matrix and validator at `fec7671`. That historical CRLF identity remains authoritative for this integrity check; it is not replaced by a newly measured hash. The descriptor remains the academic authority and the CSV remains the working teaching map.

The narrow fix in [validate_traceability.py](../curriculum/validate_traceability.py) hashes `payload.replace(b'\r\n', b'\n').replace(b'\n', b'\r\n')` against the **unchanged original CRLF hash**. This explicitly permits LF and CRLF (including a mixture) as transport-equivalent terminators, mapping them back to the historical form. No text decoding, BOM stripping, whitespace trimming, Unicode normalization, bare-CR normalization or CSV reserialization occurs. Final-newline presence remains significant. The validator also logs raw byte length, CRLF/LF counts and SHA-256 so actual Linux checkouts can be compared directly with Windows. No input, expected hash, integrity check or workflow step is removed or skipped.

[Five regression tests](../tests/test_traceability.py) run the full CLI in disposable repositories. They pin both historically established hashes, accept unchanged LF/CRLF/mixed forms, and reject changed mode, LO, title, session number and spacing under both LF and CRLF. They also reject UTF-8 BOM insertion, UTF-16 encoding, changed non-ASCII bytes, bare CR endings, missing/extra final newline and extra whitespace.

Local Windows/Python 3.13.2 verification after correction: **88 tests passed**; traceability, curriculum, delivery, bibliography audit and lecture validators passed; both notebooks passed two fresh Jupyter kernels with identical outputs. Source comparison against `100c072` confirmed unchanged bytes after only checkout CRLF-to-LF normalization for the session CSV, curriculum JSON, traceability matrix/gaps, production plan and delivery plan. In particular, curriculum JSON retains SHA-256 `0183f76df295b2946b4274c172ed25a89c067aab3ff121118851fd8b7d9a0ded`: approved outcomes, assessment rules and teaching modes are unchanged. The correction changes only the traceability validator, its new tests and this report.

Linux GitHub Actions [run 39625163207](https://github.com/fajouri/msc-machine-learning/actions/runs/39625163207), after correction commit `7b7d839`, passed all jobs on Python **3.10.22, 3.12.15 and 3.13.16**. Each job ran all **88 tests**, both notebooks twice in fresh Jupyter kernels, every listed validator and the clean-tree check. All three actual Linux logs reported `bytes=1527 CRLF=0 LF=17 SHA-256=92b4f9665a376bcca52d08401d974e81e3e1b69c2910367c1a773964f0424b6d`, directly confirming the Git/LF form above and its equivalence to the Windows audit bytes. The historical-identity tests also checked ASCII/no-BOM on each runner. Other PR checks passed. This evidence-only follow-up records those observed results; consult the PR checks for its subsequent head run.

Hosted Colab and professor/release review remain separate gates. PR #64 is not merged and Issue #9 is not closed by this correction.
