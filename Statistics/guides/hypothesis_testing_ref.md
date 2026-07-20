# 🔬 Hypothesis Testing Reference Guide

> 🟡 **Level:** Intermediate  ·  **Prerequisites:** [Descriptive Statistics](descriptive_statistics_ref.md)

Hypothesis testing is how we decide whether a pattern in a **sample** is real evidence about a **population**, or just chance. This guide covers the **logic** (null vs. alternative), **p-values**, **errors and power**, **confidence intervals**, and a **decision table** for picking the right test — parametric or nonparametric.

> The core idea: a hypothesis test pits two competing claims against each other, and only one can win. We never *prove* the alternative true — we gather enough evidence to **reject the null**.

## 📚 Table of Contents

* [⚖️ The Two Hypotheses](#-the-two-hypotheses)
* [🎲 Sampling & Data Collection](#-sampling--data-collection)
* [📉 P-values & Significance](#-p-values--significance)
* [🧪 Test Statistics](#-test-statistics)
* [📐 Effect Size & Power](#-effect-size--power)
* [❌ Type I & Type II Errors](#-type-i--type-ii-errors)
* [📊 Standard Error & the CLT](#-standard-error--the-clt)
* [🎯 Confidence Intervals](#-confidence-intervals)
* [↔️ One-Tailed vs. Two-Tailed Tests](#-one-tailed-vs-two-tailed-tests)
* [🗺️ Choosing the Right Test](#-choosing-the-right-test)
* [🐍 The Python Workflow](#-the-python-workflow)
* [📚 Glossary](#-glossary)

---

## ⚖️ The Two Hypotheses

Every test compares:

- **Null hypothesis (H₀)** — the existing idea, *assumed true* until proven otherwise ("there is no difference / no relationship").
- **Alternative hypothesis (Hₐ or H₁)** — the researcher's new "challenger" claim ("there is a difference / a relationship").

A test ends in one of two verdicts: **"reject H₀"** or **"fail to reject H₀."** We never "accept H₀" and never "prove Hₐ."

> Note: This mirrors **falsificationism** — you can't prove a theory true, only expose it to rigorous attempts at being proven false. We disprove "no difference" to be left with "there is a difference."

---

## 🎲 Sampling & Data Collection

- **Population** — the entire group of interest (e.g., all swordfish in the Atlantic).
- **Sample** — a subset of the population (almost always what we actually measure).
- **Simple random sample** — every member has an equal chance of selection, and one selection doesn't affect another. This is essential to avoid **bias**.
- **Convenience sample** (only who's easy to reach) and high **non-response** are poor bases for conclusions.

**Explanatory vs. response variables:** the explanatory variable is the suspected cause; the response variable is the effect. ⚠️ **Association does not imply causation.**

**Observational study vs. experiment:** an observational study collects data *without interfering*; an **experiment** deliberately intervenes and is what lets you argue for **causation**.

> Pro Tip: The larger the random sample, the more likely it represents the population — but size never fixes a **biased** sampling method.

---

## 📉 P-values & Significance

A **p-value** is the probability of obtaining a result *at least as extreme* as the one observed, **assuming H₀ is true**.

- **Large p-value** → result is consistent with H₀ → **fail to reject** H₀.
- **Small p-value** (close to zero) → strong evidence against H₀ → **reject** H₀.
- The **significance level (α)** is the threshold dividing "small" from "large." Common values: **0.10, 0.05, 0.01**.

> Note: A p-value tells you *whether* an effect likely exists, **not how big or important it is**. Anyone presenting p-values alone (with no effect size) is missing the point — or misleading you.

---

## 🧪 Test Statistics

Nearly every test (t-test, F-test, …) is a ratio of explained to unexplained variation:

$$\text{statistic} = \frac{\text{variance explained}}{\text{variance not explained}} = \frac{\text{effect}}{\text{error}}$$

- A **significant** statistic means you've found support *against the null* — not proof the alternative is right.
- A **non-significant** result doesn't prove your hypothesis wrong; it can also mean measurement error or too small a sample.

---

## 📐 Effect Size & Power

Because increasing sample size alone can make almost anything "significant" (a form of **p-hacking — don't do it**), we also report **effect size**: a standardized measure of *how big* an effect is, comparable across studies.

| Effect size | Interpretation |
|-------------|----------------|
| ~0.1        | Small          |
| ~0.3        | Medium         |
| ~0.5        | Large          |

Common metrics: **Cohen's d**, **Pearson's r**, **odds ratios**.

**Statistical power** — the probability of detecting an effect that really exists. Convention (Cohen): aim for **0.8**. Power depends on sample size, α, and effect size.

> Pro Tip: When someone says "it's significant," the first question to ask is **"what's the effect size?"** Significance ≠ importance.

---

## ❌ Type I & Type II Errors

| | H₀ is actually true | H₀ is actually false |
|---|---|---|
| **Reject H₀** | ❌ Type I error (false positive) | ✅ Correct |
| **Fail to reject H₀** | ✅ Correct | ❌ Type II error (false negative) |

- **Type I (false positive):** you claim an effect that isn't there. Controlled by **α**.
- **Type II (false negative):** you miss a real effect. Controlled by **power (1 − β)**.

---

## 📊 Standard Error & the CLT

- **Sampling variation:** different samples give different means.
- **Sampling distribution:** the distribution of those sample means.
- **Standard error (SE):** the standard deviation of the sampling distribution:
$$SE = \frac{s}{\sqrt{n}}$$

**Central Limit Theorem (CLT):** as sample size grows, the sampling distribution (1) becomes **normal**, (2) has a mean equal to the population mean, and (3) has a standard deviation equal to the standard error — *regardless of the population's shape*.

> Note: The CLT is why so many tests assume normality "for large enough samples." Understand it now — it's often referenced later without explanation.

---

## 🎯 Confidence Intervals

A confidence interval gives a range that likely contains the true population parameter. For significance level α, use a confidence level of **1 − α**.

$$\bar{x} \pm 1.96 \times SE$$

- A z-score of **1.96** captures the middle **95%** of a normal distribution.
- Example: sample mean GPA 2.75 ± 1.96·SE → "we're 95% confident the population mean falls in this range."

---

## ↔️ One-Tailed vs. Two-Tailed Tests

| Alternative hypothesis          | Test        |
|---------------------------------|-------------|
| different from the null         | two-tailed  |
| greater than the null           | right-tailed|
| less than the null              | left-tailed |

- **Two-tailed** (no direction): with α = 0.05, look for the upper 2.5% *or* lower 2.5%.
- **One-tailed** (directional): with α = 0.05, put all 5% in a single tail.

---

## 🗺️ Choosing the Right Test

### Parametric tests
Assume something about the population's distribution. **z-test, t-test, and ANOVA** are parametric. Assumptions:

- **Normality** — the population is approximately normal.
- **Randomness** — samples are random subsets of the population.
- **Independence** — each observation is independent of the others.
- **Sample size** — big enough for the CLT (rule of thumb: ≥ 30 per group for t-tests/ANOVA; ≥ 10 successes *and* failures for proportion tests; ≥ 5 per cell for chi-square).

| Test | Tests for | Independent var | Dependent var |
|------|-----------|-----------------|---------------|
| **1-sample z-test** | Population mean vs. a value (σ known) | None | 1 quantitative |
| **1-sample t-test** | Population mean vs. a value (σ unknown) | None | 1 quantitative |
| **2-sample t-test** | Two population means differ | 1 categorical, 2 groups | 1 quantitative |
| **1-sample proportion z-test** | A proportion vs. a target | None | 1 categorical, 2 levels |
| **2-sample proportion z-test** | Two proportions differ | 1 categorical, 2 groups | 1 categorical, 2 levels |
| **Chi-square (independence)** | Association between two categoricals | 1 categorical, 2+ groups | 1 categorical, 2+ groups |
| **Chi-square (goodness-of-fit)** | Does a categorical follow an expected distribution | None | 1 categorical, 2+ groups |
| **One-way ANOVA** | Means differ across 2+ groups | 1 categorical, 2+ groups | 1 quantitative |

### Nonparametric tests
Don't require a specific distribution — use them when parametric assumptions fail, samples are small, or data isn't normal. They're often based on **ranks** and typically test the **median** rather than the mean.

| Nonparametric test | Parametric equivalent | Use for |
|--------------------|-----------------------|---------|
| **Wilcoxon signed-rank** | Paired t-test | Two paired groups |
| **Mann-Whitney U (Wilcoxon rank-sum)** | 2-sample t-test | Two independent groups |
| **Kruskal-Wallis** | One-way ANOVA | 2+ independent groups |
| **1-sample Wilcoxon / sign test** | 1-sample t-test | One group vs. a median |
| **Welch's t-test** | 2-sample t-test | Two groups with **unequal variances** |
| **Mood's median** | — | Compare medians of 2+ groups |

> Pro Tip: If two samples have clearly **unequal variances**, use **Welch's t-test** instead of the standard 2-sample t-test.

---

## 🐍 The Python Workflow

A general process for testing a single variable:

1. **State the hypothesis** about an unknown population parameter.
2. **Set α** (e.g., 0.05).
3. **Compute the point estimate** (sample statistic).
4. **Build a bootstrap distribution** of that statistic.
5. **Standardize** with a z-score.
6. **Calculate the p-value** and decide.

```python
import numpy as np
from scipy.stats import norm

alpha = 0.05
prop_samp = (df['col'] == "Value").mean()      # sample statistic
prop_hyp  = 0.5                                  # from the null hypothesis
std_error = np.std(bootstrap_distn, ddof=1)
z_score   = (prop_samp - prop_hyp) / std_error

# p-value depends on the tail:
p_value = 1 - norm.cdf(z_score)   # right-tailed
# p_value = norm.cdf(z_score)     # left-tailed

reject = p_value <= alpha          # True → reject H0; False → fail to reject

# 95% confidence interval from the bootstrap distribution
lower = np.quantile(bootstrap_distn, 0.025)
upper = np.quantile(bootstrap_distn, 0.975)
```

> Note: The `pingouin` library offers clean one-liners for many tests: `pingouin.ttest`, `pingouin.wilcoxon`, `pingouin.mwu`, `pingouin.kruskal`.

---

## 📚 Glossary

| Term            | Definition                                                     | When it matters                 |
|-----------------|---------------------------------------------------------------|---------------------------------|
| Null hypothesis (H₀) | The "no effect" claim assumed true                       | The thing you try to reject     |
| P-value         | P(result this extreme \| H₀ true)                             | Deciding significance           |
| Significance level (α) | Threshold for rejecting H₀                              | Setting your standard of proof  |
| Effect size     | Standardized magnitude of an effect                           | Judging importance              |
| Power           | P(detecting a real effect)                                    | Study design                    |
| Type I error    | False positive (reject a true H₀)                             | Controlled by α                 |
| Type II error   | False negative (keep a false H₀)                              | Controlled by power             |
| Standard error  | SD of the sampling distribution                               | Confidence intervals, z-scores  |
| CLT             | Sampling distribution → normal as n grows                     | Why normality assumptions hold  |

---

🧠 **Pro Tips:**
* Always report **effect size and confidence intervals** alongside p-values.
* Never chase significance by inflating sample size — that's **p-hacking**.
* Check assumptions first: if the bootstrap distribution isn't normal, reconsider randomness, independence, and sample size — or switch to a **nonparametric** test.

🔗 Helpful Links:
* https://www.scribbr.com/statistics/hypothesis-testing/
* https://docs.scipy.org/doc/scipy/reference/stats.html
* https://pingouin-stats.org/
