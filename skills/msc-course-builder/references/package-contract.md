# Session package contract

## Commands and stages

Run from the repository root with Python 3.13 (standard library only):

```powershell
python -s skills/msc-course-builder/scripts/session_package.py plan --session S01 --issue 13
python -s skills/msc-course-builder/scripts/session_package.py init --session S01 --issue 13
# Author the drafts, then record deliberate file changes:
python -s skills/msc-course-builder/scripts/session_package.py snapshot --session S01
python -s skills/msc-course-builder/scripts/session_package.py check --session S01
python -s skills/msc-course-builder/scripts/session_package.py check --session S01 --review-ready
```

Use the actual session/issue. `plan` and `init` accept `--package source|full`, default `source`. `init` creates templates, not a completed lesson. Review existing packages in place; do not delete them to rerun initialization. `snapshot` explicitly updates the integrity baseline after authoring; it is not proof of correctness. It refuses source/session/contract drift and unexpected files, and cannot change provenance or approval status. Commands return 1 for failed checks (argparse usage errors: 2). None accesses GitHub, installs packages or publishes.

| Stage | Files and meaning | Evidence |
| --- | --- | --- |
| Plan | JSON printed by `plan`: session record, issue, sources, outputs | Task dependencies manually checked; source/delivery/bibliography audit checks pass |
| Source draft | `brief.md`, `lecture.md`, `exercises.md`, `references.md`, `student-lab.ipynb`, `completion.md`, `manifest.json` | Templates completed, lab tested and citation ledger updated by author |
| Full draft | Source files plus `lecture.docx`, `slides.pptx` | Editable files generated, rendered and visually inspected |
| Review candidate | Requested files exist, hashes match, no drafting TODOs | `check --review-ready` plus manual checks below; professor approval still pending |
| Release | No helper export/release command | Bibliography release gate, manual inspection and professor approval; publication separately authorised |

## Manifest version 1

The manifest is an inventory, not publication permission. Fields: `schema_version`, positive integer `issue`, entire selected curriculum `session`, `package`, `audience: public_student`, `approval: pending_professor_review`, `sources` and `outputs`. Sources map required repository-relative input paths to SHA-256 of UTF-8 text with CRLF normalised to LF. The curriculum validator separately checks descriptor/transcription identity and approved invariants. No absolute user paths or student information belong here.

Outputs contain the exact required filenames, each with `path` and raw-byte `sha256`. A missing requested binary has a null hash and is allowed only in draft checks; missing source files are errors. `snapshot` records present files without creating binaries. `check` rejects changed/extra/missing inventory records, source drift, missing source files, unexpected directory content and output hash drift. It checks notebook structure and rejects stored outputs/execution counts and cell metadata. `--review-ready` also requires all files, rejects TODO/TBD/FIXME/template tokens in text/notebooks and checks DOCX/PPTX container identity. These checks cannot evaluate teaching quality, binary layout or prose completeness.

AUTO-03 amendment: the sole readiness marker exception is the exact literal `STUDENT TODO:` inside notebook cells whose IDs start with `student-`; it denotes intentionally uncompleted student work. All other drafting markers in those cells still fail. This exception does not allow unresolved author work to be relabelled as a student task.

AUTO-03 supplies the canonical notebook asset and [reusable notebook conventions](../../../templates/notebook/README.md). Its standard-library path runs without completing exercises; explicit NOT ATTEMPTED feedback is not completion evidence. Run notebook execution validation in addition to package integrity checks. The manifest version, notebook metadata allowlist and single `student-lab.ipynb` output remain unchanged; no lecture-schema fields or private solution outputs are added.

The completion report is hashed; the manifest does not hash itself. Record planned final commands in the report before snapshot and their actual results in the final response to avoid recursive hash updates. Subsequent edits need another snapshot/check.

## Authoring and human checks

- **Academic:** exact LOs/block retained, proposed links explicit; definitions, assumptions, dimensions, derivations, interpretation and limitations checked. Include justified methodological comparisons and reproducible experiments where appropriate. Do not invent graded exercises, a rubric or leaderboard/report split.
- **Delivery:** 180-minute schedule, mapped mode, online participation/campus instructions, accessibility, outages and account/data prerequisites. Preserve self-study allocation. S16 retains ten ten-minute presentations and feasible remaining time.
- **Notebook:** licensed accessible data with provenance/version/hash; record Python/dependency versions, seed and hardware assumptions. Split before preprocessing, use baselines/appropriate validation, discuss variability/ethics. Execute the clean student path in an isolated environment. Exercise stubs must run without solutions; identify student-dependent results that cannot yet be executed. Clear outputs, execution counts and incidental metadata before snapshot. Only the helper's kernel/language metadata and cell IDs are permitted.
- **References:** inspect all artifacts and reconcile uses with the existing citation ledger; verify locators/asset-specific rights. Availability is not permission. New sources need explicit registry verification, never invented keys. Run audit checks while drafting; run `python -s references/validate_bibliography.py --release` before publication. It currently fails on Ng's unresolved entry; there is no bypass.
- **Formats:** inspect editable files, rendered pages/slides, equations, contrast, alt text and screen-sharing legibility. Public notes contain no answers. Later AUTO-02–06 tasks supply their own templates, notebook/test conventions and handoffs; this issue does not implement them.
- **Boundary:** inspect text, binaries, links and hidden metadata for confidential content. A checked manifest cannot authenticate permissions, professor approval or absence of personal information.
- **Report:** issue/session, provenance, actual versus deferred artifacts, environment/commands/results, academic/visual review status, citation TODOs, decisions, acceptance checklist and explicit no-release status. Do not invent successful execution or approvals.

If a dependency cannot be verified, an academic change is required, data rights are unknown, an environment is unavailable or a sensitive output is requested, identify the blocked item and stop dependent work. Continue unrelated source drafting only if the task authorises that partial scope; never call it a completed full package.
