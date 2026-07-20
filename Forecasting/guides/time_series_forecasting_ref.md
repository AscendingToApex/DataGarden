# 📉 Time Series Forecasting Reference Guide

> 🟡 **Level:** Intermediate  ·  **Prerequisites:** [Pandas](../../Python/guides/pandas_ref.md), [Descriptive Statistics](../../Statistics/guides/descriptive_statistics_ref.md)

**Forecasting** brings science to what's often a gut-feeling job — quantifying where a business is headed, spotting turning points, and uncovering opportunities. This guide covers **time-series concepts**, the **first steps** to prepare data, **seasonal decomposition**, and a tour of the main **forecasting models** (Holt-Winters, SARIMAX, TBATS, Prophet, XGBoost, and structural time series).

> Core insight: **forecasting is all about error modeling.** Once you strip out trend and seasonality, the art is explaining what's left.

## 📚 Table of Contents

* [🤔 Why Forecast?](#-why-forecast)
* [🕰️ What Is Time Series Data?](#-what-is-time-series-data)
* [📖 Key Concepts](#-key-concepts)
* [🚦 First Steps](#-first-steps)
* [🧩 Seasonal Decomposition (ETS)](#-seasonal-decomposition-ets)
* [➕✖️ Additive vs. Multiplicative](#-additive-vs-multiplicative)
* [🧠 Forecasting Models](#-forecasting-models)
* [⚠️ When *Not* to Forecast](#-when-not-to-forecast)
* [🔄 The Forecasting Workflow](#-the-forecasting-workflow)
* [📚 Glossary](#-glossary)

---

## 🤔 Why Forecast?

- Brings **science** to a sometimes gut-feeling job.
- Acts as a **barometer** for the company — quantifies direction.
- Helps you understand **turning points**.
- Can **uncover opportunities** hidden in the data.

---

## 🕰️ What Is Time Series Data?

- A **sequence of data points in time order** (oldest → newest).
- Most commonly recorded at **equally spaced** intervals (daily, weekly, monthly…).
- A type of **panel data** (a multidimensional dataset).

---

## 📖 Key Concepts

| Term | Definition |
|------|------------|
| **Time series data** | Data recurring over periods (day, week, month, quarter, year) |
| **Trend** | The direction the series is heading |
| **Seasonality** | A cyclical pattern within one complete period |
| **Error (residual)** | The gap between prediction and actual value |
| **Random walk** | Data that follows *no* pattern |
| **Seasonal decomposition (ETS)** | Splitting data into **trend + seasonality + error** |
| **Univariate** | Forecasting a single series |
| **Multivariate** | Forecasting more than one series |

> Note: Data recorded more finely can have *multiple* seasonalities — hourly data may show daily, weekly, *and* yearly cycles; monthly data usually just yearly.

---

## 🚦 First Steps

Before modeling, shape the data correctly:

1. Set the **datetime column as the index** and parse dates on import.
2. Select the columns of interest.
3. Rename the forecasting variable to **`y`**.
4. Set the index **frequency**: `data = data.asfreq("D")` for daily (check `data.index` for a `freq` attribute).
5. **Visualize** with a line plot.

```python
import pandas as pd
data = pd.read_csv('sales.csv', parse_dates=['date'], index_col='date')
data = data.rename(columns={'sales': 'y'})
data = data.asfreq('D')      # daily frequency
data['y'].plot()
```

> Pro Tip: Don't manually engineer season/weekday columns — good models learn seasonality themselves. Only add external factors the model *can't* infer (e.g., "was the store open?").

---

## 🧩 Seasonal Decomposition (ETS)

A seasonal series decomposes into three parts:

- **Trend** — the mostly-linear long-term direction.
- **Seasonality** — the repeating cyclical pattern.
- **Error** — everything the trend and seasonality can't explain.

```python
from statsmodels.tsa.seasonal import seasonal_decompose
result = seasonal_decompose(data['y'], model='additive', period=12)
result.plot()
```

We then try to model the remaining **error** using **external regressors**.

---

## ➕✖️ Additive vs. Multiplicative

| Type | Behavior | Formula |
|------|----------|---------|
| **Additive** | Fluctuations stay **constant** as the level rises | `y[t] = T[t] + S[t] + e[t]` |
| **Multiplicative** | Fluctuations **grow** with the level | `y[t] = T[t] × S[t] × e[t]` |

- Think in **percentages** → multiplicative.
- Think in **absolute values** → additive.
- **Exponential** trend → multiplicative.

---

## 🧠 Forecasting Models

| Model | Best for | Notes |
|-------|----------|-------|
| **Holt-Winters (Triple Exp. Smoothing)** | Clear trend + one seasonality | Simple, fast baseline |
| **SARIMAX** | Trend + seasonality + external regressors | Classic statistical workhorse (`statsmodels`) |
| **TBATS** | **Multiple / complex** seasonalities | Handles several seasonal cycles at once |
| **Facebook Prophet** | Business series with holidays & missing data | Robust, easy, handles outliers/gaps well |
| **Prophet + XGBoost** | Prophet trend/season + ML on the residuals | Hybrid: model error with gradient boosting |
| **TensorFlow Structural Time Series (STS)** | Bayesian, uncertainty-aware forecasts | Flexible components + credible intervals |
| **Ensemble** | Combining several models | Often more robust than any single model |

> Pro Tip: Start with a simple baseline (Holt-Winters or SARIMAX). Only reach for TBATS/Prophet/ML hybrids when the data's complexity (multiple seasonalities, holidays, messy gaps) justifies it.

---

## ⚠️ When *Not* to Forecast

If the data has **no pattern** (like most individual stock prices — a random walk), forecasting models won't help. These models work best with **consistent trend and seasonality**.

- **Trend** depends heavily on the specific company.
- **Seasonality** depends more on the **industry**, making it more predictable.

---

## 🔄 The Forecasting Workflow

1. **Prepare** — datetime index, `y`, frequency, visualize.
2. **Decompose** — inspect trend, seasonality, error; decide additive vs. multiplicative.
3. **Choose a model** — from a simple baseline up to complex/hybrid as needed.
4. **Fit & forecast** — train on history, predict future periods.
5. **Evaluate error** — compare predictions to a hold-out; model the residuals with external regressors.
6. **Iterate** — discard bad early data, add regressors, or ensemble.

---

## 📚 Glossary

| Term | Definition | When it matters |
|------|------------|-----------------|
| Trend | Long-term direction of a series | Decomposition |
| Seasonality | Repeating cyclical pattern | Model choice |
| ETS | Error-Trend-Seasonality decomposition | Understanding structure |
| Random walk | Patternless series | Knowing when *not* to forecast |
| Additive/Multiplicative | Constant vs. growing seasonal swings | Model configuration |
| External regressor | Extra variable explaining the error | Improving accuracy |

---

🧠 **Pro Tips:**
* Always **visualize first** — the plot tells you additive vs. multiplicative and whether a pattern even exists.
* Let models learn seasonality; only feed them factors they *can't* infer.
* Judge models on **out-of-sample error**, and consider **ensembling** for robustness.

🔗 Helpful Links:
* https://otexts.com/fpp3/ (Forecasting: Principles and Practice)
* https://www.statsmodels.org/stable/tsa.html
* https://facebook.github.io/prophet/
