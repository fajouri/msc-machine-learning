# SETUP-05 bibliography and reuse audit

[Issue #5](https://github.com/fajouri/msc-machine-learning/issues/5), audited 2026-10-21. Scope: the five readings in the approved M5 descriptor, bibliographic provenance, reuse decisions and future citation tracking. No course material or replacement reading list is produced.

## Dependency and authority

Declared dependency SETUP-02 ([#2](https://github.com/fajouri/msc-machine-learning/issues/2)) was closed at 2026-10-21T12:56:18Z, has no comments, and its artifacts are present in repository commit `fec7671`. `python -s curriculum/validate_traceability.py` passes, including the descriptor hash check. This is sufficient to proceed with the bibliography audit. The prior artifacts still label pedagogical recommendations as pending review: closure is not treated as approval to amend outcomes or assessments.

Inputs: `AGENTS.md`, `docs/PRODUCTION_PLAN.md`, `curriculum/session-map.csv`, the three traceability documents and validator, and the full Issue #5 body (no comments). The full two-page descriptor was read and visually inspected in SETUP-02 in this conversation; its unchanged SHA-256 is `BDC82A68602E666E13B869DE83279241C85D81A307A7F770742F245690F40660`. Its p. 2 reading list supplies the five exact baseline citations in [bibliography.json](bibliography.json). Core/supplementary status is preserved. Metadata normalisation is kept separate from descriptor wording. No descriptor or approved academic requirement is edited.

## Findings and evidence

All links below were inspected via web search/open on the audit date. These are primary publisher/author sources, except the legacy URL, which is inspected only to flag its changed content. Evidence summaries, rather than copied pages or book content, are stored in the registry. Verification concerns named fields, not the reliability of every argument or example in a book.

| Citation key | Bibliographic finding | Reading access and reuse decision |
| --- | --- | --- |
| geron2022 | Author, title, third edition and 2022 confirmed by [O'Reilly](https://www.oreilly.com/library/view/hands-on-machine-learning/9781098125967/). | Publisher access; link and cite. Book extracts/figures require asset-specific clearance under the [publisher permissions route](https://www.oreilly.com/rights/). |
| goodfellow2016 | Authors, title, MIT Press and 2016 confirmed by the [author citation entry](https://www.deeplearningbook.org/). | Free HTML reading; FAQ restricts distribution of easily copied formats. Do not mirror or convert the book for repository distribution. |
| hastie2009 | Authors, subtitle, second edition, 2009 and DOI confirmed by [Springer](https://doi.org/10.1007/978-0-387-84858-7). | [Author download page](https://hastie.su.domains/ElemStatLearn/main.html) provides a corrected 2017 printing of the 2009 edition. Availability is not evidence of general adaptation/redistribution rights. Link only pending asset-specific clearance. |
| provost2013 | Authors, title, O'Reilly and 2013 confirmed by [publisher listing](https://www.oreilly.com/library/view/data-science-for/9781449374273/). | Publisher access; same permissions route as Géron. Institutional subscriptions are not verified. |
| ng2017 | [Official page](https://info.deeplearning.ai/machine-learning-yearning-book) confirms title/author, not 2017 or an exact version. **TODO: date/version verification.** Key retains descriptor year, not a verified date. | Official ebook access offered, but no general reuse grant verified. [Legacy URL](https://www.mlyearning.org/) now displays broader AI/commercial content; do not use it as evidence of author provenance. **TODO: professor review of URL correction.** |

No ISBN or edition number is guessed from a URL. Null metadata fields mean not established in this audit, not that a value does not exist. Ng's year remains null in verified metadata and 2017 in the immutable descriptor transcription. No unverified replacement date is offered.

The [Géron companion repository licence](https://github.com/ageron/handson-ml3/blob/main/LICENSE) is Apache-2.0. This does not licence the printed book or automatically clear every dataset/image inside the repository. Before importing any companion asset, inspect its own notices at a pinned revision and record licence/notice obligations. No companion content is imported here. Licences found on third-party mirrors or translations are not used as authority for the English books.

## Citation and reuse tracking

[citation-usage.json](citation-usage.json) is intentionally empty: there are no lesson artifacts in this issue. The bibliography audit's citations are tracked by each source's metadata/rights URLs and dated audit record; the usage ledger is for subsequent teaching artifacts. Do not manufacture chapter/page assignments or claim planned readings have been taught.

For each future use, add an object to `uses` with these fields:

| Field | Required meaning |
| --- | --- |
| source_id | Stable key from bibliography.json. |
| artifact | Repository-relative existing student artifact path; instructor-only work stays in private storage and must not be listed with sensitive details here. |
| locator | Exact page/section/figure or code revision and path checked in the cited edition. For a whole-book reading link, use `whole work`. |
| kind | `link`, `paraphrase`, `quotation`, `figure`, or `code`. |
| attribution | Human-readable citation to appear beside the use, including locator where relevant. |
| rights_status | `link_only`, `TODO`, or `cleared`. |
| permission_evidence | Public evidence URL for clearance (licence or public permission reference); keep private correspondence outside this repository. Empty only for link-only or pending uses. |
| review_note | Reviewer/date and asset-specific conditions, or an explicit TODO. |
| clearance | Structured human approval record required only when `rights_status` is `cleared`; fields below. |

For a `cleared` use, retain `permission_evidence` as the public evidence URL and provide a `clearance` object with all of the following fields. A URL alone is insufficient. Do not publish private correspondence or personal details; use an authorised reviewer role and a public permission reference where appropriate.

| Clearance field | Validation and meaning |
| --- | --- |
| permission_source | Nonblank string identifying the rights holder or licence issuer. |
| permitted_use | Nonblank string describing the specific asset, proposed reuse, modifications and distribution destination covered. |
| conditions | Nonblank string naming the applicable licence/permission and its conditions, including attribution and modification limits. Explicitly record if there are no additional conditions. |
| reviewer | Nonblank reviewer identity or accountable institutional role. |
| review_date | Valid calendar date in exactly `YYYY-MM-DD` format. |
| approval_status | Exactly `approved`; pending, rejected, missing or boolean values cannot support `cleared`. |

Human approval remains mandatory. These checks establish that an approval record is present and structured; they cannot authenticate the reviewer, verify evidence, interpret licence scope or determine legal validity. `TODO` and `link_only` entries do not require a clearance object. Pending permissions remain `TODO` until reviewed and explicitly approved.

Use original explanations and examples with scholarly attribution. Citation is not clearance to copy or closely adapt protected expression. For quotations, figures and code, record applicable licence/permission, scope, attribution and modification requirements before release. A public educational repository is a distribution destination; access through a library does not itself establish reuse permission. `link_only` is this project's conservative handling decision, not a legal assertion that no exception could ever apply. No blanket fair-use or classroom exemption is assumed.

Use the validator's `--release` mode to reject unresolved metadata and pending rights before publication. This intentionally fails today on Ng's unresolved reference. Audit mode permits explicit TODOs, allowing an honest audit to be complete without inventing missing facts. Tests validate record integrity and release gates; they cannot authenticate a rights holder or establish legal sufficiency. Professor review remains required for publication decisions.

### Mandatory manual release coverage checklist

`--release` validates registered entries only. Successful execution does **not** establish complete coverage of all reused third-party materials in teaching artifacts: omitted citations cannot be detected by this validator. Repository inspection for PR #59 found no separate asset manifest or tracking convention; reuse `citation-usage.json` rather than introducing a parallel inventory system.

Before every release, the human reviewer must complete and record this checklist in the release validation report, identifying the artifact paths/revisions reviewed, reviewer role, date, findings and final approval:

- [ ] Enumerate all artifacts in the release, including embedded slides/images, notebooks and outputs, PDFs, code, datasets and supporting downloads.
- [ ] Inspect each artifact for third-party quotations, paraphrases, figures, code and other reused material, including content missing from the ledger.
- [ ] Reconcile each use with `citation-usage.json`, confirming source, exact locator, destination artifact and visible attribution. Unrepresentable or unregistered uses block release until recorded and reviewed; do not mislabel them to pass validation.
- [ ] Check each clearance against the actual use and destination, licence conditions and modifications. Verify permission evidence and human approval rather than relying on URL syntax.
- [ ] Confirm restricted content, instructor answers and private correspondence are excluded; record any genuinely empty reuse inventory as a reviewed finding, not an assumption.
- [ ] Resolve discrepancies, run `--release`, and record professor approval separately. Both automated checks and this manual review must pass before publication.

Proposed follow-up issue (not created): **Reconcile a pilot session's declared asset inventory with citation usage.** Limit the pilot to one session's explicit artifact list and references to `citation-usage.json`; report missing/orphaned registrations and require reviewer sign-off. Acceptance should include fixtures for omitted registrations and explicitly original assets. This can check inventory consistency, not discover all third-party content or prove legal validity. A reliable general content scanner is outside Issue #5; manual inspection remains required.

### Continuous integration

[Bibliography audit workflow](../.github/workflows/bibliography.yml) runs the audit validator and unit tests on relevant pull requests and pushes to `master`, with only `contents: read` permissions. Repository inspection found no pre-existing workflow or declared Python version; this focused workflow uses Python 3.13, matching the locally validated 3.13.2 environment, without imposing a version on future teaching notebooks. It uses standard-library tests and installs no external Python packages. Action usage follows the official [setup-python v5 documentation](https://github.com/actions/setup-python/blob/v5/README.md) and [checkout v4 documentation](https://github.com/actions/checkout/blob/v4/README.md).

CI does not run the blocked publication gate as a required successful command. A regression test checks that `--release` returns exit code 1 specifically for Ng's unresolved metadata; this expected failure makes the test pass. Update that regression only when the underlying academic decision is legitimately resolved. Passing CI is not publication approval.

## Reproduction and outstanding decisions

```powershell
gh api repos/fajouri/msc-machine-learning/issues/5
gh api repos/fajouri/msc-machine-learning/issues/2
python -s references/validate_bibliography.py
python -s -m unittest discover -s tests -p 'test_bibliography.py' -v
python -s curriculum/validate_traceability.py
git diff --check
```

Revisit each primary URL, check the named metadata and rights statements, update evidence/date if changed, then run the offline checks. No book downloads or network calls occur in tests. Re-run `--release` only when preparing publication; current expected result is a nonzero exit with the Ng TODO.

Outstanding: professor decides the Ng citation correction after exact-version verification, confirms any institutional reading access, and approves any future asset reuse. These are recorded audit findings rather than missing prerequisites to performing SETUP-05.

Execution history: the original local Codex audit stopped without committing, pushing or creating a PR. Subsequent GitHub commits brought the artifacts to [PR #59](https://github.com/fajouri/msc-machine-learning/pull/59), whose pre-review head was `dd527990aa7f9347445b0af53b6257b85a906d82`. The review-fix task authorises committing/pushing corrections and updating that existing PR for [Issue #5](https://github.com/fajouri/msc-machine-learning/issues/5). This engineering workflow does not establish professor approval or copyright clearance. No rights-holder requests were sent.
