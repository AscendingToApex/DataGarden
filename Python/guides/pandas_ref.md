# 🐼 Pandas Reference Guide

> 🟢 **Level:** Beginner  ·  **Prerequisites:** [NumPy](numpy_ref.md)

**Pandas** (short for *"panel data"*) is Python's go-to library for working with tables of data — think of it as a programmable spreadsheet or an in-memory database. It's built on NumPy and pairs with it constantly. This guide covers the two core objects (**Series** and **DataFrame**), everyday **operations**, working with **dates**, and how to **speed up** slow row-by-row loops.

> Rule of thumb: Pandas shines when your data **fits in memory**. It gives you SQL-style filtering/joining, Excel-style pivots, and R-style NA handling — all in Python.

## 📚 Table of Contents

* [🚀 Getting Started](#-getting-started)
* [🧾 Series](#-series)
* [🗃️ DataFrames](#-dataframes)
* [📥 Loading Data](#-loading-data)
* [🔎 Inspecting a DataFrame](#-inspecting-a-dataframe)
* [🎯 Selecting & Filtering](#-selecting--filtering)
* [🧹 Dropping Rows & Columns](#-dropping-rows--columns)
* [➕ Creating New Columns](#-creating-new-columns)
* [↕️ Sorting & Ranking](#-sorting--ranking)
* [📅 Working with Dates](#-working-with-dates)
* [⚡ Loop Optimization](#-loop-optimization)
* [🧠 Common Commands](#-common-commands)
* [📚 Glossary](#-glossary)

---

## 🚀 Getting Started

```bash
pip install pandas
```
```python
import numpy as np
import pandas as pd
```

Pandas gives you "batteries-included" analysis: loading data (`read_csv`, `read_sql`, `read_html`), SQL-style selection/filtering/aggregation, pivot tables, NA handling, quick stats (`mean`, `describe`), and plotting (`plot`, `hist`).

---

## 🧾 Series

A **Series** is a one-dimensional labeled array — like a NumPy array, but with an **index** you can see and customize. It's essentially one column of a table.

```python
data = pd.Series([0.25, 0.5, 0.75, 1.0])
data.values          # the underlying values
data.index           # the labels (default: 0,1,2,3)

# Custom labels
data = pd.Series([0.25, 0.5, 0.75, 1.0], index=['a', 'b', 'c', 'd'])
data['b']            # 0.5 → look up by label

# From a dictionary (keys become the index)
pd.Series({'CA': 38, 'TX': 26, 'NY': 19})
```

> Note: The big difference from a NumPy array is the **flexible index** — it makes real-world data far easier to align and look up. And unlike Python slicing, slicing a Series **by label is inclusive** of the last value.

---

## 🗃️ DataFrames

A **DataFrame** is a two-dimensional table — rows and columns, like a SQL table or Excel sheet. Technically it's a dictionary of Series sharing one index.

```python
df = pd.DataFrame({
    'name': ['Ann', 'Ben', 'Cid'],
    'age':  [25, 30, 22],
    'city': ['NYC', 'LA', 'SF'],
})
df['age']          # a single column (a Series)
df[['name', 'age']]# multiple columns (a DataFrame)
```

- Columns are **type-homogeneous** (like SQL); cells can hold Python objects.
- Missing values are called **NA** (not NULL). Pandas may **upcast** integers to float64 to store NAs.

---

## 📥 Loading Data

```python
df = pd.read_csv('data.csv')          # most common
df = pd.read_excel('data.xlsx')
df = pd.read_sql('SELECT * FROM t', conn)
df = pd.read_html('https://site/page')[0]
df.to_csv('out.csv', index=False)     # save back out
```

---

## 🔎 Inspecting a DataFrame

```python
df.head()          # first 5 rows
df.tail(3)         # last 3 rows
df.shape           # (rows, columns)
df.info()          # column names, dtypes, non-null counts
df.describe()      # summary stats for numeric columns
df.columns         # column labels
'age' in df        # check if a column exists → True/False
```

---

## 🎯 Selecting & Filtering

```python
df['age']                       # one column
df.loc[0]                       # a row by LABEL
df.iloc[0]                      # a row by POSITION
df.loc[df['age'] > 24]          # boolean filter (SQL WHERE)
df.loc[(df['age'] > 24) & (df['city'] == 'NYC')]   # combine with & / |
```

> Pro Tip: Use `&`, `|`, `~` (not `and`, `or`, `not`) for boolean filters, and wrap each condition in parentheses.

---

## 🧹 Dropping Rows & Columns

```python
df.drop(0, axis=0)              # drop a row (axis=0)
df.drop('city', axis=1)        # drop a column (axis=1)
df.dropna()                     # drop rows containing NA
df.drop_duplicates()            # remove duplicate rows
```

> Note: `axis=0` = rows, `axis=1` = columns. Most methods return a **new** DataFrame; use `inplace=True` or reassign to keep the change.

---

## ➕ Creating New Columns

One of Pandas' best features: compute a new column from existing ones with the full power of Python.

```python
df['age_in_months'] = df['age'] * 12
df['is_adult'] = df['age'] >= 18
df['label'] = df['city'] + '-' + df['name']
```

---

## ↕️ Sorting & Ranking

```python
df.sort_values('age')                       # sort by a column's values
df.sort_values('age', ascending=False)      # descending
df.sort_index()                             # sort by the index labels
df['age'].rank()                            # assign ranks to entries
```

---

## 📅 Working with Dates

Pandas has first-class support for dates and times, built on Python's `datetime`.

```python
# Parse strings into real datetimes
df['date'] = pd.to_datetime(df['date'])

# Access parts via the .dt accessor
df['date'].dt.year
df['date'].dt.month
df['date'].dt.day_name()

# Math with dates
df['days_since'] = (pd.Timestamp('today') - df['date']).dt.days
```

Formatting and parsing single dates:

```python
from datetime import datetime
dt = datetime(2023, 7, 1, 8, 30)
dt.strftime("%Y-%m-%d")                     # datetime → string ('2023-07-01')
datetime.strptime("2023-07-01", "%Y-%m-%d") # string → datetime
```

> Pro Tip: Store dates as real `datetime`/`Timestamp` types, not strings. It unlocks sorting, filtering by range, and the whole `.dt` toolkit.

---

## ⚡ Loop Optimization

When you need to transform each row, **how** you loop dramatically changes speed. From **slowest to fastest** (same task: bucketing 100,000 review scores into star ratings):

| Approach            | Idea                                         | Speed        |
|---------------------|----------------------------------------------|--------------|
| Basic Python loop   | `for i in range(len(df))` + `.iloc`          | 🐌 Slowest   |
| `iterrows()`        | Yields `(index, Series)` pairs               | 🐢 Slow      |
| `apply()`           | Run a function over rows/columns             | 🚶 Moderate  |
| `itertuples()`      | Yields fast named tuples, preserves dtypes   | 🏃 Faster    |
| **Vectorization**   | NumPy/Pandas operations on whole columns     | 🚀 Fastest   |

```python
# 🐌 Basic loop — avoid on large data
for i in range(len(df)):
    ...

# 🚶 apply — readable, decent
df['stars'] = df['score'].apply(bucket_fn)

# 🏃 itertuples — faster than iterrows, keeps dtypes
for row in df.itertuples():
    ...

# 🚀 Vectorized — no Python loop at all
bins   = [-1, 20, 40, 60, 80, 100]
labels = ['One', 'Two', 'Three', 'Four', 'Five']
df['stars'] = pd.cut(df['score'], bins=bins, labels=labels)
```

> Note: **Never modify something you're iterating over.** And prefer `itertuples()` over `iterrows()` — it's faster and preserves column data types.

> Pro Tip: Before writing any loop, ask *"can this be a column operation?"* Vectorized code is usually both shorter and orders of magnitude faster.

---

## 🧠 Common Commands

| Command                         | What it does                          |
|---------------------------------|---------------------------------------|
| `pd.read_csv(path)`             | Load a CSV into a DataFrame           |
| `df.head()` / `df.info()`       | Peek at data / see structure          |
| `df.describe()`                 | Summary statistics                    |
| `df['col']`                     | Select a column                       |
| `df.loc[]` / `df.iloc[]`        | Select by label / by position         |
| `df[df['c'] > x]`               | Filter rows                           |
| `df.groupby('c').mean()`        | Aggregate by group                    |
| `df.sort_values('c')`           | Sort rows                             |
| `pd.to_datetime(df['c'])`       | Convert to datetime                   |
| `df.apply(fn)`                  | Apply a function                      |

---

## 📚 Glossary

| Term         | Definition                                                  | When it matters                     |
|--------------|------------------------------------------------------------|-------------------------------------|
| Series       | 1-D labeled array (one column)                             | Building block of a DataFrame       |
| DataFrame    | 2-D labeled table (rows × columns)                        | The main Pandas object              |
| Index        | The row labels of a Series/DataFrame                       | Alignment, lookups                  |
| NA           | Pandas' "missing value" marker                            | Cleaning, `dropna`, `fillna`        |
| `.loc` / `.iloc` | Select by **label** / by **position**                 | Row/column selection                |
| Vectorization| Operating on whole columns instead of row loops            | Performance on big data             |
| `.dt` accessor | Gateway to date/time parts of a datetime column          | Feature engineering from dates      |

---

🧠 **Pro Tips:**
* Think in **columns**, not rows — vectorized operations are the Pandas way.
* Convert date columns with `pd.to_datetime` early so the `.dt` tools work.
* Use `df.info()` and `df.describe()` first on any new dataset to understand it.

🔗 Helpful Links:
* https://pandas.pydata.org/docs/
* https://pandas.pydata.org/docs/user_guide/10min.html
* https://pandas.pydata.org/docs/reference/index.html
