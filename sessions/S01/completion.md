# S01 — Source package completion and review record

Issue [#13](https://github.com/fajouri/msc-machine-learning/issues/13), 2026-10-21. Public student-readable **source draft**, pending professor review. No release, commit, push, PR, issue comment or closure is authorised by this record.

## Authority and actual artifacts

The hash-pinned approved curriculum supplies MQF Level 7, B01 Foundations and exact LO1 wording. The working map proposes S01 online, and the lecturer reports Google Meet, roughly ten students and Colab permission. The 180-minute timing, cases, diagrams, self-study sequence and formative checks are pedagogical proposals. The 60/30/10 weights, topic sequence, 48 teaching hours plus separate two-hour university certification allocation, and separate three-hour M5 exam are unchanged.

The course-builder preflight was run first: python -s skills/msc-course-builder/scripts/session_package.py plan --session S01 --issue 13 (exit 0). It verified required input hashes and identified the six source-package outputs. The four declared issues were read through GitHub API: SETUP-02 #2, AUTO-01 #7, AUTO-02 #8 and AUTO-03 #9 are closed; #13 remains open with zero comments. Closure is task provenance, not professor approval. Curriculum/traceability, delivery, bibliography, lecture-template and notebook-template contracts were read.

| File | Content and status |
| --- | --- |
| brief.md | Complete proposed 180-minute Meet run sheet, access and campus adaptations, LO1 traceability, S02 boundary |
| lecture.md | Detailed conceptual/mathematical teaching source and 18 slide records with seven public-safe note fields each |
| exercises.md | Student scenarios, guided audit, distinct unanswered investigation and critical extension |
| references.md | Five descriptor readings, verified primary links/locators, explicit unresolved Ng item and rights inventory |
| student-lab.ipynb | 14-cell student notebook with synthetic data, environment/hash/split record, guided baseline and unattempted independent cells |
| completion.md | This evidence and unresolved-gate record |
| manifest.json | Course-builder integrity inventory, to be snapshotted after this text is final |

No private instructor solution notebook, guidance, exam item/key, student record or credential was created. The public boundary decision excludes those outputs absent separately approved private storage. No external dataset or protected reading content is embedded. All cases, text diagrams and synthetic data are original. Five bibliography links in references.md and three on lecture slide SL18 are registered in references/citation-usage.json. A professor must still inspect every artifact for omitted reuse and verify actual rights.

## Verification observed

Environment: Windows PowerShell; Python 3.13.2. Student runtime requirement: Python 3.10+ CPU and standard library only. The existing local .venv uses Python 3.13.2 with nbclient 0.10.2, nbformat 5.10.4 and ipykernel 6.29.5, matching templates/notebook/requirements-validation.txt. These are validation tools, not student runtime dependencies.

| Command | Observed result |
| --- | --- |
| python -s curriculum/validate_traceability.py | Exit 0: descriptor hash, source identities, 16 sessions, 9/7 working modes and approved constraints pass structural checks |
| python -s references/validate_bibliography.py | Exit 0: five records and current teaching-use ledger pass offline audit |
| python -s templates/lecture/validate.py | Exit 0: reusable source contracts pass; it does not validate this prose or render slides |
| python -s templates/notebook/validate.py --notebook sessions/S01/student-lab.ipynb | Exit 0: two fresh isolated Python processes, unattempted cells remain unattempted |
| .venv/Scripts/python -s templates/notebook/validate.py --notebook sessions/S01/student-lab.ipynb --execute | Exit 0: two fresh Jupyter kernels, equal outputs, no execution errors; kernel emitted harmless profile-permission warnings |
| .venv/Scripts/python -m pip check | Exit 0: no broken validation-tool requirements |
| python -s -m unittest discover -s tests -q | Exit 0: 88 tests after fixture correction |
| git diff --check | Exit 0 at this report stage |
| python -s references/validate_bibliography.py --release | Expected exit 1: ng2017 unresolved metadata blocks publication |

The initial system-Python real-kernel command lacked nbformat; rerunning with the existing pinned .venv succeeded. The first full test run failed because the course-builder disposable fixture copied the live ledger's eight S01 uses but no session files; tests/test_course_builder.py now resets only that fixture ledger to empty. The 20 course-builder and 22 bibliography tests, then all 88 tests, passed. This is a fixture consistency correction, not a relaxation of production citation checks.

The notebook source retains null execution counts, empty outputs and empty cell metadata. Two clean runs establish computational repeatability for this local Python/Jupyter setup, not hosted Colab compatibility, statistical reliability or scientific validity. No hosted Colab upload/run-all occurred; that smoke test remains before delivery. Student-dependent investigation results cannot be executed until a student attempts them and are intentionally absent.

## Integrity commands to run after this report

1. python -s skills/msc-course-builder/scripts/session_package.py snapshot --session S01
2. python -s skills/msc-course-builder/scripts/session_package.py check --session S01
3. python -s skills/msc-course-builder/scripts/session_package.py check --session S01 --review-ready
4. git diff --check

Actual results of these final commands belong in the handoff response to avoid changing this report after it is hashed.

## Missing outputs and decisions

Editable lecture.docx and slides.pptx are **missing**. The document/presentation skills require a supported workspace dependency loader and rendered visual inspection; no such loader or authoritative artifact runtime is exposed in this session. The AUTO-02 template explicitly defers binary conversion. The existing source-package allowlist prevents placing an invented substitute binary in sessions/S01. Future work must create editable binaries from the reviewed source, preserve equations/notes/citations, render every page/slide, inspect at 1280×720 and in Meet, and register any new citation destinations. Microsoft 365 Copilot remains a human handoff.

The Ng year/version and official-URL decision remain **TODO** in the approved bibliography audit. This explicitly blocks the bibliography release gate. Professor decisions are also needed on academic depth, the proposed break/timing, final S01 mode/timetable, institutional contact channel, accessibility arrangements, reading access, asset/rights coverage and final release. No assessment rule or learning outcome has been changed.

Source package prepared for review; complete binary package, hosted execution, visual approval and publication remain open.
