# Issue #5 validation and PR #59 review report

Date: 2026-10-21. Scope: [Issue #5](https://github.com/fajouri/msc-machine-learning/issues/5), [PR #59](https://github.com/fajouri/msc-machine-learning/pull/59). Engineering corrections are ready for review; academic citation corrections and publication approval remain pending.

## Execution history

The original local Codex audit produced six files without committing, pushing or creating a PR. Those statements described that execution only. Subsequent GitHub commits and PR creation are evidenced by PR #59, with pre-review head `dd527990aa7f9347445b0af53b6257b85a906d82`. The current task explicitly authorises a review-fix commit, push to the existing branch and PR description update. No new PR, merge or issue closure is authorised by this report.

## Review findings and changed files

| Finding | Disposition | Evidence |
| --- | --- | --- |
| F1 | FIXED | [Validator](validate_bibliography.py) requires structured clearance plus evidence URL, nonblank permission source/scope/conditions/reviewer, valid YYYY-MM-DD date and explicit approved status. [Tests](../tests/test_bibliography.py) cover valid and invalid records. No real material is marked cleared. |
| F2 | FIXED | [Guide](README.md) and CLI state registered-entry-only coverage. Mandatory manual release checklist reuses the existing ledger. A narrowly scoped inventory-reconciliation follow-up is proposed, not created; no content scanner added. |
| F3 | FIXED | This report and the guide distinguish original local execution from subsequent commits and PR creation, retain open decisions, and reference #5/#59. PR description is updated as part of the authorised handoff. |
| F4 | FIXED | [Workflow](../.github/workflows/bibliography.yml) runs audit validation and tests on relevant PRs/master pushes with read-only permissions and no external Python packages. Publication-gate failure is tested as an expected result, not used to fail normal CI. |

Five changed files: the validator, guide, report, tests and new workflow. The five-source [bibliography](bibliography.json), [usage ledger](citation-usage.json), descriptor and curriculum are unchanged. Structured approval test records are synthetic fixtures only.

## Reproducible validation

Local environment: Python 3.13.2 on Windows. No prior repository Python-version declaration/workflow was found; focused CI uses Python 3.13. Commands run from repository root:

```powershell
python -s references/validate_bibliography.py
python -s -m unittest discover -s tests -p "test_bibliography.py" -v
python -s references/validate_bibliography.py --release
git diff --check
```

| Check | Actual result |
| --- | --- |
| Audit validator | PASS, exit 0. |
| Complete relevant unit suite | PASS, 22/22 tests. Includes missing evidence, permission scope, reviewer/approval, invalid dates, rejected approval, valid structured clearance, link-only/TODO, unknown sources, path escapes and private artifacts. |
| Publication gate | EXPECTED FAIL, exit 1, exactly `FAIL: ng2017: unresolved metadata/TODO prevents release`; no additional error or stderr. CLI regression verifies this. |
| Git whitespace check | PASS. |
| Scope/metadata comparison | Bibliography, ledger, descriptor and approved academic files unchanged from pre-review HEAD. |

Local checks exercise both workflow commands; hosted CI results are reported by PR #59's checks, rather than inferred from local success. No claim of hosted CI success is made in this committed report.

## Acceptance and unresolved decisions

Issue #5 provenance, scoped artifacts, tests and restricted-content boundaries are implemented. This report supplies evidence and file links for the existing PR description. Issue #5 remains open: professor review of Ng date/version and URL, future permissions and publication approval are unresolved. No closing keyword is used for #5.

The validator cannot discover omitted third-party materials, authenticate human reviewers or determine legal validity from URLs or populated records. Manual coverage review and human approval remain mandatory. Four references retain verified metadata; Ng retains its explicit TODO and no replacement date is invented. Institutional subscriptions are unverified. No book content, instructor answers, private correspondence or student data are introduced. No rights-holder messages were sent.
