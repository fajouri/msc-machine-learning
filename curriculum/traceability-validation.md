# SETUP-02 validation report

Audit date: 2026-10-21. Deliverables: [matrix](traceability-matrix.md), [separate findings/recommendations](traceability-gaps.md), [validator](validate_traceability.py). Professor review pending.

## Reproducible checks

From the repository root, run:

```powershell
python -s curriculum/validate_traceability.py
git diff --check
git status --short
```

The validator uses Python's standard library only. It checks baseline source hashes, all 16 session identifiers and modes, all 128 LO/session cells, exact preservation of existing M links, eight outcome records, all 24 LO/assessment cells, sixteen session-evidence rows, assessment constraint markers, finding/recommendation counts and local Markdown links. If the private/local descriptor is absent, its hash check explicitly reports SKIP; the audit cannot then be reauthenticated against the PDF. Structural checks cannot certify academic validity.

## Source and manual academic review

- Complete two-page descriptor inspected as extracted text and rendered page images. LO8 continues on page 2; no outcome is missing. Outcome transcription checked against the images, including scikit-learn, bias-variance and Q-learning hyphens.
- All nine approved topic blocks checked against the session evidence table without reordering. The OpenAI Gym omission is explicitly recorded as G05, not silently corrected in the source CSV.
- Exam 60% / 3 hours, capstone 30% / leaderboard plus technical report, and presentation 10% / 10 minutes preserved. Weights sum to 100%; no internal weight split, fourth assessment or new pass rule introduced.
- All eight outcome verbs reviewed: theoretical exam evidence is not treated as proof of implementation. Conditional capstone evidence for LO3–LO6 remains visibly conditional; LO8 documentation and presentation are traced across K/P.
- Approved requirements, lecturer operational decisions, existing CSV mappings and new pedagogical proposals are explicitly distinguished. Findings and recommendations are in separate sections/files from source requirements.
- No external references added or bibliographic claims made; the descriptor reading list was not revalidated or reproduced. No lesson materials, solutions, exam keys, student information or dataset content generated.
- Local descriptor was already untracked at the start. It is not staged, uploaded or modified. No commits, pushes, PRs or issue comments are made by this task.

## Results

Automated structural validation: **PASS**. Git whitespace check: **PASS**. Existing tracked files: **unchanged**. New curriculum deliverables: four files. Local PDF: still untracked and unchanged.

Manual audit conclusion: all LOs have existing session-level labels; full assessed attainment cannot yet be certified. Eleven findings and nine recommendations are recorded for professor review. No academic approval is implied by these validation results.
