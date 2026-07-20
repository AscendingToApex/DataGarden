# 📈 Matplotlib Reference Guide

**Matplotlib** is the foundational plotting library for Python — most other Python viz tools (including Seaborn) are built on top of it. This guide covers the **two interfaces**, building **line, scatter, bar, histogram, pie**, and **statistical** plots, plus **styling** and **saving** figures.

> Remember *why* you're plotting: a visualization exists to **communicate** something. As Kieran Healy puts it, charts are *tools* to deliberately simplify data so a reader can see past the cloud of points.

## 📚 Table of Contents

* [🚀 Getting Started](#-getting-started)
* [⚠️ Three Ways Charts Mislead](#-three-ways-charts-mislead)
* [🖥️ Running Matplotlib](#-running-matplotlib)
* [🧭 The Two Interfaces](#-the-two-interfaces)
* [🎨 Styles & Style Sheets](#-styles--style-sheets)
* [📏 Labels, Titles & Legends](#-labels-titles--legends)
* [📉 Line Plots](#-line-plots)
* [🔵 Scatter Plots](#-scatter-plots)
* [📊 Bar Charts](#-bar-charts)
* [📶 Histograms](#-histograms)
* [🥧 Pie Charts](#-pie-charts)
* [📐 Statistical Plots](#-statistical-plots)
* [💾 Saving Figures](#-saving-figures)
* [🧠 Common Commands](#-common-commands)
* [📚 Glossary](#-glossary)

---

## 🚀 Getting Started

```bash
pip install matplotlib numpy pandas
```
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt   # the standard alias
```

---

## ⚠️ Three Ways Charts Mislead

Great charts avoid three classes of problems:

- **Aesthetic** — overlapping bars, distracting backgrounds, clutter.
- **Substantive** — the underlying data are wrong or not represented accurately.
- **Perceptual** — tricks of human vision: a truncated y-axis that doesn't start at zero, an out-of-order x-axis, misleading sizes, optical illusions.

> Note: "Statistics can lie, and visualizations can at least bend the truth." Always start the y-axis at zero for bar charts, and keep axes in a sensible order.

---

## 🖥️ Running Matplotlib

In a **Jupyter notebook**, set the display mode once per session:

```python
%matplotlib inline      # static images (most common)
%matplotlib notebook    # interactive plots
```

From a **script** or **IPython**, end your plotting code with `plt.show()`:

```bash
python myplot.py        # from the terminal
```
```python
%run myplot.py          # from IPython / a notebook
```

---

## 🧭 The Two Interfaces

Because Matplotlib grew out of MATLAB but Python is object-oriented, there are **two ways** to plot. Don't mix them.

**MATLAB-style** (quick, stateful — good for simple plots):
```python
plt.figure()
plt.subplot(2, 1, 1)          # 2 rows, 1 col, panel 1
plt.plot(x, np.sin(x))
plt.subplot(2, 1, 2)          # panel 2
plt.plot(x, np.cos(x))
```

**Object-oriented** (explicit, scalable — preferred for complex figures):
```python
fig, ax = plt.subplots(2)     # ax is an array of Axes
ax[0].plot(x, np.sin(x))
ax[1].plot(x, np.cos(x))
```

> Pro Tip: Learn the **object-oriented** interface early. `fig, ax = plt.subplots()` gives you precise control and scales to multi-panel figures.

---

## 🎨 Styles & Style Sheets

Change the whole look with one line:

```python
plt.style.use('ggplot')          # try 'fivethirtyeight', 'seaborn', 'bmh'
plt.style.available              # list all built-in styles
```

---

## 📏 Labels, Titles & Legends

```python
fig = plt.figure(figsize=(8, 5))     # width, height in inches
plt.plot(x, np.sin(x), '-r', label='sin')   # '-' line, 'r' red
plt.plot(x, np.cos(x), '--', label='cos')   # '--' dashed
plt.xlabel('x value')
plt.ylabel('y value')
plt.title('Sine and Cosine')
plt.legend()                         # uses the labels above
plt.text(1, 0.5, 'annotation')       # text at an arbitrary point
```

Format-string shortcuts: `'o'` markers, `'--'` dashed, `'r'` red, combined like `'--or'`.

---

## 📉 Line Plots

```python
x = np.linspace(0, 10, 100)
plt.plot(x, np.sin(x))
plt.plot(x, np.cos(x))     # multiple lines on the same axes
plt.show()
```

---

## 🔵 Scatter Plots

```python
plt.scatter(df['x'], df['y'],
            alpha=0.5,          # transparency (helps with overplotting)
            c=df['group'],      # color by a value
            s=df['size'])       # marker size by a value
```

> Pro Tip: Lower `alpha` when points overlap heavily — it reveals density instead of a solid blob.

---

## 📊 Bar Charts

```python
# Standard
plt.bar(categories, values)

# Stacked — plot the second series on top of the first
plt.bar(categories, values1, label='A')
plt.bar(categories, values2, bottom=values1, label='B')

# Automating: iterate a dataset to build the bars
for label, group in df.groupby('category'):
    plt.bar(label, group['value'].sum())
```

---

## 📶 Histograms

```python
plt.hist(df['values'], bins=30, alpha=0.7)
```

---

## 🥧 Pie Charts

```python
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.axis('equal')    # keep it a circle
```

> Note: Use pie charts sparingly — bar charts almost always communicate proportions more clearly.

---

## 📐 Statistical Plots

```python
# Error bars
plt.errorbar(x, y, yerr=errors, fmt='o')

# Boxplot — shows median, quartiles, and outliers
plt.boxplot([group1, group2], labels=['A', 'B'])
```

---

## 💾 Saving Figures

```python
fig.savefig('my_figure.png', dpi=300, bbox_inches='tight')
```

The file lands in your current working directory. Re-open it in a notebook with:

```python
from IPython.display import Image
Image('my_figure.png', width=600)
```

---

## 🧠 Common Commands

| Command                       | What it does                        |
|-------------------------------|-------------------------------------|
| `plt.plot(x, y)`              | Line plot                           |
| `plt.scatter(x, y)`           | Scatter plot                        |
| `plt.bar(x, h)`               | Bar chart                           |
| `plt.hist(data, bins=n)`      | Histogram                           |
| `plt.subplots(r, c)`          | Grid of Axes (OO interface)         |
| `plt.xlabel/ylabel/title`     | Labels                              |
| `plt.legend()`                | Show a legend                       |
| `plt.style.use('name')`       | Apply a style sheet                 |
| `fig.savefig('f.png')`        | Save to disk                        |
| `plt.show()`                  | Render (scripts/IPython)            |

---

## 📚 Glossary

| Term      | Definition                                                | When it matters                 |
|-----------|-----------------------------------------------------------|---------------------------------|
| Figure    | The whole canvas that holds one or more plots             | `fig = plt.figure()`            |
| Axes      | A single plot (with its x/y axes) inside a figure         | The thing you draw on           |
| Subplot   | One Axes in a grid of plots                               | Multi-panel figures             |
| Style sheet | A preset bundle of colors/fonts/gridlines               | Consistent look                 |
| Format string | Shorthand like `'--or'` for line/marker/color         | Quick styling of lines          |
| Alpha     | Transparency from 0 (clear) to 1 (solid)                  | Overplotting                    |

---

🧠 **Pro Tips:**
* Prefer the **object-oriented** interface (`fig, ax = plt.subplots()`) for anything non-trivial.
* Start bar/line y-axes at **zero** and keep axes ordered — avoid perceptual lies.
* Set `figsize` up front so labels and legends have room to breathe.

🔗 Helpful Links:
* https://matplotlib.org/stable/
* https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html
* https://matplotlib.org/stable/tutorials/index.html
