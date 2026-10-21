# S01 — ML foundations and Python stack: lecture and slide source

Issue #13. Public student-readable source and slide-by-slide professor notes; pending professor review. The approved outcome is **LO1: Explain and compare supervised, unsupervised, and reinforcement learning paradigms, identifying appropriate algorithms for given problem types.** Block B01 and the working online S01 topic inventory are retained. The visual tokens, slide vocabulary and seven public-note fields follow templates/lecture/design-system.md. Every diagram below is an original text specification; no third-party figure, chapter, code or data is copied.

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

Python supplies control flow, data structures, environments and tests. NumPy supplies homogeneous n-dimensional arrays and vectorised numerical operations; pandas supplies labelled tables, missing-value inspection and joins; Matplotlib supplies plots whose axes and units require interpretation; scikit-learn provides estimators, preprocessing pipelines and evaluation utilities. Colab is a hosted execution environment, not an ML method. In S01 students use a standard-library example to inspect the same concepts without installation or external data. S02 applies pandas/scikit-learn to data preparation. A tool can make a transformation convenient; it cannot decide whether that transformation is permitted by the study design.

A workflow starts with a decision question and a target population. Inventory provenance, rights, measurement times and missingness. Define units and a split protocol before fitting anything. Reserve a validation role and, when a credible final performance claim is required, a truly untouched final test set; 24 synthetic rows in this introductory demonstration cannot support such a claim. Fit baselines on training rows only. Compare methods under the same protocol, report uncertainty and error costs, audit representativeness and document the model/data/environment revision. Deployment introduces monitoring for changing data and harms. This sequence is a reasoning scaffold, not a claim that S01 teaches the detailed preprocessing of S02 or cross-validation of S07.

### Worked example distinct from independent work

The notebook generates 24 original, dimensionless rows x and y from a documented arithmetic rule. A deterministic SHA-256 sort selects 18 training and 6 validation IDs using seed 42. This is a reproducible partition, not a random sample of people. Fit a **constant** c by minimising L(c)=Σᵢ∈T(yᵢ−c)². Expanding gives Σyᵢ²−2cΣyᵢ+nc²; differentiate to obtain dL/dc=−2Σyᵢ+2nc. Setting it to zero yields c=Σyᵢ/n; the second derivative 2n>0 makes it the unique minimum for n>0. Here y and c share dimensionless units; L has squared-response units. If each large residual is costly, this baseline is interpretable, but it ignores x and squared loss magnifies outliers.

Validation mean squared error is MSE_V=|V|⁻¹ Σᵢ∈V(yᵢ−c)². The estimate c uses only T. V evaluates that frozen choice. Repeatedly choosing algorithms or seeds because they score well on V turns V into training information. The notebook prints exact rational values, split IDs and a data hash so another learner can detect a changed generator or partition. Identical results across reruns demonstrate computational repeatability, not statistical precision, causal validity, external validity or societal fairness. A changed split may change MSE even when the data generator stays fixed.

### Assumptions, alternatives and ethics

The illustration assumes rows are independent for the split argument, stable in meaning, and available before prediction. Those assumptions fail for time series, families, sites or repeated measures; split by time/group where the application demands. A constant or majority baseline is a necessary reference but rarely sufficient. A richer model may reduce systematic error while increasing variance, complexity and explanation cost; defer actual regression fitting to S03. For clustering, articulate why Euclidean distance and compact groups are appropriate; for RL, articulate reward validity and exploration safety. In all cases, ask who is represented and who bears an error. Statistical bias (difference between an estimator's expectation and target) is distinct from unfair treatment of groups. This synthetic dataset has no demographic groups and cannot support a fairness metric.

## 4. Slide-by-slide presentation source

Use one principal claim per slide, 16:9, selectable text, minimum proposed 24 pt body and 18 pt citation footers. Slide IDs are stable. Each note has the seven AUTO-02 fields and is safe to distribute to students. Times locate the slide within the run sheet; activities may continue while the slide stays visible.

### SL01 · opening · A task before an algorithm
**Visible:** S01, ML foundations and Python stack. Prompt: “What observation, feedback and future decision does this problem contain?” **LO:** LO1. **Visual:** Original three-lane text diagram: fixed labelled examples; unlabelled examples; state → action → reward → new state. **Source/alt text:** Original diagram; arrows in the third lane denote temporal feedback, not causation proven by data.
**Notes — explanation:** Define the three questions students will ask of every case. **Reasoning:** A named tool does not determine the learning problem. **Timing:** 0–10. **Online:** Invite ten brief voice/chat diagnoses. **Campus:** Individual cards then pair comparison. **Fallback:** Read the lanes as text. **Transition:** Show approved outcome.

### SL02 · outcomes · The approved LO1
**Visible:** “Explain and compare supervised, unsupervised, and reinforcement learning paradigms, identifying appropriate algorithms for given problem types.” No other outcome is claimed. **LO:** LO1.
**Notes — explanation:** Explain the verbs: define, compare with common criteria, and condition an algorithm choice on evidence. **Reasoning:** An algorithm name alone does not meet LO1. **Timing:** 8–12. **Online:** Ask for one required piece of evidence. **Campus:** Same prompt on cards. **Fallback:** Quote the line from the downloaded brief. **Transition:** Establish notation.

### SL03 · concept · Observations are not a population
**Visible:** Observed (xᵢ,yᵢ) versus future (X,Y); n rows, p features, X shape n×p. Units, time and provenance matter. **LO:** LO1.
**Notes — explanation:** Define indices and shapes aloud. **Reasoning:** The sampling process and measurement time determine what prediction claims transfer. **Timing:** 12–18. **Online:** Ask whether a post-outcome field may be a predictor. **Campus:** Annotate a schema. **Fallback:** Plain-text row schema. **Transition:** Add the target signal.

### SL04 · concept · Supervised learning needs a defined target
**Visible:** Paired X,y → fit fθ → predict unseen y; examples: numeric demand or category. Candidate families: constant baseline, linear model, tree. **LO:** LO1.
**Notes — explanation:** A target is an operational definition, not necessarily truth. **Reasoning:** A labelled table can still leak future information or mismeasure the outcome. **Timing:** 18–23. **Online:** Ask what changes if labels are unavailable at training time. **Campus:** Pair explanation. **Fallback:** Read data flow as text. **Transition:** State the loss.

### SL05 · equation · Empirical risk is an average on observed training data
**Visible:** R̂_T(θ)=|T|⁻¹Σᵢ∈T ℓ(fθ(xᵢ),yᵢ); R(θ)=E[ℓ(fθ(X),Y)]. **LO:** LO1. **Spoken equation:** Mean training loss versus expected future loss.
**Notes — explanation:** Define T, θ, ℓ and the two denominators/domains. **Reasoning:** Minimising the first does not prove the second is small; the split must represent intended use. **Timing:** 23–28. **Online:** Ask for an assumption needed to compare them. **Campus:** Annotate symbols. **Fallback:** Give the two formulas in words. **Transition:** Remove labels and ask what objective remains.

### SL06 · concept · Unsupervised learning still makes choices
**Visible:** X without task labels; k-means seeks compactness under a specified distance; PCA seeks a variance-preserving low-dimensional representation. **LO:** LO1.
**Notes — explanation:** Cluster IDs are assigned names, not external truth. **Reasoning:** Scaling and distance can change the partition; projected variance need not equal usefulness. **Timing:** 28–32. **Online:** Ask for a case where compact clusters mislead. **Campus:** Pair critique. **Fallback:** Text description of two alternative groupings. **Transition:** Display the objective.

### SL07 · equation · A clustering objective encodes a worldview
**Visible:** min over z,μ of Σᵢ||xᵢ−μ_{zᵢ}||²; xᵢ,μₖ ∈ ℝᵖ. **LO:** LO1. **Spoken equation:** Sum squared distances to assigned centres.
**Notes — explanation:** Define zᵢ, centre and squared units; no y appears. **Reasoning:** Minimisation is compactness in the selected representation, not a proof of natural kinds. **Timing:** 32–35. **Online:** Ask what changing units does. **Campus:** Mark a distance-dependent example. **Fallback:** Describe distances verbally. **Transition:** Introduce actions and delayed feedback.

### SL08 · concept · Reinforcement learning evaluates a policy over time
**Visible:** sₜ → aₜ → (rₜ₊₁,sₜ₊₁); policy π(a|s); delayed consequences and safe exploration. **LO:** LO1.
**Notes — explanation:** A reward is feedback after action, potentially dependent on the action. **Reasoning:** Logged data about one policy do not automatically validate another. **Timing:** 35–38. **Online:** Ask how an action can change tomorrow's state. **Campus:** Trace a two-step paper example without numerical solution. **Fallback:** Read the transition tuple. **Transition:** State the objective.

### SL09 · equation · Return combines delayed rewards
**Visible:** J(π)=E_π[Σₜ₌₀^∞ γᵗrₜ₊₁], 0≤γ<1. **LO:** LO1. **Spoken equation:** Expected discounted sum of subsequent rewards.
**Notes — explanation:** Define policy, horizon, reward and γ; bounded reward is assumed for this infinite sum. **Reasoning:** A larger γ gives later rewards more numerical influence, but reward design and safety cannot be settled by γ. **Timing:** 38–40. **Online:** Ask for an unsafe exploration case. **Campus:** Same oral question. **Fallback:** Verbal formula. **Transition:** Students classify scenarios.

### SL10 · activity · Defend a formulation
**Visible:** For each scenario, name the available signal, goal, plausible paradigm and one missing fact. Use exercises A–C. **LO:** LO1.
**Notes — explanation:** Give five minutes alone, then peer critique. **Reasoning:** Some scenarios admit more than one formulation under different evidence. **Timing:** 40–65. **Online:** Five pairs or structured main-room turns. **Campus:** Five paired cards. **Fallback:** Downloaded exercise sheet. **Transition:** Show a reproducible supervised illustration.

### SL11 · comparison · Same case, different question
**Visible:** A device log: predict next-day failure (label); group behaviour profiles (no task label); schedule maintenance actions with downstream cost (sequential feedback). **LO:** LO1. **Visual:** Original three-column native-table specification, read row-wise.
**Notes — explanation:** This is an invented non-identifying case, not empirical evidence. **Reasoning:** Data access and goal change the valid formulation; none of these claims is established by merely collecting logs. **Timing:** 65–70. **Online:** Ask which columns require new data. **Campus:** Annotate table. **Fallback:** Read each row. **Transition:** Map the Python stack.

### SL12 · concept · The scientific Python stack has distinct jobs
**Visible:** Python: reproducible program; NumPy: numerical arrays; pandas: labelled tables; Matplotlib: plots; scikit-learn: estimators and pipelines; Colab: hosted runtime. **LO:** LO1 through enabling workflow.
**Notes — explanation:** Explain shape, type, index, missingness and API roles. **Reasoning:** Library availability does not justify a split or loss. The S01 notebook uses standard library to make each operation inspectable; S02 teaches pandas cleaning and preprocessing. **Timing:** 70–77. **Online:** Ask what artifact records the data version. **Campus:** Map tools to workflow. **Fallback:** Read text list; no live installation. **Transition:** Show split discipline.

### SL13 · figure · Separate fitting from checking
**Visible:** Original editable-shapes plan: data version → partition IDs → training-only fit → frozen predictor → validation score → qualified interpretation. Dashed arrow from validation back to design is labelled “selection uses validation information.” **LO:** LO1. **Alt text:** Six ordered stages; validation should not feed the fitted estimate, although repeated model selection consumes validation information.
**Notes — explanation:** Clarify split before fitting. **Reasoning:** Validation is an estimate under a protocol, not a final universal score. **Timing:** 77–82. **Online:** Ask which arrow creates leakage. **Campus:** Draw arrows on paper. **Fallback:** Use the sentence sequence. **Transition:** Derive the baseline.

### SL14 · equation · Training-only constant is a defensible baseline
**Visible:** L(c)=Σᵢ∈T(yᵢ−c)²; dL/dc=−2Σyᵢ+2nc=0; c=mean_T(y). **LO:** LO1. **Spoken equation:** The squared-error-minimising constant is the training mean.
**Notes — explanation:** Expand one square, sum, differentiate and note d²L/dc²=2n>0. **Reasoning:** This model ignores x, establishing a reference point rather than a regression lesson. c has y units; loss has squared units. **Timing:** 82–87. **Online:** Predict what the model cannot learn. **Campus:** Check dimensions. **Fallback:** Read derivation in section 3. **Transition:** Run the notebook.

### SL15 · worked_example · Reproduce the result, then question it
**Visible:** Original 24-row synthetic generator; seed 42; 18/6 split; print Python version, data SHA-256, IDs, rational c and MSE. Do not display independent-task results. **LO:** LO1.
**Notes — explanation:** Demonstrate top-to-bottom execution and the meaning of each record. **Reasoning:** Same hash/score shows repeatability; no population or fairness claim follows. **Timing:** 87–90 and 100–125. **Online:** Learners compare records in text without sharing account details. **Campus:** Rotate driver/reviewer. **Fallback:** Trace the formulas and restore execution later. **Transition:** Independent investigation.

### SL16 · activity · What changes when a partition changes?
**Visible:** Plan a finite-seed investigation before code; preserve the original run; record design, scores, interpretation and limits privately. **LO:** LO1.
**Notes — explanation:** Refer to the unanswered notebook cell and exercise sheet. **Reasoning:** Variation across overlapping splits is not a confidence interval; repeated validation-based selection can bias claims. **Timing:** 125–140. **Online:** Ask for a hypothesis and limitation, not results. **Campus:** Each learner writes an independent plan. **Fallback:** Paper pseudocode followed by supervised execution. **Transition:** Compare paradigms and harms.

### SL17 · synthesis · A model choice is conditional
**Visible:** Ask: signal? objective? baseline? evaluation protocol? affected people? Three paradigms can coexist. **LO:** LO1.
**Notes — explanation:** Revisit the comparison matrix and an alternative formulation. **Reasoning:** Distinguish estimator bias/variance from societal fairness. Synthetic data have no protected groups and cannot establish fairness. **Timing:** 140–165. **Online:** Pair critique, then ten short turns. **Campus:** Pair and individual note. **Fallback:** Text matrix. **Transition:** Exit check and S02.

### SL18 · references and handoff · Read, test, prepare
**Visible:** Verified link-only readings: [Géron (2022), publisher whole-work page](https://www.oreilly.com/library/view/hands-on-machine-learning/9781098125967/); [Goodfellow, Bengio and Courville (2016), author page and §5 Machine Learning Basics](https://www.deeplearningbook.org/); [Hastie, Tibshirani and Friedman (2009), publisher whole-work page](https://doi.org/10.1007/978-0-387-84858-7). S02: cleaning, encoding and EDA with pandas/scikit-learn. **LO:** LO1.
**Notes — explanation:** The cited pages identify works; no protected excerpt or figure is reused. The §5 locator is confirmed by the author table of contents, not a claim about a specific argument there. **Reasoning:** Students carry schema/split/version habits into S02, which owns hands-on preprocessing. **Timing:** 165–180. **Online:** Individual exit response with choice and caveat. **Campus:** Written exit card. **Fallback:** Private written route and approved live recovery. **Transition:** End; unresolved access issues handled privately.

## Sources, rights and review boundary

All substantive exposition, equations, scenarios and diagram specifications above are original pedagogical writing. The three link-only reading uses on SL18 and in the reading plan are recorded in references/citation-usage.json with verified whole-work or table-of-contents locator and visible attribution. No publisher figure, passage or code is reproduced. See references.md for full bibliographic entries and the unresolved Ng metadata gate. This source has not been rendered as editable DOCX/PPTX or checked at screen-share scale. Professor review must inspect mathematical accuracy, LO1 coverage, readability and rights before release.
