# AUTO-02 source validation and acceptance

[Issue #8](https://github.com/fajouri/msc-machine-learning/issues/8), 2026-10-21. **Partial implementation only; keep the issue open.** The lecturer explicitly limited this continuation to runtime-independent design, schemas, templates, handoff and validation. No presentation skill invocation, replacement library installation, plugin change or Office generation was performed in this continuation.

## Prerequisites and provenance

Read AGENTS.md, the production plan/session map, the full issue, AUTO-01's skill/assets/package contract, boundary decision, validation report, curriculum model and bibliography rules. AUTO-01 (#7) was verified closed with no comments in the prior prerequisite check; its local preflight and all 19 tests passed. Issue #8 was refreshed through GitHub API and remains open with AUTO-01 as its sole declared dependency. The user's explicit partial-scope instruction resolves the previous stop for this source-only work, without asserting that the artifact runtime now exists.

The canonical curriculum and approved descriptor transcription remain unchanged. The source template uses canonical S01 metadata solely as a concrete reusable scaffold; it is not an approved S01 lesson. All visual values, Word mappings and slide-type choices are proposed. No new academic sources or borrowed figures are used, so the existing citation ledger is unchanged. The tracked descriptor is neither copied nor uploaded.

## Changed files

| Files | Purpose |
| --- | --- |
| [Guide](../templates/lecture/README.md) | Scope, provenance, contracts, commands, AUTO-01 integration and exact runtime limitation |
| [Design tokens](../templates/lecture/design.json), [schema](../templates/lecture/design.schema.json), [design rules](../templates/lecture/design-system.md) | 16:9 baseline, mathematical/citation/accessibility rules, editable figures and Word style mapping |
| [Lecture schema](../templates/lecture/lecture.schema.json) | Shared structured Markdown/Word source and slide/notes contract |
| [JSON scaffold](../templates/lecture/lecture.template.json), [Markdown scaffold](../templates/lecture/lecture.template.md) | Ten slide-type examples with explicit TODOs and public notes |
| [Copilot handoff](../templates/lecture/copilot-handoff.md) | Human submission, constrained prompt, return evidence, fidelity checks and failure handling |
| [Validator](../templates/lecture/validate.py) | Standard-library read-only schema/source checks and Markdown stdout |
| [Tests](../tests/test_lecture_templates.py) | Positive and mutation tests, malformed input and CLI checks |
| [CI](../.github/workflows/lecture-templates.yml) | Read-only source validation/tests; no dependency installation |
| [Root README](../README.md), this report | Navigation and acceptance evidence |

## Execution evidence

Local environment: Windows, Python 3.13.2. Run from repository root:

```powershell
python -s templates/lecture/validate.py
python -s -m unittest discover -s tests -p test_lecture_templates.py -v
python -s -m unittest discover -s tests -v
python -s curriculum/validate_traceability.py
python -s references/validate_bibliography.py
git diff --check
```

| Check | Result |
| --- | --- |
| Source bundle | PASS: both schemas, canonical metadata, all slide types, JSON/Markdown equality |
| New tests | PASS: 17 tests covering every required object field, unknown fields, invalid types/constants, malformed JSON/duplicate keys, all 16 session selections, metadata/LO drift, duplicate slide IDs, equation/figure requirements, third-party citations, missing registry/ledger entries, draft/completion separation, Markdown fidelity, contrast/geometry and CLI failures |
| Entire suite | PASS: 70 tests, no skips; includes all 19 AUTO-01 tests and existing curriculum/delivery/bibliography regressions |
| Traceability | PASS, including unchanged local descriptor identity |
| Bibliography audit | PASS; existing regression confirms the release gate still fails on unresolved Ng metadata |
| Whitespace and local Markdown links | PASS after final documentation changes |
| Source content inspection | Public TODO scaffold only; no answers, student records, copied academic content or binary outputs |
| Hosted CI | Not run; nothing pushed |
| PPTX/DOCX, rendering and device tests | NOT RUN; deferred, not passed |

The completed-source success test uses a synthetic fixture to exercise structure; it is not an academically completed lecture. The validator cannot establish semantic correctness, citation coverage, confidentiality or visual quality. Proposed contrast tokens pass numeric checks; actual display contrast and font rendering remain untested.

## Acceptance status and outstanding decisions

- [x] All seven requested runtime-independent work items implemented: design, source schemas/templates, detailed academic/visual conventions, manual Copilot contract, offline validation, explicit deferral and schema/template tests.
- [x] No fabricated citations or changes to approved outcomes, topic blocks, hours or assessment weights.
- [x] Public student/instructor boundary preserved in authored files; future content requires manual inspection.
- [x] Source-only acceptance tests pass and local evidence/file links are prepared.
- [ ] Full Issue #8 editable Word/PPTX artifacts and baseline styles instantiated in Office files.
- [ ] Rendered page/slide visual QA, native editability, accessibility, projector and Google Meet checks.
- [ ] Professor approval of proposed academic/visual choices and any future lesson/release.
- [ ] Verification evidence posted to GitHub and a relevant PR references #8, after user approval.

The unavailable capability is `load_workspace_dependencies` (supported runtime executable/package/renderer discovery), with no Artifact Session alternative exposed. The supported artifact build/renderer environment therefore cannot be established. Resume binary generation only when available and authorised; do not install substitutes. The handoff remains a specification until a checked baseline exists and a human verifies their actual Microsoft 365 capabilities.

Further decisions: professor acceptance of typography/layout and Word mapping, font availability during build, actual Copilot licence/features, and existing bibliography/release decisions including Ng metadata. No broad assessment or curriculum decision is made here. No commit, push, PR, issue comment, closure or publication has been performed.
