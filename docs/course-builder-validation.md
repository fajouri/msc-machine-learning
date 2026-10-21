# AUTO-01 validation and acceptance report

[Issue #7](https://github.com/fajouri/msc-machine-learning/issues/7), implemented locally on 2026-10-21. Engineering scope: reusable session-production skill, templates, stage/inventory helper and tests. No actual session lesson, private repository, assessment package or publishing pipeline is created.

## Dependencies and decisions

Read the full issue (zero comments), AGENTS.md, production plan, session map, curriculum contract, descriptor traceability/gaps, delivery plan/validation and bibliography rules. GitHub API verification on 2026-10-21 found SETUP-02 through SETUP-06 closed. SETUP-02–05 artifacts are present and their relevant structural checks pass. Closed issues do not imply professor approval of their remaining pedagogical proposals.

The initial prerequisite check stopped because SETUP-06 did not establish private storage. The lecturer then explicitly confirmed that no private repository will be used, excluded student names/final marks, and instructed #7 to proceed. The [public-only decision](course-builder-boundary.md) records the resulting scope: no instructor-only output generation and no private-store prerequisite. It agrees with the existing [#6 comment](https://github.com/fajouri/msc-machine-learning/issues/6#issuecomment-6317983264). This does not assert that every original SETUP-06 security/history task was implemented; it resolves the dependency for this public-only skill under the user's explicit instruction.

The existing audited descriptor transcription is used; the local descriptor identity passes the existing traceability check. No new visual PDF audit or source-publication permission is claimed. Approved files and their hashes are unchanged. OpenAI's [skill authoring documentation](https://learn.chatgpt.com/docs/build-skills), retrieved 2026-10-21, and the local skill-creator guidance informed the SKILL.md plus supporting-resource structure. No new academic bibliography entry is introduced.

## Changed files

| Path | Purpose |
| --- | --- |
| [SKILL.md](../skills/msc-course-builder/SKILL.md) | Session/task selection, source checks, academic/reference rules, staged authoring, fail-fast conditions and handoff |
| [Package contract](../skills/msc-course-builder/references/package-contract.md) | Commands, manifest semantics, reproducibility and manual acceptance requirements |
| [Session helper](../skills/msc-course-builder/scripts/session_package.py) | Read-only plan, non-overwriting initialization, explicit hash snapshot and draft/review integrity checks |
| [Brief](../skills/msc-course-builder/assets/brief.md), [lecture](../skills/msc-course-builder/assets/lecture.md), [exercises](../skills/msc-course-builder/assets/exercises.md) | Reusable LO-aligned source templates; no finished teaching content |
| [References](../skills/msc-course-builder/assets/references.md), [completion](../skills/msc-course-builder/assets/completion.md), [student notebook](../skills/msc-course-builder/assets/student-lab.ipynb) | Citation/review prompts and executable answer-free scaffold |
| [Boundary decision](course-builder-boundary.md) | Current public-only handling decision and limits |
| [Tests](../tests/test_course_builder.py) | Disposable-repository lifecycle, failure and path-boundary tests |
| [CI](../.github/workflows/course-builder.yml) | Read-only, standard-library checks on relevant changes; no credentials retained |
| [README](../README.md) | Skill navigation and current public-only decision |
| This report | Reproduction, verification evidence, remaining decisions and acceptance status |

## Execution evidence

Local environment: Windows, Python 3.13.2. Commands run from repository root:

```powershell
python -s skills/msc-course-builder/scripts/session_package.py plan --session S01 --issue 13
python -s -m unittest discover -s tests -p test_course_builder.py -v
python -s -m unittest discover -s tests -v
python -s curriculum/validate_traceability.py
git diff --check
```

| Check | Observed result |
| --- | --- |
| Read-only S01 plan | PASS; selected canonical session, source hashes and output inventory; no sessions directory created |
| New tests | PASS: 19 tests, including all 16 session selections; S01 online and S02 campus draft initialization/checks; CLI lifecycle; malformed input; overwrite refusal; missing prerequisites/templates; source/manifest/hash drift; unlisted files; missing/empty files; notebook output/metadata rejection; full-package missing/invalid binaries; redirected directory rejection |
| Student notebook scaffold | PASS: code cells executed in an isolated Python subprocess; no output or embedded solution. This is not validation of future session labs |
| Review-ready separation | PASS: fresh templates rejected; synthetic completed-text fixture passes structural checks while approval remains pending. It does not represent an academically reviewed lesson |
| Existing and new tests | PASS: 53 total tests, no skips; curriculum, delivery and bibliography audit checks run through tests/preflight |
| Traceability | PASS: source identity, local descriptor hash, session/LO coverage and assessment constraints |
| Bibliography release gate | Existing regression passes by confirming expected exit 1 for unresolved Ng metadata; no release bypass added |
| Skill-creator quick validator | PASS: “Skill is valid!” Initial attempt lacked PyYAML; PyYAML 6.0.3 was then installed into a temporary directory and the unchanged validator rerun successfully. No repository/global runtime dependency added |
| Whitespace and documentation links | PASS; includes new files and local Markdown links |
| Hosted CI | Not run; workflow has not been pushed |

To reproduce the external skill-creator check, run its `scripts/quick_validate.py skills/msc-course-builder` using an environment with PyYAML. This optional development validator is separate from the repository helper and CI, which need only the standard library. Tests create and remove synthetic packages in temporary directories, not real `sessions/` artifacts. No network or user data is needed for those tests.

Manual workflow review covered choosing a campus session, requesting instructor answers, encountering unresolved citations, missing full-format outputs, and resuming an existing draft: instructions respectively retain mode/LOs, stop before sensitive generation, preserve TODO/release failure, report the missing build prerequisite, and edit in place without reinitializing. This is a review of instructions, not an independent agent execution or professor sign-off.

## Acceptance and limits

- [x] Replaces the scaffold with scoped session selection, templates, staged outputs, reference/fail-fast rules, manifests and completion reports.
- [x] Documents provenance, dependency verification, the user's boundary decision and reproducible commands.
- [x] Adds tests and local verification evidence; source checks preserve approved requirements and bibliography unknowns.
- [x] Excludes private outputs; no student records, solutions, keys, copied book content or new descriptor copy introduced.
- [ ] Professor approves future academic/visual session content and release; a passing helper never grants approval.
- [ ] Evidence posted to Issue #7 or a PR referencing #7, after the user's authorization. This report is prepared for that handoff; no remote write is performed.

The skill is ready for local use within this contract. It does not implement AUTO-02–06, generate finished DOCX/PPTX, execute substantive future labs, provide institutional templates, automatically detect all personal information, or establish legal permission. Full packages still require actual rendering/execution evidence and human review. The mutable citation ledger is validated on every preflight rather than frozen into source hashes, so adding legitimate uses for another session does not invalidate all existing packages; record the reviewed ledger revision in each completion report.

Outstanding release decisions remain Ng's exact date/version/URL, descriptor publication permission and professor academic/visual review. Existing timetable, environment and assessment-design decisions remain with their original tasks. No approved outcomes, topic blocks, hours, assessment weights, curriculum/source hashes or bibliography records are changed.

Initial implementation and validation were completed without committing or publishing. The user subsequently authorised committing and pushing these Issue #7 changes to the current branch. No PR, issue comment or student-material release is authorised by that instruction; professor approval remains separate.
