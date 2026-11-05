# S04 — Regression II: Polynomial Models and Regularisation

**Mode:** campus · **Duration:** 180 minutes · **Outcomes:** LO3 and LO7

## Purpose

S03 introduced linear regression, a training-mean baseline, fold-local preprocessing and a reserved final test. S04 explores what happens when a straight line is too simple, and how regularisation can control an overly flexible model.

Students compare polynomial degrees and Ridge/Lasso models on identical development folds, diagnose underfitting and overfitting, select a candidate without consulting the test set, and evaluate the locked model once.

## Learning goals

By the end, students should be able to:
1. Explain how polynomial features let a linear estimator represent nonlinear relationships.
2. Diagnose evidence consistent with underfitting and overfitting using training and validation results.
3. Explain Ridge (L2), Lasso (L1), alpha and the importance of scaling.
4. Compare model complexity and regularisation using common folds and a declared metric.
5. Select on development data and report final test performance and limitations.

## Materials

- [Detailed lecture](lecture.md)
- [Slides and presenter notes](slides.md)
- [Exercises and experiment log](exercises.md)
- [Student notebook](student-lab.ipynb)
- [Open in Colab](https://colab.research.google.com/github/fajouri/msc-machine-learning/blob/master/sessions/S04/student-lab.ipynb)

## 180-minute plan

| Minutes | Activity |
|---|---|
| 0–10 | S03 retrieval: residuals, baseline, CV and final test |
| 10–30 | Polynomial feature mapping and nonlinear relationships |
| 30–50 | Degree, complexity and diagnostics |
| 50–65 | Underfitting, overfitting and bias–variance |
| 65–75 | Break |
| 75–95 | Ridge, Lasso, alpha and scaling |
| 95–115 | Guided leakage-safe pipeline |
| 115–140 | Pair experiment: degrees and penalties on common folds |
| 140–160 | Learning curves, selection and final test discipline |
| 160–175 | Peer explanation and experiment log |
| 175–180 | Exit ticket and S05 preview |

## Delivery notes

The notebook generates deterministic synthetic observations. Rows are independent, so a shuffled split is suitable for this demonstration only. Repeated users, groups or temporal observations require an appropriate group-aware or time-aware split. Polynomial expansion and scaling are kept inside a pipeline fitted separately in each CV fold. The test set remains untouched until selection is locked.

The experiment log is formative, not a new graded assessment. No change is made to the approved 60/30/10 scheme. Synthetic results are not evidence about real customers or production forecasting. Professor review and Colab execution remain pending before student release.
