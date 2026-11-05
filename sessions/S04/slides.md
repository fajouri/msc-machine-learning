# S04 — Slide source and presenter notes

Campus session · 180 minutes · LO3 and LO7

## SL01 — Regression II
**On slide:** Polynomial models; regularisation; generalisation; bias–variance.  
**Notes:** Connect to S03: we know how to fit a line and evaluate it fairly. Today vary flexibility while keeping evaluation fixed.

## SL02 — Retrieve the S03 workflow
**On slide:** Define task → pipeline → common folds → select on development → final test once.  
**Ask:** What leaks if a scaler sees validation rows?  
**Notes:** Validation distribution information influences a transformation fitted for training.

## SL03 — A straight line can be too simple
**On slide:** y-hat = b0 + b1x. Some relationships curve. More flexibility can fit signal and noise.  
**Visual:** Labelled scatter plot with straight-line overlay.  
**Notes:** Model complexity should answer a data-pattern need, not be added automatically.

## SL04 — Polynomial features
**On slide:** y-hat = b0 + b1x + b2x² + ... + bd x^d. Degree 1: line; degree 2: quadratic; higher degree: more flexibility.  
**Notes:** The estimator is still linear in coefficients; the representation is nonlinear in x.

## SL05 — Complexity is not free
**On slide:** Training error often falls with added flexibility; validation error can improve, flatten or worsen. Lowest training error is not the selection rule.  
**Visual:** Conceptual train/validation curves; label as illustrative.  
**Notes:** Validation estimates generalisation better than training fit, but is still subject to sampling variation.

## SL06 — Underfitting and overfitting
**On slide:** Underfit: high train and validation error. Overfit: low train, much higher validation error. Useful fit: low and reasonably close.  
**Notes:** These are common patterns, not proofs. Discuss sample size, noise and metric.

## SL07 — Bias–variance intuition
**On slide:** Bias: restrictive assumptions. Variance: sensitivity to training sample. Irreducible noise remains. Seek generalisation, not training perfection.  
**Notes:** Avoid presenting a universal monotonic curve as a law.

## SL08 — Regularisation
**On slide:** Add a penalty to discourage large coefficients. Ridge: L2, shrinks coefficients. Lasso: L1, can set coefficients to zero. Alpha controls strength.  
**Notes:** Penalty changes the fitting trade-off; it does not guarantee improved test performance.

## SL09 — Why scale before penalising?
**On slide:** Coefficient size depends on units. Polynomial terms have different ranges. Standardise generated columns. Fit scaling inside each training fold.  
**Notes:** Pipeline: polynomial expansion → scaling → Ridge/Lasso. Keep all steps inside CV.

## SL10 — Experiment contract
**On slide:** Same split; same folds; same primary metric; same feature availability; declared candidates.  
**Ask:** What becomes unfair if candidates get different folds?

## SL11 — Candidate models
**On slide:** Degree 1 baseline; degrees 2, 3, 5, 8; Ridge and Lasso variants. Compare mean validation MAE and fold variation.  
**Notes:** Candidate list is a teaching design, not a universal search grid.

## SL12 — Learning curves
**On slide:** Training and validation score versus training-set size. High and close may indicate bias; low train/high validation may indicate variance. More data may help; inspect evidence.  
**Notes:** Curves are estimates and can be noisy.

## SL13 — Residual diagnostics
**On slide:** Look for curvature, changing spread, extreme errors and unsafe extrapolation.  
**Notes:** Residual = actual minus predicted. Diagnostics support investigation, not proof.

## SL14 — Break
**On slide:** 10-minute break. After the break: build a leakage-safe pipeline and compare candidates.

## SL15 — Guided notebook
**On slide:** Inspect data; reserve test; build pipeline; evaluate common folds; record experiment.  
**Notes:** Ask which transformations are learned and when they are fitted.

## SL16 — Pair experiment
**On slide:** Driver runs and records; reviewer challenges split, metric and interpretation; swap roles. Deliver candidate table and evidence-based diagnosis.

## SL17 — Lock, refit, test
**On slide:** Select using development CV; refit on all development rows; evaluate reserved test once; report limitations.  
**Ask:** Can a disappointing test justify trying another degree on the same test? No.

## SL18 — Exit ticket
**On slide:** Why can degree 8 overfit? How do Ridge and Lasso differ? Why scale inside pipeline? What data may influence selection? What does a test score not prove?  
**Next:** S05 — Classification I.

## Accessibility notes
Use labelled axes, direct text labels and non-colour identifiers. The SL05 curve is conceptual. Use notebook plots for measured results and state their seed and metric.
