# Tutorial 01 — AI Subscription Economy: Data Cleaning and EDA

**Session:** S02 — Data Wrangling and Exploratory Data Analysis  
**Estimated duration:** 90–120 minutes  
**Format:** Guided Jupyter notebook  
**Dataset:** Deterministically generated synthetic data (1,200 base records plus 12 deliberate exact duplicates).

## Scenario
A fictional analytics team is preparing AI subscription usage records for future analysis. Variables include age, country, subscription plan, AI tool, monthly spend, usage frequency, primary use, satisfaction and a possible future-spend outcome.

The data deliberately include missing values, inconsistent category spellings, malformed numeric values, implausible values, extreme observations and exact duplicate rows. No real user information or external dataset is used.

## Learning objectives
Students will inspect dimensions, types and missingness; identify exact duplicates without confusing them with repeated entity IDs; normalise categories; parse numeric values and apply domain checks; perform descriptive EDA; create a derived feature; separate features from outcomes; split before fitting transformations; and build a ColumnTransformer with imputation, scaling and one-hot encoding.

## Files
- [tutorial.ipynb](tutorial.ipynb) — guided notebook with explanations, code, checkpoints, exercises and reflection.
- The notebook generates ai_subscription_raw.csv when executed.

## How to run
1. Open the notebook in Google Colab or Jupyter.
2. Run cells from top to bottom.
3. Required packages: Python, NumPy, pandas, Matplotlib and scikit-learn.
4. No API keys, credentials, external dataset, GPU or paid service are required.

## Relationship to S01, S02 and S03
- **S01:** reinforces observations, features, outcomes, learning-task framing, reproducibility and train/validation discipline.
- **S02:** practices data quality, cleaning, EDA, feature engineering, imputation, scaling, encoding and leakage-resistant preprocessing.
- **S03:** introduces predictive modelling. This tutorial intentionally does not fit a predictive model.

The notebook keeps future_spend separate as a possible outcome and excludes it from the feature matrix. The holdout is used only to demonstrate train-only preprocessing; no predictive performance claim is made.

## Instructor notes
- The generated dataset is synthetic and is not evidence about actual AI subscription users or market behaviour.
- Discuss whether negative spend could represent a refund in a real billing system.
- The random split is pedagogical. Repeated user snapshots or temporal prediction require group-aware or time-based splitting.
- Verify notebook execution, package compatibility and Colab/Jupyter behaviour before class.
- This is formative material and introduces no graded assessment.
