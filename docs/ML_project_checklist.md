# 🧠 Machine Learning Project Checklist Reference Guide

📚 Table of Contents  
* [🎯 Frame the Problem and Look at the Big Picture](#-frame-the-problem-and-look-at-the-big-picture)  
* [📥 Get the Data](#-get-the-data)  
* [📊 Explore the Data](#-explore-the-data)  
* [🛠️ Prepare the Data](#️-prepare-the-data)  
* [🤖 Shortlist Promising Models](#-shortlist-promising-models)  
* [🔧 Fine-Tune the System](#-fine-tune-the-system)  
* [🚀 Present Your Solution](#-present-your-solution)  
* [🚀 Launch](#-launch)  

## 🎯 Frame the Problem and Look at the Big Picture  
1. Define the objective in business terms.  
2. Determine how the solution will be used and by whom.  
3. Audit existing workarounds or systems.  
4. Choose ML framing: supervised vs. unsupervised vs. reinforcement; classification vs. regression; batch vs. online learning.  
5. Select performance metrics (e.g., RMSE vs. MAE) and set minimum acceptable thresholds.  
6. Document assumptions and simulate a manual solution.  
7. Research comparable problems and reusable tools.  

> Note: A clear problem statement keeps scope creep at bay.  
> Pro Tip: Draft a one-sentence “elevator pitch” linking business goal to ML task.  

> Questions:  
> * What is the business objective?  
> * How will end users leverage the solution?  
> * What are current workarounds?  
> * Which ML task best fits the problem?  
> * How will success be measured?  
> * What are the minimum performance requirements?  
> * What assumptions are you making?  
> * How would you solve it manually?  

## 📥 Get the Data  
1. List required datasets, fields, and expected volumes.  
2. Locate sources and document access methods.  
3. Assess storage, network, and compute needs.  
4. Review legal/privacy constraints; secure authorizations.  
5. Ingest data into a version-controlled workspace.  
6. Convert to analysis-friendly formats (e.g., Parquet, CSV).  
7. Anonymize or protect sensitive information.  
8. Profile data types, arrival rates, and sizes.  

> Pro Tip: Automate ingestion and version your raw data snapshots.  
> Note: Early legal checks save headaches later.  

> Questions:  
> * Which data do you need and where does it live?  
> * When and how frequently will new data arrive?  
> * How large is the dataset and at what velocity?  
> * Are there legal or privacy restrictions?  
> * Who needs access and how will you grant it?  
> * How will you store, back up, and version the data?  

## 📊 Explore the Data  
1. Copy training data for exploration:  
   ```python
   df = X_train.copy()
   ```  
2. Create a notebook and document each step.  
3. For each feature, record name, type, % missing, noise, distribution, and usefulness.  
4. Visualize univariate distributions:  
   ```python
   df.hist(figsize=(10,8))
   ```  
5. Study feature relationships & correlation:  
   ```python
   import seaborn as sns
   sns.scatterplot(x="feat1", y="feat2", data=df)
   corr = df.corr()
   sns.heatmap(corr, annot=True)
   ```  
   - Interpret `r_xy` ∈ [–1, +1]: sign = direction, |r| = strength  
   - Beware: **correlation ≠ causation**; only linear links.  
6. Identify outliers, anomalies, and potential new features.  
7. Document insights, quirks, and follow-up data needs.  

> Pro Tip: Share initial charts with domain experts for quick feedback.  
> Note: Flag |r|>0.8 for multicollinearity.  

> Questions:  
> * Does each feature’s distribution make sense?  
> * Are there outliers or missing patterns?  
> * What are basic summary stats?  
> * How correlated are features with each other and the target?  
> * Are there nonlinear relationships worth probing?  
> * Which new features could you derive?  

## 🛠️ Prepare the Data  
1. Create train/validation/test splits (e.g., 60/20/20):  
   ```python
   from sklearn.model_selection import train_test_split
   X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.4, random_state=42)
   X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)
   ```  
2. Handle missing values (drop, median, model-based).  
3. Encode categorical variables (one-hot, ordinal).  
4. Scale or transform features (StandardScaler, MinMax, log).  
5. Engineer new features and interactions.  
6. Build pipelines to streamline preprocessing:  
   ```python
   from sklearn.pipeline import Pipeline
   from sklearn.impute import SimpleImputer
   from sklearn.preprocessing import StandardScaler

   pipeline = Pipeline([
       ("imputer", SimpleImputer(strategy="median")),
       ("scaler", StandardScaler()),
   ])
   X_prepared = pipeline.fit_transform(X_train)
   ```  
7. Optionally, select or drop features based on importance or domain rules.  

> Pro Tip: Encapsulate every step in a reproducible pipeline.  
> Note: Never fit scalers or imputers on test/val data.  

> Questions:  
> * How will you handle missing values?  
> * Which encoding strategy suits each categorical feature?  
> * Do numerical features need scaling or transformation?  
> * Which new features or interactions add signal?  
> * How will you structure preprocessing pipelines?  
> * Should you reduce dimensionality or select features?  

## 🤖 Shortlist Promising Models  
1. Establish a baseline model (e.g., `DummyRegressor` or `DummyClassifier`).  
2. Identify candidate algorithms per task:  
   - Classification – logistic regression, tree-based, SVM, KNN, neural nets  
   - Regression – linear, decision tree, random forest, XGBoost, neural nets  
   - Unsupervised – K-means, hierarchical clustering, PCA  
3. Compare models via cross-validation:  
   ```python
   from sklearn.model_selection import cross_val_score
   scores = cross_val_score(
       RandomForestRegressor(), X_train, y_train,
       cv=5, scoring="neg_root_mean_squared_error"
   )
   ```  
4. Balance interpretability, training/prediction speed, and performance.  
5. Shortlist top 2–3 models for tuning.  

> Pro Tip: Always track baseline performance to validate gains.  
> Note: Use consistent CV folds and random seeds.  

> Questions:  
> * What is your baseline performance?  
> * Which model families are appropriate?  
> * What evaluation metric and CV strategy will you use?  
> * How do models compare on speed vs. accuracy?  
> * Which top candidates will you tune?  

### Model Comparison Table

| Model                                    | Learning Type   | Task Type                   | Input Data                        | Data Assumptions                                                    | When to Use                                                     | Benefits                                           | Disadvantages                                        |
|------------------------------------------|-----------------|-----------------------------|-----------------------------------|----------------------------------------------------------------------|-----------------------------------------------------------------|----------------------------------------------------|------------------------------------------------------|
| Linear Regression                       | Supervised      | Regression                  | Numerical features                | Linear relationship, independent errors, homoscedasticity, normality | Predict continuous targets with linear trends                  | Fast, interpretable, baseline                       | Struggles with nonlinearity, sensitive to outliers   |
| Ridge / Lasso Regression                | Supervised      | Regression                  | Numerical features                | Same as linear regression; 〈multicollinearity〉; lasso: sparsity      | When multicollinearity exists or you need feature selection     | Regularization reduces overfitting; lasso selects features | Requires α tuning; still linear                       |
| Logistic Regression                     | Supervised      | Classification              | Numerical or encoded categorical  | Linear decision boundary, independent observations, no multicollinearity | Binary or multiclass problems with approximate linear separability | Fast, interpretable, probabilistic outputs         | Cannot capture complex nonlinear patterns             |
| Decision Tree                           | Supervised      | Classification & Regression | Numerical & categorical           | None (nonparametric)                                                | When interpretability and mixed data types matter               | Visualizable, handles nonlinearity, little prep   | Prone to overfitting; high variance                  |
| Random Forest                           | Supervised      | Classification & Regression | Numerical & categorical           | Independent samples, random feature subsets                         | Noisy/high-dimensional data                                     | Robust, reduces overfitting, handles missing data  | Slower training; less interpretable                  |
| Extra Trees                             | Supervised      | Classification & Regression | Numerical & categorical           | Same as RF; more randomized splits                                  | Large datasets needing faster RF-style ensembles                | Very fast; lowers variance through randomness      | Unstable splits; may overfit without pruning          |
| Gradient Boosting (XGBoost/LightGBM/CatBoost) | Supervised  | Classification & Regression | Numerical & categorical           | Independent samples; stage-wise additive modeling                   | Structured data when accuracy is critical                       | SOTA performance; built-in regularization          | Complex tuning; longer training times                 |
| Support Vector Machine (SVM)            | Supervised      | Classification & Regression | Numerical features                | Features on similar scale; separable classes (for classification)   | Medium-scale, high-dimensional, margin-based tasks              | Effective in high dims; flexible kernels            | Slow on large sets; complex tuning                    |
| K-Nearest Neighbors (KNN)               | Supervised      | Classification & Regression | Numerical features                | Meaningful distance metric; locally smooth distributions            | Small datasets; simple tasks                                   | No training phase; intuitive; nonparametric       | Slow inference; sensitive to scaling                  |
| Naive Bayes                             | Supervised      | Classification              | Categorical or numerical          | Feature conditional independence; specific distribution (e.g. Gaussian) | Text classification, high-dimensional sparse data               | Extremely fast; works well with small data         | Unrealistic independence assumption                   |
| K-Means Clustering                      | Unsupervised    | Clustering                  | Numerical features                | Spherical clusters of similar variance; k known                     | Discovering k distinct groups in continuous data                | Simple; scalable; fast                             | Poor with non-spherical clusters; k must be chosen    |
| Principal Component Analysis (PCA)      | Unsupervised    | Dimensionality Reduction     | Numerical features                | Linearity; large variances capture signal; features centered       | Reducing dimensionality before modeling                         | Removes noise; speeds downstream models             | Hard to interpret; only linear variance captured      |
| Neural Network                          | Supervised      | Classification & Regression | Numerical, images, text embeddings | Data IID; stationary distribution; large sample size               | Complex pattern recognition (images, text, sequences)           | Highly flexible; captures complex nonlinearities   | Data-hungry; long training; low interpretability      |

## 🔧 Fine-Tune the System  
1. Choose hyperparameters and search spaces.  
2. Run randomized or Bayesian search with CV:  
   ```python
   from sklearn.model_selection import RandomizedSearchCV
   search = RandomizedSearchCV(
       XGBoostRegressor(), param_distributions=params,
       n_iter=50, cv=5, scoring="neg_mean_absolute_error", random_state=42
   )
   search.fit(X_train, y_train)
   ```  
3. Evaluate on validation set; avoid peeking at test set.  
4. Try ensemble strategies (bagging, boosting, stacking).  
5. Finalize model and freeze parameters.  

> Note: Log every experiment with parameters and metrics.  
> Pro Tip: Use early stopping and regularization to curb overfitting.  

> Questions:  
> * Which hyperparameters matter most?  
> * What search strategy and budget will you use?  
> * How will you track and compare runs?  
> * Which ensemble methods are worth exploring?  
> * When have you tuned enough?  

## 🚀 Present Your Solution  
1. Summarize end-to-end workflow and key findings.  
2. Highlight business impact and ROI.  
3. Explain chosen model and why it meets objectives.  
4. Show performance metrics and comparison to baseline.  
5. Visualize insights with clear charts.  
6. Enumerate assumptions, limitations, and next steps.  

> Pro Tip: Tailor storytelling to your audience—executives, engineers, or domain experts.  
> Note: Keep visuals simple and focused on actionable insights.  

> Questions:  
> * Who is the audience and what do they care about?  
> * What formats and visuals communicate best?  
> * What is your core recommendation?  
> * How does this solution deliver ROI?  
> * What caveats and future work remain?  

## 🚀 Launch  
1. Package model into a deployable artifact (API, batch job).  
2. Integrate with production pipelines and data sources.  
3. Implement monitoring for data drift, performance, and errors.  
4. Establish automated retraining or alerting triggers.  
5. Collect user feedback and performance logs.  
6. Plan for model versioning and rollback strategies.  

> Note: A model in production is just the beginning—monitor and iterate.  
> Pro Tip: Start with a shadow deployment or A/B test before full rollout.  

> Questions:  
> * How will you deploy—real-time or batch?  
> * What monitoring and alerting are required?  
> * How will you handle drift and data anomalies?  
> * What is your retraining cadence?  
> * How will you manage versions and rollbacks?  

## 🧠 Common Machine Learning Project Checklist Commands

| Command                  | Snippet                                                          |
|--------------------------|------------------------------------------------------------------|
| Read CSV                 | `import pandas as pd`<br>`df = pd.read_csv('data.csv')`         |
| Split data               | `train_test_split(X, y, test_size=0.2, random_state=42)`         |
| Copy DataFrame           | `df = X_train.copy()`                                            |
| Summary statistics       | `df.describe()`                                                  |
| Plot histograms          | `df.hist(figsize=(10,8))`                                        |
| Plot correlation heatmap | `sns.heatmap(df.corr(), annot=True)`                             |

## 📚 Glossary

| Term                   | Definition                                                                                   | When to Use                                      |
|------------------------|----------------------------------------------------------------------------------------------|--------------------------------------------------|
| Supervised Learning    | Models learn mappings from inputs to known outputs                                           | When labeled data is available                   |
| Unsupervised Learning  | Discover patterns in unlabeled data (clustering, dimensionality reduction)                   | When labels are unavailable                      |
| RMSE                   | Root Mean Square Error; sqrt of avg. squared prediction errors                               | Regression tasks with few outliers               |
| MAE                    | Mean Absolute Error; avg. absolute prediction errors                                         | Regression tasks with many outliers              |
| Stratified Sampling    | Sampling preserving class proportions in train/test splits                                   | When target classes are imbalanced               |
| Data Snooping Bias     | Bias from using test set insights to shape the model or analysis                             | Always avoid to ensure realistic generalization  |
| Multicollinearity      | High correlation among features that can distort model estimates                             | During feature selection and model interpretation|

🧠 **Pro Tips:**  
* Version-control both code and data schemas to guarantee reproducibility.  
* Modularize pipelines: separate ingestion, cleaning, modeling, and evaluation.  
* Engage domain experts early and document every assumption.  

🔗 Helpful Links:  
* https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html  
* https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.corr.html  
* https://seaborn.pydata.org/examples/many_pairwise_correlations.html