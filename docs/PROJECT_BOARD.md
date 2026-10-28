# Project board — MSc Machine Learning

This file is the lightweight, repository-based project board. Update the **Status** column whenever work changes. The curriculum source of truth remains `curriculum/session-map.csv` and `docs/PRODUCTION_PLAN.md`.

## Workflow

- Work directly on **`main`**.
- No feature branches and no pull requests for routine course-material production.
- Take one task at a time; keep commits small and descriptive.
- Before producing a session, read `AGENTS.md`, `docs/PRODUCTION_PLAN.md`, `curriculum/session-map.csv`, and `skills/msc-course-builder/SKILL.md`.
- Produce sessions in the order shown below unless a dependency or the lecturer changes the priority.
- Update this board in the same commit as meaningful task progress.
- A task is not **Done** merely because files exist: run applicable checks and record limitations. Lecturer approval and publication are separate release gates.
- This repository is public. Never commit student records, marks, instructor solutions, private exam questions/keys, credentials, or other confidential material.

## Status definitions

| Status | Meaning |
| --- | --- |
| Backlog | Not started. |
| In progress | Work has begun; deliverables or checks remain. |
| Blocked | Cannot proceed until a named dependency or decision is resolved. |
| Review | Draft is complete and awaits academic/content/quality review. |
| Done | Required artifacts and checks are complete; any required approval is recorded. |

## Project tasks

| ID | Task | Scope / completion criteria | Status | Notes |
| --- | --- | --- | --- | --- |
| SETUP-01 | Confirm course constraints | Preserve approved outcomes, assessment weights, workload, delivery assumptions, and public-repository safety boundary. | Done | Decisions and open clarifications are recorded in `docs/PRODUCTION_PLAN.md`. |
| SETUP-02 | Maintain curriculum and session plan | Keep the 16-session map aligned with the approved descriptor and traceability evidence. | In progress | Use `curriculum/session-map.csv` and the curriculum validation scripts as sources of truth. |
| SETUP-03 | Simplify repository workflow | Use `main` as the working branch; track tasks in this document; remove routine PR requirements. | In progress | Update instructions and links to point to this board. |
| S01 | ML foundations and Python stack | Session brief, 180-minute run sheet, lecture, exercises, student lab, references, manifest/completion evidence, and applicable validation. | In progress | Existing draft files are present; verify completeness and quality before marking Done. |
| S02 | Data wrangling and EDA | Complete the student-facing session package and validate it against the session map. | Backlog | Campus session. |
| S03 | Regression I | Complete the student-facing session package and validate it against the session map. | Backlog | Online session. |
| S04 | Regression II | Complete the student-facing session package and validate it against the session map. | Backlog | Campus session. |
| S05 | Classification I | Complete the student-facing session package and validate it against the session map. | Backlog | Online session. |
| S06 | Classification II | Complete the student-facing session package and validate it against the session map. | Backlog | Campus session. |
| S07 | Evaluation I | Complete the student-facing session package and validate it against the session map. | Backlog | Online session. |
| S08 | Optimisation II | Complete the student-facing session package and validate it against the session map. | Backlog | Campus session. |
| S09 | Unsupervised I | Complete the student-facing session package and validate it against the session map. | Backlog | Online session. |
| S10 | Unsupervised II | Complete the student-facing session package and validate it against the session map. | Backlog | Campus session. |
| S11 | Reinforcement learning I | Complete the student-facing session package and validate it against the session map. | Backlog | Online session. |
| S12 | Reinforcement learning II | Complete the student-facing session package and validate it against the session map. | Backlog | Campus session. |
| S13 | Deep learning I | Complete the student-facing session package and validate it against the session map. | Backlog | Online session. |
| S14 | Deep learning II | Complete the student-facing session package and validate it against the session map. | Backlog | Online session. |
| S15 | Ethics, fairness and explainability | Complete the student-facing session package and validate it against the session map. | Backlog | Online session. |
| S16 | Capstone presentations and exam preparation | Complete session plan, student-facing materials, presentation timing, synthesis, and exam-preparation guidance. | Backlog | Campus session; verify the 180-minute capacity and university timetable. |
| QA-01 | Validate all session packages | Run applicable curriculum/session checks; verify notebooks, citations, learning-outcome alignment, accessibility and student-safe content. | Backlog | Track concrete failures as notes or separate tasks if they block delivery. |
| RELEASE-01 | Final academic review and publication | Lecturer reviews academic quality, copyright/attribution, assessment validity, and release readiness before student publication. | Backlog | Do not equate automated validation with lecturer approval. |

## Session package checklist

For each S01–S16 task, use the applicable requirements in `docs/PRODUCTION_PLAN.md` and the course-builder skill. At minimum, track:

- [ ] Session brief with learning-outcome mapping and a 180-minute run sheet.
- [ ] Lecture source with explanations, examples, and student-safe instructor notes.
- [ ] Exercises and extension activity.
- [ ] Reproducible student lab/notebook with no embedded answers to independent tasks.
- [ ] Verified references and citation provenance; unresolved citations are explicit TODOs.
- [ ] Completion/manifest evidence and applicable automated checks.
- [ ] Online/campus adaptations, accessibility, privacy, licensing, and release checks as relevant.

Instructor solutions and live exam keys must remain outside this public repository.

## Updating the board

When starting or finishing a task, edit its **Status** and **Notes** cells in this file. Keep notes factual: name the artifact, check, blocker, or decision. Do not mark a task Done without evidence.
