# 🧹 Data Cleaning & Prep Reference Guide

**"Garbage in, garbage out."** Real-world data is messy — wrong types, missing values, duplicates, outliers, and inconsistent text. This guide walks the cleaning pipeline: **inspect → fix types → handle missing data → drop duplicates → treat outliers → clean strings → standardize categories → bin**.

> Cleaning is where most of a data project's time goes. Do it carefully and everything downstream gets easier.

## 📚 Table of Contents

* [🔍 Inspect the Data First](#-inspect-the-data-first)
* [🏷️ Rename Columns & Values](#-rename-columns--values)
* [🔧 Data Type Constraints](#-data-type-constraints)
* [❓ Missing Data](#-missing-data)
* [👯 Duplicates](#-duplicates)
* [📈 Outliers](#-outliers)
* [🔤 Cleaning Strings](#-cleaning-strings)
* [🧭 Uniformity & Categories](#-uniformity--categories)
* [🪣 Binning](#-binning)
* [🧠 Common Commands](#-common-commands)
* [📚 Glossary](#-glossary)

---

## 🔍 Inspect the Data First

Always start by understanding what you have:

```python
import seaborn as sns
import pandas as pd

df = sns.load_dataset('titanic')
df.head()        # first rows
df.info()        # columns, dtypes, non-null counts
df.shape         # (rows, columns)
df.describe()    # numeric summary stats
df.columns       # column labels
df.index         # row index
```

> Pro Tip: `df.info()` is the single most useful first command — it reveals wrong dtypes *and* missing values at once.

---

## 🏷️ Rename Columns & Values

Work on a **copy** so you don't clobber the original:

```python
df2 = df.copy()

# Rename columns with a mapping dictionary
df2 = df2.rename(columns={'sex': 'gender'})

# Inspect and replace values
df2['embark_town'].unique()                       # see distinct values
df2['embark_town'] = df2['embark_town'].replace({'Southampton': 'S'})
```

---

## 🔧 Data Type Constraints

Wrong types silently break analysis (numbers stored as text, dates stored as objects). Convert and then **assert** the result:

```python
# object = string in pandas
df.dtypes

# Common conversions: str, int, float, bool, category
df['age'] = df['age'].astype('float')
assert df['age'].dtype == 'float'          # AssertionError if it failed

# Dates need to_datetime
df['date'] = pd.to_datetime(df['date'])
assert df['date'].dtype == 'datetime64[ns]'
```

> Note: Use `category` dtype for columns with a small set of repeated values — it saves memory and speeds up grouping.

---

## ❓ Missing Data

A four-step approach: **detect → decide → drop or fill**.

```python
# Detect
df.isna().sum()               # count NAs per column
df['col'].isna().mean()       # fraction missing

# Drop
df.dropna()                   # rows with ANY NA
df.dropna(subset=['col'])     # only where a specific column is NA
df.dropna(axis=1)             # drop columns with NAs

# Fill (impute)
df['col'].fillna(0)                       # constant
df['col'].fillna(df['col'].mean())        # mean imputation
df['col'].fillna(method='ffill')          # carry last value forward
```

> Pro Tip: Don't blindly drop rows — first ask *why* the data is missing. Missing-not-at-random can bias your results.

---

## 👯 Duplicates

```python
df.duplicated().sum()               # how many full-row duplicates
df.drop_duplicates()                # drop exact duplicate rows
df.drop_duplicates(subset=['id'])   # dedupe on a key column
df.drop_duplicates(subset=['id'], keep='last')
```

---

## 📈 Outliers

Detect with the **IQR rule** or z-scores, then decide whether to cap, remove, or keep:

```python
Q1, Q3 = df['col'].quantile([0.25, 0.75])
IQR = Q3 - Q1
low, high = Q1 - 1.5 * IQR, Q3 + 1.5 * IQR
outliers = df[(df['col'] < low) | (df['col'] > high)]
```

> Note: An outlier isn't automatically an error — it may be the most interesting data point. Investigate before removing.

---

## 🔤 Cleaning Strings

```python
# Remove unwanted characters
chars_to_remove = ['+', ',', '$']
for char in chars_to_remove:
    df['price'] = df['price'].apply(lambda x: x.replace(char, ''))

# Strip whitespace from every text column
for col in df.columns:
    if df[col].dtype == 'object':
        df[col] = df[col].str.strip()

# Vectorized string methods
df['name'] = df['name'].str.lower().str.strip()
df['code'] = df['code'].str.replace('-', '')
```

Use **regular expressions** for pattern-based cleaning:

```python
df['phone'] = df['phone'].str.replace(r'\D', '', regex=True)  # keep digits only
```

---

## 🧭 Uniformity & Categories

Inconsistent categories ("NY", "New York", "new york ") must be **standardized** before grouping:

```python
df['state'].unique()                     # spot the variants
df['state'] = df['state'].str.strip().str.title()
df['state'] = df['state'].replace({'Ny': 'New York'})
```

**Cross-form validation / record linkage** matches records that refer to the same entity but aren't identical (e.g., fuzzy-matching names across two datasets).

---

## 🪣 Binning

Turn a continuous variable into labeled buckets:

```python
bins   = [0, 12, 19, 59, 120]
labels = ['Child', 'Teen', 'Adult', 'Senior']
df['age_group'] = pd.cut(df['age'], bins=bins, labels=labels)

# Equal-frequency bins
df['quartile'] = pd.qcut(df['income'], q=4)
```

---

## 🧠 Common Commands

| Command                       | What it does                          |
|-------------------------------|---------------------------------------|
| `df.info()` / `df.dtypes`     | Inspect structure & types             |
| `df.rename(columns=...)`      | Rename columns                        |
| `df.astype(t)` / `pd.to_datetime` | Convert types                     |
| `df.isna().sum()`             | Count missing values                  |
| `df.dropna()` / `df.fillna()` | Remove / impute NAs                   |
| `df.drop_duplicates()`        | Remove duplicate rows                 |
| `df['c'].str.strip()`         | Trim whitespace                       |
| `pd.cut()` / `pd.qcut()`      | Bin continuous data                   |

---

## 📚 Glossary

| Term          | Definition                                                   | When it matters                 |
|---------------|--------------------------------------------------------------|---------------------------------|
| Dtype         | The data type of a column                                    | Type constraints                |
| Imputation    | Filling missing values with estimates                        | Handling NAs                    |
| Outlier       | A value far from the rest of the distribution                | Robustness of analysis          |
| Uniformity    | Consistent formatting within a column                        | Grouping/joining reliably       |
| Record linkage| Matching records that refer to the same entity               | Merging messy datasets          |
| Binning       | Grouping continuous values into categories                   | Simplifying / feature eng.      |

---

🧠 **Pro Tips:**
* Clean on a **copy**, and `assert` type conversions so failures are loud, not silent.
* Standardize categories (case + whitespace) *before* you group or join.
* Investigate missing values and outliers before deleting — the "error" may be signal.

🔗 Helpful Links:
* https://pandas.pydata.org/docs/user_guide/missing_data.html
* https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.astype.html
* https://pandas.pydata.org/docs/reference/api/pandas.cut.html
