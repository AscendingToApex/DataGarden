# 🌊 Seaborn Reference Guide

> 🟡 **Level:** Intermediate  ·  **Prerequisites:** [Matplotlib](matplotlib_ref.md)

**Seaborn** is a statistical plotting library built on top of Matplotlib that works best with **Pandas DataFrames**. It makes attractive, informative statistical graphics with far less code than raw Matplotlib. This guide covers **choosing the right plot**, **styling** (styles, palettes, context), **distribution / categorical / relational / regression** plots, and multi-panel **grids**.

> Mental model: Seaborn handles the *statistics and good defaults*; Matplotlib underneath still handles the *fine-tuning*. You'll use both together.

## 📚 Table of Contents

* [🚀 Getting Started](#-getting-started)
* [🧭 Choosing the Right Plot](#-choosing-the-right-plot)
* [🎨 Styles, Palettes & Context](#-styles-palettes--context)
* [🏷️ Titles, Labels & Tweaks](#-titles-labels--tweaks)
* [📊 Distribution Plots](#-distribution-plots)
* [🗂️ Categorical Plots](#-categorical-plots)
* [🔗 Relational Plots](#-relational-plots)
* [📈 Regression Plots](#-regression-plots)
* [🧩 Grids: Facet, Pair & Joint](#-grids-facet-pair--joint)
* [🌡️ Matrix Plots (Heatmaps)](#-matrix-plots-heatmaps)
* [🧠 Common Commands](#-common-commands)
* [📚 Glossary](#-glossary)

---

## 🚀 Getting Started

```bash
pip install seaborn
```
```python
import seaborn as sns
import matplotlib.pyplot as plt

sns.set()          # apply Seaborn's clean default theme
```

---

## 🧭 Choosing the Right Plot

Pick a starting point based on your question:

| Goal                                   | Start with                                  |
|----------------------------------------|---------------------------------------------|
| One variable's distribution            | `displot()` (also `kdeplot`, `ecdfplot`, `rugplot`) |
| Relationship between two variables     | `lmplot()` (regression + facetting)         |
| Compare across categories              | `boxplot()`, `violinplot()`, then `barplot`/`countplot`/`pointplot` |
| Category comparisons across facets     | `catplot()`                                 |
| Explore many pairs at once             | `pairplot()`, `jointplot()` (after initial analysis) |

> Pro Tip: Use `pairplot`/`jointplot` *after* you've done some distribution or regression exploration — they're most useful once you know what to look for.

---

## 🎨 Styles, Palettes & Context

```python
# Background / axes style
sns.set_style("whitegrid")   # white, dark, whitegrid, darkgrid, ticks

# Color palette — match to your data
sns.set_palette("Blues")     # Sequential: low→high (Greys, Blues, GnBu)
sns.set_palette("RdBu")      # Diverging: both extremes matter (PRGn, RdBu_r)
sns.set_palette("Paired")    # Circular/qualitative: unordered categories
sns.color_palette()          # current palette
sns.palplot(sns.color_palette())   # preview it

# Scale for the output medium
sns.set_context("talk")      # paper, notebook, talk, poster
```

> Note: Choose the palette **type** to match the data: **sequential** for ordered magnitudes, **diverging** when both high and low ends are interesting, **qualitative** for unordered categories.

---

## 🏷️ Titles, Labels & Tweaks

First check whether your plot returned an **AxesSubplot** or a **FacetGrid** — the styling calls differ.

```python
ax = sns.scatterplot(x='a', y='b', data=df)
ax.set(xlabel="X", ylabel="Y", xlim=(0, 100), ylim=(0, 50))
ax.set_title("My Title")
plt.xticks(rotation=90)              # rotate crowded x labels
sns.despine(left=True)              # remove axis spines
ax.axvline(x=100, linestyle='--', label="Budget")   # reference line

# For a FacetGrid (g):
g.fig.suptitle("Overall Title", y=1.03)
g.set_titles("{col_name}")
```

---

## 📊 Distribution Plots

```python
sns.displot(df['value'])                  # histogram (default)
sns.displot(df['value'], kind='kde')      # smooth density curve
sns.histplot(df['value'])                 # histogram on an existing Axes
```

---

## 🗂️ Categorical Plots

```python
sns.countplot(x='category', data=df)      # count of rows per category
sns.boxplot(x='cat', y='value', data=df)  # distribution + outliers
sns.violinplot(x='cat', y='value', data=df)
sns.barplot(x='cat', y='value', data=df)  # mean per category + CI

# catplot facets categorical plots across rows/columns
sns.catplot(x='cat', y='value', data=df, kind='box', col='region')
```

---

## 🔗 Relational Plots

For two quantitative variables. **Scatter** = independent observations; **line** = the same thing tracked over time.

```python
sns.scatterplot(x='a', y='b', data=df,
                hue='group',      # 3rd variable via color
                size='pop',       # 4th variable via marker size
                style='type',     # 5th variable via marker shape
                alpha=0.6)

# relplot adds faceting via col / row
sns.relplot(x='a', y='b', data=df, kind='line',
            col='region', col_wrap=3,
            hue='group')          # shaded 95% CI around the mean by default
```

---

## 📈 Regression Plots

```python
sns.regplot(x='a', y='b', data=df)        # single scatter + fitted line
sns.lmplot(x='a', y='b', data=df,
           hue='group', col='region')     # regression with facetting
```

---

## 🧩 Grids: Facet, Pair & Joint

**Facetting** draws the same plot across subsets of your data:
```python
g = sns.FacetGrid(df, col='region')
g.map(sns.histplot, 'value')
```

**PairGrid / pairplot** — every variable against every other:
```python
sns.pairplot(df, hue='group')             # quick version
g = sns.PairGrid(df)                       # customizable version
g.map_diag(sns.histplot)
g.map_offdiag(sns.scatterplot)
```

**JointGrid / jointplot** — a scatter plus marginal distributions:
```python
sns.jointplot(x='a', y='b', data=df, kind='reg')
```

---

## 🌡️ Matrix Plots (Heatmaps)

Great for correlation matrices and pivot tables:
```python
corr = df.corr()
sns.heatmap(corr, annot=True, cmap='RdBu_r', center=0)
```

---

## 🧠 Common Commands

| Command                        | What it does                          |
|--------------------------------|---------------------------------------|
| `sns.set()` / `set_style()`    | Apply theme / background style        |
| `sns.set_palette()`            | Set the color palette                 |
| `sns.displot()`                | Distribution of one variable          |
| `sns.countplot()`              | Counts per category                   |
| `sns.boxplot()` / `violinplot`| Category distributions                |
| `sns.scatterplot()` / `relplot`| Two-variable relationships            |
| `sns.lmplot()` / `regplot`     | Regression plots                      |
| `sns.pairplot()`               | All pairwise relationships            |
| `sns.heatmap()`                | Matrix / correlation heatmap          |

---

## 📚 Glossary

| Term         | Definition                                                   | When it matters                    |
|--------------|--------------------------------------------------------------|------------------------------------|
| Facetting    | Repeating a plot across subsets (col/row)                    | Comparing groups side by side      |
| Hue          | Encoding a category with color                               | Adding a 3rd dimension             |
| FacetGrid    | A grid object returned by facetted plots                     | Grid-level titles/labels           |
| AxesSubplot  | A single-Axes object returned by simple plots                | Axes-level titles/labels           |
| Sequential palette | Colors ordered low→high                                | Ordered magnitude data             |
| Diverging palette  | Colors emphasizing both extremes                       | Data with a meaningful midpoint    |
| KDE          | Kernel Density Estimate (smooth distribution curve)          | Distribution shape                 |

---

🧠 **Pro Tips:**
* Feed Seaborn **tidy DataFrames** (one row per observation, one column per variable).
* Match the **palette type** to your data — it's the difference between clarity and confusion.
* Drop to Matplotlib (`ax.set(...)`) for the last 10% of polish Seaborn doesn't expose.

🔗 Helpful Links:
* https://seaborn.pydata.org/
* https://seaborn.pydata.org/tutorial.html
* https://seaborn.pydata.org/examples/index.html
