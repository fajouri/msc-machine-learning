# S01 — ML foundations and Python stack: lecture and slide source

Issue #13. Public student-readable source and slide-by-slide professor notes; pending professor review. The approved outcome is **LO1: Explain and compare supervised, unsupervised, and reinforcement learning paradigms, identifying appropriate algorithms for given problem types.** Block B01 and the working online S01 topic inventory are retained. The visual tokens, slide vocabulary and seven public-note fields follow templates/lecture/design-system.md. Every diagram below is an original text specification; no third-party figure, chapter, code or data is copied.

The approved M5 assessment structure is a three-hour written exam (60%), a Kaggle capstone challenge with final model/leaderboard evidence and a methodology/experiments/findings report (30%), and a ten-minute presentation of capstone methodology and results (10%). The production plan places the written exam on campus. No internal split of the project mark or grading rubric is specified. The separate university-administered two-hour certification activity is distinct from the M5 exam. S01 practice remains ungraded.

## 1. Framing and notation

Machine learning is a family of procedures that use data or interaction to choose a rule whose behaviour is evaluated against a defined task. The question is not merely “which algorithm?” First establish what can be observed, what feedback exists, which future cases matter, the cost of errors and whether the recorded data represent those cases. A fitted rule is an estimate under assumptions, not a property of the world.

Let an observation i have feature vector **x**ᵢ ∈ ℝᵖ, with p measured features. For n observations, **X** ∈ ℝⁿˣᵖ has one row per observation. A supervised target yᵢ may be numeric, categorical or structured. A random pair (X,Y) denotes a data-generating population; (xᵢ,yᵢ) is an observed pair. A data table is not automatically an independent random sample from that population. Units, measurement time and provenance belong in the schema. A feature that is only known after the decision point is unavailable for real deployment even if it appears in a spreadsheet.

For a supervised predictor fθ, a loss ℓ(fθ(xᵢ),yᵢ) states how a prediction is judged. The empirical risk on a training set T is R̂_T(θ)=|T|⁻¹ Σᵢ∈T ℓ(fθ(xᵢ),yᵢ). This is an average of observed losses, not the population risk R(θ)=E[ℓ(fθ(X),Y)] on future cases. Training reduces the former; validation estimates behaviour under a specified sampling protocol. The estimate is only relevant if the protocol resembles use. An outcome measured with systematic error can make a low loss scientifically misleading.

In unsupervised learning, the input is **X** without a task label y. An objective is still needed: for example, k-means chooses assignments zᵢ and centres μₖ ∈ ℝᵖ to reduce Σᵢ ||xᵢ−μ_{zᵢ}||². This objective measures compactness in a chosen feature space; it does not discover an objectively true social or clinical category. Feature scale and distance choice alter the result. Cluster labels are arbitrary names, not known ground truth.

In reinforcement learning, an agent observes state sₜ, chooses action aₜ, receives reward rₜ₊₁ and a new state sₜ₊₁. A policy π(a|s) specifies action probabilities. A common objective is E_π[Σₜ₌₀^∞ γᵗ rₜ₊₁], with discount 0≤γ<1 for a bounded infinite-horizon illustration. This sum expresses delayed consequences; γ is a modelling choice, not an ethical weight. State and reward design, safe exploration and simulator-to-reality transfer matter. S11/S12 develop MDPs and Q-learning; here the equation only distinguishes sequential feedback from a fixed labelled table.

## 2. Paradigm choice under a common set of criteria

| Criterion | Supervised | Unsupervised | Reinforcement |
| --- | --- | --- | --- |
| Available signal | Paired features and a target defined for training cases | Features or observations without the proposed task target | State, feasible actions, transitions and reward through interaction |
| Immediate purpose | Predict a defined target for new cases | Represent structure under a specified similarity/objective | Choose actions to improve cumulative consequences |
| Candidate algorithm family | Constant/majority baseline, linear model, tree; choice depends on target and constraints | k-means or hierarchical grouping for a distance-based question; PCA for variance-preserving projection | Contextual bandit for independent action rounds; value or policy methods for sequential state effects |
| What can falsify the claim? | Out-of-sample error under a justified split and a relevant baseline | Instability, implausible metric, no domain utility, changed result under scale/distance | Poor return or unsafe behaviour under a credible evaluation policy/environment |
| Frequent mistake | Using future information or fitting a transformation before splitting | Calling discovered clusters true labels | Treating logged rewards as unbiased evidence for an untried policy |

These families can coexist in a project. A set of patient measurements might be clustered for exploration and later support a supervised prediction once a reliable outcome is defined. A recommendation decision may be supervised if it predicts a known rating for a fixed context, a contextual bandit if actions change observed reward but not future context, or sequential RL if actions affect later states. State the causal/temporal assumption before naming an algorithm. Do not infer a paradigm from whether code uses a particular library.

## 3. Scientific Python and a defensible workflow

Python supplies control flow, data structures, environments and tests. NumPy supplies homogeneous n-dimensional arrays and vectorised numerical operations; pandas supplies labelled tables, missing-value inspection and joins; Matplotlib supplies plots whose axes and units require interpretation; scikit-learn provides estimators, preprocessing pipelines and evaluation utilities. Colab is a hosted execution environment, not an ML method. In S01 students convert the same original synthetic rows into a 24×2 NumPy array of x and y and a 24×3 pandas DataFrame that also includes row_id. They select columns positionally or by name and calculate count, mean, minimum and maximum. These are descriptive views of constructed data; they do not fit a model or establish generalisation. The notebook checks NumPy 2.1.3 and pandas 2.2.3 on Python 3.10–3.13 CPU and records actual versions. S02 applies pandas/scikit-learn to cleaning, feature engineering, scaling and encoding. A tool can make a transformation convenient; it cannot decide whether that transformation is permitted by the study design.

A workflow starts with a decision question and a target population. Inventory provenance, rights, measurement times and missingness. Define units and a split protocol before fitting anything. Reserve a validation role and, when a credible final performance claim is required, a truly untouched final test set; 24 synthetic rows in this introductory demonstration cannot support such a claim. Fit baselines on training rows only. Compare methods under the same protocol, report uncertainty and error costs, audit representativeness and document the model/data/environment revision. Deployment introduces monitoring for changing data and harms. This sequence is a reasoning scaffold, not a claim that S01 teaches the detailed preprocessing of S02 or cross-validation of S07.

### Worked example distinct from independent work

The notebook generates 24 original, dimensionless rows x and y from a documented arithmetic rule. A deterministic SHA-256 sort selects 18 training and 6 validation IDs using seed 42. This is a reproducible partition, not a random sample of people. Fit a **constant** c by minimising L(c)=Σᵢ∈T(yᵢ−c)². Expanding gives Σyᵢ²−2cΣyᵢ+nc²; differentiate to obtain dL/dc=−2Σyᵢ+2nc. Setting it to zero yields c=Σyᵢ/n; the second derivative 2n>0 makes it the unique minimum for n>0. Here y and c share dimensionless units; L has squared-response units. If each large residual is costly, this baseline is interpretable, but it ignores x and squared loss magnifies outliers.

Validation mean squared error is MSE_V=|V|⁻¹ Σᵢ∈V(yᵢ−c)². The estimate c uses only T. V evaluates that frozen choice. Repeatedly choosing algorithms or seeds because they score well on V turns V into training information. The notebook prints exact rational values, split IDs and a data hash so another learner can detect a changed generator or partition. Identical results across reruns demonstrate computational repeatability, not statistical precision, causal validity, external validity or societal fairness. A changed split may change MSE even when the data generator stays fixed.

### Assumptions, alternatives and ethics

The illustration assumes rows are independent for the split argument, stable in meaning, and available before prediction. Those assumptions fail for time series, families, sites or repeated measures; split by time/group where the application demands. A constant or majority baseline is a necessary reference but rarely sufficient. A richer model may reduce systematic error while increasing variance, complexity and explanation cost; defer actual regression fitting to S03. For clustering, articulate why Euclidean distance and compact groups are appropriate; for RL, articulate reward validity and exploration safety. In all cases, ask who is represented and who bears an error. Statistical bias (difference between an estimator's expectation and target) is distinct from unfair treatment of groups. This synthetic dataset has no demographic groups and cannot support a fairness metric.

## 4. Slide-by-slide presentation source

Use one principal claim per slide, 16:9, selectable text, minimum proposed 24 pt body and 18 pt citation footers. Slide IDs are stable. Each note has the seven AUTO-02 fields and is safe to distribute to students. Times locate the slide within the run sheet; activities may continue while the slide stays visible.

### SL01 · opening · A task before an algorithm
**Visible:** M5 orientation: written exam 60% (three hours); Kaggle challenge plus technical report 30%; ten-minute capstone presentation 10%. S01 practice is ungraded. Prompt: “What observation, feedback and future decision does this problem contain?” **LO:** LO1. **Visual:** Original three-lane text diagram: fixed labelled examples; unlabelled examples; state → action → reward → new state. **Source/alt text:** Original diagram; arrows in the third lane denote temporal feedback, not causation proven by data.
**Public speaker notes**
- **Explanation:** Spend three minutes orienting students to the approved 60/30/10 structure. The exam is three hours and on campus; the Kaggle project combines final model/leaderboard evidence with a technical report, and the presentation is ten minutes. Do not imply a split within the 30% or that today's prompts are graded. Read the three original diagram lanes as fixed labelled examples, unlabelled observations and action-dependent feedback.
- **Reasoning:** Ask what observation, feedback and future decision each lane would require. A useful quick answer is that labels support a prediction task, absent task labels invite a structural question, and repeated actions with later rewards suggest sequential decisions. Students may mistake “uses Python” for a paradigm; a tool does not define the task.
- **Timing:** 0–8 minutes: three for assessment orientation, three for the diagnostic prompt and two to collect the first distinctions.
- **Participation online:** Invite short speech or chat replies; cameras remain optional. Keep assessment questions in the agreed course channel if they need an institutional answer.
- **Participation campus:** Use individual response cards followed by a neighbour comparison.
- **Fallback:** Read the assessment percentages and diagram lanes from the distributed text; if Meet fails, use the pre-agreed recovery route.
- **Transition:** State the exact approved LO1 wording on SL02.

### SL02 · outcomes · The approved LO1
**Visible:** “Explain and compare supervised, unsupervised, and reinforcement learning paradigms, identifying appropriate algorithms for given problem types.” No other outcome is claimed. **LO:** LO1.
**Public speaker notes**
- **Explanation:** Read LO1 verbatim. “Explain” requires a signal and objective for each paradigm; “compare” requires applying the same criteria; “identify” requires a conditional algorithm choice for a specified problem. The lesson's synthetic Python example supports this reasoning but does not add a new assessed outcome.
- **Reasoning:** Ask what evidence must precede an algorithm name. A concise answer is the available target or reward, the intended decision and the observations available when the decision is made. Anticipate “we can use a neural network for everything”; architecture choice cannot repair a missing target or invalid feedback.
- **Timing:** 8–12 minutes, including a one-minute response and a short bridge to notation.
- **Participation online:** Collect one evidence item per learner by chat or voice as time permits.
- **Participation campus:** Use the same one-sentence prompt on cards.
- **Fallback:** Read the exact wording from brief.md.
- **Transition:** Define what a row, feature and future case mean.

### SL03 · concept · Observations are not a population
**Visible:** Observed (xᵢ,yᵢ) versus future (X,Y); n rows, p features, X shape n×p. Units, time and provenance matter. **LO:** LO1.
**Public speaker notes**
- **Explanation:** Write xᵢ as one observed p-component feature vector, yᵢ as its observed target, and X as n rows by p columns; capital (X,Y) denotes a future random pair, not the table already in hand. State units and the time at which each field becomes known. In the notebook the 24-row table includes row_id, which is an identifier rather than automatically a useful feature.
- **Reasoning:** Ask whether a field recorded after the outcome may be used for an earlier decision. The formative answer is no: it is unavailable at that decision time, however predictive it appears retrospectively. Anticipate the misconception that a large table automatically represents future cases; selection and measurement processes must support that claim.
- **Timing:** 12–18 minutes, with a two-minute schema annotation.
- **Participation online:** Invite one candidate leakage field and one reason.
- **Participation campus:** Annotate a plain-text schema in pairs.
- **Fallback:** Read each row and column name aloud.
- **Transition:** A supervised task adds a defined target to those observations.

### SL04 · concept · Supervised learning needs a defined target
**Visible:** Paired X,y → fit fθ → predict unseen y; examples: numeric demand or category. Candidate families: constant baseline, linear model, tree. **LO:** LO1.
**Public speaker notes**
- **Explanation:** In the diagram X contains inputs known at prediction time, y is the training target, and fθ maps a new x to a prediction. Numeric and categorical targets invite different losses and baseline families. A measured target may be delayed or noisy, so the operational definition must be stated before fitting.
- **Reasoning:** If no training labels exist, a conventional supervised fit for that target cannot proceed; obtain defensible labels or ask a different question such as describing structure. This answer is about the general paradigm, not an exercise-sheet scenario. Warn that a field named “label” may still contain future information or an unreliable proxy.
- **Timing:** 18–23 minutes; reserve the last minute for the question.
- **Participation online:** Let a learner explain the missing-label consequence in text or speech.
- **Participation campus:** Ask pairs to identify input and target in a generic table.
- **Fallback:** Narrate the arrows in order, including the point when y is observed.
- **Transition:** A loss makes the supervised objective explicit.

### SL05 · equation · Empirical risk is an average on observed training data
**Visible:** R̂_T(θ)=|T|⁻¹Σᵢ∈T ℓ(fθ(xᵢ),yᵢ); R(θ)=E[ℓ(fθ(X),Y)]. **LO:** LO1. **Spoken equation:** Mean training loss versus expected future loss.
**Public speaker notes**
- **Explanation:** T is the set of training row indices, |T| its size, θ the predictor parameters, and ℓ a per-case loss in units determined by the task. The hat marks an observed sample average. The population expression is an expectation over future (X,Y), which we cannot calculate directly from the training table.
- **Reasoning:** Ask when training loss might approximate future loss. A compact answer is that training cases must be informative about the future distribution and the fitted rule must avoid exploiting quirks of those cases; even then, an independent evaluation design is needed. Do not equate a low empirical average with a proven deployment result.
- **Timing:** 23–28 minutes; speak the formula before displaying its symbols.
- **Participation online:** Ask for one assumption, accepting a written reply.
- **Participation campus:** Have students label T, θ and ℓ on the formula.
- **Fallback:** Read “average observed training loss” and “expected future loss” aloud.
- **Transition:** Remove y and ask what an unsupervised objective could measure.

### SL06 · concept · Unsupervised learning still makes choices
**Visible:** X without task labels; k-means seeks compactness under a specified distance; PCA seeks a variance-preserving low-dimensional representation. **LO:** LO1.
**Public speaker notes**
- **Explanation:** Unsupervised data lack the proposed task target y, but a method still imposes a criterion. K-means seeks compact groups under a chosen distance; PCA preserves a stated form of variance in a lower-dimensional linear representation. Neither method supplies domain labels by itself.
- **Reasoning:** A concise formative answer is that compact groups can mislead when a continuum is forced into categories or one measured variable dominates distance because of its units. Anticipate “unsupervised means no assumptions”; similarity and representation choices are assumptions.
- **Timing:** 28–32 minutes, with a brief counterexample exchange.
- **Participation online:** Request one limitation by chat or voice.
- **Participation campus:** Pair critique of two text-described groupings.
- **Fallback:** Read the alternatives without a visual plot.
- **Transition:** Show how the k-means objective encodes the compactness choice.

### SL07 · equation · A clustering objective encodes a worldview
**Visible:** min over z,μ of Σᵢ||xᵢ−μ_{zᵢ}||²; xᵢ,μₖ ∈ ℝᵖ. **LO:** LO1. **Spoken equation:** Sum squared distances to assigned centres.
**Public speaker notes**
- **Explanation:** Read the objective as a sum over rows of squared Euclidean distance to the centre assigned to each row. zᵢ is an assignment in {1,…,k}; μₖ and xᵢ are p-component vectors, so the objective has squared feature units only if features share a meaningful scale. The absence of y is deliberate.
- **Reasoning:** Changing a feature's units rescales its contribution to distance and can change assignments without changing the underlying cases. The formative answer is therefore that “the clusters” are conditional on the representation and metric. Do not imply this objective establishes naturally existing categories.
- **Timing:** 32–35 minutes; name symbols before interpreting minimisation.
- **Participation online:** Ask what happens if one feature is expressed in millimetres rather than metres.
- **Participation campus:** Mark the feature whose units dominate a hypothetical distance.
- **Fallback:** Describe “near a selected centre” in words.
- **Transition:** Some tasks require actions that alter later observations.

### SL08 · concept · Reinforcement learning evaluates a policy over time
**Visible:** sₜ → aₜ → (rₜ₊₁,sₜ₊₁); policy π(a|s); delayed consequences and safe exploration. **LO:** LO1.
**Public speaker notes**
- **Explanation:** Identify sₜ as information available now, aₜ as a feasible decision, rₜ₊₁ as feedback after that decision, and sₜ₊₁ as the next observation. A policy π(a|s) can be deterministic or probabilistic. Merely predicting a known label is not automatically reinforcement learning.
- **Reasoning:** The key question is whether actions affect subsequent state or available evidence. For a generic inventory decision, ordering today can change tomorrow's stock and shortage cost. Logged data from one policy may omit outcomes of alternatives, so evaluation needs a justified environment or careful off-policy assumptions.
- **Timing:** 35–38 minutes; use one two-step verbal trace.
- **Participation online:** Ask for a state change caused by an action.
- **Participation campus:** Sketch two time steps with labelled arrows.
- **Fallback:** Read the tuple in temporal order.
- **Transition:** Delayed consequences motivate a return rather than a single-step score.

### SL09 · equation · Return combines delayed rewards
**Visible:** J(π)=E_π[Σₜ₌₀^∞ γᵗrₜ₊₁], 0≤γ<1. **LO:** LO1. **Spoken equation:** Expected discounted sum of subsequent rewards.
**Public speaker notes**
- **Explanation:** J(π) is an expected value under trajectories induced by the policy. At time t, γᵗ discounts the subsequent reward rₜ₊₁; 0≤γ<1 and bounded rewards make this illustrative infinite sum finite. Reward units carry through the sum, while γ is dimensionless.
- **Reasoning:** A larger γ weights later rewards more, but it does not make an unsafe action permissible or prove a reward is aligned with human interests. A general unsafe-exploration answer is an irreversible action with potential harm before its payoff can be learned. Leave MDP solution methods to S11/S12.
- **Timing:** 38–40 minutes; give only the interpretation needed for paradigm comparison.
- **Participation online:** Accept one safety concern in chat.
- **Participation campus:** Ask for a one-sentence interpretation of γ.
- **Fallback:** Read “expected discounted sum of later rewards” aloud.
- **Transition:** Give students time to defend a formulation independently.

### SL10 · activity · Defend a formulation
**Visible:** For each scenario, name the available signal, goal, plausible paradigm and one missing fact. Use exercise A. **LO:** LO1.
**Public speaker notes**
- **Explanation:** Use exercise A only. Students first write the available signal, decision time, proposed objective, plausible paradigm/algorithm family and one missing fact; then peers challenge assumptions. Facilitate without displaying a solved exercise sheet or treating a majority vote as evidence of correctness.
- **Reasoning:** The formative standard is a conditional justification: “if this target/reward is actually observed and available at the right time, this family is plausible; otherwise I would reformulate.” More than one answer can be defensible if the goal or feedback changes. Do not give case-specific answers to the independent extension.
- **Timing:** 40–65 minutes: five alone, ten pair/main-room exchange and ten plenary critique.
- **Participation online:** Arrange five pairs if available or structured turns in the main Meet room; gather ten individual statements.
- **Participation campus:** Five pairs rotate explainer and challenger; finish with individual notes.
- **Fallback:** Use the downloaded text sheet and recover missed live discussion through the agreed route.
- **Transition:** Examine a separate worked device-log example and its data flow.

### SL11 · comparison · Same case, different question
**Visible:** A device log: predict next-day failure (label); group behaviour profiles (no task label); schedule maintenance actions with downstream cost (sequential feedback). **LO:** LO1. **Visual:** Original three-column native-table specification, read row-wise.
**Public speaker notes**
- **Explanation:** This is an original worked teaching case, separate from the unanswered exercise scenarios. For next-day failure prediction, a verified outcome is required; for grouping, describe structure without claiming true classes; for maintenance scheduling, actions, later states and costs must be observed or credibly simulated.
- **Reasoning:** The formative answer to “which columns require new data?” is conditional: the first framing needs failure outcomes, the second needs a defensible feature representation, and the third needs action and downstream feedback records. A device log alone may not contain all three. Do not infer causality from a label or a cluster.
- **Timing:** 65–70 minutes, ending with a one-minute comparison.
- **Participation online:** Ask learners to name a missing field in the worked table.
- **Participation campus:** Annotate the three rows in pairs.
- **Fallback:** Read each row and the required signal aloud.
- **Transition:** Show how Python represents and records the same observations.

### SL12 · concept · The scientific Python stack has distinct jobs
**Visible:** Python: reproducible program; NumPy: 24×2 numeric array; pandas: 24×3 labelled table with row_id; Matplotlib: plots; scikit-learn: estimators and pipelines; Colab: hosted runtime. Compare column selection and means on the same original rows. **LO:** LO1 through enabling workflow.
**Public speaker notes**
- **Explanation:** In the notebook, Python generates the 24 original rows; NumPy arranges x and y in a 24×2 integer array, while pandas builds a 24×3 labelled table that also includes row_id. Slicing array[:,0] and selecting frame["x"] reach the same x values through position and name. Descriptive count/mean/min/max summarise the constructed rows; they are not a model fit.
- **Reasoning:** The data version and SHA-256 identify the generator output, while Python/NumPy/pandas versions identify the execution environment. A 24×3 DataFrame does not imply three predictive features: row_id is an identifier. Matplotlib and scikit-learn are named for their future roles; S02 owns preprocessing and S03 owns regression fitting.
- **Timing:** 70–77 minutes: two for roles, three for array/table shapes and two for a guided comparison.
- **Participation online:** Ask why the two shapes differ; the concise answer is the extra identifier column.
- **Participation campus:** Compare positional and named selection at each device.
- **Fallback:** Use the printed three-column table and shape descriptions; recover package execution later.
- **Transition:** Before fitting any estimate, separate row roles.

### SL13 · figure · Separate fitting from checking
**Visible:** Original editable-shapes plan: data version → partition IDs → training-only fit → frozen predictor → validation score → qualified interpretation. Dashed arrow from validation back to design is labelled “selection uses validation information.” **LO:** LO1. **Alt text:** Six ordered stages; validation should not feed the fitted estimate, although repeated model selection consumes validation information.
**Public speaker notes**
- **Explanation:** Read the six stages in order: identify the dataset, record partition IDs, fit only on training rows, freeze the predictor, calculate a validation score and qualify the interpretation. A fitted statistic or transformation that uses validation rows before evaluation would compromise that check. The dashed arrow back to design marks model selection, which is allowed for development but consumes validation information.
- **Reasoning:** Ask which arrow would be direct leakage. The concise answer is a new arrow from validation rows into the training fit or a fitted preprocessing step. Repeatedly selecting the best-looking design on the same validation set is a different source of optimistic bias, not a pristine final test. This early distinction prepares for S07 without teaching its full cross-validation methods.
- **Timing:** 77–82 minutes: three for sequence, two for the arrow question.
- **Participation online:** Ask a learner to narrate the arrows in text.
- **Participation campus:** Draw the permitted and prohibited flows on paper.
- **Fallback:** Read the stage sequence from lecture.md without the diagram.
- **Transition:** Derive one transparent training-only baseline.

### SL14 · equation · Training-only constant is a defensible baseline
**Visible:** L(c)=Σᵢ∈T(yᵢ−c)²; dL/dc=−2Σyᵢ+2nc=0; c=mean_T(y). **LO:** LO1. **Spoken equation:** The squared-error-minimising constant is the training mean.
**Public speaker notes**
- **Explanation:** For n=|T|>0 training responses, expand L(c) to Σyᵢ²−2cΣyᵢ+nc². Its derivative vanishes when c equals the training mean, and the second derivative 2n>0 confirms a minimum. Define c as a constant prediction with the same units as y; each squared residual and L has squared y units.
- **Reasoning:** The formative answer to “what can it not learn?” is any relationship between x and y, because x never appears in L(c). It is a transparent baseline against which a future fitted model can be judged, not the regression lesson itself. Do not use validation y values to obtain c.
- **Timing:** 82–87 minutes: three for intermediate algebra and two for interpretation.
- **Participation online:** Invite a prediction before revealing the training mean.
- **Participation campus:** Check units and the positive second derivative in pairs.
- **Fallback:** Read the derivation line by line from section 3.
- **Transition:** Execute the documented generator and compare the recorded evidence.

### SL15 · worked_example · Reproduce the result, then question it
**Visible:** Original 24-row synthetic generator; NumPy/pandas versions; seed 42; 18/6 split; print data SHA-256, IDs, rational c and MSE. Do not display independent-task results. **LO:** LO1.
**Public speaker notes**
- **Explanation:** Before the break, preview the 24-row generator and 18/6 partition. After the break, have learners Run all in a fresh CPU runtime, including the pinned dependency check, NumPy/pandas shape and summary cells, and exact-fraction baseline. Read Python/package versions, seed, data version/hash and partition IDs as separate reproducibility evidence.
- **Reasoning:** An identical hash says the generated rows match; matching split IDs says their assigned roles match; matching rational scores says this computation repeats. None establishes sampling validity, uncertainty, population performance or fairness. Anticipate the misconception that the pandas mean is the model result: the descriptive full-table mean is not the training-only constant.
- **Timing:** 87–90 minutes for preview; 100–125 minutes for student execution and guided interpretation. Preserve the 90–100 break.
- **Participation online:** Ask for shape, version and hash checks through chat without account or personal details.
- **Participation campus:** Rotate driver/reviewer; each learner saves an individual version record.
- **Fallback:** Use the downloaded table and formulas for interim reasoning; later supervised execution remains necessary.
- **Transition:** Students now design, but do not receive answers to, the independent sensitivity study.

### SL16 · activity · What changes when a partition changes?
**Visible:** Plan a finite-seed investigation before code; preserve the original run; record design, scores, interpretation and limits privately. **LO:** LO1.
**Public speaker notes**
- **Explanation:** Direct students to the unanswered student-experiment cell. Ask them to predeclare a finite seed list, retain the original run, record each partition and score, and explain why a changed partition might alter the validation score. The public format checker verifies only record shape when attempted.
- **Reasoning:** A suitable formative response names a planned comparison and a limitation without supplying numerical outcomes or code. Scores from overlapping partitions are dependent; a spread of them is not automatically a confidence interval. Repeatedly picking a preferred seed because it looks good would contaminate the intended comparison.
- **Timing:** 125–140 minutes: three for instructions, nine for independent planning/coding and three for limitations.
- **Participation online:** Ask for one hypothesis and one caveat, not completed work.
- **Participation campus:** Require each learner's own plan after pair discussion.
- **Fallback:** Write pseudocode privately; arrange later supervised execution.
- **Transition:** Return from the worked supervised path to three-way paradigm choice.

### SL17 · synthesis · A model choice is conditional
**Visible:** Ask: signal? objective? baseline? evaluation protocol? affected people? Three paradigms can coexist. **LO:** LO1.
**Public speaker notes**
- **Explanation:** Reapply the same criteria to all three paradigms: observed signal, task objective, candidate family, evaluation evidence and affected people. Invite students to revise a formulation when a target is missing, a distance is unhelpful or actions change future states. Do not require a single method for every project.
- **Reasoning:** Statistical estimator bias/variance concerns repeated estimates relative to a defined target; societal fairness concerns the distribution and consequences of errors among people or groups. The synthetic rows represent no population or protected groups, so the notebook cannot support a fairness metric. A formative answer should name a missing dataset or deployment fact before claiming safety or effectiveness.
- **Timing:** 140–165 minutes: ten for paired critique, ten for ten short individual turns and five for synthesis.
- **Participation online:** Use chat or speech; allow a private equivalent route for an accessibility need.
- **Participation campus:** Pair critique followed by an individual written caveat.
- **Fallback:** Read the comparison matrix and collect responses after approved live recovery.
- **Transition:** Ask each learner for an individual LO1 explanation and preview S02.

### SL18 · references and handoff · Read, test, prepare
**Visible:** Verified link-only readings: [Géron (2022), publisher whole-work page](https://www.oreilly.com/library/view/hands-on-machine-learning/9781098125967/); [Goodfellow, Bengio and Courville (2016), author page and §5 Machine Learning Basics](https://www.deeplearningbook.org/); [Hastie, Tibshirani and Friedman (2009), publisher whole-work page](https://doi.org/10.1007/978-0-387-84858-7). S02: cleaning, encoding and EDA with pandas/scikit-learn. **LO:** LO1.
**Public speaker notes**
- **Explanation:** Give students the three verified link-only readings without reproducing publisher text. Géron's publisher listing and the Goodfellow author table of contents support the displayed reading locators; the Hastie link is a whole-work publisher record. The Ng entry remains unresolved in references.md and is not assigned here.
- **Reasoning:** S02 begins from the row schema, split IDs and environment record already practised, then owns actual cleaning, encoding, scaling and EDA under LO2. An appropriate exit response conditionally names a paradigm and algorithm family, plus one validation or ethical limit; it does not need a fitted model. Keep any assessment-policy clarification separate from formative feedback.
- **Timing:** 165–180 minutes: two for reading and S02 handoff, ten for independent exit responses and three for access/recovery needs.
- **Participation online:** Collect ten individual responses by speech or chat; handle account issues privately.
- **Participation campus:** Use individual written exit cards.
- **Fallback:** Use the pre-agreed private response route and restore lost synchronous teaching as approved.
- **Transition:** End; no exam answer or independent exercise solution is distributed.

## Sources, rights and review boundary

All substantive exposition, equations, scenarios and diagram specifications above are original pedagogical writing. The three link-only reading uses on SL18 and in the reading plan are recorded in references/citation-usage.json with verified whole-work or table-of-contents locator and visible attribution. No publisher figure, passage or code is reproduced. See references.md for full bibliographic entries and the unresolved Ng metadata gate. This source has not been rendered as editable DOCX/PPTX or checked at screen-share scale. Professor review must inspect mathematical accuracy, LO1 coverage, readability and rights before release.
