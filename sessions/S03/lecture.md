# S03 — Detailed teaching notes: Regression I

## 1. The prediction contract

S02 produced trustworthy features and reusable transformations. S03 adds a predictor and an evaluation protocol. Begin by asking what a feature must satisfy beyond having a numeric data type: it must be available when the prediction is made. A future invoice may be highly correlated with future spend and still be unusable.

Our main example uses fictional AI subscription users. At the end of the current month, predict each user's **total spend during the next 30 days, in euros**. One row describes one independently generated user observed once. Current monthly spend, weekly sessions, tenure and current plan are available inputs. `user_id` is an identifier. `future_spend` is the outcome we want to predict, observed later. The tutorial generates a fresh dataset and does not reuse S02's holdout.

This is regression because the target is a numeric amount. Predicting whether a user will cancel would instead define a classification task. LinearRegression predictions are unrestricted numeric estimates, not probabilities. A numeric encoding of a class label does not turn the scientific question into regression.

**Prediction contract:** record the population, unit of observation, prediction time, target horizon, feature availability, intended decision and cost of errors. The synthetic generator establishes a teaching relationship by design. It cannot establish customer behaviour, business value, fairness or causal effects in the real world.

## 2. The line and its parameters

For a single input, write the fitted prediction as

\[
\hat y_i=b_0+b_1x_i.
\]

The intercept is the prediction at x=0. The slope is the change in the prediction per unit increase in x. In a teaching line `predicted spend = 10 + 2 × sessions`, twelve sessions give a prediction of €34. This is an illustrative line, not a fit to market data. If zero sessions lies outside the observed range, the intercept has limited substantive meaning.

Multiple regression uses `ŷ = b₀ + b₁x₁ + … + bₚxₚ`. A coefficient describes a conditional association within the specified model while holding its other encoded inputs fixed. It does not prove that changing the input causes that effect. Correlated predictors can make coefficients unstable even when predictions are useful.

StandardScaler changes numeric inputs to `(x − training_mean) / training_sd`. A numeric coefficient after scaling refers to one training standard deviation in that input. Do not interpret it as euros per original session. The short concept notebook separately fits an unscaled, single-input demonstration so its slope has simple units. That explanatory fit does not replace the main validation comparison.

## 3. Residuals and least squares

Define the residual as `eᵢ = yᵢ − ŷᵢ`. A positive residual means the model underpredicted. A negative residual means it overpredicted. Other software may use the opposite sign, so define the convention before interpreting a residual plot.

Ordinary least squares chooses coefficients to minimize the residual sum of squares:

\[
SSE(b)=\sum_{i=1}^{n}(y_i-\hat y_i)^2.
\]

Dividing by the fixed sample size gives the mean squared error:

\[
MSE(b)=\frac{1}{n}\sum_{i=1}^{n}(y_i-\hat y_i)^2.
\]

SSE and MSE have the same minimizer for a fixed dataset. Squaring prevents positive and negative errors from cancelling and gives large errors more influence. In the public worked example `y=[20,30,40]` and `pred=[18,33,39]`, residuals are `[2,-3,1]`, SSE is 14 and MSE is 14/3. Students then implement their own function and test it on different inputs.

For the simple, unweighted fit with an intercept and nonconstant x, minimizing MSE gives `b₀ = mean(y) − b₁ mean(x)` and

\[
b_1=\frac{\sum_i(x_i-\bar x)(y_i-\bar y)}{\sum_i(x_i-\bar x)^2}.
\]

Explain the logic: for a chosen slope, centre the line through the sample means, substitute this intercept into the objective, differentiate with respect to the slope, then solve the zero derivative. The denominator is zero for a constant input. With many features, numerical linear-algebra solvers are preferable to explicitly forming a matrix inverse. Dense scikit-learn LinearRegression solves least squares numerically. It does not expose a neural-network epoch count. Calling `.fit()` once trains one estimator. Five-fold validation fits five fresh estimators for that candidate.

## 4. Metrics and units

| Quantity | Definition | Interpretation for euro targets |
| --- | --- | --- |
| MAE | mean of absolute residuals | Average absolute error in euros |
| MSE | mean of squared residuals | Error in squared euros |
| RMSE | square root of MSE | Error in euros, with more influence from large residuals |
| R² | 1 − SSE / sum((y − mean(y))²) | Dimensionless relative squared-error measure |

Choose the primary metric before comparing models. This tutorial uses MAE for the selection rule because an average euro error is easy to discuss, while fitting OLS still minimizes squared error. Training loss and selection metric may differ and must be named separately. RMSE and R² provide context. R² is not classification accuracy or a percentage of correct predictions. It can be negative on unseen data. For constant targets its usual denominator is zero, so discuss the metric's implementation conventions instead of treating it as a reliable summary.

A held-out R² of zero corresponds to predictions whose squared error equals that of the held-out target mean used in the R² formula. This differs from DummyRegressor's deployable baseline, which estimates its constant from training targets only. On new data, that training-mean baseline can itself have negative R².

Neither MAE nor RMSE estimates every individual's error. A €5 MAE is not a guarantee that the next error is below €5. The tutorial's new-user prediction is a point estimate and has no calibrated prediction interval.

## 5. Baselines make success measurable

A mean DummyRegressor predicts the mean of the training targets for every row. It learns that constant within each training fold. It ignores feature values. A median baseline is appropriate to discuss when absolute error is the central loss, but the required core comparison uses a mean baseline to connect to squared loss. Avoid selecting whichever baseline makes the model look best after looking at test results.

Use the same development rows, folds, primary metric and reporting protocol for both candidates. Baseline preprocessing appears in the same pipeline structure for consistency. DummyRegressor does not benefit from those transformations, but the baseline's target mean must still come from each training fold.

A regressor that performs poorly deserves an honest conclusion. XP rewards a correctly executed comparison even when the baseline wins. Never award more XP for a smaller MAE, a larger R² or a fortunate split.

## 6. Development, validation and the final test

First split 500 rows into **400 development and 100 test rows**, with a fixed seed. This seed controls the row allocation; it does not train anything. The synthetic rows are independent users, which makes shuffled splits a reasonable teaching simplification. In actual next-month forecasting, calendar drift may require forward-in-time validation. Multiple rows per user require group-aware splitting. A random seed cannot repair an unsuitable validation design.

On the development set, define a shuffled five-fold KFold with a fixed seed. Each fold fits on 320 development rows and validates on 80. Across the five iterations every development row serves once as validation. The final test rows never enter this process. Compare baseline and linear regression on these identical folds.

Fit the entire Pipeline within cross_validate. Numeric transformations include median imputation and scaling. Categorical transformations include mode imputation and one-hot encoding. The tutorial uses a reference category with `drop='first'`, helping explain category coefficients relative to a reference. Since all three categories occur in every training fold in the generated example, no novel-category handling question is needed for the core comparison. Deployment with new categories still requires monitoring even if an encoder can technically transform the input.

Passing already-imputed or already-scaled development data into cross-validation leaks validation-fold information into training. A preprocessing fit on development data is safe only for the final refit after selection, not as a preprocessing step before cross-validation. Check that each fold's imputer statistics match its training rows and that the fold validation indices are excluded.

scikit-learn scorers follow the convention that larger is better. Its `neg_mean_absolute_error` and `neg_mean_squared_error` therefore return negatives. Negate MAE scores for reporting. Calculate each fold's RMSE as `sqrt(-fold_neg_mse)`, then report the mean of the fold RMSEs. Do not label `sqrt(mean(fold_mse))` as the mean fold RMSE.

The five-fold standard deviation describes variation across these folds. It is not a confidence interval and folds share training rows. Avoid claiming significance from the mean alone. S07 expands evaluation design.

## 7. A predeclared final check

Choose the candidate with the lower mean development CV MAE, using a predeclared tie rule that favours the simpler baseline. Refit that selected pipeline on all 400 development rows. The notebook also refits the baseline as a fixed reference. Evaluate these locked estimators on the 100 test rows in one final evaluation stage, reporting MAE, RMSE and R². The test does not choose the model.

The new-user prediction uses the already fitted selected pipeline. It neither refits transformations nor reveals future outcomes. Report the input units, the prediction horizon and the limitations of a synthetic teaching model. If the final test disappoints, preserve that result. A further modelling iteration needs a new evaluation plan. Repeatedly rerunning the same unchanged notebook is a reproducibility check, but choosing changes based on its test output consumes the test's independence.

Diagnostic plots in the tutorial use out-of-fold development predictions, not test residuals for iterative design. The predicted-versus-observed plot has an equality reference line. The residual plot uses prediction on the x-axis and `actual − predicted` on the y-axis. Curvature suggests that the chosen mean relationship may be inadequate. A widening spread suggests changing error variance. A small sample and a pleasing plot do not prove assumptions.

## 8. The tutorial and XP review

The tutorial provides a fully runnable example in each section, followed by a separate student task. Starter values are `None` or empty text, so Run all works without falsely completing a task. Code checks contribute code XP. Students then explain their decisions to a peer or lecturer, who reviews the reasoning against the visible criteria. Students update the local review flag only after that discussion. Reasoning XP is a private formative record, not an automated assessment or proof of understanding.

Each mission can earn points once. Re-running a check updates that mission rather than adding duplicate points. Hints and retries are unlimited. The optional bonus implements a median baseline on development CV only. It must not change the locked core test comparison.

For students who finish early, request a methodological critique: identify what would change with repeated users or a later calendar period. For students needing support, use the short concept notebook and pair them with a reviewer. Require one explanation from each learner even when they share code.

## 9. Closing and self-study

Exit ticket: write the residual sign for underprediction, name what a fold's imputer may see, and explain why a baseline may win. Collect privately or discuss orally. Preview S04's polynomial regression and regularisation without teaching them as additional S03 requirements.

The curriculum proposes 10 self-study hours for S03. Suggested distribution: 2 hours revisiting the line and objective derivation, 3 hours completing or revising the tutorial, 2 hours reading and annotating validation choices, 2 hours independent practice, and 1 hour writing a model card. This is a teaching allocation, not a new assessment.

## References

Primary project documentation, checked 4 November 2026. Runtime versions are printed by both notebooks. APIs use broadly supported methods, including `sqrt(mean_squared_error(...))` for RMSE.

- [LinearRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html): least-squares objective and estimator behaviour.
- [Linear models guide](https://scikit-learn.org/stable/modules/linear_model.html#ordinary-least-squares): interpretation and numerical formulation.
- [DummyRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.dummy.DummyRegressor.html): baseline strategies.
- [Cross-validation](https://scikit-learn.org/stable/modules/cross_validation.html): train/test roles and evaluation.
- [Metrics and scoring](https://scikit-learn.org/stable/modules/model_evaluation.html): regression metrics and scorer signs.
- [Common pitfalls](https://scikit-learn.org/stable/common_pitfalls.html): leakage and pipelines.

All examples and diagrams are original teaching material. No real customer data or protected assessment solutions are included.
