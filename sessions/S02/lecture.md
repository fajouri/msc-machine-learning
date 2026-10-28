# S02 — Detailed teaching notes: data wrangling and EDA

## 1. Why preprocessing is a modelling decision (15 min)

S01 introduced the idea that a model receives a feature matrix X and may learn from a target y. Today we examine the usually invisible decisions that produce X. Bad measurements, absent values, inconsistent categories, and post-outcome information can lead to misleading numerical results even when the future model is implemented correctly. Ask: **Can the feature be measured when the prediction would actually be made?**

**LO2 (exact):** Implement data preprocessing pipelines including cleaning, feature engineering, scaling, and encoding using Python (pandas, scikit-learn).

Explain that cleaning is neither blind row deletion nor an automatic search for perfect-looking distributions. Every choice depends on the data-generating process, target question, and acceptable information at decision time.

## 2. Data quality inventory (25 min)

Introduce a small, *synthetic* dataset describing fictional service transactions, with `age`, `monthly_spend`, `visits`, `channel`, `region` and `future_spend`. These are made-up values, not customer data. Explicitly distinguish `future_spend` (illustrative outcome: not a predictor at decision time) from inputs.

**Checks:** row and column count; dtype vs semantic type; categorical cardinalities; null counts and proportions; duplicate IDs vs duplicate events; implausible age, negative spend, inconsistent capitalization and leading/trailing spaces; measurement units; selection process; grouped or temporal dependence. A duplicate record and a legitimate repeated transaction are not interchangeable. Reject impossible measurements only with an explicit documented rule. Coercing a string to numeric can create a new missing value—log how many and why.

**Missing-data mechanisms:** MCAR (missing completely at random), MAR (missing at random conditional on observed data) and MNAR (missingness depends on missing values even after conditioning). These are hypotheses not identities one can infer solely from a missingness percentage. Deleting all incomplete rows can bias the sample. Median/most-frequent imputation is a pragmatic baseline, not an estimate guaranteed unbiased.

Demo:
```python
df.info()
df.isna().mean().sort_values(ascending=False)
df["channel"].astype("string").str.strip().str.lower().value_counts(dropna=False)
pd.to_numeric(df["monthly_spend"], errors="coerce")
```
Discuss the effect of `errors="coerce"` and keep raw vs cleaned copies for audit.

## 3. Cleaning and EDA: different purposes (25 min)

**Cleaning** corrects or flags violations of a declared schema; **EDA** makes data quality, shape and patterns visible. Show tables of missingness, quantiles, distributions, categories and a scatter plot. A histogram helps reveal skew, but its appearance depends on bin width. A box plot flags unusual values under a chosen convention; unusual does not mean incorrect. A relationship plot does not establish causality.

Explain why fitting data-dependent operations on **all records before the split** contaminates honest validation. Even if you do not look at the target, median and standard deviation of the held-out fold provide information about that fold. Split before fitting imputer/scaler/encoder. For teaching, visualize the synthetic *training subset* and avoid turning the test set into an iterative design dashboard.

## 4. Cleaning policy vs fitted transformations (25 min)

Distinguish:
- **Deterministic schema correction:** normalized category casing, conversion of known units, documented impossible-value rules; define once without consulting held-out statistics.
- **Learned transformation:** median/mode imputation, category vocabulary and scaling statistics; fit on training data only.
- **Feature engineering:** construct `spend_per_visit` from features available at the same decision time. For zero visits, keep a missing ratio for later imputation rather than dividing by zero or inventing a value.
- **Feature exclusion:** drop identifiers, target and future-only information; keep a record of the choice.

For a numeric feature x in the training set, the standard score is `z = (x - mean_train) / sd_train`. Zero variance needs explicit treatment (scikit-learn StandardScaler uses a safe scale of 1); values can be outside the interval [-1,1]. Scaling is not a guarantee of normal distribution or reduced bias.

One-hot encoding of channel categories avoids pretending that the lexical category order is meaningful. Unknown categories at deployment need a defined policy, e.g. `handle_unknown="ignore"`; this may produce an all-zero encoded representation for that feature, which requires interpretation. Do not one-hot encode an unbounded unique identifier.

## 5. Campus pair exercise (25 min)

Each pair gets the synthetic data in Colab. Ask one student to identify three data-quality risks and the other to propose documented handling and explain the risks of naive deletion. Swap roles for the EDA visualization. Discuss whether a high-age entry is necessarily invalid and what information would confirm it. Capture a one-sentence summary of uncertainty. Use only synthetic data; avoid real student information.

## 6. End-to-end pipeline reasoning (30 min)

A scikit-learn `ColumnTransformer` applies preprocessing to named sets of columns. Numeric: `SimpleImputer(strategy="median")` followed by `StandardScaler()`. Categorical: `SimpleImputer(strategy="most_frequent")` followed by `OneHotEncoder(handle_unknown="ignore")`. Wrap both in `Pipeline` to preserve sequential fit/transform behaviour. The final `fit_transform(X_train)` estimates statistics from training data; `transform(X_test)` applies them unchanged. No predictive estimator is needed to demonstrate LO2.

Use `train_test_split` with explicit `random_state`, explain the caveat: real time-series, families or sites require time/group-aware splitting rather than indiscriminate random records. A small split is useful to demonstrate mechanics but not stable performance inference.

## 7. Interpretation and extension (20 min)

Ask students to compare numeric medians before and after imputation and check whether one-hot features unexpectedly multiply dimensions. Discuss a hypothetical high-cardinality variable and how a learner should decide whether to include it. Invite an independent modification: introduce a previously unseen category in *test only* and explain why `handle_unknown="ignore"` permits transforming the data without fitting the vocabulary again.

**Avoid:** computing medians on full data, calling the result a fitted machine-learning predictor, or reporting evaluation metrics for a model we have not trained. The holdout remains untouched for future model evaluation.

## 8. Closing and exit ticket (5 min)

Ask each learner: (a) identify two data-quality hazards; (b) explain what is fitted on training-only data; (c) justify why a test-only category must not redefine the encoder. Summarize the transition to S03: compare regression baselines and least-squares fitting on a carefully preprocessed feature table.

## Instructor quick-reference

- **Missing vs zero:** absence of measurement is not an observed value of zero.
- **Outlier vs error:** investigate plausibility before deletion.
- **Correlation vs causation:** exploratory associations are hypotheses, not interventions.
- **Standardization vs normalization:** standard scores use training mean/std; min–max maps to a chosen range based on train extrema, not always bounded for future examples.
- **Imputation vs inference:** imputers choose replacement values; they do not prove what the missing person/transaction would have reported.
- **Repeatability vs validity:** a fixed random seed reproduces a computation, not a trustworthy sample design.

## Further reading
- pandas user guide: https://pandas.pydata.org/docs/user_guide/index.html
- scikit-learn preprocessing: https://scikit-learn.org/stable/modules/preprocessing.html
- scikit-learn common pitfalls: https://scikit-learn.org/stable/common_pitfalls.html
- scikit-learn ColumnTransformer: https://scikit-learn.org/stable/modules/compose.html#columntransformer-for-heterogeneous-data

Links point to project documentation; check current versions before class.
