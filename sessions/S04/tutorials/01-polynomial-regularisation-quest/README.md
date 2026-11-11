# Session 04 — Polynomial Regression Quest: Ridge, Lasso and Alpha

**Level:** beginner-friendly MSc practical | **Duration:** 75–95 minutes | **Tools:** Google Colab, Python, scikit-learn | **Language:** simple English

> **Learning goal:** Explain why a more complicated model is not always better, and use Ridge, Lasso and alpha to control complexity. This tutorial is formative practice, not a graded assessment.

## The big idea — in plain English

Imagine learning the answers to ten practice questions by heart. You may score 100% on those ten questions but struggle with new questions. A machine-learning model can do the same thing. This is called **overfitting**.

- **Underfitting:** The model is too simple. It misses the important pattern. Both training and validation errors may be high.
- **Overfitting:** The model is too flexible. It learns accidental details or noise. Training error can be low, while validation error is higher.
- **Generalisation:** The model predicts new, unseen examples well.

A polynomial model adds columns such as `x²`, `x³` and `x⁵`. This helps the model learn curves, but many extra columns can make it overly flexible.

### Ridge (L2): "Keep the coefficients small"

Ridge is linear regression with an extra rule: **large coefficients cost extra**. It tries to fit the data well *and* keep the coefficients reasonably small. Think of it as turning down the volume on an overly dramatic model. Ridge usually makes coefficients smaller, but generally does **not** make them exactly zero.

Simplified objective (intercept not penalised): **squared prediction error + alpha × sum of squared coefficients**.

### Lasso (L1): "Some coefficients may become zero"

Lasso also discourages large coefficients, but it uses the **absolute values** of coefficients. Unlike Ridge, it can make some coefficients **exactly zero**. That means the corresponding transformed features no longer contribute to the prediction.

Simplified objective (intercept not penalised): **squared prediction error + alpha × sum of absolute coefficients**.

**Important:** A zero Lasso coefficient does **not** prove a feature is useless. With correlated features, Lasso may choose one and discard another. The result depends on the data and alpha.

### Alpha: "How strong is the brake?"

**Alpha (α)** controls how strongly Ridge or Lasso penalises large coefficients.

| Alpha | Meaning | Possible outcome |
|---|---|---|
| Small, e.g. 0.01 | Gentle penalty | Flexible model; may still overfit |
| Medium, e.g. 1 | Stronger penalty | Often smaller coefficients |
| Large, e.g. 100 | Very strong penalty | Model may become too simple and underfit |

**Larger alpha does not always mean better predictions.** We choose alpha using **validation data**, not the final test.

### Why scaling matters

Imagine one feature is measured in metres and another in millimetres. Their coefficients can have very different sizes even when they represent similar information. Ridge and Lasso penalise coefficient sizes, so this would make the comparison unfair. **StandardScaler** puts generated features on comparable scales. We fit it **inside a Pipeline** during cross-validation to avoid learning information from validation rows.

## Mission map — 100 XP total

| Mission | What you do | XP |
|---|---|---:|
| 1 | Predict which model might underfit | 10 |
| 2 | Create and inspect curved data | 10 |
| 3 | Compare polynomial degrees fairly | 15 |
| 4 | Explain Ridge, Lasso and alpha | 15 |
| 5 | Experiment with alpha | 20 |
| 6 | Examine coefficients and explain zero | 10 |
| 7 | Choose a model using validation only | 10 |
| 8 | Evaluate the locked model once | 10 |

**XP is for completing and explaining tasks, not for achieving the lowest score.** Work with a partner if possible. One student runs the code; the other explains what it means. Switch roles halfway through.

## Mission 1 — Predict before coding (10 XP, 5 minutes)

Consider three models:

| Model | Training MAE | Validation MAE |
|---|---:|---:|
| A | 12 | 13 |
| B | 4 | 5 |
| C | 1 | 18 |

**Your tasks:** Which model might be underfitting? Which might be overfitting? Which would you prefer based on this evidence? Why is the smallest training MAE not necessarily best?

Write 2–3 sentences before reading on. **Hint:** Lower MAE is better; compare training and validation.

## Mission 2 — Generate data (10 XP, 10 minutes)

Open a new notebook at https://colab.new. Copy the following into a code cell and run it.

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, KFold, cross_validate
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.metrics import mean_absolute_error, mean_squared_error

SEED = 42
rng = np.random.default_rng(SEED)
X = np.sort(rng.uniform(-3, 3, 500)).reshape(-1, 1)
y = (4 + 1.5 * X[:, 0] - 1.2 * X[:, 0]**2
     + 0.35 * X[:, 0]**3 + rng.normal(0, 3, 500))

# Set aside 100 observations. Do not use them for model selection.
X_dev, X_test, y_dev, y_test = train_test_split(
    X, y, test_size=0.20, random_state=SEED
)
cv = KFold(n_splits=5, shuffle=True, random_state=SEED)
print("Development rows:", len(X_dev), "| Reserved test rows:", len(X_test))

plt.scatter(X_dev[:, 0], y_dev, s=14, alpha=0.55)
plt.xlabel("Input x")
plt.ylabel("Target y")
plt.title("Development data: a curved pattern with noise")
plt.show()
```

**Explain:** Is the relationship perfectly straight? What is noise? Why do we reserve the 100 test observations?

**Checkpoint:** You should see 400 development rows and 100 test rows. The scatter plot should show a noisy curve.

## Mission 3 — Compare degrees (15 XP, 15 minutes)

We will use the **same five folds** and the **same MAE metric** for every model. Each fold trains on 320 development rows and validates on 80. The final test rows are untouched.

```python
def make_model(degree, penalty="none", alpha=1.0):
    if penalty == "ridge":
        estimator = Ridge(alpha=alpha)
    elif penalty == "lasso":
        estimator = Lasso(alpha=alpha, max_iter=100000)
    elif penalty == "none":
        estimator = LinearRegression()
    else:
        raise ValueError("Unknown penalty")

    return Pipeline([
        ("polynomial", PolynomialFeatures(degree=degree, include_bias=False)),
        ("scaler", StandardScaler()),
        ("regression", estimator),
    ])

def evaluate_cv(model):
    scores = cross_validate(
        model, X_dev, y_dev, cv=cv,
        scoring="neg_mean_absolute_error",
        return_train_score=True,
    )
    # scikit-learn uses negative MAE for scoring; change the sign.
    return {
        "train_mae": -scores["train_score"].mean(),
        "validation_mae": -scores["test_score"].mean(),
        "validation_sd": scores["test_score"].std(ddof=1),
    }

degree_rows = []
for degree in [1, 2, 3, 5, 8]:
    degree_rows.append({
        "model": f"Linear degree {degree}",
        "degree": degree,
        "penalty": "none",
        "alpha": None,
        **evaluate_cv(make_model(degree)),
    })
degree_table = pd.DataFrame(degree_rows)
display(degree_table.round(3))
```

**Your tasks:** Find the smallest *training* MAE. Find the smallest *validation* MAE. Are they from the same model? Explain why a higher degree may be worse on new observations.

**Checkpoint:** The table should have five rows and three error columns. The exact values depend on library versions, but degree 3 should be competitive on this synthetic data.

## Mission 4 — Teach the concepts back (15 XP, 10 minutes)

Complete these sentences in your own words:

1. Ridge makes coefficients ______ but usually not exactly ______.
2. Lasso can make some coefficients exactly ______.
3. Alpha controls the strength of the ______.
4. A very large alpha can lead to ______.
5. We scale polynomial features because ______.

**Mini-quiz:** True or false? "If Lasso sets a coefficient to zero, the corresponding feature is scientifically proven irrelevant." Explain.

## Mission 5 — Change alpha, observe what happens (20 XP, 15 minutes)

Hold the degree fixed at **5** so we can isolate the effect of Ridge vs Lasso and alpha.

```python
regularisation_rows = []
for penalty in ["ridge", "lasso"]:
    for alpha in [0.01, 0.1, 1.0, 10.0, 100.0]:
        regularisation_rows.append({
            "model": f"{penalty} degree 5 alpha {alpha}",
            "degree": 5,
            "penalty": penalty,
            "alpha": alpha,
            **evaluate_cv(make_model(5, penalty, alpha)),
        })
regularisation_table = pd.DataFrame(regularisation_rows)
display(regularisation_table.round(3))

for penalty in ["ridge", "lasso"]:
    subset = regularisation_table[regularisation_table["penalty"] == penalty]
    plt.plot(subset["alpha"], subset["validation_mae"], marker="o", label=penalty)
plt.xscale("log")
plt.xlabel("Alpha (log scale)")
plt.ylabel("Mean validation MAE (lower is better)")
plt.title("How regularisation strength affects validation error")
plt.legend()
plt.show()
```

**Your tasks:** For each method, identify the best alpha *among the values tried*. Does increasing alpha always improve MAE? Which values seem to make the model too simple? Explain in everyday English.

**Hint:** Alpha is not a polynomial degree. Degree changes which features are available; alpha changes how strongly their coefficients are penalised.

## Mission 6 — Look at the coefficients (10 XP, 10 minutes)

Fit two models **only on development data**. This is for understanding coefficients, not for selecting using the final test.

```python
for penalty in ["ridge", "lasso"]:
    demo = make_model(degree=5, penalty=penalty, alpha=1.0)
    demo.fit(X_dev, y_dev)
    coefficients = demo.named_steps["regression"].coef_
    print(penalty, "coefficients:", np.round(coefficients, 3))
    print("Exactly zero:", np.sum(np.isclose(coefficients, 0, atol=1e-10)))
```

**Explain:** Which method can produce exact zeros? Does this mean the zeroed feature has no relationship with the target? Why not?

**Note:** Polynomial features can be correlated; Lasso's choice is not a causal explanation.

## Mission 7 — Select and lock a model (10 XP, 10 minutes)

Compare **all candidates using development cross-validation only**. Select the candidate with the smallest mean validation MAE. If practically tied, explain why a simpler model might be preferable. Record your choice **before** running Mission 8.

```python
candidates = pd.concat(
    [degree_table, regularisation_table], ignore_index=True
)
ranked = candidates.sort_values("validation_mae").reset_index(drop=True)
display(ranked[["model", "train_mae", "validation_mae", "validation_sd"]].round(3))

chosen = ranked.iloc[0]
selected_degree = int(chosen["degree"])
selected_penalty = str(chosen["penalty"])
selected_alpha = (1.0 if pd.isna(chosen["alpha"]) else float(chosen["alpha"]))

print("LOCKED:", chosen["model"])
print("CV validation MAE:", round(chosen["validation_mae"], 3))
```

**Write down:** Selected model, degree, penalty, alpha, mean validation MAE, and a two-sentence justification. Do not change this choice after looking at the final test.

## Mission 8 — Final test, once (10 XP, 10 minutes)

Only after you have recorded the locked choice, run:

```python
final_model = make_model(
    selected_degree, selected_penalty, selected_alpha
)
final_model.fit(X_dev, y_dev)
predictions = final_model.predict(X_test)

print("Final test MAE:", round(mean_absolute_error(y_test, predictions), 3))
print("Final test RMSE:", round(np.sqrt(mean_squared_error(y_test, predictions)), 3))

residuals = y_test - predictions
plt.scatter(predictions, residuals, alpha=0.65)
plt.axhline(0, linestyle="--", color="black")
plt.xlabel("Predicted y")
plt.ylabel("Residual: actual minus predicted")
plt.title("Final test residuals — descriptive only")
plt.show()
```

**Explain:** Is the final test error similar to validation MAE? Do residuals show an obvious pattern? What could go wrong if we used this test result to choose a different degree or alpha?

**Critical rule:** Do **not** revise the model based on the final test result. That would turn the test into another validation set.

## Exit ticket — five questions

1. Why can a straight line underfit curved data?
2. Why can degree 8 perform worse than degree 3 on validation?
3. Explain Ridge vs Lasso to a friend without using a formula.
4. What happens if alpha is much too large?
5. Why must the scaler be inside the cross-validation Pipeline?

## Optional bonus (20 XP, after class)

**Bonus A (10 XP):** Plot predicted curves for degrees 1, 3 and 8 after fitting each model on development data. Plot only in the observed x-range. Explain which curves look too simple or too wiggly.

**Bonus B (10 XP):** Explain why a random split may be inappropriate for time-series forecasting or repeated observations from the same customer. Describe a better split for one of these cases.

## Lecturer notes / suggested answers (keep separate when assigning)

- Mission 1: A may underfit; C shows a large generalisation gap consistent with overfitting; B is preferable on the supplied validation evidence.
- Mission 4: smaller; zero; zero; penalty; underfitting; comparable scales. A zero Lasso coefficient is **not** proof of irrelevance.
- Mission 5: The best alpha is empirical. Too much penalty can increase both training and validation error.
- Mission 7: Validation MAE selects the candidate; the reserved test must not be used for model choice.
- Mission 8: A single test estimate is limited by sample size, sampling noise and whether the synthetic setup reflects real use.
- **Timing:** Missions total approximately 85 minutes plus discussion. The synthetic generator intentionally contains a cubic term and noise. This is a learning exercise, not evidence about real-world braking or customers.
- **Academic caution:** A low training MAE alone does not prove overfitting; use the validation gap and other diagnostics. The simplified Ridge/Lasso objective above omits implementation-specific constants.
