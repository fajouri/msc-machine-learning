# S02 — Lecturer's spoken script (English)

**Session:** Data Wrangling and Exploratory Data Analysis · **Mode:** campus · **Duration:** 180 minutes · **LO2**.

This is a spoken, student-safe companion to `slides.md`. Read the **Say** sections aloud in your own voice. Cues in square brackets are actions, not sentences to read. The clock ranges include demonstrations, discussion, group work and a break: the spoken text by itself is not intended to occupy the full three hours. Use `student-lab.ipynb` for demonstrations. Do not read commands character by character; point students to the cell.

## SL01 — From raw data to trustworthy features (0–5 min)

**Say:**

“Welcome back, everyone. Last time, we discussed what machine learning is, how supervised learning differs from unsupervised and reinforcement learning, and why we must distinguish training data from data used to evaluate our work.

Today we move one step closer to building an actual machine learning system. But instead of jumping into algorithms, we will focus on something that often determines whether an entire project succeeds or fails: the data.

Imagine you have a perfectly implemented model, but half the numerical values were entered as text, some customers appear twice, and an important feature was only recorded after the event you want to predict. Would a sophisticated model fix those problems? No. It may learn misleading patterns extremely efficiently.

Our journey today starts with raw data. We will inspect it, document cleaning decisions, explore what it contains, and finally transform it into features that future models can use. The critical rule is that any transformation which learns statistics must learn them from training data only.”

**[Ask:]** “What is one way a dataset can mislead us before we train anything?” Take two or three replies.

**Transition:** “Let us define exactly what we want to achieve.”

## SL02 — LO2 and the route through today's lab (5–15 min)

**Say:**

“Our learning outcome for this session is: *Implement data preprocessing pipelines including cleaning, feature engineering, scaling, and encoding using Python, pandas, and scikit-learn.*

There are four important verbs here. Cleaning means identifying and handling data problems. Feature engineering means constructing useful inputs from information we actually have. Scaling means transforming numerical magnitudes into a representation useful for some algorithms. Encoding means converting categories into a numerical form without inventing a false ordering.

We will use pandas to understand and manipulate tables, Matplotlib to explore distributions and relationships, and scikit-learn to assemble a reliable preprocessing pipeline.

You do not need to memorise every method name. What matters is understanding why a transformation is appropriate, what it learns, and when it is allowed to learn it. At the end, you should be able to explain your preprocessing choices, not just show that the code runs.”

**[Ask:]** “Have you ever opened a spreadsheet where one column contained different formats or missing values? What problems did that create?” Invite short examples.

**Transition:** “We need a dataset that deliberately contains these problems.”

## SL03 — A fictional service transaction dataset (15–22 min)

**Say:**

“We will work with a small dataset of fictional service transactions. The records are synthetic, which means we generated them ourselves. They do not describe real people or businesses.

Each row has fields such as age, monthly spending, number of visits, service channel, and region. We also have a column called future spending. Think carefully about the word *future*. It represents an outcome we might eventually want to predict, but we do not know it at the time we make today's decision. Therefore, we must not include it as a predictor.

We also have a record identifier. An identifier helps us track data quality, but it is not automatically a meaningful numerical feature.

Notice how much we have already decided before selecting an algorithm: which columns exist, what they mean, which can be measured at decision time, and which are outcomes rather than inputs. These choices define the task.”

**[Demo:]** Open the synthetic-data generation cell in Colab and display the first rows.

**[Ask:]** “What would happen if we included future spending as an input to predict future spending?” Discuss target leakage.

**Transition:** “Now we will inspect the dataset as if someone else handed it to us.”

## SL04 — Data-quality audit checklist (22–30 min)

**Say:**

“When receiving a dataset, do not immediately start replacing missing values. First, perform an audit.

Check data types. A column containing numbers may actually be stored as text because one record says ‘not recorded’. Check missing values, but remember that missing is not the same as zero. Zero visits is an observed count; an absent visit count is unknown.

Check duplicates, but ask what a row represents. If each row is a transaction, the same customer may appear several times legitimately. A repeated customer ID is not enough to conclude that two transactions are duplicates.

Check impossible or suspicious ranges. A negative amount of spending may indicate an error, but in another dataset it might represent a refund. A very high age could be a typo, or could reveal that our assumptions need investigation.

Finally, check categories and provenance. ‘WEB’, ‘web’, and ‘ web ’ may refer to one channel, but we need a documented reason to merge them.”

**[Demo:]** Show the data types, null counts, duplicate-ID count and channel categories.

**Transition:** “Missing values are particularly interesting because they can tell us something about how data was collected.”

## SL05 — What does missingness mean? (30–40 min)

**Say:**

“When a value is missing, we know it is absent. We usually do not know why it is absent.

Statistics gives us three common ways to reason about missingness. MCAR means missing completely at random: whether a value is missing is unrelated to the data values. MAR means missingness may depend on information we observed. MNAR means missingness may still depend on an unobserved value itself, even after considering what we observed.

For example, suppose customers with lower spending are less likely to report their spending. If that missingness depends on the spending amount we never see, simply replacing it with the median can produce a misleading picture.

These are assumptions about the data collection process, not labels that pandas can discover from a missing-value percentage.

A common reaction is to delete every incomplete row. But imagine that missingness occurs mainly for one geographic region. Removing those rows could make that region almost disappear from our analysis.

So the question is not ‘Which command removes nulls?’ It is ‘What information might we lose or distort?’”

**[Ask:]** “Could two datasets both have ten percent missing values, but require different strategies?” Discuss a concrete example.

**Transition:** “Let's use pandas to make these issues visible.”

## SL06 — pandas inspection in four operations (40–50 min)

**Say:**

“Pandas gives us concise tools for a first inspection.

The first is `info()`, which reveals column types and non-null counts. The second is `isna().mean()`, which shows the proportion of missing values in each column. Third, `value_counts()` is excellent for detecting unexpected category spelling and rare categories.

The fourth operation, `to_numeric()`, attempts to turn values into numbers. When we use `errors='coerce'`, values that cannot be interpreted numerically become missing values.

That last point matters: the conversion did not magically repair the original information. It exposed values that need further investigation. If we only look at missing values before conversion, we may underestimate the problem.

Watch as we inspect the synthetic spending column. Then compare the missing-value count before and after conversion. Always keep an unmodified version of the raw dataset, so that cleaning decisions are traceable.”

**[Demo:]** Run the audit and cleaning cells. Ask students to predict whether the missing count will increase.

**Transition:** “We have identified problems, but fixing them requires a policy.”

## SL07 — Cleaning needs a documented policy (50–58 min)

**Say:**

“Cleaning is a set of decisions, not a single function.

Suppose channel names contain inconsistent capitalisation or extra spaces. If our domain definition says they are the same channel, we can standardise them. That is a clear, rule-based correction.

Now consider an age of 145. We might decide that ages outside a documented valid range are invalid. In our teaching notebook we flag this value as missing under an illustrative rule, but that range is not a universal rule for all datasets.

And what about a customer spending much more than everyone else? It may be an error, but it may also be our most important customer. Removing unusual values simply because they are inconvenient can make an analysis look cleaner while making it less truthful.

A good cleaning policy states what we changed, why we changed it, and what limitation remains.”

**[Ask:]** “If the dataset contains a channel called ‘mobile-app’, should we automatically convert it to ‘web’?” Highlight the need for domain evidence.

**Transition:** “Once we have a defined schema, we can start asking exploratory questions.”

## SL08 — EDA asks questions, not causal conclusions (58–65 min)

**Say:**

“Exploratory data analysis, or EDA, helps us understand distributions, patterns, and possible data problems.

A histogram shows how a numerical variable is distributed. Does monthly spending concentrate around a particular range? Are there long tails? Remember that changing the number of bins can change its appearance.

A bar chart shows how often categories appear. It can reveal rare categories or remaining spelling inconsistencies.

A scatter plot can reveal an association between visits and spending. But association does not prove causation. More visits may accompany more spending because of customer behaviour, pricing, or some third factor we have not measured.

Every useful chart needs meaningful labels, including units, and an explanation of what its evidence cannot establish.”

**[Demo:]** Run the training-data EDA cell. Ask students to describe one observation without using causal language.

**Transition:** “Now it is your turn to investigate before you modify.”

## SL09 — Pair challenge: diagnose before fixing (65–90 min)

**Say:**

“For the next activity, work in pairs. One person will be the driver, operating Colab. The other will be the reviewer, questioning each proposed decision. Halfway through, switch roles.

Your first task is to identify three data-quality problems in the synthetic dataset. Your second task is to propose three corrections or handling policies, and explain why each is appropriate. Finally, identify one uncertainty you cannot resolve from the dataset alone.

Do not try to make every number look normal. If you discover an outlier, consider whether it is plausible. If you discover a missing value, consider what replacing it might imply. We care about the reasoning as much as the code.

You can use the exercises document as a checklist. Near the end, I will ask each pair to explain one decision and one trade-off.”

**[Activity:]** Let students work; circulate. After approximately 12 minutes ask them to swap roles. Debrief for the final five minutes, without revealing answers to independent exercises.

**Transition:** “After our break, we will examine a subtle mistake that can invalidate later model evaluation.”

## SL10 — Break and reset (90–100 min)

**Say:**

“We will take a ten-minute break. When we return, we will use scikit-learn to turn this cleaned table into numerical features. The most important idea in the second half of the lesson is simple: transformations that learn from data must not learn from our holdout set.

Before you leave, save your Colab copy and make sure you can reopen it.”

**[Action:]** Resume at minute 100.

## SL11 — The leakage trap (100–112 min)

**Say:**

“Imagine that we want to evaluate a future model on data it has never seen. We split our dataset into a training set and a holdout set. That sounds safe, but there is a common trap.

Suppose we calculate the average and standard deviation using *all* rows, and only then split into training and holdout. Our preprocessing has already learned something about the holdout distribution. The model pipeline is no longer independent of the evaluation data.

The correct order is: first split; next fit the transformation using training rows; then apply the already-fitted transformation to training and holdout rows. The holdout contributes no information when deciding the transformation parameters.

The same principle applies to imputing missing values and discovering categorical vocabularies. These operations may look simple, but they still learn from the data.

In real projects, split design must also match the problem. If repeated measurements from the same person appear in both groups, a random row split can produce misleadingly optimistic estimates. Time and groups sometimes matter more than randomness.”

**[Ask:]** “Can leakage happen even if we never look at the target column?” Give the training-versus-all-data median example.

**Transition:** “What exactly is the preprocessor learning?”

## SL12 — What a transformation learns (112–125 min)

**Say:**

“Let's look at the parameters learned by transformations.

A median imputer learns a median from the observed training values. When a later record has a missing value, the imputer uses that training median. It does not recompute a different median using the holdout.

A standard scaler learns the training mean and standard deviation. It then transforms a value using the formula: value minus training mean, divided by training standard deviation.

This produces standardised values. It does not make the distribution normal, and it does not guarantee the results lie between minus one and one.

A categorical encoder learns which category names were present during fitting. Later, it must have a defined response when it encounters a previously unseen category.

In all three cases, the transformation has state. Once we have fitted that state on the training set, we should reuse it consistently.”

**[Demo:]** Inspect the numeric medians and the transformed column names after fitting.

**[Ask:]** “If the holdout has a larger mean than training, should we update the scaler?” Explain why not during independent evaluation.

**Transition:** “Let's package these transformations so they are less likely to be applied inconsistently.”

## SL13 — Two pipelines, one feature matrix (125–138 min)

**Say:**

“Our dataset contains two broad kinds of features: numerical and categorical.

For numerical columns, we will use a pipeline that first imputes missing values with the training median, then standardises the numbers. The order matters because a scaler cannot use an unknown numerical value as though it were a valid measurement.

For categorical columns, we will first replace missing categories with the most frequent category in training. Then we will apply one-hot encoding to represent categories with indicator columns.

Scikit-learn offers `Pipeline` for sequencing steps and `ColumnTransformer` for applying different steps to different columns. Together they give us a repeatable recipe.

When we call `fit_transform` on training data, the transformations learn their parameters and produce a feature matrix. When we call `transform` on the holdout, they use those same parameters without learning again.

We have prepared model-ready features. We have **not** trained a regression model yet. That comes in S03.”

**[Demo:]** Open the ColumnTransformer cell and explain the numeric and categorical branches before running it.

**Transition:** “Categorical encoding changes the number of columns, so let's inspect the result.”

## SL14 — The encoded feature-space expands (138–148 min)

**Say:**

“A categorical feature may look like one column in pandas, but the resulting model-ready representation may contain several columns.

For example, a channel with the categories web, store and phone may become three indicator columns. The value one marks the observed category; zeros mark the alternatives. This avoids treating category names as if they had a meaningful numerical order.

But there are trade-offs. If a field has thousands of unique values, one-hot encoding can create many columns. A unique record identifier, for example, is rarely useful as an ordinary categorical predictor.

We must also handle unseen values. With `handle_unknown='ignore'`, a category not learned during training does not cause the encoder to fit a new vocabulary. Its encoded block may contain all zeros. That makes the pipeline operationally stable, but we still need to decide whether the unknown category has domain significance.”

**[Ask:]** “Would you one-hot encode a transaction ID?” Invite a justification.

**Transition:** “Now run the complete transformation and inspect exactly what it produces.”

## SL15 — Lab: transform train and holdout (148–155 min)

**Say:**

“Please move to the preprocessing cell in the notebook.

First, look at the list of numeric and categorical columns. Check that the target and record identifier are not included. Next, run the pipeline fit on the training subset only. Then transform the holdout without fitting again.

Compare the shapes of the two resulting matrices. Their row counts should differ because the two splits contain different observations, but their feature-column counts should match.

Finally, inspect the feature names. Can you still explain what each output column represents? A model-ready matrix is useful only if we can interpret and reproduce the steps that created it.”

**[Activity:]** Help pairs run the cell and inspect medians, feature names and shapes. Do not introduce prediction metrics.

**Transition:** “Let's test whether that same pipeline survives a realistic surprise.”

## SL16 — Independent challenge (155–175 min)

**Say:**

“Now you will work independently in your own notebook copy. Imagine that a region is missing, that one record has zero visits, and that a new category appears in data we did not use for fitting.

Your job is to examine how our pipeline handles each case, not simply to force the code to produce an output.

For the zero-visits case, consider the engineered feature ‘spending per visit’. Dividing by zero is not a meaningful numerical measurement. What should that feature represent, and how should the subsequent imputer treat it?

For an unseen category, test whether the already-fitted encoder can transform the record without changing the set of output columns.

As you work, write a brief explanation of the choices you made, what is learned from training, and what uncertainty remains. You may propose a different policy, as long as you explain its trade-off. There is no single universally correct cleaning strategy.”

**[Activity:]** Allow approximately 15 minutes for individual work and five minutes for discussion. Keep student answers in their own copies, not the public repository.

**Transition:** “We will end by connecting these decisions to the model-building work ahead.”

## SL17 — Three questions before S03 (175–180 min)

**Say:**

“Today we learned that preparing data is not just a technical preliminary step. It is part of the scientific reasoning behind a machine learning system.

Before we finish, I want each of you to answer three questions in your own words.

First, how do we distinguish a data error from a legitimate unusual observation? Second, which preprocessing steps learn parameters from training data, and why must they not learn from holdout data? Third, what could go wrong if we repeatedly adjust our pipeline based on results from a supposedly untouched test set?

These questions matter because next session we will start fitting regression models. The quality of those models will depend on the feature preparation and evaluation discipline we established today.

Please keep your notebook and your written explanations. In S03, we will connect this feature matrix to linear regression, a baseline and an objective function. Thank you, everyone.”

**[Action:]** Collect a brief individual exit response through the agreed institutional method. No new graded assessment is implied.

---

## Lecturer checklist before delivering

- Run every Colab cell in a fresh environment and confirm current package compatibility.
- Keep the synthetic-data caveat explicit; never imply a tiny holdout supports stable statistical claims.
- Point students to the slide visuals and notebook rather than reading source code character-by-character.
- Leave time for genuine interaction in SL09, SL15 and SL16.
- Confirm room equipment, accessible copies, break accounting and local policy.
- Do not publish instructor-only solutions, assessment keys or student records in this public repository.
