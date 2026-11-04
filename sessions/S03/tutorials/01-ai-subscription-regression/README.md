# Tutorial 01 — AI Subscription Regression Quest

**S03:** Regression I · **Duration:** 90–120 minutes · **Core XP:** 100 · **Optional bonus:** 20

Predict next month's spend for fictional AI subscription users. Complete eight missions, explain your choices and record XP as you progress. The goal is a defensible modelling workflow and an honest result.

[Open in Google Colab](https://colab.research.google.com/github/fajouri/msc-machine-learning/blob/master/sessions/S03/tutorials/01-ai-subscription-regression/tutorial.ipynb) · [Notebook source](tutorial.ipynb) · [Full XP rubric](../../exercises.md)

## Start step by step

1. Open the Colab link and choose **File → Save a copy in Drive**, or download the notebook for local Jupyter.
2. Read the prediction contract and the XP rules at the top.
3. Run setup and the data-generation cells. No download is required.
4. Work through M1–M8 in order. Read the example, edit the student task, then run its check.
5. Explain each result to a peer or lecturer using the listed review criteria. Update review flags only after that conversation.
6. Run the scoreboard, save your private copy and complete the exit ticket. Bonus B1 is optional.

**Run all works in the starter notebook**, but student task placeholders remain incomplete and earn zero points. Guided code and student tasks are visibly separate. Hints and retries are unlimited. Re-running checks cannot duplicate XP. XP are formative and do not change the official 60/30/10 assessment.

## Scenario and data dictionary

One row represents one independent synthetic user observed at the end of the current month. Predict the total spend in the next 30 days. A new deterministic generator creates 500 records, with limited missing input values. These data continue S02's scenario but are not S02's dataset or exported files.

| Column | Meaning and units | Role at prediction time |
| --- | --- | --- |
| `user_id` | Unique synthetic user identifier | Exclude from features |
| `monthly_spend` | Current-month spend, EUR | Numeric input |
| `weekly_sessions` | Mean sessions per week in the current month | Numeric input |
| `tenure_months` | Completed months with the service | Numeric input |
| `plan` | Current plan: Basic, Pro, Team | Categorical input |
| `future_spend` | Spend in the next 30 days, EUR | Outcome, never an input |

The generator intentionally creates a mostly linear signal. Good results on this synthetic task do not establish real business performance or causal effects. Random splits simplify the example because rows are independent. Real monthly forecasting can require time-aware or group-aware validation.

## Mission route

| Mission | Task | XP |
| --- | --- | ---: |
| M1 | Define target, features and prediction time | 10 |
| M2 | Reserve the final test set | 10 |
| M3 | Implement and interpret squared error | 10 |
| M4 | Establish a training-mean baseline | 15 |
| M5 | Build a fold-local regression pipeline | 15 |
| M6 | Compare identical validation folds | 15 |
| M7 | Report one locked final test stage | 15 |
| M8 | Predict for a new user and explain limits | 10 |
| B1 | Optional median baseline, development CV only | 20 |

## Reproducibility and boundaries

Requirements: Python, NumPy, pandas, Matplotlib and scikit-learn. CPU only, no credentials or paid APIs. Setup prints the versions used. No student records are uploaded by the notebook. Keep your own answers, review flags and XP table private.

The notebook uses a 400/100 development/test split. Five-fold development CV trains on 320 rows and validates on 80 per fold. Pipeline transformations fit within each fold. MAE selects the core candidate before test evaluation. The optional bonus cannot revise that selection. Diagnostic plots use development out-of-fold predictions.

If a student task check remains incomplete, continue with the guided reference variables, then return to the task. This supports discussion without silently awarding completion points. A passing code check is useful feedback, not academic approval or secure assessment.

For a package/version error, restart the runtime and run setup again, then read the full message. The short [concept notebook](../../student-lab.ipynb) is the fallback. Local execution was checked on 4 November 2026. Google Colab execution and professor review remain pending.
