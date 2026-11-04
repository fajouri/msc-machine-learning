# S03 — Regression I

**Mode:** online via Google Meet · **Duration:** 180 minutes · **Block:** B02 Regression · **Primary outcome:** LO3

**Approved LO3:** Build, train, and evaluate supervised learning models (regression and classification) using scikit-learn, applying rigorous cross-validation.

This session develops the regression component of LO3. Classification and deeper evaluation methods follow in later sessions. The approved course sequence and assessment weights remain unchanged.

## Learning goals

By the end, students should be able to:

1. Define a numeric target, its units, the prediction time and available inputs.
2. Explain slope, intercept, residuals and the least-squares objective.
3. Compare linear regression against a training-mean baseline on identical validation folds.
4. Put learned preprocessing inside a pipeline so each fold fits its own transformations.
5. Report MAE, RMSE and R² with limitations, and reserve a test set for a final check.

## Materials

- [Editable PowerPoint](slides.pptx) and [slide source with notes](slides.md).
- [Detailed lecture notes and reading](lecture.md).
- [Read-aloud professor script](speaker-script.md), matching the 18 slides.
- [Exercises and XP rules](exercises.md).
- [Short concept-demonstration notebook](student-lab.ipynb), for lecturer preparation or catch-up.
- [Main tutorial: AI Subscription Regression Quest](tutorials/01-ai-subscription-regression/README.md).
- [Open the main tutorial in Colab](https://colab.research.google.com/github/fajouri/msc-machine-learning/blob/master/sessions/S03/tutorials/01-ai-subscription-regression/tutorial.ipynb).

## Class agenda

| Minutes | Activity |
| --- | --- |
| 0–10 | S02 recall: features, target, train-only preprocessing |
| 10–25 | Prediction task, slope and intercept, one manual prediction |
| 25–45 | Residuals, squared loss, least squares and metric units |
| 45–60 | Mean baseline, fair comparison and model limitations |
| 60–75 | Five-fold validation, fold-local pipelines and final test set |
| 75–85 | Break |
| 85–105 | Tutorial missions 1–3: task, split, objective function |
| 105–130 | Missions 4–5: baseline and regression pipeline |
| 130–155 | Missions 6–7: cross-validation and one final test evaluation |
| 155–175 | Mission 8: a new prediction, model card and peer explanation |
| 175–180 | Individual exit ticket and S04 preview |

Use slides 1–13 for the concepts, slide 14 for the break, and slides 15–18 during practice and closing. The tutorial takes about 90 minutes with lecturer support, or 90–120 minutes independently. The optional bonus is follow-up practice. The concept notebook is a shorter alternative, not an additional compulsory lab in the same 180 minutes.

## XP game

Eight missions offer **100 core XP**, plus **20 optional bonus XP**. Points reward demonstrated work and explanations, with retries and hints allowed. No points depend on speed or obtaining the lowest prediction error. Running the supplied examples alone earns no XP. Code checks and peer/lecturer review are recorded separately in each student's private notebook. XP is formative practice and introduces no graded assessment or change to the 60/30/10 scheme.

## Delivery and accessibility

Use pairs in Meet breakout rooms where available, or individual work with chat check-ins. Rotate driver and reviewer after mission 4. Permit typed explanations or a short oral explanation. All figures include labelled axes and text descriptions. Share pseudonyms only if students voluntarily compare XP. Keep student submissions and XP records outside the public repository.

Python, NumPy, pandas, Matplotlib and scikit-learn are sufficient. CPU only. No external data, account tokens, GPU or paid service is required. The tutorial generates a **new synthetic dataset**, independent of S02's export, so all students begin from the same schema. It continues S02's scenario without depending on its runtime files.

## Completion notes

Created 4 November 2026. Local Python execution checked for both notebooks, including the tutorial starter and a private completed challenge run. Slides rendered and inspected. Google Colab/browser behaviour and professor academic review remain to be checked before student release. Synthetic results demonstrate a method and provide no evidence about real subscription customers.
