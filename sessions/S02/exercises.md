# S02 — Student exercises (formative, no answer key)

## Exercise A — Data-quality review (15 minutes)
From the generated synthetic dataset:
1. Identify the data types of six columns and report missingness in each.
2. Check for duplicate identifiers and discuss why a repeated ID may or may not be a duplicate event.
3. Find any negative spending, inconsistent category spelling, implausible ages or numeric strings. Choose a cleanup rule for each, with a reason and a potential downside.
4. Explain why `future_spend` must not be a feature for a same-day prediction.

**Deliverable:** a short schema-and-quality table with the chosen policy (keep/flag/drop/convert/impute).

## Exercise B — Interpret EDA (20 minutes)
Produce a histogram of `monthly_spend`, a category frequency chart, and a scatter plot of `visits` versus `monthly_spend` using the *training* split. Describe each chart’s axes/units and what it cannot prove. Which unusual value would you investigate, rather than silently delete?

**Deliverable:** charts plus three evidence-based sentences and two limitations.

## Exercise C — Train-only preprocessing (25 minutes)
Use the notebook to:
1. Split into train and holdout; exclude target/ID.
2. Apply a numeric median imputer and StandardScaler.
3. Apply categorical most-frequent imputer and OneHotEncoder with unknown-category handling.
4. Show the transformed dimensions and feature names.
5. Explain why fitting an imputer or scaler before splitting leaks holdout information.

**Deliverable:** runnable cell outputs and a written justification of the pipeline. Do not train a predictive model yet.

## Exercise D — Independent challenge (20 minutes)
Without copying an instructor answer, modify your *private* notebook:
- Add a missing region in one record, a new region that appears only in holdout, and a zero-visits record.
- Create `spend_per_visit` safely and explain how you handle division by zero.
- Investigate which transformed features change, and why the number of columns may not change for an unknown category.
- State whether random splitting is appropriate for a hypothetical dataset containing successive observations from the same customer.

**Exit ticket:** In 90 words or fewer, distinguish cleaning, EDA, feature engineering and a fitted preprocessing pipeline.

## Optional self-study (proposed 10 hours)
Audit a second synthetic dataset (2h), compare documented missing-value policies (2h), implement a leakage-resistant column transformer (3h), compare alternate feature definitions (2h), reflect on limitations and references (1h). No additional graded work is specified.

## Self-check
The work should be reproducible, explain what is learned on train only, preserve plausible observations, name the source and meaning of each variable, and avoid publishing confidential data or independent solutions.
