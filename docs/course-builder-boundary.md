# Public-only scope for AUTO-01

Decision recorded on 2026-10-21 for [Issue #7](https://github.com/fajouri/msc-machine-learning/issues/7).

The lecturer confirmed in the implementation conversation that this repository remains public, no private repository will be used, and student names and final marks must be kept out. This agrees with the [SETUP-06 comment](https://github.com/fajouri/msc-machine-learning/issues/6#issuecomment-6317983264). The lecturer then instructed implementation of #7 to proceed.

For this skill, the consequence is a **public student-output workflow**. No private store is assumed, provisioned or required. Instructor solutions, exam questions/keys, student submissions, names, IDs, marks, credentials and private correspondence are excluded from files, manifests and logs. Public instructional examples and public-safe presentation notes are permitted; independent exercise/assessment answers are not. If a future task requires excluded outputs, stop that part before generation and obtain a separate handling decision. This does not authorise publication of confidential material.

Earlier planning references to private storage are conditional requirements for handling instructor-only work; they do not require this skill to create such work. The approved descriptor, outcomes, assessments and source hashes remain unchanged. This records the user's decision for AUTO-01, not completion of a repository-wide security/history audit or a rewrite of SETUP-06.

The helper writes only enumerated student artifact filenames inside `sessions/Sxx/`. It rejects path redirection, existing destinations and unlisted files. It does not stage, commit, upload, export or publish. `.gitignore` is only an accidental-commit aid; tracked material remains in history. The existing tracked descriptor is not copied into packages, and its publication permission remains separately unresolved.

Before later publication, inspect the actual diff and each artifact (including notebook output/metadata, embedded objects and speaker notes), verify rights/citation coverage, and obtain professor release approval. Neither a filename allowlist nor a hash can detect all sensitive information. No broad Git history or hosting change is part of #7.
