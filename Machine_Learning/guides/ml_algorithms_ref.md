# 🧮 ML Algorithms Reference Guide

> 🟡 **Level:** Intermediate  ·  **Prerequisites:** [ML Fundamentals](ml_fundamentals_ref.md)

A beginner's map of the most common **supervised** learning algorithms — when to reach for each **classification** and **regression** model, plus a note on **unsupervised** methods. All examples use scikit-learn's uniform `fit` / `predict` interface.

> How to choose: balance **dataset size**, **interpretability** (can you explain it to stakeholders?), and **flexibility** (fewer assumptions can mean higher accuracy but more data needed).

## 📚 Table of Contents

* [🔁 The scikit-learn Pattern](#-the-scikit-learn-pattern)
* [🏷️ Classification Algorithms](#-classification-algorithms)
* [📉 Regression Algorithms](#-regression-algorithms)
* [🗂️ Model Selection Cheat Table](#-model-selection-cheat-table)
* [🔍 Unsupervised Methods](#-unsupervised-methods)
* [🧭 How to Pick a Model](#-how-to-pick-a-model)
* [📚 Glossary](#-glossary)

---

## 🔁 The scikit-learn Pattern

Every model follows the same four steps:

```python
from sklearn.module import Model
model = Model()               # 1. instantiate (set hyperparameters here)
model.fit(X_train, y_train)   # 2. train
y_pred = model.predict(X_test)# 3. predict
model.score(X_test, y_test)   # 4. evaluate
```

---

## 🏷️ Classification Algorithms

Predict a **discrete class label**.

- **Logistic Regression** — despite the name, a *classifier*. Outputs the **probability** of belonging to a class; best for **binary** (True/False) targets. Highly interpretable coefficients.
- **k-Nearest Neighbors (KNN)** — classifies a point by the majority vote of its *k* closest neighbors. Learns a **decision boundary**; flexible, assumes no linear relationship. **Sensitive to scaling.**
- **Decision Tree** — splits the data on feature thresholds into a tree of if/else rules. Very interpretable; handles non-linearities; prone to overfitting.
- **Random Forest** — an **ensemble** of many decision trees whose votes are averaged. More accurate and robust than a single tree; less interpretable.
- **Support Vector Machine (SVM / SVC)** — finds the boundary that best separates classes with the widest margin. Powerful for high-dimensional data.
- **Stochastic Gradient Descent (SGD)** — trains linear classifiers efficiently on **very large** datasets by updating on one sample at a time.

```python
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=7)
knn.fit(X_train, y_train)
```

---

## 📉 Regression Algorithms

Predict a **continuous numeric target**.

- **Linear Regression** — fits a straight line (`y = mx + b`); highly interpretable coefficients. Baseline for most regression problems.
- **Ridge Regression** — linear regression with **L2 regularization** (`alpha` shrinks coefficients) to reduce overfitting.
- **Lasso Regression** — linear regression with **L1 regularization**; can shrink coefficients to **zero**, so it doubles as **feature selection**.
- **Support Vector Regression (SVR)** — the regression form of SVM.
- **Decision Tree / Random Forest Regressors** — tree-based regression; capture non-linear relationships.

```python
from sklearn.linear_model import Ridge
ridge = Ridge(alpha=1.0)
ridge.fit(X_train, y_train)
```

> Pro Tip: **Lasso** is great for figuring out which features actually matter — inspect which coefficients it drives to zero.

---

## 🗂️ Model Selection Cheat Table

| Method | When to use | Performance metrics | Scale first? |
|--------|-------------|---------------------|--------------|
| **Linear Regression** | Baseline continuous prediction | RMSE, R² | ✅ |
| **Ridge Regression** | Overfitting linear model | RMSE, R² | ✅ |
| **Lasso Regression** | Select important features | RMSE, R² | ✅ |
| **Logistic Regression** | Binary (T/F) classification | Accuracy, confusion matrix, precision/recall/F1, ROC AUC | ✅ |
| **k-Nearest Neighbors** | Flexible decision boundary | Accuracy, confusion matrix, precision/recall/F1, ROC AUC | ✅ |
| **Decision Tree** | Interpretable rules | Accuracy / RMSE | ❌ |
| **Random Forest** | High accuracy, robustness | Accuracy / RMSE | ❌ |

---

## 🔍 Unsupervised Methods

For **unlabeled** data:

- **Clustering** (e.g., K-Means) — groups similar observations. **Hierarchical clustering** nests groups within groups.
- **Dimensionality reduction** (e.g., PCA) — compress many features into fewer while keeping most information.
- **Visualization algorithms** — project complex data into 2D/3D to reveal structure.

---

## 🧭 How to Pick a Model

Guiding principles:

- **Dataset size** — fewer features → simpler, faster models; some models need lots of data.
- **Interpretability** — linear/logistic regression and single trees are easy to explain; ensembles less so.
- **Flexibility** — flexible models (KNN, trees) make fewer assumptions and can be more accurate, at the cost of data hunger and overfitting risk.
- **It's all in the metrics** — train several models "out of the box" and compare on the right metric.

> Note: When comparing models that are scale-sensitive, **scale the data first** so the comparison is fair.

---

## 📚 Glossary

| Term          | Definition                                                   | When it matters                |
|---------------|--------------------------------------------------------------|--------------------------------|
| Classifier    | Model predicting a discrete class                            | Classification tasks           |
| Regressor     | Model predicting a continuous value                          | Regression tasks               |
| Ensemble      | Many models combined (e.g., Random Forest)                   | Accuracy & robustness          |
| Regularization| Penalty (Ridge L2 / Lasso L1) that shrinks coefficients      | Reducing overfitting           |
| Decision boundary | The surface separating predicted classes                 | KNN, SVM, logistic regression  |
| Hyperparameter| A setting chosen before training (`k`, `alpha`)              | Model tuning                   |

---

🧠 **Pro Tips:**
* Start with a **simple, interpretable baseline** (linear/logistic regression) before reaching for ensembles.
* **Tree-based models don't need scaling**; distance/linear models do.
* Don't judge a model on accuracy alone — pick the metric that matches your goal.

🔗 Helpful Links:
* https://scikit-learn.org/stable/supervised_learning.html
* https://scikit-learn.org/stable/machine_learning_map.html
* https://scikit-learn.org/stable/modules/linear_model.html
