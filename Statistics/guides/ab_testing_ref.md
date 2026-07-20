# 🧪 A/B Testing & Experimentation Reference Guide

> 🟡 **Level:** Intermediate  ·  **Prerequisites:** [Hypothesis Testing](hypothesis_testing_ref.md)  ·  **Related:** [Descriptive Statistics](descriptive_statistics_ref.md) · [Probability](probability_ref.md)

An **A/B test** is a controlled experiment that compares two versions (A = control, B = variant) to learn which performs better — the backbone of data-driven product and marketing decisions. This guide covers designing a valid test, sizing it, reading the results, and the pitfalls that invalidate them.

> An A/B test is just [hypothesis testing](hypothesis_testing_ref.md) applied to a live decision. If you know H₀/Hₐ, p-values, and power, you already know the theory — this guide is the practice.

## 📚 Table of Contents

* [🔬 What Is an A/B Test?](#-what-is-an-ab-test)
* [🎯 Designing a Test](#-designing-a-test)
* [📏 Sample Size & Duration](#-sample-size--duration)
* [📊 Reading the Results](#-reading-the-results)
* [⚠️ Common Pitfalls](#-common-pitfalls)
* [🚀 Beyond A/B](#-beyond-ab)
* [✅ Experiment Checklist](#-experiment-checklist)
* [📚 Glossary](#-glossary)

---

## 🔬 What Is an A/B Test?

- Randomly split users into a **control (A)** and one or more **variants (B)**.
- Show each group a different experience; hold everything else constant.
- Compare a single **primary metric** (conversion rate, click-through, revenue per user).
- **Randomization** is what makes it causal — it balances out confounders on average.

> Note: The whole point is **causation, not correlation**. Random assignment is the ingredient that lets you say "B *caused* the lift."

---

## 🎯 Designing a Test

1. **State a hypothesis** — "Changing the button to green will increase sign-ups."
   - H₀: no difference in sign-up rate. Hₐ: the variant differs.
2. **Pick ONE primary metric** (the Overall Evaluation Criterion). Track guardrail metrics too (e.g., don't tank revenue to boost clicks).
3. **Choose the unit of randomization** — usually the *user*, not the *session* (so a person always sees the same variant).
4. **Set α and power up front** — commonly α = 0.05, power = 0.80.
5. **Decide the effect size worth detecting** (the Minimum Detectable Effect) *before* looking at data.

---

## 📏 Sample Size & Duration

The four levers of sample size trade off against each other:

| Lever | Effect on required sample |
|-------|---------------------------|
| Smaller **effect** you want to detect (MDE) | ⬆ needs more users |
| Higher **power** (1−β) | ⬆ needs more users |
| Lower **α** (stricter) | ⬆ needs more users |
| Higher baseline **variance** | ⬆ needs more users |

- **Compute sample size *before* launching** (use an online calculator or `statsmodels`), so you know when you'll have an answer.
- **Run for full business cycles** — usually at least **1–2 weeks** to cover weekday/weekend and novelty effects.

> Pro Tip: Never decide the sample size by "checking if it's significant yet." That's peeking — the #1 way to get false positives (see pitfalls).

---

## 📊 Reading the Results

- Compare the metric between groups and compute a **p-value** and, better, a **confidence interval** on the *difference*.
- **p < α** → statistically significant; reject H₀.
- Report the **effect size with its confidence interval**, not just "significant." A 0.1% lift with a huge CI is not actionable.
- **Statistical vs. practical significance** — a tiny, significant lift may not be worth the engineering cost.

```python
from statsmodels.stats.proportion import proportions_ztest
# successes and totals for control (A) and variant (B)
count = [conv_A, conv_B]
nobs  = [n_A, n_B]
stat, pval = proportions_ztest(count, nobs)
```

---

## ⚠️ Common Pitfalls

- **Peeking / early stopping** — repeatedly checking and stopping when significant inflates false positives. Decide the sample size up front, or use sequential-testing methods.
- **Multiple comparisons** — testing many metrics/variants raises the chance one looks significant by luck. Correct for it (e.g., Bonferroni).
- **Sample Ratio Mismatch (SRM)** — if the actual split isn't your intended 50/50, the randomization is broken; distrust the result.
- **Novelty & primacy effects** — users react to *change* itself; run long enough for it to wear off.
- **Confounding / contamination** — external events, or users leaking between groups, bias results.
- **Simpson's paradox** — an aggregate result can reverse within segments; check key segments.
- **Underpowered tests** — too few users → a real effect looks non-significant (false negative).

> Note: A non-significant result does **not** prove "no difference" — it may mean the test was underpowered.

---

## 🚀 Beyond A/B

- **A/B/n** — more than one variant at once (mind the multiple-comparison correction).
- **Multivariate testing** — several changes combined to find interactions (needs lots of traffic).
- **Multi-armed bandits** — dynamically shift traffic toward the winning variant; good for short campaigns.
- **Quasi-experiments** (difference-in-differences, matching) — when true randomization isn't possible.

---

## ✅ Experiment Checklist

- [ ] Clear hypothesis and one primary metric (+ guardrails)
- [ ] Randomize by the right unit (usually user)
- [ ] α, power, and MDE set **before** launch
- [ ] Required sample size and duration computed up front
- [ ] Randomization verified (no sample ratio mismatch)
- [ ] Run for full business cycles; no peeking
- [ ] Report effect size + confidence interval, not just p-value
- [ ] Check key segments for Simpson's paradox

---

## 📚 Glossary

| Term | Definition | When it matters |
|------|------------|-----------------|
| Control / Variant | The A (baseline) vs. B (change) group | Every test |
| OEC | Overall Evaluation Criterion (primary metric) | Deciding a winner |
| MDE | Minimum Detectable Effect | Sample sizing |
| Power | P(detecting a real effect) | Avoiding false negatives |
| Peeking | Checking results before the planned end | False positives |
| SRM | Sample Ratio Mismatch | Validating randomization |
| Guardrail metric | A metric that must not get worse | Protecting the business |

---

🧠 **Pro Tips:**
* Fix your **sample size and stop date before launch** — then don't peek.
* Always report the **effect size and its confidence interval**, not just significance.
* Distinguish **statistical** from **practical** significance before shipping a change.

🔗 Helpful Links:
* https://www.evanmiller.org/ab-testing/
* https://exp-platform.com/ (Kohavi et al., experimentation research)
* https://www.statsmodels.org/stable/stats.html
