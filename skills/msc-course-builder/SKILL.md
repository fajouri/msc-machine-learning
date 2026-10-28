---
name: msc-course-builder
description: Build or revise a complete M5 Machine Learning teaching session with lightweight, professor-led workflow, no required board, issue or PR.
---

# M5 Machine Learning — simple course builder

Use this skill for preparing one M5 session (S01–S16) at a time. Read `AGENTS.md`, `course-plan.md`, `COURSE_STATUS.md`, the existing files under `sessions/Sxx/` and the detailed curriculum mapping when exact outcome verification is needed.

## Method

1. Identify the session and the exact approved learning outcomes and coverage. Do not invent institutional requirements or alter the approved 60/30/10 assessment scheme.
2. Check existing session content first. Preserve useful material; avoid duplicating or replacing it unnecessarily.
3. Prepare a clear `README.md`, detailed `lecture.md`, slide source `slides.md` and editable `slides.pptx` if generation is supported, `exercises.md`, and a runnable `student-lab.ipynb` when applicable. Follow the existing naming when maintaining S01.
4. Make the session teachable in 180 minutes with explanations, examples, demonstrations and student participation. Include accessible, reproducible material, linked references and lecturer guidance within normal teaching files.
5. Check correctness and learning outcome coverage. Execute the notebook if the environment allows; inspect slide readability and factual claims. Explain honestly when a check or artifact cannot be completed.
6. Update `COURSE_STATUS.md` with verified status. Summarize changed files and open academic decisions.

## Workflow rules

- **No required GitHub Project Board, issue, PR, review, feature branch, manifest, or GitHub Actions gate.**
- Work directly on `master` when explicitly instructed to commit/push there. An optional issue or PR may be used only if the professor chooses to.
- Older templates in `skills/msc-course-builder/assets/`, the package helper and historical evidence files remain optional references. They must not block ordinary session creation.
- Never claim academic approval merely because code validation passes.
- This is a public repository: do not include identifiable student records, grades, exam keys, private instructor solutions, credentials or unlicensed material.
