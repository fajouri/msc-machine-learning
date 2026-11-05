# S04 — Detailed teaching notes: Regression II

## 1. Bridge from S03

S03 introduced a straight-line model, a mean baseline and a disciplined evaluation protocol. Today we vary model flexibility while keeping the data split, folds and metric fixed. If all of these change together, we cannot tell which change explains a result.

## 2. Polynomial regression

A simple linear model is y-hat = b0 + b1x. Polynomial regression expands the input: y-hat = b0 + b1x + b2x² + ... + bd x^d. Degree 2 can represent a parabola; higher degrees can represent more varied curvature. The estimator remains linear in its learned coefficients: the feature representation is what becomes nonlinear.

With multiple inputs, polynomial expansion can also create interactions such as x1*x2. The number of columns can grow quickly, so inspect the transformed feature count and avoid adding complexity without a reason.

## 3. Complexity and generalisation

A flexible model can fit more patterns in training data, including noise. Underfitting is a model too restricted to capture important structure; training and validation errors are often both high. Overfitting is fitting training-specific noise; training error is low while validation error is materially worse. A useful fit generalises beyond the training sample.

These are diagnoses, not labels proved by one score. Inspect the train/validation gap, learning curves, residual structure, sample size and data context. The bias–variance framework is an intuition: restrictive assumptions can create systematic error (bias), while sensitivity to the particular training sample creates variance. Irreducible noise remains. No universal monotonic curve is guaranteed for every finite experiment.

## 4. Regularisation

Regularisation adds a penalty to discourage large coefficients. Ridge (L2) minimises squared error plus alpha times the sum of squared coefficients. It shrinks coefficients towards zero but generally does not set them exactly to zero. Lasso (L1) uses the sum of absolute coefficients and can set some coefficients exactly to zero. With correlated inputs, which coefficient remains can be unstable.

Alpha controls penalty strength. Larger alpha usually means stronger shrinkage, but the best value depends on data, scaling and model family. Do not assume that increasing alpha always improves generalisation. Use LinearRegression for the unregularised candidate rather than relying on Ridge(alpha=0).

## 5. Why scaling matters

A coefficient penalty depends on coefficient magnitude. Inputs measured in different units can produce incomparable coefficient scales. Polynomial columns can also have very different magnitudes. Standardise the expanded columns before Ridge or Lasso. Crucially, fit the scaler inside each training fold. Scaling the full dataset before cross-validation leaks validation-fold distribution information.

The pipeline order is PolynomialFeatures, StandardScaler, then Ridge or Lasso. Put the entire pipeline inside cross-validation so every learned transformation is fitted only on that fold's training partition.

## 6. Fair comparison

Fix the development/test split, CV splitter and fold assignments, primary metric, available features, preprocessing and candidate list. This session uses MAE as the primary selection metric because it is expressed in target units. RMSE is a useful secondary metric because it gives larger errors more influence. Neither metric alone explains every failure mode.

Use cross_validate with return_train_score enabled. Scikit-learn's neg_mean_absolute_error scorer is negative because its convention is that larger scores are better; multiply scores by -1 for reporting MAE. Compare fold means and variation, not just a single split. A low training error is not a selection rule.

## 7. Learning curves

A learning curve compares training and validation performance as training-set size increases. Both errors high and close can be evidence consistent with high bias. Low training error with high validation error can be evidence consistent with high variance. If both are low and reasonably close, the model may be useful for this task, subject to final evaluation and external validity. Curves can be noisy, especially with small datasets; explain observed evidence rather than applying a slogan mechanically.

## 8. Model selection and final test

Select the candidate using development cross-validation and the predeclared primary metric. If candidates are practically tied, prefer the simpler model; if using a tolerance, state it before examining the final test. Refit the selected pipeline on all development rows, then evaluate once on the reserved test. Do not revisit the candidate list because the test score disappoints. That would turn the test into another validation set.

## 9. Diagnostics and limitations

Plot residuals (actual minus predicted) against predictions. Look for systematic curvature, changing spread and extreme errors. These plots support investigation; they do not prove assumptions or causality. Polynomial models can extrapolate wildly outside the training range. A good in-range fit does not guarantee sensible predictions far beyond observed inputs. Regularisation does not automatically make a model robust to outliers.

## 10. Teaching prompts

- If degree 8 has the smallest training error, is it best? No: training error does not estimate generalisation.
- Why scale after polynomial expansion? Generated columns can have different scales and the penalty acts on coefficient magnitudes.
- Why put expansion inside the pipeline? So each CV training fold fits its own transformations.
- Does a zero Lasso coefficient prove a feature irrelevant? No; selection depends on sample, scaling, alpha and correlated inputs.
- Can the test score decide whether to increase degree? No; model selection belongs to development data.

## References

- [Polynomial regression](https://scikit-learn.org/stable/modules/linear_model.html#polynomial-regression-extending-linear-models-with-basis-functions)
- [PolynomialFeatures API](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PolynomialFeatures.html)
- [Ridge API](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html)
- [Lasso API](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html)
- [Preprocessing](https://scikit-learn.org/stable/modules/preprocessing.html)
- [Cross-validation](https://scikit-learn.org/stable/modules/cross_validation.html)
- [Learning curves](https://scikit-learn.org/stable/modules/learning_curve.html)
- [Metrics and scoring](https://scikit-learn.org/stable/modules/model_evaluation.html)

Original synthetic teaching material. Confirm installed library versions and Colab execution before student release.
