# S03 — Read-aloud professor script

Matches the 18-slide presentation. Use the README agenda for timing. During practice, leave the corresponding mission slide visible and demonstrate the notebook. All content is in English, matching the course.

## Slide 01 — Regression I

**Say**

Today we will train a model that predicts a numeric amount. Last session we prepared features, and today we will use those features to compare a regression model with a simple reference. We will work with fictional subscription users and predict their spend over the next thirty days. The numbers are synthetic, so our goal is to learn a method we can defend. We will define the task, explain the line and its error, and evaluate it without letting the final test influence our choices. After the concepts, you will complete a quest in Colab. You can earn points by doing the tasks and explaining your reasoning. The points are practice feedback and do not affect the module's formal assessment.

**Do / ask**

Ask in chat: what did our S02 preprocessor learn from its training rows?

**Transition**

First, let us connect today's work to the learning outcome.

## Slide 02 — Today’s learning goals

**Say**

The approved outcome for this part of the course is LO3: Build, train, and evaluate supervised learning models, regression and classification, using scikit-learn, applying rigorous cross-validation. Today develops its regression component. We will cover classification later. By the end you should be able to explain a line's parameters, calculate an error, compare a baseline with linear regression, and state what the validation result does and does not establish. You will also need to identify which rows each transformation may learn from. There is a ten-minute break before the practical work. During the tutorial, work with a partner where possible and take turns explaining the results. Your explanation matters as much as the code running.

**Do / ask**

Ask: which transformation statistics from S02 must stay inside the training partition?

**Transition**

We need to define exactly what the model will predict.

## Slide 03 — The prediction contract

**Say**

Imagine that our fictional service reaches the end of the current month. We know the user's current spend, current usage, completed tenure and current plan. We want to estimate total spending during the next thirty days. Notice the separation between now and later. The future outcome exists in our teaching table because we need labels to learn and evaluate, but we would not know it when making a new prediction. The user ID identifies a row and is not part of the input. One user appears once in this synthetic dataset. In a real system, repeated monthly snapshots would change the splitting strategy. Keep the unit of observation, prediction time, horizon and units in your notebook. This contract will help you detect leakage before looking at any scores.

**Do / ask**

Ask: would a next-month invoice be available at the end of this month?

**Transition**

Now we can describe a simple relationship between an input and that numeric outcome.

## Slide 04 — Slope and intercept

**Say**

This is a teaching line chosen so we can reason about its units. It is not a fit to real users. The slope tells us how much the prediction changes when weekly sessions increase by one. The intercept is the prediction when that input is zero. For twelve sessions, this line produces thirty-four euros. Read the chart as noisy fictional observations near a line, rather than a promise that every person follows it. With more than one input we add a coefficient for each encoded feature. That coefficient is conditional on the other inputs in the model. It does not establish what would happen if we intervened and changed the user's behaviour. Also remember that scaling changes the coefficient's units. A coefficient on a standardised input refers to a training standard deviation.

**Do / ask**

Pause for a manual prediction at seven sessions. Ask students to label the units.

**Transition**

The observations will usually miss the line, so we need to quantify that gap.

## Slide 05 — Residuals

**Say**

We will use actual minus predicted as our residual convention. In the first row, the actual amount is twenty and the prediction is eighteen, so the residual is positive two euros. In the second row the prediction is larger than the actual amount, so the residual is negative. Always state your convention before interpreting a residual plot. The table also shows squared residuals. They are all nonnegative. If we simply averaged the signed errors, positive and negative mistakes could cancel and hide poor predictions. These three rows are a worked explanation. In your own task, you will implement a function and verify it on other inputs. Keep the distinction between an individual residual and an aggregate metric.

**Do / ask**

Ask: which row is the largest miss in absolute euros?

**Transition**

Squaring these gaps gives the objective used by ordinary least squares.

## Slide 06 — The least-squares objective

**Say**

Ordinary least squares chooses coefficients that minimise the sum of squared residuals. If we divide that sum by the fixed number of rows, we obtain mean squared error and the best coefficients stay the same. The square makes large errors more influential. In our three-row example, the squared residuals sum to fourteen. Dividing by three gives the mean squared error. Because the target is euros, the squared error is in squared euros. Do not confuse the loss that fits the model with the metric we later use to select a candidate. We will fit squared error but use validation MAE for selection. That is a deliberate choice and we will name both quantities. You do not need to implement a numerical solver for today's lab.

**Do / ask**

Ask: what changes in the loss if one error doubles?

**Transition**

A small grid can show what it means for a coefficient to minimise this objective.

## Slide 07 — A coefficient changes the loss

**Say**

Here we hold the intercept at ten and try several slopes on three perfectly linear teaching points. A slope of two matches all three points and gives zero mean squared error. Moving away from two makes the loss grow. This is a deliberately simple example so the meaning of a minimum is visible. Real data have noise, missing measurements and multiple inputs. The numerical solver finds least-squares coefficients without requiring us to try this hand grid. Dense LinearRegression uses numerical linear algebra. Its fit call is not an epoch loop. When we perform five-fold validation, we train five separate fitted estimators for that candidate. The split seed controls how rows are allocated, and changing it does not define a number of training epochs.

**Do / ask**

Ask: does a zero loss on these three invented rows establish real predictive performance?

**Transition**

For reporting, we need metrics whose units we can explain.

## Slide 08 — Regression metrics

**Say**

MAE averages the absolute residuals, so we can read it in euros. RMSE is the square root of MSE and also has euro units, while giving large errors more influence. R squared is dimensionless and compares squared error with variation around the evaluated target mean. It is not a percentage of correct predictions. It can be negative on unseen data. A training-mean baseline uses a constant learned from training targets, which differs from the held-out target mean inside the R squared formula. That is why even the baseline can have a negative test R squared. An MAE of five euros does not guarantee that the next individual error is below five euros. We will keep these limits visible in our final report.

**Do / ask**

Ask: which of these metrics has squared-euro units, and which has no units?

**Transition**

Before interpreting any model score, we need a simple reference.

## Slide 09 — The training-mean baseline

**Say**

Suppose we ignore the features and always predict the average target amount observed in the training rows. That is our mean baseline. It may sound simple, but it gives us a meaningful reference: does using the inputs improve the validation result? The baseline's constant must be calculated separately for every training fold. Computing a mean from all development targets before cross-validation would expose validation targets. In the notebook, both candidates use the same rows, folds and metrics. DummyRegressor ignores the transformed features, but its training-target mean still respects the fold boundaries. If a baseline wins, report that honestly. The quest gives full credit for a valid comparison and a supported conclusion. It never rewards making the scores look better.

**Do / ask**

Ask: what information does the baseline learn, even though it ignores X?

**Transition**

We will reserve a test set before comparing the candidates.

## Slide 10 — Development and final test

**Say**

The first split reserves one hundred rows for a final test. The remaining four hundred rows form our development data. All candidate comparison happens within the development portion. We will not inspect test outcomes to decide which features, transformations or candidate to use. A fixed seed makes this demonstration repeatable, but it does not make an inappropriate split scientifically valid. For monthly observations of the same user, we might need a group split. For forecasting into a later calendar period, we might need a chronological split. The independent synthetic users let us use shuffled splits for this lesson. Keep that assumption in the final model card. The notebook generates new records, so it does not accidentally recycle a holdout already explored in S02.

**Do / ask**

Ask: does reserving a test set after fitting the scaler keep it independent?

**Transition**

The development data will rotate through five validation folds.

## Slide 11 — Five-fold development validation

**Say**

For the first iteration, train on four fifths of the development rows and validate on the remaining fifth. Repeat the process until each development row has served once as validation. There are three hundred and twenty training rows and eighty validation rows in each fold. For each candidate, the procedure fits five fresh estimators. Their validation scores help us compare a modelling procedure across these partitions. The variation between folds is useful context, but its standard deviation is not a confidence interval. The training subsets overlap, so we should not casually treat the fold scores as independent experiments. We will use a modest comparison today and return to evaluation design in S07.

**Do / ask**

Ask students to state the number of fits per candidate, and the role of the 100 test rows.

**Transition**

Every fold also needs its own learned preprocessing.

## Slide 12 — Preprocessing inside every fold

**Say**

A pipeline keeps the fitted transformations with the estimator. In one fold, it learns medians, scaling statistics and categorical vocabulary from that fold's training rows. It then applies those learned transformations to the validation rows. This repeats from a fresh clone in each fold. Fitting the preprocessor on all development rows before cross-validation would leak validation information, even though the separate final test remains untouched. In the tutorial, we will inspect the first fold's imputer and compare its medians with the actual training rows for that fold. That provides concrete evidence of where the statistics came from. The final refit can use all development rows after selection, because it serves a different stage of the protocol.

**Do / ask**

Ask: where should cross_validate receive the raw development table?

**Transition**

We can now state the selection rule before we see the final test.

## Slide 13 — Candidate selection and final refit

**Say**

Our rule is fixed before test evaluation: choose the candidate with the lower average development validation MAE. If the means are exactly tied, keep the mean baseline. We will refit the selected pipeline on the full development data. We also refit the baseline as a fixed reference for the final report. The final test stage evaluates these locked choices. It does not choose the candidate. If the result disappoints us, we preserve it and discuss what a future evaluation plan would require. Notice that scikit-learn's loss scorers return negative values so that a larger score is better. We reverse their signs for reporting errors. For RMSE we square-root each fold's MSE before averaging fold RMSE values.

**Do / ask**

Check understanding: can a surprising test result change today's locked winner?

**Transition**

Take a break. Then we will implement the full workflow in the quest.

## Slide 14 — 10-minute break

**Say**

We will pause for ten minutes. When you return, open the tutorial link from the session README and save a private copy. Keep the original course notebook unchanged. You can work individually or with a partner, and both people should be ready to explain a result. We will use synthetic records only. There is no need to upload personal customer data or obtain an API key. If you have difficulty with the runtime, show me the error message and we can use the short concept notebook as a fallback.

**Do / ask**

Display the README tutorial link in Meet chat.

**Transition**

After the break, start with the task contract rather than jumping to model fitting.

## Slide 15 — Regression Quest: missions 1–5

**Say**

The first five missions take us from the prediction contract to the regression pipeline. Each section includes a runnable guided example and a separate student task. Running all the examples will not award completion points. Replace the student placeholders, run the check and write your explanation. Code checks earn the code portion of a mission. Reasoning points follow a conversation with a peer or lecturer using the listed criteria. Only then should you update that mission's review flag in your private notebook. You can retry and use the hints without losing points. The ledger uses mission identifiers, so rerunning a check cannot add duplicate points. Start with the four allowed inputs, then establish the split, implement squared error, calculate the baseline fold errors and build your own pipeline.

**Do / ask**

Demo the save-copy action and M1 check. Around mission 4, rotate driver and reviewer.

**Transition**

Once both candidates exist, compare the validation evidence.

## Slide 16 — Validation evidence: missions 6–7

**Say**

Mission six asks you to produce the five fold MAEs and explain the comparison. In the checked local run, linear regression has a lower average development MAE than the mean baseline. Your runtime prints its own evidence, which is what your report should cite. These are synthetic teaching results and the generator intentionally contains a linear signal. We also inspect out-of-fold development predictions and residuals. Those plots help us reason about errors without turning the test into an iterative design tool. Mission seven then performs the locked final test stage. Report its actual numbers, explain the units, compare with the reference and state limitations. A large R squared on this dataset cannot establish real customer usefulness. Keep your interpretation proportional to the evidence.

**Do / ask**

Ask pairs to explain one fold result and identify one limitation before opening the final test stage.

**Transition**

The final mission uses the already fitted selected pipeline for a new input.

## Slide 17 — A new prediction: mission 8

**Say**

Create one new fictional user with current input values inside the stated ranges. Pass that one-row table through the fitted selected pipeline. Do not fit again and do not invent a future outcome. Explain the next-thirty-day horizon, the euro units and why we have no calibrated individual prediction interval. Then view your scoreboard. Bonus points appear separately and cannot replace unfinished core missions. If you finish early, compare a median baseline using development validation only. That optional work cannot revise the core test result. Save your answers and XP privately. We will not put student notebooks or marks in the public repository. Each learner should explain at least one methodological choice in their own words, even when working in a pair.

**Do / ask**

Request a short model-card explanation. Let students finish reviews and save their copy.

**Transition**

We will finish with three individual checks and a preview of S04.

## Slide 18 — Exit ticket

**Say**

Answer these questions individually in your own words. You can type privately or explain orally. First, state what a positive residual means under our actual-minus-predicted convention. Second, identify precisely which rows a fold's imputer may learn from. Third, explain why a simple baseline can be an appropriate model choice. Today we defined a numeric task, linked a line to a loss function, and compared candidates within a validation protocol. The exercise is complete when the code and your explanation agree. In S04 we will explore how polynomial features and regularisation change the modelling choices. Keep today's final test result as recorded, and use the self-study time to strengthen the derivation and model card rather than chasing a nicer test score.

**Do / ask**

Collect individual responses through the usual private teaching channel.

**Transition**

End of session

