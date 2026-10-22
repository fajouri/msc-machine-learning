# S01 — Student practice and extension

Issue #13. Public, formative and ungraded; no solutions or marking key. Write a reasoned choice, identify evidence that would change it, and keep completed work in your private copy. Use the LO1 wording in brief.md. The scenarios are invented teaching cases and contain no personal data.

## A. Supervised, unsupervised or reinforcement?

For each case, make a four-column table: observable input, feedback/target, immediate decision, and plausible paradigm with candidate algorithm family. State one crucial fact the case omits. Do not assume that the named data have permission or represent future deployment.

1. A building manager has hourly meter readings and a verified next-day energy demand for past days; they need a next-day numeric forecast. Would a constant baseline and a regression family answer the same task? What would make a chronological split preferable?
2. A museum has object measurements and wants an exploratory grouping without an established category label. Under what assumptions could distance-based clustering be useful, and when might a dimensionality-reduction display help? Why is a cluster ID not a validated class?
3. A warehouse robot repeatedly chooses a route, receives delayed energy/time feedback, and its current route changes future congestion. Define state, action and reward candidates. What information and safety condition would be necessary before a sequential policy method is defensible?
4. A service allocates maintenance visits weekly using historic failure labels. Someone proposes “reinforcement learning” because visits are decisions. What evidence about action-dependent future states and rewards would distinguish a sequential problem from a fixed supervised prediction?

For a live Meet check, each of ten students shares one choice and one assumption by speech or chat. Peers challenge an assumption, not the person. For campus use, rotate a driver and reviewer in five pairs, then write an individual answer. If connection fails, use the downloaded sheet and the agreed private recovery route.

## B. Guided reproducibility audit

Open student-lab.ipynb, predict the constant model's behaviour before execution, then run all cells in a fresh Python 3 CPU runtime. Record Python version, data version/hash, seed and partition IDs. Explain which rows affect the fitted constant and which only evaluate it. Check whether a rerun matches, and distinguish this evidence of repeatability from evidence of generalisation. Explain why fitting any future transformation on all rows before splitting would invalidate the intended check. The public worked derivation in lecture.md may support the audit; it does not answer the independent tasks below.

## C. Independent investigation

Before writing code, state a hypothesis about how the validation MSE might change across a finite, predeclared list of seeds. Implement the experiment in the notebook's unanswered student cell. Record the split IDs and scores for each run privately, compare to the original seed-42 run, and explain why overlapping partitions limit interpretation. State how repeated choices based on validation results could affect a later claim. The format check only verifies record shape; it does not validate your method.

Independently choose one of A1–A4 and propose a second defensible formulation under a **changed** goal or feedback assumption. Specify the extra data needed, a simple baseline, a plausible algorithm family, a validation design and one ethical or deployment limitation. A mere relabelling of the same goal is insufficient. Keep the response unanswered in the public repository.

## D. Extension within the proposed S01 self-study budget

Critique a claim that a low validation error on the notebook's synthetic 24 rows proves a fair or reliable real-world model. Identify at least four distinct missing links, including sampling/shift, target meaning, uncertainty and affected groups. Then compare the cost of a simple transparent baseline with a more flexible method without fitting a new regression model. State what evidence would justify advancing to that method. This is critical analysis, not an extra assessed deliverable.

## Self-check criteria

An adequate response defines observed signal and decision time, compares paradigms on the same criteria, conditions the algorithm family on assumptions, makes a split/evaluation argument, records reproducibility information, and distinguishes computational repeatability from validity and societal fairness. These are prompts for reflection, not a rubric or model answer.

S02 takes the recorded schema and partition habit into actual cleaning, encoding, scaling and EDA under LO2. Those operations are intentionally left to S02.
