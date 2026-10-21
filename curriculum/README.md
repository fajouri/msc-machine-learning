# SETUP-03 curriculum model and workload proposal

Issue: [#3](https://github.com/fajouri/msc-machine-learning/issues/3). Prepared 2026-10-21. **Draft: detailed workload allocations require professor approval.**

## Inputs and prerequisites

SETUP-01 ([#1](https://github.com/fajouri/msc-machine-learning/issues/1)) and SETUP-02 ([#2](https://github.com/fajouri/msc-machine-learning/issues/2)) were both verified closed via the GitHub API on 2026-10-21; neither had comments. SETUP-01's decisions are recorded in the [production plan](../docs/PRODUCTION_PLAN.md). SETUP-02 supplies the [audited source transcription and crosswalk](traceability-matrix.md), [coverage risks](traceability-gaps.md), and passing structural validator. No blocking prerequisite is missing. SETUP-02's outstanding pedagogical reviews are not presumed approved by issue closure.

The local descriptor hash matches the SETUP-02 baseline. This implementation uses that audit's complete LO transcription and topic/assessment summaries, rather than claiming a new visual PDF audit: PDF reader packages were unavailable in the current Python environment. Contrary to the earlier audit's untracked-file statement, the descriptor is already tracked in the current checkout. This task does not modify, upload or authorise publication of it; the professor should confirm its publication permission separately. No new bibliography or citations to external academic works are introduced.

## Machine-readable contract

[curriculum.json](curriculum.json) is a UTF-8 JSON document, schema version 1. [validate_curriculum.py](validate_curriculum.py) is its executable validation contract; it requires only Python's standard library. Identifiers are stable: LO1–LO8, B01–B09, S01–S16, and E/K/P. CERT identifies the separate university activity, never a fourth M5 assessment. Numeric hours represent **one student's workload**, not a class-wide sum; duration_minutes is a duration, not an additional workload allocation.

| Field | Meaning and authority |
| --- | --- |
| `sources` | Relative source paths, SHA-256 identities, hash conventions and authority labels; text hashes normalise CRLF to LF, PDF hashes use raw bytes. PDF hash is metadata only, not publication permission. |
| `dependencies` | Dated verification of the two declared GitHub prerequisites. |
| `approved` | Audited descriptor requirements: MQF, ECTS, hour budgets, exact LO wording, nine ordered topic-block summaries and three assessment requirements. |
| `contact_reconciliation` | Lecturer-reported university decision dated 2026-10-21; distinct from descriptor text. |
| `sessions` | Sixteen records preserving CSV titles, modes, LO links and indicative topics; linked to approved blocks. Individual modes remain proposed. Each has three contact hours and a proposed self-study activity/budget. |
| `assessment_workload` | Proposed ungraded workload accounting within the approved 40-hour envelope; it does not define a rubric or new assessment requirement. |
| `decisions_pending` | Academic and timetable decisions still requiring review. |

`session-map.csv` remains the working-map source; the JSON must agree with it. Source hashes detect later drift and require deliberate review before refreshing the manifest. Block descriptions summarise the audit; they are not verbatim quotations. Proposed reinforcement links from SETUP-02 are not promoted into approved LO mappings. OpenAI Gym stays in the block inventory without claiming a tested environment or authorising a substitute.

## Proposed workload and counting rules

The descriptor's total stays **250 = 50 contact + 160 self-study + 40 assessment**. Flagged teaching/contact difference: **50 − 16 × 3 = 2 hours**. SETUP-01 resolves this as a university-administered certification exam outside lecturer responsibility. It remains separate from the three-hour M5 written exam and contributes nothing to the proposed 40-hour M5 assessment allocation. No certification preparation or administration deliverable is assigned to the lecturer.

| Sessions | Self-study hours per session | Subtotal |
| --- | --- | --- |
| S01 | 8 | 8 |
| S02–S09 | 10 | 80 |
| S10 | 12 | 12 |
| S11–S12 | 10 | 20 |
| S13–S14 | 12 | 24 |
| S15–S16 | 8 | 16 |
| Total | | **160** |

More time is proposed for dimensionality reduction/autoencoder prerequisites and neural-network breadth. Each session's JSON activity asks for mathematical reasoning, methodological justification, reproducibility or ethical interpretation as appropriate to MQF Level 7. These are practice proposals, not delivered labs or proof of attainment. Self-study excludes work producing graded capstone submissions, dedicated exam revision and presentation preparation, which are budgeted below. Practice may inform assessed work, but the same time must not be logged in both categories.

| Assessment work | Proposed hours |
| --- | --- |
| Written exam: dedicated revision/practice | 9 |
| Written exam: sitting (approved duration) | 3 |
| Capstone: problem, permissions and validation design | 4 |
| Capstone: implementation, experiments and evaluation | 14 |
| Capstone: report, limitations and reproducibility package | 8 |
| Presentation: preparation and rehearsal | 2 |
| Total | **40** |

The proposed assessment totals are E = 12, K = 26, P = 2 hours; they do not imply proportional grading weights. The approved **60/30/10** weights, **three-hour exam**, **leaderboard plus technical report**, and **ten-minute presentation** remain unchanged. No leaderboard/report split, rubric, new pass rule or mandatory model family is introduced. Capstone design and reporting are placed inside the existing capstone budget to address SETUP-02's planning risk without imposing new graded milestones.

Presentation delivery is counted once within S16's three contact hours, with zero additional assessment hours. This is an explicit **accounting proposal pending professor approval**, not an institutional ruling about overlapping categories. Ten students' presentations occupy 100 minutes of the shared session; this is not 100 minutes of assessment workload added for every student. The remaining 80 minutes require a feasible Q&A/changeover/debrief/synthesis timetable. No extra contact time is invented. S16 self-study is synthesis/reflection, separate from dedicated exam revision.

## Validation and review

From the repository root:

```powershell
python -s curriculum/validate_curriculum.py
python -s curriculum/validate_traceability.py
python -s -m unittest discover -s tests -v
git diff --check
```

The curriculum validator checks source identities, exact audited outcomes, CSV agreement, block ranges, 9/7 modes, 16 × 3 hours, nonnegative finite numeric workload, 160/40 totals, assessment weights/durations, certification separation and presentation counting. Regression tests exercise invalid values, changed sources, changed requirements, duplicates and missing data, including an LF checkout without the PDF. Structural checks do not judge mathematical depth, workload realism, comprehensive assessment coverage, or approve academic decisions. Block-summary fidelity and activity quality require human review. The new CI workflow runs the curriculum validator and its tests; the earlier traceability validator is run locally because its pre-existing raw CSV hash depends on Windows line endings. Changing that earlier validator is outside this issue.

See [validation evidence and acceptance checklist](workload-validation.md). Existing SETUP-02 gaps about assessment coverage, neural prerequisites, environment choice and S16 logistics remain open. The detailed allocations are reviewable proposals; they should not be released as an approved student schedule until the professor accepts them.
