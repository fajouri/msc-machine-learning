# Microsoft 365 Copilot manual handoff contract

This is a reusable human handoff specification for Issue #8. It does not invoke Copilot, upload content or establish that the required Microsoft 365 licence/features exist. It becomes actionable only after an editable baseline PPTX is generated and checked in the supported runtime. That prerequisite is currently missing.

## Submission record

The lecturer records the task issue, session ID, baseline PPTX path and SHA-256, source JSON/Markdown paths and hashes, design-contract version, permitted scope, submission date and reviewer role. Include the academic/visual approval state and unresolved items. Only public-safe, rights-reviewed content may enter the handoff. Verify institutional account permissions and actual PowerPoint Copilot capabilities before uploading anything. No account integration is assumed.

Provide the checked baseline PPTX, completed lecture source, design system and the relevant public citation records. Do not submit the module descriptor, student records, instructor answers, exam keys or private correspondence. Stop if any input contains excluded content. Do not use a new empty presentation to disguise the missing baseline build.

## Reusable instruction to the human operator

Replace bracketed fields before use:

> Refine the supplied baseline presentation for [session ID] under Issue [number]. Apply the attached proposed M5 design contract [version] to improve spacing, alignment and visual hierarchy for a projector and Google Meet. Preserve slide IDs/order, exact approved outcome wording, academic claims, examples, notation, equations, data, citations, public notes and assessment statements. Keep charts, tables, diagrams and text editable. Preserve 16:9 dimensions and font-size baselines. Do not add sources, images, inferred results, solutions or university branding. Record unsupported features or proposed content changes for human review rather than silently changing them. Return an editable copy with a change log keyed by slide ID. Do not publish or replace the baseline.

## Return contract

Return a new PPTX file plus a UTF-8 Markdown change log identifying input/output hashes, date, operator role, application/version if available and actual features used. For each changed slide, list visual changes, content changes (or explicitly none), unsupported requirements, equation/figure conversion decisions and outstanding questions. Include the exact operator prompt and material deviations in the log, after checking for private information. Avoid claiming that Copilot preserves content automatically.

The human reviewer compares returned slides and notes to the frozen source, verifies every mathematical symbol, native chart data, figure editability, attribution and LO wording, and checks hidden slides/comments/embedded objects for excluded content. Reject or correct unapproved academic changes. Re-render every returned slide, inspect all images, run accessibility checks and repeat projector/Google Meet checks. Record actual results, reviewer role, date and file hashes. A returned file or automated pass is not professor approval.

## Failure and approval handling

If Copilot is unavailable, features are absent, fidelity is lost or source rights are unresolved, record the specific failure and stop the refinement handoff. Preserve the validated baseline; do not invent a completed refinement. Professor academic/visual approval and release approval remain separate, explicit decisions. No release, commit, upload to this public repository or issue closure follows automatically from this contract.
