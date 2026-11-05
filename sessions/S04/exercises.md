# S04 — Exercises and experiment log

Formative practice for LO3 and LO7; not an additional graded assessment.

## 1. Predict the effect of degree (10 min)
A straight line has high training and validation MAE. Degree 2 reduces both. Degree 8 reduces training MAE again but validation MAE rises.
1. Which result is evidence consistent with underfitting?
2. Which result is evidence consistent with overfitting?
3. Why is degree 8 not automatically best?
4. What additional evidence would you inspect?

## 2. Explain the penalty (10 min)
Mark true/false and justify: Ridge can shrink without zeroing coefficients; Lasso can zero coefficients; larger alpha always improves test performance; scaling matters for coefficient penalties; a zero Lasso coefficient proves a feature irrelevant.

## 3. Pipeline design (10 min)
Arrange PolynomialFeatures, StandardScaler and Ridge/Lasso. Explain why the entire sequence belongs inside a Pipeline passed to cross-validation. Identify what leaks if scaling is fitted before folds are created.

## 4. Experiment (60–80 min)
Use the notebook to compare degree 1, 2, 3, 5 and 8, plus at least two Ridge and two Lasso alpha values. Use the same development folds and MAE selection metric. Record train and validation results. Do not inspect test results until selection is recorded.

| Candidate | Degree | Penalty | Alpha | Mean train MAE | Mean validation MAE | Validation SD | Notes |
|---|---:|---|---:|---:|---:|---:|---|
| Linear | 1 | none | — | | | | |
| Polynomial | 2 | none | — | | | | |
| Polynomial | 3 | none | — | | | | |
| Polynomial | 5 | none | — | | | | |
| Polynomial | 8 | none | — | | | | |
| Ridge | | L2 | | | | | |
| Ridge | | L2 | | | | | |
| Lasso | | L1 | | | | | |
| Lasso | | L1 | | | | | |

### Selection record — before final test
- Primary metric:
- Fold design:
- Selected candidate:
- Mean development validation MAE:
- Why selected:
- Evidence of underfit/overfit:
- Remaining limitations:

## 5. Interpret diagnostics (15 min)
Inspect learning curve and residual plot. Do train and validation errors converge? Is there residual structure? Is the observed input range sufficient? What changes for repeated users or future-month forecasting?

## 6. Final report (15 min)
After locking selection, run the final test. Report task/units, pipeline and hyperparameters, validation design, final test MAE and RMSE, one diagnostic observation and two limitations. Do not claim synthetic data demonstrate real business performance.

## Pair-review checklist
- Same folds for every candidate?
- Transformations fitted inside each fold?
- Metric declared before test?
- Selection recorded before final test?
- Interpretation distinguishes train and validation?
- Limitations specific?

## Exit ticket
1. Difference between adding polynomial features and changing estimator?
2. How do Ridge and Lasso differ?
3. Why is scaling fold-local?
4. One sign of overfitting?
5. Why must test not select degree or alpha?

## Optional extension
Change the synthetic noise level and repeat development CV. Explain how the best candidate changes. Create a fresh final test for the new experiment; do not reuse the original test to iterate.
