# S01 — Source package completion and review record

Issue [#13](https://github.com/fajouri/msc-machine-learning/issues/13), initial PR [#65](https://github.com/fajouri/msc-machine-learning/pull/65), 2026-10-21. Public student-readable **source draft**, pending professor review. PR #65 was merged during review before these corrections landed; this revision is for a separate follow-up review. This record grants no release or academic approval.

## Authority and actual artifacts

The hash-pinned approved curriculum supplies MQF Level 7, B01 Foundations and exact LO1 wording. The working map proposes S01 online, and the lecturer reports Google Meet, roughly ten students and Colab permission. The 180-minute timing, cases, diagrams, self-study sequence and formative checks are pedagogical proposals. The approved assessment orientation now explicitly names the three-hour written exam (60%), class-internal Kaggle capstone with final model/leaderboard evidence and technical report (30%), and ten-minute presentation (10%). It introduces no project subweight, rubric or new assessed activity. The topic sequence and 48 teaching hours plus separate two-hour university certification allocation are unchanged.

The course-builder preflight was run first: python -s skills/msc-course-builder/scripts/session_package.py plan --session S01 --issue 13 (exit 0). It verified required input hashes and identified the six source-package outputs. The four declared issues were read through GitHub API: SETUP-02 #2, AUTO-01 #7, AUTO-02 #8 and AUTO-03 #9 are closed; #13 was open with zero comments at initial preflight and was later auto-closed when PR #65 merged. Closure is task provenance, not professor approval. Curriculum/traceability, delivery, bibliography, lecture-template and notebook-template contracts were read.

| File | Content and status |
| --- | --- |
| brief.md | Proposed 180-minute Meet run sheet, three-minute approved assessment orientation within 0–12, adaptations, LO1 traceability and S02 boundary |
| lecture.md | Detailed conceptual/mathematical source and 18 slide records with expanded seven-field public speaker notes |
| exercises.md | Student scenarios, guided NumPy/pandas and workflow audit, distinct unanswered investigation and extension |
| references.md | Five descriptor readings, verified primary links/locators, explicit unresolved Ng item and rights inventory |
| student-lab.ipynb | 20-cell notebook with pinned NumPy/pandas setup, array/DataFrame shape, selection and descriptive statistics, original synthetic data, guided baseline and unattempted independent cells |
| completion.md | This evidence and unresolved-gate record |
| manifest.json | Course-builder integrity inventory, to be snapshotted after this text is final |

No private instructor solution notebook, guidance, exam item/key, student record or credential was created. The public boundary decision excludes those outputs absent separately approved private storage. No external dataset or protected reading content is embedded. All cases, text diagrams and synthetic data are original. Five bibliography links in references.md and three on lecture slide SL18 are registered in references/citation-usage.json. A professor must still inspect every artifact for omitted reuse and verify actual rights.

## Verification observed

Environment: Windows PowerShell; Python 3.13.2. The S01 student path requires Python 3.10–3.13 CPU, NumPy 2.1.3 and pandas 2.2.3. The first dependency cell checks and, if needed, installs exact pins before import; it prints actual versions. A fresh Colab runtime needs internet for installation if its preinstalled versions differ. NumPy's [2.1 release notes](https://numpy.org/doc/2.1/release/2.1.0-notes.html) state Python 3.10–3.13 support, and the [pandas 2.2.3 notes](https://pandas.pydata.org/pandas-docs/version/2.2.3/whatsnew/v2.2.3.html) state Python 3.13 and NumPy 2.1 compatibility. Local .venv has those versions plus nbclient 0.10.2, nbformat 5.10.4 and ipykernel 6.29.5 for validation. Hosted Colab has not been tested.

| Command | Observed result |
| --- | --- |
| python -s curriculum/validate_traceability.py | Exit 0: descriptor hash, source identities, 16 sessions, 9/7 working modes and approved constraints pass structural checks |
| python -s references/validate_bibliography.py | Exit 0: five records and current teaching-use ledger pass offline audit |
| python -s templates/lecture/validate.py | Exit 0: reusable source contracts pass; it does not validate this prose or render slides |
| .venv/Scripts/python -s templates/notebook/validate.py --notebook sessions/S01/student-lab.ipynb | Exit 0: two fresh isolated Python processes, unattempted cells remain unattempted |
| .venv/Scripts/python -s templates/notebook/validate.py --notebook sessions/S01/student-lab.ipynb --execute | Exit 0: two fresh Jupyter kernels, equal outputs, no execution errors; kernel emitted harmless profile-permission warnings |
| .venv/Scripts/python -m pip check | Exit 0: no broken installed requirements |
| python -s templates/notebook/validate.py | Exit 0: unchanged reusable student templates run in two fresh processes |
| python -s -m unittest discover -s tests -q | Exit 0: all 88 tests |
| Slide-note field audit | 18 slide IDs; every slide has explanation, reasoning, timing, online/campus participation, fallback and transition |
| Run-sheet and LO1 audit | Eight continuous slots cover 0–180 minutes exactly; exact approved LO1 wording is present in brief.md |
| python -s references/validate_bibliography.py --release | Expected exit 1: ng2017 unresolved metadata blocks publication |

The prior PR revision used a standard-library-only student path. This correction uses the same original synthetic rows for a 24×2 NumPy array and a 24×3 pandas DataFrame with row_id, then keeps the training-only exact-fraction baseline and independent unanswered task. The local validation environment has the pins installed; the notebook's conditional online installation branch and hosted Colab upload/run-all still need a live smoke test before delivery. The earlier course-builder disposable-fixture correction remains unchanged in this revision.

The notebook source retains null execution counts, empty outputs and empty cell metadata. Two clean runs establish computational repeatability for this local pinned Python/Jupyter setup, not statistical reliability, hosted Colab compatibility or scientific validity. No hosted Colab upload/run-all occurred. Student-dependent investigation results cannot be executed until a student attempts them and are intentionally absent.

## Integrity commands to run after this report

1. python -s skills/msc-course-builder/scripts/session_package.py snapshot --session S01
2. python -s skills/msc-course-builder/scripts/session_package.py check --session S01
3. git diff --check

Actual results of these final commands belong in the handoff response to avoid changing this report after it is hashed. The review-ready command is deferred while the existing Ng TODO remains unresolved.

## Missing outputs and decisions

Editable lecture.docx and slides.pptx are **missing**. The document/presentation skills require a supported workspace dependency loader and rendered visual inspection; no such loader or authoritative artifact runtime is exposed in this session. The AUTO-02 template explicitly defers binary conversion. The existing source-package allowlist prevents placing an invented substitute binary in sessions/S01. Future work must create editable binaries from the reviewed source, preserve equations/notes/citations, render every page/slide, inspect at 1280×720 and in Meet, and register any new citation destinations. Microsoft 365 Copilot remains a human handoff.

The Ng year/version and official-URL decision remain **TODO** in the approved bibliography audit. This explicitly blocks the bibliography release gate. Professor decisions are also needed on academic depth, the proposed break/timing, final S01 mode/timetable, institutional contact channel, accessibility arrangements, reading access, asset/rights coverage and final release. No assessment rule or learning outcome has been changed.

Source package prepared for review; complete binary package, hosted execution, visual approval and publication remain open.
