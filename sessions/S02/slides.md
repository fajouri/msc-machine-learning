# S02 — Slide source and speaker notes (16:9, 180-minute campus session)

Use the content below to produce a 16:9 editable PPTX. Suggested body ≥24pt, diagram labels ≥18pt, accessible contrast, no text-only walls. Presenter notes may be visible to students, so no answer key.

## SL01 — From raw data to trustworthy features
**On slide:** Data quality → exploratory analysis → split → train-only fit → reusable transformations.
**Speaker notes:** Ask students what can go wrong before fitting a single algorithm. Explain S01→S02→S03 transition. (0–5)

## SL02 — LO2 and the route through today's lab
**On slide:** Cleaning · feature engineering · scaling · encoding · pandas + scikit-learn.
**Notes:** State the exact LO2 and expected artifacts. Ask for one prior experience with a messy spreadsheet. (5–15)

## SL03 — A fictional service transaction dataset
**On slide:** Features: age, monthly_spend, visits, channel, region. Outcome (not feature): future_spend.
**Notes:** Discuss time-of-prediction availability, ID, units and provenance. Synthetic example. (15–22)

## SL04 — Data-quality audit checklist
**On slide:** Types · missing values · duplicates · invalid ranges · inconsistent categories · provenance.
**Notes:** Demonstrate the distinction between null, 0 and invalid string. (22–30)

## SL05 — What does missingness mean?
**On slide:** MCAR / MAR / MNAR are assumptions, not labels from a null count.
**Notes:** Discuss bias from complete-case deletion; do not assert missingness mechanisms from the chart alone. (30–40)

## SL06 — pandas inspection in four operations
**On slide:** `info()`, `isna().mean()`, `value_counts()`, `to_numeric(errors="coerce")`.
**Notes:** Live demonstrate resulting data types and report which values become null. (40–50)

## SL07 — Cleaning needs a documented policy
**On slide:** Normalize known formats; flag dubious ranges; do not erase outliers automatically.
**Notes:** Ask students to distinguish a category typo from a legitimate novel category. (50–58)

## SL08 — EDA asks questions, not causal conclusions
**On slide:** Histogram (shape) · bar chart (frequency) · scatter (association).
**Notes:** Explain units, axis interpretation, selection bias and bin sensitivity. (58–65)

## SL09 — Pair challenge: diagnose before fixing
**On slide:** Identify 3 quality issues; propose 3 defensible corrections; state 1 uncertainty.
**Notes:** Rotate driver/reviewer and request short rationales. (65–90)

## SL10 — Break and reset
**On slide:** 10-minute break. Next: avoid leaking held-out information.
**Notes:** (90–100)

## SL11 — The leakage trap
**On slide:** Wrong: fit scaler on all rows → split. Right: split → fit on train → transform holdout.
**Notes:** Even target-free summary statistics of the holdout leak information. (100–112)

## SL12 — What a transformation learns
**On slide:** Median; mean/std; categorical vocabulary. These are *fitted parameters*.
**Notes:** Explain `z=(x−mean_train)/std_train`; not normality and not guaranteed within [-1,1]. (112–125)

## SL13 — Two pipelines, one feature matrix
**On slide:** Numeric: median → standardize. Categorical: mode → one-hot.
**Notes:** Show scikit-learn Pipeline + ColumnTransformer and why sequential fit/transform is crucial. (125–138)

## SL14 — The encoded feature-space expands
**On slide:** One categorical input may create several binary columns; unseen values require a policy.
**Notes:** Discuss interpretability and feature names; warn about unique identifiers. (138–148)

## SL15 — Lab: transform train and holdout
**On slide:** Fit `X_train` only; transform both; inspect feature names and shape.
**Notes:** Pair students; debug version-specific API differences, avoid training a predictor. (148–155)

## SL16 — Independent challenge
**On slide:** Missing region, zero visits, unknown category, justified feature engineering.
**Notes:** Request students edit their private copy; invite alternative policy with trade-off. (155–175)

## SL17 — Three questions before S03
**On slide:** What is a data error? What is fitted? Why should the holdout remain untouched?
**Notes:** Individual exit ticket; preview linear regression in S03. (175–180)

## Visual guidance
Use original vector diagrams for data flow; never paste third-party charts or copyrighted figures without permission. Include descriptive titles and text alternatives. Slide content is an editable source, not a claim that a PPTX file was rendered.
