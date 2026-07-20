# 📏 ML Model Evaluation & Tuning Reference Guide

Training a model is only half the job — you have to **measure how good it is** and **tune it** without fooling yourself. This guide covers **train/test splits**, **cross-validation**, **classification metrics** (confusion matrix, precision, recall, F1, ROC AUC), **regression metrics** (RMSE, R²), and **hyperparameter tuning** (grid & randomized search).

> The golden rule: never let the **test set** influence training or tuning decisions. Reserve it for one final, honest score.

## 📚 Table of Contents

* [✂️ Train/Test Split](#-traintest-split)
* [🔁 Cross-Validation](#-cross-validation)
* [🎯 Why Accuracy Isn't Enough](#-why-accuracy-isnt-enough)
* [🧮 The Confusion Matrix](#-the-confusion-matrix)
* [📊 Precision, Recall & F1](#-precision-recall--f1)
* [📈 ROC & AUC](#-roc--auc)
* [📉 Regression Metrics](#-regression-metrics)
* [🎛️ Hyperparameter Tuning](#-hyperparameter-tuning)
* [🧠 Common Commands](#-common-commands)
* [📚 Glossary](#-glossary)

---

## ✂️ Train/Test Split

```python
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42)
```

Train on `X_train`, evaluate on the held-out `X_test`. The error on the test set estimates the **generalization error** (how the model does on unseen data).

---

## 🔁 Cross-Validation

A single split can be lucky or unlucky. **k-fold cross-validation** splits the training data into *k* folds, trains on *k−1* and validates on the remaining one, rotating through all folds:

```python
from sklearn.model_selection import cross_val_score, KFold
import numpy as np

kf = KFold(n_splits=5, shuffle=True, random_state=42)
scores = cross_val_score(model, X_train, y_train, cv=kf,
                         scoring='neg_mean_squared_error')
print(np.sqrt(-scores))    # RMSE per fold
```

> Note: Cross-validate on the **training set** and keep the test set untouched for the final evaluation.

---

## 🎯 Why Accuracy Isn't Enough

**Accuracy** = fraction of correct predictions — but it's misleading under **class imbalance**. If 99% of transactions are legitimate, a model that always predicts "legitimate" is 99% accurate and **100% useless** at catching fraud.

> Pro Tip: Whenever classes are imbalanced, ignore raw accuracy and look at precision/recall for the class you care about.

---

## 🧮 The Confusion Matrix

|                       | Predicted Positive | Predicted Negative |
|-----------------------|--------------------|--------------------|
| **Actual Positive**   | True Positive (TP) | False Negative (FN)|
| **Actual Negative**   | False Positive (FP)| True Negative (TN) |

The **positive class** is usually the one you care about (e.g., fraudulent transactions).

```python
from sklearn.metrics import confusion_matrix, classification_report
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
```

---

## 📊 Precision, Recall & F1

| Metric | Formula | High value means… |
|--------|---------|-------------------|
| **Accuracy** | `(TP+TN) / (TP+TN+FP+FN)` | Overall correctness |
| **Precision** (positive predictive value) | `TP / (TP+FP)` | Few false positives — when it says positive, it's usually right |
| **Recall** (sensitivity) | `TP / (TP+FN)` | Few false negatives — it catches most actual positives |
| **F1 score** | `2 · (precision·recall)/(precision+recall)` | Good balance of both |

- **High precision** → not many legitimate cases flagged as fraud.
- **High recall** → most actual fraud correctly caught.
- **F1** is the harmonic mean — use it when you want a single number that balances both.

> Note: There's usually a **trade-off** — pushing recall up tends to lower precision and vice versa. Choose based on which error is costlier.

---

## 📈 ROC & AUC

The **ROC curve** plots the true-positive rate against the false-positive rate across all classification thresholds. **AUC** (Area Under the Curve) summarizes it: `0.5` = random guessing, `1.0` = perfect.

```python
from sklearn.metrics import roc_auc_score, roc_curve
y_proba = model.predict_proba(X_test)[:, 1]
print(roc_auc_score(y_test, y_proba))
```

---

## 📉 Regression Metrics

| Metric | Meaning | Better when… |
|--------|---------|--------------|
| **RMSE** (Root Mean Squared Error) | Typical error size, in target units; penalizes big errors | Lower |
| **MAE** (Mean Absolute Error) | Average absolute error; less sensitive to outliers | Lower |
| **R²** (coefficient of determination) | Fraction of variance explained (0–1) | Higher |

```python
from sklearn.metrics import mean_squared_error, r2_score
rmse = mean_squared_error(y_test, y_pred, squared=False)
r2   = r2_score(y_test, y_pred)
```

---

## 🎛️ Hyperparameter Tuning

**Hyperparameters** are set *before* training (e.g., `n_neighbors` for KNN, `alpha` for Ridge/Lasso). Tune them by trying many values and keeping the best — always with **cross-validation** so you don't overfit the test set.

```python
from sklearn.model_selection import GridSearchCV
param_grid = {'n_neighbors': range(1, 20)}
grid = GridSearchCV(knn, param_grid, cv=5)
grid.fit(X_train, y_train)
print(grid.best_params_, grid.best_score_)
```

- **Grid search** — tries every combination. Thorough but doesn't scale (3-fold CV × 30 values = 90 fits; add hyperparameters and it explodes).
- **Randomized search** (`RandomizedSearchCV`) — samples random combinations; far cheaper for large search spaces.

> Pro Tip: Start with a coarse **randomized search** to find a promising region, then a fine **grid search** around it.

---

## 🧠 Common Commands

| Command                          | What it does                          |
|----------------------------------|---------------------------------------|
| `train_test_split(...)`          | Hold out a test set                   |
| `cross_val_score(...)`           | k-fold cross-validation               |
| `confusion_matrix(y, yhat)`      | TP/FP/FN/TN table                     |
| `classification_report(...)`     | Precision/recall/F1 per class         |
| `roc_auc_score(...)`             | Area under the ROC curve              |
| `mean_squared_error(..., squared=False)` | RMSE                          |
| `r2_score(...)`                  | R²                                    |
| `GridSearchCV / RandomizedSearchCV` | Hyperparameter tuning              |

---

## 📚 Glossary

| Term          | Definition                                                   | When it matters                |
|---------------|--------------------------------------------------------------|--------------------------------|
| Generalization error | Error on unseen data                                  | The number that really matters |
| Cross-validation | Rotating train/validation folds                          | Reliable performance estimates |
| Class imbalance | Very unequal class frequencies                             | Choosing metrics               |
| Precision / Recall | False-positive vs. false-negative control               | Imbalanced classification      |
| ROC AUC       | Threshold-independent classifier quality                     | Comparing classifiers          |
| Hyperparameter| A setting chosen before training                             | Tuning                         |

---

🧠 **Pro Tips:**
* Report the metric that matches the **cost of each error** — precision, recall, or F1, not just accuracy.
* Tune with **cross-validation**; keep the test set for a single final score.
* Use **randomized search** first to save compute, then grid search to refine.

🔗 Helpful Links:
* https://scikit-learn.org/stable/modules/model_evaluation.html
* https://scikit-learn.org/stable/modules/cross_validation.html
* https://scikit-learn.org/stable/modules/grid_search.html
