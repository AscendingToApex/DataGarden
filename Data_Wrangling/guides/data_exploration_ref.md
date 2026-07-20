# 🔎 Data Wrangling & Exploration Reference Guide

> 🟡 **Level:** Intermediate  ·  **Prerequisites:** [Data Cleaning](data_cleaning_ref.md)

Once data is loaded and cleaned, you **reshape it** and **explore it** to find patterns. This guide covers **combining data** (adding rows/columns, merging), **indexing**, **summary statistics**, **GroupBy** aggregation, **pivot tables**, and quick **value counts** — the everyday tools of exploratory data analysis (EDA).

> Wrangling = getting the table into the right shape. Exploration = asking it questions.

## 📚 Table of Contents

* [🗺️ First Look](#-first-look)
* [➕ Adding Columns](#-adding-columns)
* [🧱 Adding Rows (Concatenate)](#-adding-rows-concatenate)
* [🔗 Merging / Joining](#-merging--joining)
* [🎯 Indexing & Selection](#-indexing--selection)
* [📊 Summary Statistics](#-summary-statistics)
* [🧮 GroupBy](#-groupby)
* [🔄 Pivot Tables](#-pivot-tables)
* [🔢 Counting & Proportions](#-counting--proportions)
* [📅 Working with Dates](#-working-with-dates)
* [🧠 Common Commands](#-common-commands)
* [📚 Glossary](#-glossary)

---

## 🗺️ First Look

```python
df.shape           # (rows, columns)
df.info()          # structure & dtypes
df.describe()      # numeric summary
df['col'].unique()             # distinct values
len(df['col'].unique())        # count of distinct values
df['col'].value_counts()       # frequency of each value
```

---

## ➕ Adding Columns

Compute new columns from existing ones (vectorized — no loops):

```python
df['total'] = df['price'] * df['qty']
df['is_big'] = df['total'] > 1000
df = df.assign(margin=lambda d: d['profit'] / d['total'])
```

---

## 🧱 Adding Rows (Concatenate)

Stack DataFrames on top of each other (same columns):

```python
combined = pd.concat([df_jan, df_feb], ignore_index=True)
```

---

## 🔗 Merging / Joining

Combine tables side-by-side on a key column (like a SQL JOIN):

```python
merged = df_orders.merge(df_customers, on='customer_id', how='left')
# how: 'inner' (default), 'left', 'right', 'outer'
```

> Note: `concat` stacks rows; `merge` joins columns on a key. Choose `how` deliberately — `left` keeps all rows from the left table, `inner` keeps only matches.

---

## 🎯 Indexing & Selection

```python
df.loc[df['age'] > 30, ['name', 'age']]   # rows by condition, chosen columns
df.iloc[0:5, 0:3]                          # by position (rows, cols)
df.set_index('id')                         # make a column the index
df.reset_index()                           # move the index back to a column
```

---

## 📊 Summary Statistics

```python
df['col'].mean()      # also .median, .mode, .min, .max, .var, .std, .sum
df['col'].quantile(0.4)
df['col'].agg(['mean', 'std', 'max'])      # several at once

# Custom aggregation
def pct30(column):
    return column.quantile(0.30)
df['col'].agg(pct30)

# Cumulative
df['col'].cumsum()    # also .cummax(), .cummin(), .cumprod()
```

---

## 🧮 GroupBy

The **split-apply-combine** pattern: split rows into groups, apply a function, combine the results.

```python
df.groupby('category')['sales'].sum()               # one aggregation
df.groupby('category')['sales'].agg(['sum', 'mean'])# several
df.groupby(['region', 'category'])['sales'].mean()  # multiple keys

# Apply a custom function per group
df.groupby('category')['sales'].apply(lambda s: s.max() - s.min())
```

> Pro Tip: After a `groupby`, you can group by **index levels**, dictionaries, or functions — but selecting a column first (`['sales']`) keeps results tidy.

---

## 🔄 Pivot Tables

Spreadsheet-style cross-tabulation — rows × columns with an aggregated value:

```python
df.pivot_table(index='region',
               columns='category',
               values='sales',
               aggfunc='mean',
               fill_value=0)
```

---

## 🔢 Counting & Proportions

```python
df['col'].value_counts()                   # counts per value
df['col'].value_counts(sort=False)
df['col'].value_counts(normalize=True)     # proportions (fractions)
df.groupby('town')['town'].count()         # count per group
```

---

## 📅 Working with Dates

```python
last_10 = df.nlargest(10, 'date')          # 10 most recent rows
recent_ids = set(df.nlargest(10, 'date')['id'])
df['date'].dt.year                         # extract parts (after to_datetime)
df.set_index('date').resample('M')['sales'].sum()   # monthly totals
```

---

## 🧠 Common Commands

| Command                            | What it does                      |
|------------------------------------|-----------------------------------|
| `pd.concat([a, b])`                | Stack rows                        |
| `df.merge(other, on=, how=)`       | Join on a key                     |
| `df.loc[]` / `df.iloc[]`           | Select by label / position        |
| `df.groupby('c').agg(...)`         | Split-apply-combine               |
| `df.pivot_table(...)`              | Cross-tab aggregation             |
| `df['c'].value_counts()`           | Frequency table                   |
| `df['c'].agg([...])`               | Multiple summary stats            |
| `df.nlargest(n, 'c')`              | Top-n rows by a column            |

---

## 📚 Glossary

| Term          | Definition                                                   | When it matters                 |
|---------------|--------------------------------------------------------------|---------------------------------|
| EDA           | Exploratory Data Analysis                                    | Understanding data first        |
| Concatenate   | Stacking DataFrames (rows or columns)                        | Combining same-shaped data      |
| Merge/Join    | Combining tables on a shared key                             | Relating datasets               |
| GroupBy       | Split-apply-combine aggregation                              | Per-group summaries             |
| Pivot table   | Row×column cross-tabulation                                  | Spreadsheet-style summaries     |
| Aggregation   | Collapsing many values into one (sum, mean, …)               | Summarizing groups              |

---

🧠 **Pro Tips:**
* Reach for **GroupBy** and **pivot_table** instead of manual loops — they're the heart of EDA.
* Be intentional with merge `how=`: it decides which rows survive the join.
* `value_counts(normalize=True)` turns raw counts into easy-to-read proportions.

🔗 Helpful Links:
* https://pandas.pydata.org/docs/user_guide/groupby.html
* https://pandas.pydata.org/docs/user_guide/reshaping.html
* https://pandas.pydata.org/docs/user_guide/merging.html
