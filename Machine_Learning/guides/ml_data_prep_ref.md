# 🛠️ ML Data Preparation Reference Guide

> 🟡 **Level:** Intermediate  ·  **Prerequisites:** [ML Fundamentals](ml_fundamentals_ref.md), [Pandas](../../Python/guides/pandas_ref.md)

Scikit-learn models need **numeric data with no missing values**. This guide covers the preprocessing steps that get raw data ready: **encoding categoricals**, **imputing missing values**, **scaling features**, and wrapping it all in **pipelines** to prevent data leakage.

> Rule of thumb: whatever you learn from the data (a mean to impute, a scale to apply) must be learned from **training data only**, then applied to the test data — pipelines enforce this for you.

## 📚 Table of Contents

* [✅ scikit-learn's Requirements](#-scikit-learns-requirements)
* [🔡 Encoding Categorical Features](#-encoding-categorical-features)
* [❓ Imputing Missing Data](#-imputing-missing-data)
* [⚖️ Centering & Scaling](#-centering--scaling)
* [🔗 Pipelines](#-pipelines)
* [🚰 Avoiding Data Leakage](#-avoiding-data-leakage)
* [🧠 Common Commands](#-common-commands)
* [📚 Glossary](#-glossary)

---

## ✅ scikit-learn's Requirements

Before fitting any model:
- Data must be **numeric**.
- There must be **no missing values**.
- Data lives in a **Pandas DataFrame** or **NumPy array**.

Run EDA first to confirm these are met. The general sklearn pattern is always:

```python
from sklearn.module import Model
model = Model()          # 1. instantiate
model.fit(X, y)          # 2. train
preds = model.predict(X_new)   # 3. predict
```

---

## 🔡 Encoding Categorical Features

sklearn won't accept text categories — convert them to **dummy variables** (one binary column per category: `1` = is that category, `0` = isn't).

```python
import pandas as pd

# pandas approach
dummies = pd.get_dummies(df['genre'], drop_first=True)   # drop_first avoids redundancy
df = pd.concat([df, dummies], axis=1).drop('genre', axis=1)

# scikit-learn approach
from sklearn.preprocessing import OneHotEncoder
encoder = OneHotEncoder(handle_unknown='ignore')
```

> Note: Use `drop_first=True` to drop one dummy column — it's redundant (if it's not any of the others, it must be the dropped one) and avoids the "dummy variable trap."

---

## ❓ Imputing Missing Data

**Imputation** replaces missing values with educated guesses. Common strategies: **mean/median** for numbers, **most frequent (mode)** for categories. Imputers are **transformers**.

```python
from sklearn.impute import SimpleImputer

# Numeric → mean (default)
imp_num = SimpleImputer(strategy='mean')

# Categorical → most frequent
imp_cat = SimpleImputer(strategy='most_frequent')

# CRITICAL: fit on train, transform train AND test
X_train_num = imp_num.fit_transform(X_train_num)
X_test_num  = imp_num.transform(X_test_num)   # transform only — no re-fitting
```

You can also just drop rows when the missing fraction is tiny:

```python
df = df.dropna(subset=['genre', 'popularity', 'loudness'])   # e.g., < 5% missing
```

---

## ⚖️ Centering & Scaling

Many models use **distance** (KNN) or coefficient magnitudes (linear/logistic regression), so features on larger scales dominate. Put features on a similar scale:

| Method            | Formula                        | Result                          |
|-------------------|--------------------------------|---------------------------------|
| **Standardization** | `(x − mean) / std`           | Mean 0, variance 1              |
| **Min-max scaling** | `(x − min) / (max − min)`    | Range 0 to 1                    |
| **Normalization**   | scale to a fixed range       | e.g., −1 to +1                  |

```python
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled  = scaler.transform(X_test)
```

> Note: Models affected by scaling include **KNN, Linear/Ridge/Lasso Regression, Logistic Regression, and Neural Networks**. Always scale **before** evaluating these.

---

## 🔗 Pipelines

A **Pipeline** chains preprocessing + model into one object, so the same steps apply consistently and `fit`/`predict` "just work":

```python
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

pipe = Pipeline([
    ('imputer', SimpleImputer(strategy='mean')),
    ('scaler',  StandardScaler()),
    ('model',   KNeighborsClassifier(n_neighbors=7)),
])

pipe.fit(X_train, y_train)
pipe.score(X_test, y_test)
```

> Pro Tip: Pipelines are the cleanest way to avoid leakage — every transformer is fit only on the training folds during cross-validation.

---

## 🚰 Avoiding Data Leakage

**Data leakage** is when information from the test set sneaks into training, giving falsely optimistic scores.

- **Split first**, then fit imputers/scalers on the training set only.
- Never call `fit` or `fit_transform` on the test set — only `transform`.
- Prefer a **Pipeline** so this happens automatically inside cross-validation.

---

## 🧠 Common Commands

| Command                          | What it does                          |
|----------------------------------|---------------------------------------|
| `pd.get_dummies(col)`            | One-hot encode a category             |
| `OneHotEncoder()`                | sklearn categorical encoder           |
| `SimpleImputer(strategy=...)`    | Fill missing values                   |
| `StandardScaler()`               | Standardize features                  |
| `Pipeline([...])`                | Chain preprocessing + model           |
| `.fit_transform(X_train)`        | Learn + apply on train                |
| `.transform(X_test)`             | Apply learned transform to test       |

---

## 📚 Glossary

| Term          | Definition                                                   | When it matters                |
|---------------|--------------------------------------------------------------|--------------------------------|
| Dummy variable| Binary column for one category                               | Encoding categoricals          |
| Imputation    | Replacing missing values with estimates                      | Meeting sklearn's no-NA rule   |
| Transformer   | An object with `fit`/`transform` (imputer, scaler)           | Preprocessing steps            |
| Standardization | Rescale to mean 0, variance 1                              | Distance/coefficient models    |
| Pipeline      | Chained sequence of transformers + a model                   | Clean, leak-free workflows     |
| Data leakage  | Test info contaminating training                             | Trustworthy evaluation         |

---

🧠 **Pro Tips:**
* **Split before you preprocess** — fit transforms on training data only.
* Wrap everything in a **Pipeline** so cross-validation stays honest.
* Scale distance-based and linear models; tree-based models don't need it.

🔗 Helpful Links:
* https://scikit-learn.org/stable/modules/preprocessing.html
* https://scikit-learn.org/stable/modules/impute.html
* https://scikit-learn.org/stable/modules/compose.html
