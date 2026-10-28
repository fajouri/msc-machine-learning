# S02 — Data Wrangling and Exploratory Data Analysis

**Format:** campus lab · **Duration:** 180 minutes · **Block:** B01 Foundations · **Outcome:** LO2

> Implement data preprocessing pipelines including cleaning, feature engineering, scaling, and encoding using Python (pandas, scikit-learn).

## Learning goals
By the end, students should be able to (1) audit a dataset and explain missingness, (2) clean inconsistent values, duplicates and impossible observations without hiding decisions, (3) distinguish exploratory analysis from fitted preprocessing, (4) use training-only imputation, encoding and scaling with scikit-learn pipelines, and (5) defend a model-ready feature table with appropriate limitations.

## Class agenda
| Minutes | Activity |
|---|---|
| 0–15 | Recall S01: observations, labels and holdout discipline; diagnose messy records |
| 15–40 | Dataset quality audit, missingness, duplicates, types, ranges |
| 40–65 | pandas demonstrations: coercion, domain checks, missingness, EDA |
| 65–90 | Pair exercise: cleanup policy, exploratory charts and interpretation |
| 90–100 | Break |
| 100–125 | Why preprocessing leaks: train/test split and fitting transformations |
| 125–155 | Colab: ColumnTransformer + SimpleImputer + StandardScaler + OneHotEncoder |
| 155–175 | Independent modification, leakage critique, explain design choices |
| 175–180 | Exit ticket and S03 preview |

**Materials:** [lecture](lecture.md) · [slides source](slides.md) · [read-aloud speaker script](speaker-script.md) · [exercises](exercises.md) · [Colab lab](student-lab.ipynb).

**Requirements:** campus computer with browser/Colab, Python, pandas, NumPy, matplotlib, scikit-learn; no external dataset, credentials, GPU or paid service. The notebook uses synthetic data.

**Teaching approach:** work in pairs with rotating driver/reviewer; individual exit ticket. No graded assessment is introduced. Offer text descriptions of each chart and printed summary tables.

**Boundary:** we fit *preprocessors* in S02, not regression/classification models; S03 addresses linear regression. The held-out split is demonstration only, not a statistically reliable claim from a tiny synthetic sample.

**Before release:** instructor checks Colab execution, visualization legibility, version compatibility, all exercise instructions, LO2 alignment, and publication rights. Materials remain subject to professor review.
