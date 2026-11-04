# S03 — Exercises and Regression Quest XP

All activities are formative. Keep answers and point records in a private notebook. These XP do not enter the written exam, Kaggle capstone or presentation marks. The official weights stay 60/30/10.

## Warm-up, before the main tutorial

1. A fictional line predicts `spend = 10 + 2 × sessions`. Predict for 7 sessions. Label the slope's units. What makes the intercept hard to interpret in some datasets?
2. Use actual amounts `[16, 25, 31]` and predictions `[18, 22, 30]`. Calculate residuals, SSE, MSE, MAE and RMSE. State every unit.
3. Explain what changes when a numeric input is standardised. Does scaling establish a causal relationship?
4. A developer fills missing values using all 500 rows, reserves 100 for testing, then cross-validates on the rest. Identify two places where held-out information enters training and propose a safe order.

The warm-up and exit ticket carry no additional XP. Mission 3 uses its own function and checks.

## Main tutorial

Open [Regression Quest](tutorials/01-ai-subscription-regression/README.md) and save a private copy of its notebook. Every mission contains an example, numbered instructions, a student task, a code check and reasoning criteria. The notebook is the complete step-by-step guide.

| Mission | Deliverable | Code XP | Reviewed reasoning XP | Total |
| --- | --- | ---: | ---: | ---: |
| M1 Task detective | Feature list and prediction contract | 5 | 5 | 10 |
| M2 Split guardian | Development/test size and split explanation | 5 | 5 | 10 |
| M3 Loss mechanic | Your reusable MSE function and units | 5 | 5 | 10 |
| M4 Baseline builder | Baseline fold MAEs and comparison protocol | 10 | 5 | 15 |
| M5 Pipeline engineer | Your imputation/scaling/regression pipeline | 10 | 5 | 15 |
| M6 Validation analyst | Per-fold results and selection reasoning | 10 | 5 | 15 |
| M7 Evidence reporter | Final metric calculation and honest model card | 5 | 10 | 15 |
| M8 Prediction guide | New-user prediction and limitations | 5 | 5 | 10 |
| **Core total** | | **55** | **45** | **100** |
| B1 Optional baseline extension | Median baseline using development CV only | 10 | 10 | 20 |

## How points work

1. Run the guided example and read what it establishes.
2. Complete the separate `student_...` task in your own copy. Starter placeholders earn zero.
3. Run its check. A passing check records that mission's code XP once.
4. Write your own explanation, using the visible reasoning criteria.
5. Discuss the explanation with a peer or lecturer. After feedback and any revision, mark that mission's private review flag `True` and rerun its check to record reasoning XP.
6. Rerun the scoreboard. Repeated checks update the same mission, and never stack points.

Use hints, ask questions and retry freely. There is no speed bonus, public ranking requirement or reward for artificially good metrics. A well-supported result where the baseline wins earns full points. The code checks are learning feedback, not secure grading. No public student records are collected.

## Milestones

| Core XP | Practice milestone |
| --- | --- |
| 0–29 | Explorer |
| 30–59 | Builder |
| 60–79 | Evaluator |
| 80–99 | Analyst |
| 100 | Regression Ranger |

Bonus XP appears separately and cannot replace unfinished core missions. Code checks can confirm outputs and some pipeline properties. They cannot establish that your interpretation is correct, so the review conversation matters.

## Submission checklist

Save your notebook privately with code, outputs, explanations and the local scoreboard. Provide it to the lecturer through the institution's normal channel if requested. Include the prediction contract, feature exclusions, split protocol, baseline comparison, metric units, final test result and one limitation. Do not commit student notebooks or XP records to the public course repository.

## Exit ticket

In your own words: what does a positive residual mean; which rows can an imputer use in one CV fold; and why can a simple baseline be the correct model choice?
