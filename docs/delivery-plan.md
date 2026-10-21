# SETUP-04 hybrid delivery and contingency plan

Issue: [#4](https://github.com/fajouri/msc-machine-learning/issues/4). Prepared 2026-10-21. **Draft pending professor review.** All activities, timings, fallback thresholds and logistics below are proposals, not institutional policy or approved assessment changes.

## Inputs, dependencies and boundaries

SETUP-01 [#1](https://github.com/fajouri/msc-machine-learning/issues/1) and SETUP-03 [#3](https://github.com/fajouri/msc-machine-learning/issues/3) were verified closed through the GitHub API on 2026-10-21; both comment lists were empty. Their supporting [production decisions](PRODUCTION_PLAN.md) and [curriculum model](../curriculum/curriculum.json) are present and pass the existing validators. No blocking setup prerequisite is missing. Issue closure does not approve their outstanding pedagogical proposals.

Authority comes from the approved descriptor as transcribed in the [traceability audit](../curriculum/traceability-matrix.md), with matching local descriptor hash verified by the existing validators. This is not a fresh PDF audit. The descriptor is already tracked in this checkout despite the older audit's untracked-file statement; this task neither changes it nor establishes publication permission. The [session map](../curriculum/session-map.csv), [workload proposal](../curriculum/README.md) and [coverage risks](../curriculum/traceability-gaps.md) inform this design. No external academic citations or third-party assets are introduced.

Lecturer-reported university decisions: **9 synchronous online + 7 campus sessions**, Google Meet, Colab and Kaggle permitted, and an expected class of ten. Specific session placement remains proposed. Preserve all LO1–LO8 wording, topic blocks and sequence, **60/30/10** assessment weights, the **three-hour on-campus written exam**, and **ten-minute presentations**. The scheduled teaching allocation remains **16 × 3 = 48 hours**; the separate **two-hour university certification exam** has no lecturer deliverable. The descriptor remains **250 = 50 contact + 160 self-study + 40 assessment hours**. This plan allocates no extra assessed work or self-study hours.

## Common operating procedure

The lecturer owns preparation, facilitation, outage decisions and private follow-up. Campus IT owns room/device/network support; the university owns timetable, accommodations and exam arrangements. These are proposed responsibilities to confirm before delivery.

**Before each session:** at least 48 hours beforehand, the lecturer distributes a versioned student pack through the confirmed course channel: agenda, accessible reading/slide source, uncompleted student notebook or worksheet, permitted small dataset or synthetic substitute, environment instructions and checksums/version identifiers. Include a plain-text route through each activity, labelled illustrative outputs where needed, and a local save/export instruction. Do not include instructor solutions. Record dataset origin/licence, dependency versions, random seeds and split procedure in later lab packs. Test the pack on a clean Colab runtime and the agreed local environment before claiming either works. These packs and executable labs are later session-production deliverables; this issue specifies their requirements only.

The lecturer confirms a private announcement/contact channel with students before S01, including a route available independently of Meet. The LMS and institutional contact channel are not yet identified; do not invent an address or assume an integration. If no independent channel exists at delivery time, distribute the outage instructions in advance and agree the next scheduled contact point. Students download the pack and test access in advance within existing preparation allocations. Account problems are handled privately; do not require students to expose personal accounts or pay for compute.

**During online sessions:** use Meet for live discussion, a verbal or text response round, individual reasoning time and paired critique followed by plenary comparison. Give each of ten learners a route to contribute. Camera use is optional; accept chat, speech or a privately arranged equivalent. No paid polling, breakout or recording feature is assumed. Pairs can compare responses in the main discussion if no separate working space is available. Ask learners to justify assumptions and limitations, not merely report an accuracy score. Lecturer checks the evidence listed below formatively; it introduces no new grading component.

**During campus labs:** provision ten working seats/devices or confirm BYOD plus loan arrangements; pairing is pedagogical, not a substitute for each student's practical access. Check power, projector, accessible routes/seating, keyboard access, readable displays, local saves and network login before class. Use five pairs with rotating driver/reviewer roles and an individual explanation or saved checkpoint. Clear shared-device sessions and local personal files through the approved institutional procedure; never share credentials. Students keep their own work privately.

**After each session:** the lecturer records topic coverage, missed activity and recovery needs in private course records; students retain code/environment/seed notes and a short methodological reflection. Use existing workload allocations; do not add mandatory catch-up hours silently. Do not publish attendance, disability information, identifiable submissions, marks, private links or incident reports in GitHub. Public artifacts may contain original prompts, synthetic examples and cleared resources; instructor answers and exam keys belong only in separate private storage. Recording is off by default pending institutional policy and consent arrangements; no automatic transcription or public upload is authorised.

## Accessibility across all sessions

Distribute selectable-text materials with headings, descriptive links, image descriptions and text/table alternatives to plots; do not encode meaning through colour alone. Explain symbols aloud and provide equations in readable text with definitions. Allow zoom and keyboard navigation; provide prompts before timed responses. Test readability and navigation with the actual pack. Offer captions if available and verified in the institutional setup; do not treat captions as a guaranteed feature or the sole accommodation. Provide written prompts and a private route for clarification regardless. Confirm individual accommodations privately before delivery, including accessible campus equipment and presentation arrangements. Preserve learning goals and assessment rules; the university/professor must approve any assessment adjustment. Outages and access barriers must not become automatic attendance or grade penalties under this proposal.

## Failure and recovery protocol

| Scenario / trigger | Immediate action | Recovery and owner |
| --- | --- | --- |
| Individual connection becomes unstable | Learner switches off video, tries audio/text and uses the downloaded pack; saves work locally. Lecturer restates instructions in text where possible. | Learner contacts lecturer through the agreed private channel when reachable; lecturer checks missed interaction and offers an equivalent supervised opportunity under the timetable. |
| Meet unavailable or lecturer disconnected for 5 minutes | Try one reconnection; students consult the pre-distributed current task. Lecturer uses the independent channel if available. No unapproved platform switch or public meeting link. | At 15 minutes without a usable live class, lecturer announces suspension through the agreed channel, or students follow the pre-distributed suspension rule if all channels fail. Lecturer requests an approved replacement live slot for lost teaching. |
| Internet unavailable to the whole class | Use downloaded prompts/data and local tools if tested; campus lecturer can continue live offline. Online students may retain private draft work but are no longer assumed to be attending live. | Lecturer records lost synchronous teaching and arranges approved live recovery. Offline independent work is not relabelled synchronous contact or silently added to self-study. |
| Colab, Kaggle, login or compute unavailable | Continue live reasoning using the session fallback below; use the tested local notebook only if provisioned. Avoid paid upgrades or improvised dataset mirrors. | Lecturer/IT restore practical access and arrange supervised execution of missed implementation. Static outputs and hand traces do not establish LO2–LO6 implementation attainment. Competition deadlines/grades change only through approved arrangements. |
| Campus workstation/projector fails | Use a loan/tested device, rotate pair roles, and distribute readable local/printed prompts. Lecturer narrates diagrams and checks individual access. | Campus IT restores equipment; lecturer schedules missed individual practice. No learner loses all hands-on time by becoming a permanent observer. |
| Campus room/power unavailable or unsafe | Follow campus safety procedure; stop use of affected facilities and notify the institutional contact. | University arranges a suitable replacement campus slot. Do not silently convert campus sessions to online or change the 9/7 allocation. |
| S16 presentation equipment or service fails | Use privately preloaded slides/PDF and saved result tables; leaderboard access is unnecessary for the presentation. | If accessible presentation cannot proceed, lecturer requests an approved campus reschedule without shortening the ten-minute slot or changing grading. |

The 5/15-minute thresholds are proposed operational decisions for professor review. Instructor and student rehearse the procedure before the first online class. Restoration alone does not close an incident: lecturer verifies equivalent opportunity, actual topic coverage and practical completion, then confirms recovery privately. Do not count the same recovered time twice or assume asynchronous work replaces authorised live contact.

## Proposed three-hour run sheets

Times are elapsed minutes within the existing 180-minute scheduled session, not additional workload. The ten-minute break is explicit; confirm institutional treatment of breaks before issuing the timetable. This plan does not redefine the descriptor's contact-hour accounting. The S16 schedule assumes exactly ten students; changed enrolment or accommodations require a revised approved schedule.

### Online (S01, S03, S05, S07, S09, S11, S13, S14, S15)

| Start | End | Activity |
| --- | --- | --- |
| 0 | 10 | Access check, retrieval prompt and agenda |
| 10 | 40 | Mathematical/conceptual explanation with response pauses |
| 40 | 65 | Individual prediction and paired/plenary justification |
| 65 | 90 | Guided reproducible demonstration and critique |
| 90 | 100 | Break |
| 100 | 140 | Student practice and lecturer feedback |
| 140 | 165 | Compare methods, assumptions and limitations |
| 165 | 180 | Individual evidence check, recap and recovery needs |

### Campus labs (S02, S04, S06, S08, S10, S12)

| Start | End | Activity |
| --- | --- | --- |
| 0 | 15 | Device/access check and methodological retrieval |
| 15 | 40 | Concept explanation and lab demonstration |
| 40 | 90 | Paired implementation, rotate driver/reviewer |
| 90 | 100 | Break |
| 100 | 145 | Controlled experiment and individual saved checkpoint |
| 145 | 170 | Compare results, uncertainty and reproducibility |
| 170 | 180 | Individual explanation, local export and exit check |

### Campus presentations (S16)

| Start | End | Activity |
| --- | --- | --- |
| 0 | 10 | Accessible setup, order and assessment reminders |
| 10 | 75 | Five slots: 10-minute presentation + 2-minute Q&A + 1-minute changeover each |
| 75 | 85 | Break |
| 85 | 150 | Five slots: 10-minute presentation + 2-minute Q&A + 1-minute changeover each |
| 150 | 165 | Kaggle debrief and methodological synthesis |
| 165 | 180 | Exam preparation: concept connections and format clarification |

Ten presentations occupy 100 minutes, Q&A 20, changeovers 10, setup 10, break 10, debrief 15 and exam preparation 15: total 180. The written exam is a separate 180-minute assessment, not held inside S16. Exam preparation uses public concepts and practice prompts only, never live examination questions/keys. Presentation delivery retains SETUP-03's proposed single counting within contact time, subject to professor approval.

## Per-session delivery matrix

Every row inherits the common accessibility, preparation, privacy and recovery procedures above. Modes and order mirror the working CSV; LO links, exact titles and topic inventory remain in that unchanged source. Activities below specify observable postgraduate reasoning without supplying answers. Fallback materials are requirements to prepare and test during subsequent session production, not claims that packs already exist.

| Session | Mode | Engagement / practical activity | Formative evidence | Offline or service fallback | Specific accessibility provision | Logistics / preparation |
| --- | --- | --- | --- | --- | --- | --- |
| S01 | online | Classify problem scenarios by paradigm; compare assumptions in a response round, then inspect a scientific Python workflow. | Individual justified paradigm choice and environment/version record. | Downloaded scenario worksheet and code trace; restore execution for Python practice. | Plain-text code and glossary; verbal and text response routes. | Test Meet access and notebook export; rehearse outage rule and privately resolve account issues. |
| S02 | campus | Five pairs build pandas/scikit-learn cleaning, feature engineering, scaling and encoding steps; challenge training-only fitting. | Individual pipeline checkpoint, provenance and explanation of leakage prevention. | Local permitted small table and tested notebook; paper transformation plan until execution is restored. | Keyboard-operable table and text schema; avoid image-only data. | Ten practical seats, loan route, local dataset and tested dependencies; rotate drivers. |
| S03 | online | Predict residual behaviour, explain least-squares objective, then compare a scikit-learn baseline using fold-local preprocessing and cross-validation. | Objective-to-prediction explanation and recorded validation design. | Downloaded small regression table, objective worksheet and illustrative baseline outputs; recover model execution. | Define symbols in text; describe residual plots with tables. | Prepare small CPU example and fold identifiers; save environment and split record. |
| S04 | campus | Compare polynomial degree and regularisation with controlled validation curves; justify bias-variance diagnosis. | Individual experiment log and interpretation separating training and validation evidence. | Local notebook/data; labelled curve tables for critique if devices fail, followed by execution recovery. | Tabulated curve values and non-colour line labels. | Use common splits and seeds across pairs; preflight polynomial/scaling pipeline. |
| S05 | online | Debate candidate tree splits, fit a tree and justify metrics under imbalance and asymmetric costs. | Split reasoning, confusion-matrix interpretation and cross-validation record. | Printed/text class counts and metric worksheet; illustrative tree outputs until practical access returns. | Read confusion matrices by named rows/columns; provide text tree description. | Prepare a small permitted classification example and CPU tree run; no live learner data. |
| S06 | campus | Compare random forests, SVM and ensembles under a shared validation protocol; defend computational and generalisation trade-offs. | Individual comparison log with scaling rationale, seeds and uncertainty caveat. | Cached permitted data and tested local estimators; critique illustrative comparisons while restoring runs. | Text comparison table and verbal explanation of decision boundaries. | Preflight bounded CPU runs and scaling; ten devices, five rotating pairs. |
| S07 | online | Audit contrasting split/pipeline scenarios; defend cross-validation appropriate to the data-generating process. | Annotated leakage diagnosis distinguishing selection from final estimation. | Downloaded fold diagrams and pseudocode; annotate locally and discuss on restored live connection. | Provide fold membership as text tables as well as diagrams. | Prepare original synthetic scenarios, including dependent observations; keep held-out evaluation distinct. |
| S08 | campus | Compare bounded hyperparameter searches and critique feature importance under correlated predictors. | Individual search budget, selection record and qualified importance interpretation. | Local small search if tested; labelled search/importance tables for interim reasoning. | Sortable/readable text result tables; describe importance uncertainty. | Cap CPU budget, freeze splits and reserve independent evaluation; verify local exports. |
| S09 | online | Predict how K-means, hierarchical clustering and DBSCAN respond to scale/density; compare domain interpretations. | Method-choice justification and stability/parameter record rather than a single plot. | Downloaded coordinates, distance table and labelled illustrative clusterings; recover method execution. | Cluster labels and coordinates supplement colour plots. | Preload small synthetic data, seeds and scaling choices; no large downloads during class. |
| S10 | campus | Connect PCA to variance/projection, critique t-SNE geometry and examine autoencoder reconstruction with a short neural representation bridge. | Individual reduction checkpoint and qualified comparison of geometry, information loss and domain meaning. | Local CPU-sized examples if tested; projection/reconstruction tables for reasoning, then recover implementation. | Describe axes and reconstruction differences in text; provide a notation guide. | Professor reviews prerequisite bridge; preflight PCA/t-SNE and small autoencoder runtime without assuming GPU access. |
| S11 | online | Specify an MDP in a turn-taking discussion and reason through a Q-learning update; compare RL with other paradigms. | State/action/reward/transition specification and explanation of update terms. | Downloaded transition/reward table and blank update worksheet for discussion on reconnection. | Text state-transition table replaces diagram-only navigation. | Retain OpenAI Gym in descriptor context; prepare environment-interface explanation without claiming compatibility. |
| S12 | campus | Implement Q-learning, compare exploration and repeated-seed returns, then contrast policy gradients conceptually. | Individual executable checkpoint, seed/environment log and qualified variability interpretation. | Tested local environment when available; saved synthetic trajectories for hand traces until practical recovery. | Text trajectories and return tables; no dependence on animated rendering. | Verify OpenAI Gym environment compatibility during lab production; professor must review any successor/substitution. No environment is declared tested here. |
| S13 | online | Relate loss and gradients to TensorFlow/Keras MLP training; predict and compare regularisation effects. | Individual training checkpoint and explanation of training/validation divergence with seeds/versions. | Small tested CPU model or labelled loss tables while compute recovers; schedule missed training. | Provide layer shapes, equations and loss values in text. | Bound training time; prepare local/Colab export route and avoid paid accelerator dependence. |
| S14 | online | Compare CNN/RNN assumptions, inspect transfer learning and discuss deployment constraints through guided examples and critique. | Architecture/input-shape reasoning, training evidence where executed, and deployment limitation record. | Downloaded architecture descriptions and permitted illustrative outputs; recover missed TensorFlow/Keras practice. | Text architecture and sequence tables accompany diagrams. | Bound practical depth with professor review while retaining all four topics; cache only licensed assets, avoid live deployment credentials. |
| S15 | online | Discuss synthetic subgroup results and competing fairness interpretations; challenge explanation limits and distinguish societal bias from bias-variance. | Qualified metric comparison, uncertainty and ethical limitations statement. | Downloaded synthetic contingency tables and original case prompt for later supervised discussion. | Text descriptions of subgroup tables; private participation route for sensitive discussion. | No identifiable student/protected-attribute data; preserve approved ethics scope without adding an LO. |
| S16 | campus | Ten capstone presentations with Q&A; Kaggle debrief and synthesis for exam preparation. | Approved presentation evidence and formative methodological reflection; marks remain private. | Privately preloaded slides/PDF and saved results; accessible campus reschedule if presentation cannot proceed. | Accessible slides, microphone/seating checks and privately agreed accommodations. | Confirm ten students and 180-minute schedule; check projector and files before class, never require a live leaderboard. |

## Decisions and pre-delivery gates

Professor review is required for activity depth, run sheets (including breaks), S10 prerequisite bridge, S14 breadth, fallback equivalence, outage thresholds and S16 timings/presentation accounting. University confirmation is needed for session placement, private communication/LMS route, room/IT ownership, accessibility arrangements and exam logistics. The existing assessment blueprint/dataset/rubric gaps remain open; no within-assessment weight split is invented.

Before each session, lecturer checks: accessible pack distributed and downloaded; dataset/asset rights recorded; student-only contents checked; runtime and offline route rehearsed; private support channel established; room/device or Meet access tested; individual accommodations confirmed; recovery owner identified. Before S12, resolve and test the environment choice. Before S16, confirm enrolment and accommodation timing. A failed gate blocks that session's release/readiness, not this setup design. This plan alone does not certify delivery readiness or practical attainment.

## Reproduce validation

From the repository root, Python 3.13 standard library only:

```powershell
python -s curriculum/validate_curriculum.py
python -s curriculum/validate_delivery.py
python -s -m unittest discover -s tests -v
git diff --check
```

The delivery validator checks session order/modes against the CSV, complete planning fields, continuous 180-minute run sheets and S16 capacity. It does not authenticate approvals or judge academic sufficiency, accessibility in practice or recovery equivalence. See the [validation and acceptance report](delivery-validation.md).
