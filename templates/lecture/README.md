# M5 lecture source contract

Runtime-independent implementation for [Issue #8](https://github.com/fajouri/msc-machine-learning/issues/8). These are proposed authoring conventions pending professor review, not institutional branding or completed lessons. AUTO-01 is present and its preflight and 19 tests passed before this work. The lecturer explicitly authorised this partial scope on 2026-10-21.

## Inputs and authority

Read [AGENTS.md](../../AGENTS.md), [production plan](../../docs/PRODUCTION_PLAN.md), [session map](../../curriculum/session-map.csv), [curriculum model](../../curriculum/curriculum.json), [public boundary](../../docs/course-builder-boundary.md) and [bibliography rules](../../references/README.md). The audited curriculum holds exact LO wording. This package does not copy the descriptor or change any outcomes, topics, hours or assessments. All design values and outline choices are pedagogical proposals. No academic citations, third-party figures or fabricated teaching results are introduced.

## Files and execution

- [design.json](design.json) and [design.schema.json](design.schema.json): versioned visual tokens and strict baseline contract.
- [lecture.schema.json](lecture.schema.json): structured lecture/Word source contract with required framing, slide types, notation, figures, citations and public notes.
- [lecture.template.json](lecture.template.json): reusable S01-labelled scaffold, with one example of each slide type. It contains TODO prompts, not an authored S01 lesson. The equation and figure slots do not imply a change to S01's approved topic scope.
- [lecture.template.md](lecture.template.md): deterministic, lossless view of the scaffold for editing or later Word conversion.
- [design-system.md](design-system.md): layout, academic, accessibility and Word mapping rules.
- [copilot-handoff.md](copilot-handoff.md): formal manual handoff and return contract.
- [validate.py](validate.py): read-only offline checks and optional Markdown stdout.

From repository root, using Python 3.13 and the standard library:

```powershell
python -s templates/lecture/validate.py
python -s -m unittest discover -s tests -p test_lecture_templates.py -v
python -s templates/lecture/validate.py --source path/to/lecture-source.json
python -s templates/lecture/validate.py --source path/to/lecture-source.json --markdown
python -s templates/lecture/validate.py --source path/to/lecture-source.json --complete
```

The last command is expected to fail on the supplied TODO scaffold. Exit 0 means the requested structural checks passed; exit 1 is invalid input, missing input or unresolved completion fields; invalid CLI arguments return 2. No packages, network, Office runtime or account access are needed. The script never writes a file. Save stdout as UTF-8 using the environment's encoding-aware file writer if needed.

Copy the JSON template to an authoring location and select the canonical session title, mode and complete LO list. Retain stable slide IDs, remove irrelevant example slide types and add slides as needed. There is no compulsory ten-slide lesson or teaching-time allocation. Copy exact approved LO wording into the outcomes slide and review it manually. Complete framing, mathematical reasoning, methodological comparison, reproducibility and ethical limits. Retain only public-safe notes; do not include answers to independent exercises or assessments. Generate the Markdown view from JSON after changes; JSON is authoritative when they disagree. Do not maintain two competing source versions.

AUTO-01 integration is deliberately non-invasive: use this outline when authoring its existing `lecture.md`. Keep structured working files outside `sessions/Sxx/` until a separately authorised package-contract change allows them. AUTO-01 rejects extra files in session packages. Its manifest, filenames and readiness rules remain unchanged. Run its normal snapshot/check workflow after intentional changes to existing package files.

## Schema and validation semantics

The JSON files declare JSON Schema draft 2020-12. The dependency-free validator implements only the keywords actually used: `type`, `properties`, `required`, `additionalProperties`, `items`, `minItems`, `uniqueItems`, `enum`, `const`, `minimum`, `pattern`, and the `$schema`, `title`, `description` annotations. Unsupported keywords fail when traversed; this is not a general JSON Schema engine or a schema meta-validator. All strings must additionally be nonblank. Booleans cannot substitute for integers; duplicate JSON keys and extra object fields fail. Baseline design tokens are constants to prevent silent design drift; deliberate changes require updating the contract and review evidence together.

Source checks enforce canonical session metadata, LO subset/coverage, unique slide IDs, equation/figure records for those slide types, figure provenance and bibliography source IDs. Empty citation lists are valid for original/template content. In `--complete` mode every declared citation must match `source_id`, `artifact`, `locator` and `attribution` in the existing citation ledger; drafting markers fail. Use the bibliography validator separately for record integrity, rights and release status. No parallel rights inventory is introduced.

These checks cannot detect unregistered citations, false provenance, semantic mathematical errors, confidential prose or inadequate explanations. Completion is a source check only, never publication readiness. Always inspect every artifact and reconcile every use with the bibliography ledger. Ng metadata remains unresolved and the existing bibliography release gate remains in force.

## Output stages and deferred capabilities

| Stage | Required evidence | Current status |
| --- | --- | --- |
| Source scaffold | Schemas, design tokens, paired JSON/Markdown, tests | Implemented; proposed design |
| Completed lesson source | Complete-mode validation, canonical wording and academic review, citation reconciliation | Future session authoring |
| Editable Word | Real `lecture.docx`, mapped styles, editable equations, public notes, rendered page inspection | Deferred |
| Editable slides | Real `slides.pptx`, 16:9 layouts, native editable figures, notes, citations, rendered slide inspection | Deferred |
| Copilot refinement | Human submission, returned files and change log, fidelity comparison | Deferred manual handoff |
| Release | Rights checks, binary inspection, accessibility and professor approval | Blocked |

This session has no `load_workspace_dependencies` tool or Artifact Session. Consequently it cannot obtain the supported runtime Node/Python executables, bundled `@oai/artifact-tool`, package directory or renderer binaries through the required loader. Installed skill text alone does not supply those capabilities. No replacement libraries or plugin modifications are authorised. The user explicitly excluded invoking the presentation skill for this continuation. No PPTX/DOCX is produced or claimed validated.

When that runtime is available, a separately authorised build must map these sources into editable DOCX/PPTX, render every page/slide, inspect images, fix defects, check native equations/figure editability and hidden content, and record runtime versions and actual results. Then perform projector and Google Meet legibility checks. The absence of binaries is a deferred deliverable, not a successful build or a substitute Markdown release. Keep Issue #8 open.
