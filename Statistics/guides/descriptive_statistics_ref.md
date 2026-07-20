# 📊 Descriptive Statistics Reference Guide

> 🟢 **Level:** Beginner  ·  **Prerequisites:** none

Descriptive statistics **summarize** and **describe** a dataset so you can see its shape and spread at a glance. This guide covers **central tendency** (mean, median, mode), **variability** (range, variance, standard deviation), **distribution shape** (skew, kurtosis), and **standard scores** (z-scores, t-scores).

> Why it matters: Summary statistics are *tools we use to deliberately simplify* data so we can see past the cloud of individual points.

## 📚 Table of Contents

* [🧭 Reading a Distribution](#-reading-a-distribution)
* [🎯 Central Tendency](#-central-tendency)
* [📏 Variability](#-variability)
* [🔺 Skew & Kurtosis](#-skew--kurtosis)
* [🧮 Standard Scores](#-standard-scores)
* [🐍 In Python](#-in-python)
* [🧠 Quick Reference](#-quick-reference)
* [📚 Glossary](#-glossary)

---

## 🧭 Reading a Distribution

To get a sense of a dataset from its summary statistics, look at seven numbers together:

| Statistic          | Tells you…                                            |
|--------------------|-------------------------------------------------------|
| **Mean**           | The average / center                                  |
| **Median**         | The middle value (robust to outliers)                 |
| **Mode**           | The most frequent value (the peak)                    |
| **Variance**       | How far values spread from the mean                   |
| **Standard deviation** | Spread, in the *same units* as the data           |
| **Skewness**       | Asymmetry (which tail is longer)                      |
| **Kurtosis**       | Peakedness / tail heaviness                           |

> Pro Tip: Always pair the numbers with a **histogram**. The picture reveals skew and outliers that a single statistic can hide.

---

## 🎯 Central Tendency

Single values that represent the middle of a dataset.

### Mean — the average
$$\bar{x} = \frac{\sum_{i=1}^{n} x_i}{n}$$

- Reflects **every** score in the distribution.
- **Most influenced by outliers** and extreme values.

### Median — the middle value
- Order the data; take the middle value (or the average of the two middle values).
- **Robust to outliers** — best for skewed data. It's also the **50th percentile**.

### Mode — the most frequent value
- The value(s) that occur most often (data can be **unimodal**, **bimodal**, or **multimodal**).
- The **only** measure usable with **nominal/categorical** data.

### When to use each

| Measure | Use when…                                        | Outlier sensitivity |
|---------|--------------------------------------------------|---------------------|
| Mean    | Data is roughly symmetric, no big outliers       | High                |
| Median  | Data is skewed or has outliers                   | Low                 |
| Mode    | You need the most common value / categorical data| Very low            |

> Note: If the **mean and median differ noticeably**, your data is skewed — mean > median means right-skew; mean < median means left-skew.

---

## 📏 Variability

How spread out the values are. Greater variability = data more spread out = the mean is a *less* representative summary.

### Range
The simplest measure: `max − min`. Intuitive but very sensitive to outliers.

### Variance — mean of squared deviations
$$s^2 = \frac{\sum_{i=1}^{n} (x_i - \bar{x})^2}{n-1} \quad\text{(sample)} \qquad \sigma^2 = \frac{\sum_{i=1}^{N} (x_i - \mu)^2}{N} \quad\text{(population)}$$

- Squaring captures both **direction and magnitude** of deviations, but leaves you in **squared units**.
- Smaller variance → the mean better represents the data.

> Note: Sample variance divides by `n − 1` (Bessel's correction); population variance divides by `N`.

### Standard Deviation — the interpretable spread
$$s = \sqrt{s^2}$$

- The square root of variance, so it's back in the **original units** — far easier to interpret.
- **The 68–95–99.7 rule:** in a normal distribution, ~68% of values fall within 1 SD of the mean, ~95% within 2 SD, and ~99.7% within 3 SD.

---

## 🔺 Skew & Kurtosis

A **normal distribution** is symmetrical, bell-shaped, with most data near the center. Real data differs in two main ways:

### Skew — asymmetry
$$\text{Skewness} = \frac{3(\bar{x} - \text{median})}{s}$$

- **Positive (right) skew:** longer tail on the right; mean > median.
- **Negative (left) skew:** longer tail on the left; mean < median.
- **0:** symmetrical.
- **Fix it** by transforming (log, square root) or removing extreme values.

### Kurtosis — peakedness & tails
- **> 3 (leptokurtic):** more peaked, heavier tails than normal.
- **< 3 (platykurtic):** flatter, lighter tails than normal.
- **= 3:** normal.

> Pro Tip: Use skew and kurtosis **together** — neither alone fully describes a distribution's shape.

---

## 🧮 Standard Scores

Standard scores let you **compare values across different units/scales**.

### Z-Scores
$$z = \frac{x - \mu}{\sigma}$$

- Measures how many **standard deviations** a value sits from the mean (positive = above, negative = below).
- Any z-score distribution has **mean 0** and **standard deviation 1** (the standard normal distribution).
- Uses: spotting **outliers**, **normality testing**, and building **confidence intervals**.

### T-Scores
$$T = 10\left(\frac{x - \bar{x}}{s}\right) + 50$$

A rescaled z-score (mean 50, SD 10) used to **avoid negative numbers** — common on aptitude/educational tests.

---

## 🐍 In Python

```python
import numpy as np
import pandas as pd
from scipy import stats

df['col'].mean()          # mean
df['col'].median()        # median
df['col'].mode()          # mode
df['col'].var()           # sample variance
df['col'].std()           # sample standard deviation
df['col'].describe()      # count, mean, std, min, quartiles, max
df['col'].skew()          # skewness
df['col'].kurt()          # kurtosis
stats.zscore(df['col'])   # z-scores
```

---

## 🧠 Quick Reference

| Measure            | Formula / method                    | Robust to outliers? |
|--------------------|-------------------------------------|---------------------|
| Mean               | `sum / n`                           | ❌                  |
| Median             | middle value                        | ✅                  |
| Mode               | most frequent value                 | ✅✅                |
| Range              | `max − min`                         | ❌                  |
| Variance           | mean of squared deviations          | ❌                  |
| Standard deviation | `√variance`                         | ❌                  |
| Z-score            | `(x − μ) / σ`                       | —                   |

---

## 📚 Glossary

| Term          | Definition                                                   | When it matters                  |
|---------------|--------------------------------------------------------------|----------------------------------|
| Central tendency | The "middle" of a distribution                            | Summarizing a dataset            |
| Variability   | The spread/dispersion of values                              | How representative the mean is   |
| Skewness      | Asymmetry of a distribution                                  | Choosing mean vs. median         |
| Kurtosis      | Peakedness & tail-heaviness                                  | Describing distribution shape    |
| Z-score       | Value's distance from the mean in SD units                   | Comparing across scales, outliers|
| 68-95-99.7 rule | Coverage within 1/2/3 SD of a normal distribution          | Interpreting standard deviation  |

---

🧠 **Pro Tips:**
* Report the **median** alongside the mean whenever data might be skewed.
* Prefer **standard deviation** over variance when communicating spread — it's in real units.
* Convert to **z-scores** to compare values measured on different scales.

🔗 Helpful Links:
* https://www.khanacademy.org/math/statistics-probability/summarizing-quantitative-data
* https://docs.scipy.org/doc/scipy/reference/stats.html
* https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html
