# SETUP-02 gaps and recommendations

Source baseline and complete crosswalk: [traceability matrix](traceability-matrix.md). All findings are audit judgments. All recommendations below await professor review and do not amend the descriptor, session map, grades or assessment scheme.

## Findings

| ID | Severity | Gap or risk | Source/evidence | Consequence |
| --- | --- | --- | --- | --- |
| G01 | High | Practical attainment is not guaranteed across LO2–LO6. | Descriptor pp. 1–2: implementation verbs; exam tests theory/mathematics/interpretation; capstone task unspecified. | Written explanations and a single challenge cannot establish every implementation skill. |
| G02 | High | LO8 appears only in S16 in the working map. | CSV; descriptor LO8 and K/P requirements. | End-to-end execution and reporting need preparation before final presentations. |
| G03 | High | Rigorous cross-validation is explicit only in S07; LO3 starts in S03. | CSV S03–S07; descriptor LO3. | Early model comparisons could teach unreliable evaluation unless validation is embedded earlier. |
| G04 | Medium | Scaling/encoding, pandas/scikit-learn, domain interpretation, bias-variance diagnosis and TensorFlow/Keras are partly implicit. | CSV versus descriptor LO2–LO4, LO6–LO7. | A topic-only checklist could miss required methods and interpretation. |
| G05 | Medium | OpenAI Gym is omitted from the working topic map. | Descriptor S11–S12 versus CSV. | An approved named content item lacks an explicit implementation plan. |
| G06 | Medium | Autoencoders occur before the neural-network block; S14 has broad scope. | Descriptor S09–S10 and S13–S14; CSV. | Prerequisite and depth risks within fixed three-hour sessions. |
| G07 | High | Assessment blueprints, rubric detail and dataset are unavailable. | Descriptor supplies formats/weights but no detailed design; repository has no assessment packages. | Coverage and equivalence for all students cannot yet be certified. |
| G08 | Medium | Ethical evaluation is an approved topic block but not a standalone LO; LO7's bias-variance is distinct from societal bias. | Descriptor p. 2 S15; p. 1 LO7. | Mapping S15 to LO7 alone can conceal responsible-ML content or conflate concepts. |
| G09 | Medium | S16 presentation logistics remain unresolved. | Production plan: 10 students; descriptor: ten-minute presentations; 180-minute session. | 80 minutes remain for transitions, Q&A, debrief and synthesis; feasibility needs scheduling. |
| G10 | Low | README retains an open contact-hour discrepancy; production plan records its resolution. | README versus production-plan SETUP-01 register. | Readers could confuse certification activity, M5 exam and assessment hours. |
| G11 | Medium | Descriptor approval/version metadata and institutional hybrid approver are not recorded in the source itself. | Two-page PDF and production-plan decision register. | Audit can identify the exact file but cannot independently authenticate institutional sign-off. |

## Recommendations (proposed only)

| ID | Addresses | Recommendation | Evidence required to resolve / decision owner |
| --- | --- | --- | --- |
| R01 | G01, G07 | Build an LO-component assessment blueprint within E/K/P. Use formative practical evidence for diagnosis; do not count it as summative without approval. Explicitly review LO4–LO6 and both LO3 model families. | Professor approves coverage and evidential sufficiency; institution approves any necessary requirement changes. |
| R02 | G02 | Embed capstone orientation, baseline, experiment logging, validation review and ethical reflection in existing sessions, as P links show; schedule work within existing self-study/assessment budgets. | Professor approves milestones and workload without changing blocks, hours or grades. |
| R03 | G03, G04 | Make cross-validation and fold-local transformations explicit from S03, consolidated in S07–S08; require methodological interpretation in future activity design. | Professor reviews future session briefs against each LO component and named library. |
| R04 | G05 | Retain OpenAI Gym in the content inventory; verify environment accessibility and reproducibility during later lab design. Any successor or substitution needs review. | Professor approves environment choice; later execution evidence confirms compatibility. No compatibility claim is made here. |
| R05 | G06 | Plan a concise neural representation prerequisite bridge within S10 and bound S14 practical scope while retaining every approved topic. | Professor approves depth and timing within the existing block sequence. |
| R06 | G07 | Preserve 60/30/10, exam duration, report plus leaderboard, and presentation duration. Define fair, reproducible evaluation and report criteria later; do not invent the leaderboard/report split now. | Professor approves dataset, blueprint and rubrics; record any institutional decisions required. |
| R07 | G08 | Distinguish societal fairness from bias-variance, and surface data permissions, subgroup evaluation and explanation limitations in capstone reflection. | Professor reviews responsible-ML coverage without rewriting LO7 or adding an LO. |
| R08 | G09 | Reserve 100 minutes for ten presentations and explicitly allocate the remaining 80 minutes among transitions, Q&A, debrief and exam preparation. | Professor confirms feasible S16 timetable and accommodations. |
| R09 | G10, G11 | In a later documentation update, align README with the recorded contact-hour resolution and capture approval reference/version metadata when available. | Professor supplies institutional provenance; no source replacement or publication is assumed. |

No approved outcome is wholly absent from the working map. This is a completeness finding at label level, not a certification of postgraduate depth, delivered teaching or assessed attainment. Mathematical reasoning, methodological justification, reproducibility and ethical evaluation are specified as proposed evidence in the matrix to support subsequent MQF Level 7 design review.
