# SETUP-04 validation and acceptance report

For [Issue #4](https://github.com/fajouri/msc-machine-learning/issues/4), 2026-10-21. Status: **draft pending professor review**.

## Scope and changed files

- [Delivery plan](delivery-plan.md): source/dependency evidence, common online/campus procedures, accessibility, outage recovery, three 180-minute run sheets and session-specific activities/evidence/fallback/access/logistics for S01–S16.
- [Validator](../curriculum/validate_delivery.py): standard-library checks against the existing session map, planning completeness, schedule continuity/capacity and local links.
- [Regression tests](../tests/test_delivery.py): reject missing/duplicate/reordered sessions, mode drift, missing planning fields, invalid timing, insufficient presentation capacity, lost draft status and broken links.
- [CI workflow](../.github/workflows/delivery.yml): scoped, read-only validation with no package installation or stored credentials.
- [Root README](../README.md): links to the plan and this evidence.
- This report: acceptance evidence and unresolved decisions.

No approved source, existing curriculum manifest, workload allocation, assessment requirement or session mapping is edited. No lesson notebooks, student records, instructor solutions, exam keys, datasets or third-party assets are added. Future pack/runtime requirements are explicitly distinguished from delivered/tested materials.

## Execution evidence

Run from the repository root with Python 3.13.2; local results recorded on 2026-10-21.

| Check | Result |
| --- | --- |
| SETUP-01 and SETUP-03 | Both closed via GitHub API on 2026-10-21, no comments; supporting repository artifacts present. No blocking setup dependency missing. |
| `python -s curriculum/validate_curriculum.py` | PASS: source hashes, outcomes, session mapping, assessment constraints and 250-hour accounting. |
| `python -s curriculum/validate_traceability.py` | PASS: all structural checks and local descriptor identity in this Windows checkout. |
| `python -s curriculum/validate_delivery.py` | PASS: 16 ordered sessions, 9/7 modes, planning fields, three continuous 180-minute schedules, ten ten-minute presentations and plan links. |
| `python -s references/validate_bibliography.py` | PASS in audit mode; existing unresolved Ng metadata still blocks bibliography release, outside Issue #4 scope. |
| `python -s -m unittest discover -s tests -v` | PASS: 34 tests, including five new delivery tests with mutation subcases. |
| `git diff --check` | PASS; new-file whitespace and documentation links also checked locally. |
| Hosted CI | Local validation completed before publication; hosted results are reported on the PR. |

Manual review: the matrix retains each session's topics, including OpenAI Gym context, TensorFlow/Keras, early rigorous validation and the full S14 breadth. Proposed evidence requires explanation, methodological comparison, reproducibility and ethical qualification as appropriate. Static fallback reasoning is not asserted to establish implementation attainment. Lost synchronous teaching requires approved live recovery; the 9/7 allocation and workload budgets are not silently changed. S16 explicitly reserves 100 presentation minutes and 80 minutes for the other activities. Break treatment is a pending timetable decision, not a new contact-hour rule.

## Acceptance criteria

- [x] All 16 sessions have engagement, observable evidence, fallback, accessibility and logistics proposals.
- [x] Inputs, dependency verification, provenance, decisions and reproducible validation steps documented.
- [x] No fabricated references or changes to approved outcomes, blocks, hours or assessment weights.
- [x] Public student/instructor boundary respected; no answers, keys or personal records added.
- [x] Automated checks pass; local evidence and file links are prepared in this report.
- [ ] Professor approves academic/operational proposals and applicable presentation/accessibility decisions.
- [ ] Evidence/file links posted to Issue #4 or a PR referencing #4. Publication authorised by the user after local implementation; the PR description carries the evidence and links.

## Unresolved decisions and limits

Confirm session placement; private communication/LMS and outage announcement route; campus room, IT and loan-device arrangements; accessibility and recording policies; break treatment and recovery thresholds; S10 bridge, S12 environment and S14 depth; S16 enrolment/Q&A/accommodation timings and presentation workload accounting. Exam date/room/invigilation and assessment blueprint/dataset/rubrics remain later decisions. Existing descriptor publication permission must be resolved separately; this change does not upload or modify it.

Issue closure is not academic approval. These decisions do not block drafting this setup plan, but applicable pre-delivery gates must pass before session release. Tests verify structural coverage and timing, not actual runtime compatibility, accessibility, pedagogical sufficiency or institutional approval. No live Meet/Colab/Kaggle integration or outage rehearsal is claimed. The pre-existing traceability validator remains line-ending-sensitive; it is run locally, not added to Linux CI.

Initial implementation and validation were performed locally without staging, committing or external publication. The user subsequently authorised a commit, push and PR targeting `master`. Academic approval remains pending; repository publication does not constitute professor sign-off.
