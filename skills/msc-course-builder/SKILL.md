---
name: msc-course-builder
description: Prepare or revise one M5 MSc Machine Learning session from the approved curriculum, producing student-facing lesson sources, labs, artifact manifests and evidence for professor review. Use for M5 session production, not grading, exam keys or student records.
---

# M5 course builder

Work from the repository root. Support one atomic GitHub issue and one session at a time. This is an authoring workflow, not an unattended content generator or publisher. Keep the maintained location at `skills/msc-course-builder/`; the user can ask Codex to read this file explicitly without installing it globally.

## Establish scope before writing

1. Read `AGENTS.md`, `docs/PRODUCTION_PLAN.md` and `curriculum/session-map.csv` first. Then read the full task issue/comments, its declared dependencies, `curriculum/curriculum.json`, `curriculum/traceability-matrix.md`, relevant gaps, `docs/delivery-plan.md`, and [the public-output decision](../../docs/course-builder-boundary.md). Issue closure is not academic approval; verify artifacts too.
2. Select exactly S01–S16 from the request. Ask only if selection or scope cannot be inferred. Preserve the manifest's title, proposed mode, block and exact LO wording. Additional pedagogical links remain proposals. Do not change outcomes, topic blocks, 60/30/10 weights or workload budgets. The 48 teaching hours plus two university certification hours stay distinct from the three-hour M5 examination.
3. Run the read-only preflight below. Missing sources, changed source identities, failing prerequisite validators or unfulfilled task dependencies stop dependent work. Report the prerequisite; do not invent replacements or silently refresh hashes. The hash-pinned SETUP-02 transcription may be used if the PDF is absent under the existing curriculum contract. Never upload the descriptor as a session artifact.

```powershell
python -s skills/msc-course-builder/scripts/session_package.py plan --session S01 --issue 13
```

Replace the example issue/session with the actual task. The issue number records provenance, not API verification: read GitHub yourself. `plan` prints inputs, source hashes and output paths without writing. Python standard library only; run `--help` for commands.

## Draft in stages

Read [the package contract](references/package-contract.md). Use `init` with the same arguments to create `sessions/S01/`; it refuses an existing destination. Default `--package source` creates Markdown and a notebook skeleton. Use `--package full` only when DOCX/PPTX are requested and their prerequisites are available. The helper does not render them.

1. **Plan:** complete `brief.md` with exact LO mapping, prerequisite reasoning, a 180-minute run sheet and both delivery adaptations. Use the delivery plan for participation, outages, accessibility and S16 capacity. Activities remain formative unless separately approved.
2. **Author:** complete `lecture.md`, `exercises.md`, `references.md` and `student-lab.ipynb`. Explain assumptions, notation, derivations and interpretation at MQF Level 7. Include methodological alternatives, uncertainty, leakage prevention and ethical limitations. Teaching examples may be worked; independent exercise/assessment answers must not be embedded. Speaker notes must be safe for students to read.
3. **Build:** for a full package, create editable `lecture.docx` and `slides.pptx` from reviewed source. Use available document/presentation workflows and AUTO-02 conventions once implemented; do not invent an institutional template. Preserve equations/citations. If tools or declared prerequisites are absent, report affected outputs as missing. Microsoft 365 Copilot is a human handoff, never an assumed integration or completed refinement.
4. **Verify:** complete the contract's reproducibility and manual checks. Record actual commands, versions, results and limitations in `completion.md`. Run `snapshot` after intentional edits to record current hashes, then `check`. Run `check --review-ready` only once every requested artifact exists and drafting TODOs are resolved. Structural success is not academic, visual, copyright or release approval.

## Reference and security rules

Use `references/bibliography.json` and `references/README.md`. Register each teaching-artifact use in `references/citation-usage.json` with verified locator, attribution and rights status. Never guess chapters, pages, editions, DOIs or dates. Unresolved items remain TODO in drafts and block readiness/release. The existing Ng metadata TODO permits audit work but blocks the bibliography release gate; do not guess its year or omit it from the approved reading list.

This is a public-only workflow. Exclude student names, IDs, submissions, final marks, credentials, private correspondence, instructor solutions, live exam questions and keys. No private repo is required or created. An ignored folder is not secure storage. Stop requests requiring those outputs before generating sensitive content, including in logs, manifests, notebook metadata or slide notes. Use synthetic/non-identifying examples and appropriately licensed data.

## Complete and hand off

Return artifact links, issue/session/scope, validation evidence, missing outputs, unresolved decisions and acceptance status. Distinguish a source package from a complete session package. Claim execution, rendering, approval or release only when evidenced. No commit, push, PR, issue comment or publication is implied; follow the user's authorization. A later authorised PR must reference its task issue and attach evidence.
