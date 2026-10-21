# M5 Machine Learning — MSc Computer Science

Course production workspace for Ascencia Malta MSc Computer Science, MQF Level 7 (10 ECTS).

**Status:** Planning; no teaching materials generated yet.

- 16 × 3-hour sessions; provisional delivery: 9 synchronous online, 7 campus labs.
- Approved descriptor: 50 contact hours, 160 self-study hours, 40 assessment hours. SETUP-01 reconciles 48 teaching hours plus a separate two-hour university-administered certification exam; no lecturer deliverable is required for those two hours.
- Assessments: written examination 60%, Kaggle capstone 30%, presentation 10%.
- LO1–LO8 govern all teaching artifacts.

See the [curriculum data model and proposed workload allocation](curriculum/README.md) for the 250-hour accounting, source provenance, validation commands and pending academic decisions.

See the [proposed hybrid delivery and contingency plan](docs/delivery-plan.md) for all 16 sessions, accessibility, campus logistics, outage recovery and S16 timing. [Validation evidence](docs/delivery-validation.md) distinguishes automated checks from pending professor approval and delivery readiness.

## Production workflow

1. Confirm descriptor, hybrid approval, academic policies and source licenses.
2. Implement skill and templates using Codex; use GitHub Copilot as an optional coding assistant.
3. Produce two pilots (S01 online / S02 campus) before the remainder.
4. Build each academic package with Codex; refine slide design in Microsoft 365 Copilot where supported.
5. Validate notebooks, slide artifacts, bibliography, accessibility and outcome alignment.
6. Publish approved student artifacts only. Never publish exam keys, private instructor solutions, unlicensed books or student data.

## Important security notice

This repository is **public**. The lecturer has decided that no private repository will be used. The [course-builder boundary](docs/course-builder-boundary.md) excludes student names, marks, submissions, instructor solutions and exam keys from its outputs. GitHub history cannot be relied on to conceal material after removal.

## Reusable session production skill

Ask Codex to use [msc-course-builder](skills/msc-course-builder/SKILL.md) for one session and task issue. It provides staged templates, source preflight, output manifests and review checks. It does not publish or generate instructor-only material. See the [Issue #7 validation report](docs/course-builder-validation.md) for scope, reproducible tests and remaining release decisions.

See `docs/PRODUCTION_PLAN.md`, `curriculum/session-map.csv`, and GitHub Issues for production tasks. Project board: https://github.com/users/fajouri/projects/6/views/1

## Lecture source templates

[AUTO-02 source contracts](templates/lecture/README.md) provide proposed 16:9 design rules, structured JSON/Markdown outlines, a Word style mapping, a manual PowerPoint Copilot handoff and dependency-free validation. PPTX/DOCX generation and visual QA remain deferred because the supported artifact runtime is unavailable. See the [Issue #8 validation report](docs/lecture-templates-validation.md); the issue remains open.
