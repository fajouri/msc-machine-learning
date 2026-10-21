# SETUP-03 validation and acceptance report

Validated 2026-10-21 for [Issue #3](https://github.com/fajouri/msc-machine-learning/issues/3). Academic status: **proposal awaiting professor review**.

## Changed files

- [curriculum.json](curriculum.json): versioned curriculum/session manifest, source identities, unchanged approved requirements, lecturer contact reconciliation, proposed 160/40-hour allocations and pending decisions.
- [README.md](README.md): data contract, dependency evidence, counting rules, rationale, provenance and reproducible commands.
- [validate_curriculum.py](validate_curriculum.py): standard-library structural/accounting validator with nonzero failure exit status.
- [test_curriculum.py](../tests/test_curriculum.py): seven regression tests, including mutation cases and an LF checkout without the descriptor.
- [curriculum.yml](../.github/workflows/curriculum.yml): scoped CI with read-only repository permissions and no dependency installation.
- [Root README](../README.md): correct stale contact discrepancy and link to the model.
- This report: results, acceptance checklist and remaining decisions.

## Execution evidence

| Check | Result |
| --- | --- |
| Declared dependencies SETUP-01 and SETUP-02 | Both closed via GitHub API; supporting repository records present; no blocking prerequisite missing. |
| `python -s curriculum/validate_curriculum.py` | PASS: 16 sessions, 48 + 2 contact, 160 self-study, 40 assessment, 250 overall; source/LO/mapping/assessment checks pass. |
| `python -s curriculum/validate_traceability.py` | PASS in this Windows checkout, including descriptor identity. Existing validator is line-ending-sensitive; not added to the new Linux workflow. |
| `python -s references/validate_bibliography.py` | PASS in audit mode; no new academic references introduced. |
| `python -s -m unittest discover -s tests -v` | PASS: 29 tests (22 existing bibliography tests, 7 curriculum tests with multiple mutation subcases). |
| New Markdown local links and trailing whitespace | PASS. |
| `git diff --check` | PASS. |
| GitHub Actions execution | Not run remotely: no commit or push authorised. Equivalent curriculum commands pass locally, including LF/no-PDF regression fixture. |

Manual review compared the JSON to the existing audited transcription and CSV: all eight LO wordings, all nine block ranges, approved topic inventory, assessment weights/durations and capstone evidence components remain represented. Self-study activity descriptions retain postgraduate reasoning and reproducibility/ethical analysis without providing solutions. Full academic sufficiency is a professor judgment, not a test result.

## Acceptance checklist

- [x] Machine-readable curriculum and all 16 session records created.
- [x] Proposed self-study totals 160 hours; proposed assessment work totals 40 hours.
- [x] The 48 versus 50 difference is explicit and reconciled using SETUP-01, with no invented lecturer task or fourth assessment.
- [x] Approved outcomes, topic blocks and 60/30/10 weights preserved; new pedagogical allocations labelled proposed.
- [x] Inputs, provenance, decisions and reproducible steps documented; no fabricated citations.
- [x] No instructor solutions, exam keys, student records or dataset contents created; no private material added by this change.
- [x] Corresponding automated checks pass; local evidence and file links prepared here.
- [ ] Professor approves detailed academic allocations, especially presentation counting, workload realism and the proposed prerequisite bridge.
- [ ] Evidence posted to Issue #3 / a PR referencing #3. Deferred: no external messages sent and no PR created under the user's approval restriction.

## Unresolved decisions and limits

The assessment blueprint/dataset/rubrics, S16 timing and final timetable remain unresolved as in SETUP-02. The 2-hour university certification activity is outside lecturer scope; this proposal does not independently reclassify it within the 40 assessment hours. Presentation delivery is provisionally counted within S16 contact time only, pending professor confirmation. No proposal is asserted to be approved merely because dependencies are closed.

Source fidelity relies on SETUP-02's audited transcription and matching PDF hash; a fresh PDF extraction/render review was not performed because the current Python environment lacks PDF reader packages. The current Git index already tracks the descriptor, contrary to the historical audit's statement. This task leaves it untouched and does not establish publication permission; the professor should resolve that existing provenance/security question separately. No history changes or removal were attempted.

No commits, staging, pushes, PRs or issue comments were made. All implementation changes remain available locally for review.
