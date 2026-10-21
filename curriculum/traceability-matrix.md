# M5 curriculum traceability matrix

Issue: [SETUP-02 / #2](https://github.com/fajouri/msc-machine-learning/issues/2). Audit date: 2026-10-21. Status: draft for professor review; no academic changes approved by this audit.

## Authority and provenance

The complete local `docs/Machine Learning.pdf`, **M5: Machine Learning**, Ascencia Malta MSc Computer Science, is the authoritative descriptor for this audit. Both numbered pages (1 of 2 and 2 of 2) were extracted and visually inspected. Page 1 contains module information and LO1–LO7; page 2 contains LO8, indicative content, assessments and readings. No version, approval date or signature is printed; institutional approval provenance is supplied by the repository's production plan, not independently authenticated here. SHA-256: `BDC82A68602E666E13B869DE83279241C85D81A307A7F770742F245690F40660`. The PDF remains local and untracked; this audit does not authorise its publication.

Other inputs: `AGENTS.md`; `docs/PRODUCTION_PLAN.md` (including lecturer decisions dated 2026-10-21); `curriculum/session-map.csv`; Issue #2 (read via GitHub API, no comments). The CSV is a **working teaching map**, not the descriptor. Its baseline SHA-256 is `A60B0336DE9801C95A9ED082FF082E52CFA9B8DAAFF07EFBA4F9C855440E4F10`.

Approved constraints (descriptor p. 1): MQF Level 7; 10 ECTS; 250 hours = 50 contact + 160 self-study + 40 assessment; 16 sessions × 3 hours; face-to-face, lab-based delivery; pass mark 50%; prerequisites M3 or M4, Python proficiency and basic statistics. The production plan records lecturer-confirmed university authorisation for 9 online / 7 campus sessions and allocates the remaining 2 contact hours to a university certification exam outside lecturer responsibility. That activity is distinct from the M5 written exam. Specific session modes remain proposed. No new hour allocations or changes to requirements are made here.

Only outcome wording and assessment constraints below are authoritative source transcriptions/summaries. All activity designs, reinforcement links and assessment-evidence suggestions are **pedagogical proposals**, not existing materials, approved rubrics or evidence of student attainment. The descriptor does not provide an LO-by-assessment blueprint.

## Approved outcomes

Transcribed from descriptor pp. 1–2; line wraps and extraction artefacts in hyphen spacing normalised against the rendered pages.

| Code | Approved wording | Source |
| --- | --- | --- |
| LO1 | Explain and compare supervised, unsupervised, and reinforcement learning paradigms, identifying appropriate algorithms for given problem types. | p. 1 |
| LO2 | Implement data preprocessing pipelines including cleaning, feature engineering, scaling, and encoding using Python (pandas, scikit-learn). | p. 1 |
| LO3 | Build, train, and evaluate supervised learning models (regression and classification) using scikit-learn, applying rigorous cross-validation. | p. 1 |
| LO4 | Apply unsupervised learning techniques (clustering, dimensionality reduction) and interpret results in a domain context. | p. 1 |
| LO5 | Develop reinforcement learning solutions by defining MDPs and implementing Q-learning or policy gradient methods. | p. 1 |
| LO6 | Build and train deep neural networks using TensorFlow/Keras, applying regularisation techniques to prevent overfitting. | p. 1 |
| LO7 | Evaluate model performance using appropriate metrics, diagnose bias-variance issues, and apply hyperparameter optimisation. | p. 1 |
| LO8 | Design and execute an end-to-end machine learning competition pipeline (Kaggle-style), document findings, and present results. | p. 2 |

## Full session crosswalk (128 intersections)

**M** = explicitly mapped in the existing CSV; **P** = additional reinforcement proposed by this audit; **—** = no explicit or proposed targeted link (not a claim that the outcome is impossible in that session). M does not mean mastery or verified teaching. The CSV remains unchanged. These links are instructional-design judgments; the descriptor assigns topics to blocks, not LOs to individual sessions.

| Session | Mode (proposed) | LO1 | LO2 | LO3 | LO4 | LO5 | LO6 | LO7 | LO8 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| S01 | online | M | — | — | — | — | — | — | P |
| S02 | campus | — | M | — | — | — | — | — | P |
| S03 | online | — | P | M | — | — | — | P | P |
| S04 | campus | — | — | M | — | — | — | M | P |
| S05 | online | — | — | M | — | — | — | P | P |
| S06 | campus | — | — | M | — | — | — | M | P |
| S07 | online | — | P | P | — | — | — | M | P |
| S08 | campus | — | — | P | — | — | — | M | P |
| S09 | online | P | — | — | M | — | — | — | — |
| S10 | campus | — | — | — | M | — | — | — | — |
| S11 | online | M | — | — | — | M | — | — | — |
| S12 | campus | — | — | — | — | M | — | — | — |
| S13 | online | — | — | — | — | — | M | P | — |
| S14 | online | — | — | — | — | — | M | — | P |
| S15 | online | — | — | — | — | — | — | M | P |
| S16 | campus | P | — | — | — | — | — | P | M |

Existing explicit coverage counts: LO1 2; LO2 1; LO3 4; LO4 2; LO5 2; LO6 2; LO7 5; LO8 1. All outcomes have a named session, but counts do not establish sufficient depth or assessment validity.

## Session evidence and topic coverage

The block and key-content column summarises descriptor p. 2. Session titles and modes come from the CSV. Activities and observable evidence are proposals for subsequent design, **not lesson material or graded additions**. Each proposed evidence item supports the corresponding M/P links above. Reproducible evidence means recorded data provenance, split procedure, software environment, seeds where applicable, and experiments sufficient to reproduce reported conclusions; exact submission requirements await approval.

| Session / working title | Approved block and content | Proposed activity and observable evidence | Audit finding |
| --- | --- | --- | --- |
| S01 ML foundations and Python stack | S1–S2 Foundations: paradigms, scientific Python, wrangling, EDA | Compare problem formulations and justify algorithm families (LO1); outline competition workflow and experiment record (LO8). | LO1 comparison needs explicit evidence; capstone launch not recorded. |
| S02 Data wrangling and EDA | S1–S2 Foundations (continued) | Implement a pandas/scikit-learn pipeline with cleaning, feature engineering, scaling and encoding; explain training-only fitting and document provenance (LO2, LO8). | Scaling, encoding and named libraries are implicit in CSV. |
| S03 Regression I | S3–S4 Regression: linear/polynomial, regularisation, evaluation | Relate least-squares objective to fitted predictions, build a scikit-learn baseline with fold-local preprocessing and cross-validation; record metric rationale (LO2, LO3, LO7, LO8). | Early rigorous cross-validation is not explicit. |
| S04 Regression II | S3–S4 Regression (continued) | Compare polynomial complexity and regularisation through validation/learning curves; explain bias-variance behaviour and record experiments (LO3, LO7, LO8). | Bias-variance diagnosis needs explicit treatment. |
| S05 Classification I | S5–S6 Classification: trees, forests, SVM, ensembles | Fit and cross-validate a tree; justify classification metrics under imbalance and error costs; log baseline evidence (LO3, LO7, LO8). | Metrics alone do not demonstrate rigorous validation. |
| S06 Classification II | S5–S6 Classification (continued) | Compare forests, SVM and ensembles with a common validation protocol; explain generalisation and methodological trade-offs (LO3, LO7, LO8). | Breadth must retain justified comparison, not only API use. |
| S07 Evaluation I | S7–S8 Evaluation: cross-validation, tuning, feature importance | Audit leakage and fold-local preprocessing; justify split design for the data-generating process and distinguish model selection from final estimation (LO2, LO3, LO7, LO8). | Make this a consolidation of earlier validation, not its first use. |
| S08 Optimisation II | S7–S8 Evaluation (continued) | Compare search procedures under a stated budget, preserve independent evaluation, interpret feature importance limitations and record selection decisions (LO3, LO7, LO8). | Tuning coverage exists; bias-variance remains implicit. |
| S09 Unsupervised I | S9–S10 Unsupervised: K-means, hierarchical, DBSCAN, PCA, t-SNE, autoencoders | Compare clustering assumptions, apply the three clustering methods, interpret stability and domain meaning; distinguish unsupervised aims from predictive tasks (LO1, LO4). | Domain interpretation is absent from CSV wording. |
| S10 Unsupervised II | S9–S10 Unsupervised (continued) | Apply PCA and t-SNE and examine an autoencoder representation; justify geometry, information loss and domain interpretation (LO4). | Autoencoders precede neural-network block; prerequisite bridge needed. |
| S11 Reinforcement learning I | S11–S12 RL: MDP, Q-learning, OpenAI Gym, policy-gradient introduction | Specify states, actions, rewards and transitions; explain Bellman/Q-learning reasoning and compare RL with other paradigms (LO1, LO5). | OpenAI Gym named by descriptor is absent from CSV. |
| S12 Reinforcement learning II | S11–S12 RL (continued) | Implement and evaluate Q-learning in the descriptor's environment context; record exploration, reward design and run variability; conceptually contrast policy gradients (LO5). | Q-learning satisfies the implementation alternative; both methods need not be implemented. |
| S13 Deep learning I | S13–S14 Deep learning: MLP, CNN, RNN basics, transfer learning, deployment | Build/train a TensorFlow/Keras MLP; connect loss, gradients and optimisation; compare regularisation using training/validation curves (LO6, LO7). | Framework names missing from CSV; regularisation explicit. |
| S14 Deep learning II | S13–S14 Deep learning (continued) | Investigate CNN/RNN basics and transfer learning with regularisation; explain deployment constraints and connect a deployable pipeline to capstone synthesis without requiring a deep capstone model (LO6, LO8). | Many topics in three hours; practical depth needs review. |
| S15 Ethics, fairness and explainability | S15 Ethics: bias, fairness metrics, responsible ML, explainability | Evaluate subgroup performance, uncertainty and explanation limitations; document capstone ethical limitations and distinguish societal bias from statistical bias-variance (LO7, LO8). | Approved ethics block is broader than literal LO7 wording. |
| S16 Capstone presentations and exam preparation | S16 Capstone: Kaggle debrief, presentations, synthesis | Deliver approved presentations (LO8); synthesise paradigm choice and evaluation reasoning for exam preparation (LO1, LO7). | Ten students use 100 of 180 minutes before transitions/Q&A; schedule remaining work. |

All nine approved blocks retain their original sequence and session ranges. Key content is represented in the working map except explicit OpenAI Gym naming; some LO components and framework names are implicit. Retention of a topic label is not verification of instructional depth. No substitution of the named RL environment is authorised here.

## Approved assessments and evidence crosswalk (24 intersections)

Descriptor p. 2 defines **E: Written Exam, 60%, 3 hours**, end of module, covering theory, mathematical foundations and interpretation; **K: Kaggle Capstone Project, 30%**, a class-internal challenge on a provided dataset, graded on final model/leaderboard performance plus a technical report on methodology, experiments and findings; **P: Presentation, 10%, 10 minutes**, capstone methodology and results presented to the class. No within-assessment weights, rubric criteria, LO quotas, dataset, or exam blueprint are supplied. The production plan records the exam as on campus.

**Proposed** = suitable evidence to consider in an approved blueprint, not confirmed inclusion. **Conditional** = depends on capstone task/methods and cannot guarantee universal coverage. **Direct alignment** = descriptor assessment description directly matches outcome components, but actual performance is unverified. **Not sufficient** = cannot alone establish the implementation verb. Every cell below is an audit judgment, not an approved assessment specification.

| LO | E: Written Exam (60%) | K: Kaggle Capstone (30%) | P: Presentation (10%) |
| --- | --- | --- | --- |
| LO1 | Proposed: compare paradigms, justify algorithm choice for problem types. | Conditional: report justifies selected paradigm and alternatives; one task may not compare all three. | Conditional: explain choice and alternatives; ten minutes limits breadth. |
| LO2 | Proposed: reason about preprocessing and leakage; not sufficient to prove Python implementation. | Proposed: report traces cleaning, features, scaling and encoding to a reproducible pandas/scikit-learn pipeline; dataset may not require every operation. | Conditional: explain preprocessing rationale; not sufficient to verify implementation. |
| LO3 | Proposed: mathematical reasoning and interpretation for regression/classification and cross-validation; not sufficient for executable scikit-learn competence. | Conditional: evaluated scikit-learn models and rigorous validation; a single challenge may address only regression or classification. | Conditional: explain supervised model choices and validation; not sufficient for both model families or implementation. |
| LO4 | Proposed: reason about clustering/reduction and interpret domain results; not sufficient for application evidence. | Conditional: justified clustering/reduction with domain interpretation, only if relevant; no guaranteed coverage. | Conditional: interpret such analyses if used; no guaranteed coverage. |
| LO5 | Proposed: formulate an MDP and reason through Q-learning/policy-gradient behaviour; not sufficient for executing an RL solution. | Conditional: RL implementation only if compatible with the task; ordinary static-data challenges need not support it. | Conditional: explain RL solution if used; no guaranteed implementation evidence. |
| LO6 | Proposed: reason about training, gradients and overfitting controls; not sufficient for TensorFlow/Keras implementation. | Conditional: trained regularised TensorFlow/Keras network if justified by task; deep learning is not mandatory in the assessment description. | Conditional: explain network training and regularisation if used; not sufficient for execution evidence. |
| LO7 | Proposed: interpret metrics, diagnose bias-variance and justify optimisation and validation decisions. | Proposed: documented metric choice, diagnostics, tuning experiments and independent evaluation; leaderboard rank alone is insufficient. | Conditional: defend metrics, model selection and limitations within the capstone scope. |
| LO8 | Proposed: critique pipeline design and interpretation; not sufficient for execution, documentation and presentation together. | Direct alignment for design/execution and documentation: competition result plus methodology/experiments/findings report; does not alone satisfy oral presentation. | Direct alignment for presenting methodology/results; combined with K supports the full outcome. |

The strongest direct assessment alignment is LO8 across K and P. No descriptor text guarantees that every student demonstrates the practical components of LO2–LO6 through the three assessments. Proposed session evidence can diagnose learning formatively; it does not silently become a fourth assessment or a graded requirement. Professor review must decide how satisfactory evidence is established within the approved scheme, or seek institutional approval if a requirement change is necessary.

## Review and use

Read [gaps and recommendations](traceability-gaps.md) separately from the approved requirements. See [validation report](traceability-validation.md) and run `python -s curriculum/validate_traceability.py` from the repository root. Review status remains pending even when structural checks pass. This audit creates no lessons, exam questions, answer keys, assessment rubrics or student submissions.
