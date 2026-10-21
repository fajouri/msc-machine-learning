# S01 — ML foundations and Python stack

Issue [#13](https://github.com/fajouri/msc-machine-learning/issues/13). Public teaching source, pending professor review. The **approved** MQF Level 7 Foundations block B01 includes ML paradigms and scientific Python. The working map **proposes** S01 online. The lecturer reports Google Meet, about ten students and Colab access. All timings and activities below are pedagogical proposals, not assessment changes.

## Approved outcome and scope

**LO1, exact wording:** “Explain and compare supervised, unsupervised, and reinforcement learning paradigms, identifying appropriate algorithms for given problem types.”

S01 addresses every clause of LO1 through a three-way comparison and justified problem classification. Python workflow supports that reasoning. The notebook's constant predictor illustrates reproducibility, not the regression methods allocated to S03. S02 owns cleaning, preprocessing, feature engineering and EDA under LO2. Activities are formative. The approved 60/30/10 assessment weights and separate three-hour exam are unchanged.

## Entry and materials

The descriptor expects M3 or M4, Python proficiency and basic statistics. Diagnose comfort with arrays, means, population versus sample and splits in the first ten minutes. Send the selectable-text pack, notebook and outage rule through the confirmed institutional channel before class. Colab needs a Google account and internet; an already tested local Python 3.10+ environment is an alternative. No paid service, GPU, Drive mount, external dataset or credentials are needed. Original synthetic data, data hash, partition IDs, Python version and seed are recorded.

SETUP-02 #2, AUTO-01 #7, AUTO-02 #8 and AUTO-03 #9 are closed and their local source contracts are present. Their closure is not professor approval. AUTO-02's supported DOCX/PPTX runtime is unavailable. The course-builder preflight passed before initialisation.

## Continuous 180-minute run sheet

Elapsed minutes include a proposed ten-minute break; confirm institutional break accounting. Use Meet speech or chat, cameras optional, and a private equivalent for access needs. Facilitate ten individual contributions without recording names in public artifacts.

| Minutes | Professor explanation and activity | Engagement evidence | Fallback |
| --- | --- | --- | --- |
| 0–10 | Access, agenda and diagnostic: identify feature, label and action in short scenarios. State LO1. | Every learner gives a tentative paradigm and reason. | Use downloaded scenario text; resolve access privately. |
| 10–40 | Define prediction, representation and sequential decisions. Explain observations versus a target population; introduce supervised (X,y), unsupervised X, RL (s,a,r,s'). | At 25 and 38 minutes ask for a missing datum or counterexample. | Read the comparison table and describe diagrams aloud. |
| 40–65 | Five minutes individual classification, then five pairs or main-room turns. Challenge label/reward availability and candidate algorithm families. | Ten justified choices; peers name assumptions that could reverse them. | Downloaded worksheet and later private response after contact recovery. |
| 65–90 | Demonstrate row schema, deterministic data, partition IDs, training-only constant, validation loss and environment record. Explain dimensions and why matching hashes do not prove quality. | Predict baseline behaviour; identify which rows influence its estimate. | Trace formulas and workflow in text, then recover supervised execution. |
| 90–100 | Break. | Return check via voice/chat. | Independent contact route carries reconnection instruction. |
| 100–140 | Students run notebook in fresh Colab CPU runtime. Inspect schema/hash/split, annotate guided example, design independent seed-sensitivity study. | At 115 minutes record version/hash; at 130 name a limitation; at 140 save private copy. | Tested local Python path or interim paper reasoning; restore execution later. |
| 140–165 | Compare paradigms using common criteria: signal, objective, algorithm family, feedback, evaluation. Discuss leakage, sampling and misuse. | Pairs critique an alternative and state evidence that could falsify their choice. | Text matrix and exercise sheet. |
| 165–180 | Individual exit: defend a paradigm for a fresh scenario, candidate algorithm family and one validation/ethical limit. Preview S02. | Ten independent explanations, ungraded. | Private written response after approved live recovery. |

The delivery plan proposes one reconnection attempt after five minutes of Meet failure and suspension/recovery after fifteen minutes without usable live teaching. Confirm this rule and the independent institutional contact channel before delivery. Offline work does not silently replace synchronous contact.

## Campus and accessibility adaptations

For an authorised campus version, retain the intellectual sequence and 180 minutes. Provide ten devices or loans, rotate driver/reviewer in five pairs, use selectable-text formulas, and require individual exit evidence. Check power, network, keyboard access and local saving. This adaptation does not change the working online map.

Provide headings, plain-text scenarios and notebook in advance. Define symbols orally, describe all diagrams, avoid colour-only meaning, allow zoom and text responses, and arrange accommodations privately. No recording or transcription is assumed.

## Proposed independent study

Use the existing eight-hour S01 proposal: 2 hours rerunning the notebook and logging environment/data identity; 3 hours comparing formulations with missing evidence; 2 hours independent partition-sensitivity investigation; 1 hour linked reading and questions. This creates no graded submission or additional workload.

## LO1 traceability

| Approved component | Teaching source | Student action and observable formative evidence |
| --- | --- | --- |
| Explain three paradigms | Lecture sections 2–4; SL03–SL07 | Define signal, objective and feedback in the 25/38-minute checks. |
| Compare paradigms | Comparison matrix; SL08–SL10 | Apply common criteria and give a counterexample at 40–65 and 140–165. |
| Identify suitable algorithms | Choice guardrails; SL11–SL12 | Defend a family conditional on data and goal in the exit response. |
| Qualify claims | Workflow, notebook; SL13–SL17 | Record assumptions, leakage and ethical limits in private reflection. |

S02 begins with S01's row schema, split discipline and environment record, then teaches actual cleaning, encoding, transformations and EDA with pandas/scikit-learn under LO2. S01 does not preempt those implementation decisions.

Professor review remains needed for depth, timings, break accounting, contact channel, accommodations, hosted Colab smoke test and the Word/slide build.
