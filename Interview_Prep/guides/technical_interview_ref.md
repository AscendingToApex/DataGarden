# 🎓 Technical Interview Prep Reference Guide

> 🟡 **Level:** Intermediate  ·  **Prerequisites:** [SQL DML](../../SQL/guides/data_manipulation_language_ref.md), [Hypothesis Testing](../../Statistics/guides/hypothesis_testing_ref.md)

A study companion for **data science / analytics** technical interviews, covering the three areas that come up most: **SQL**, **statistics**, and **probability**. Each section has worked concept questions plus a **practice bank** to test yourself.

> How to use this: read the worked answers to refresh concepts, then cover the practice-bank answers and try them cold.

## 📚 Table of Contents

* [🗄️ SQL Concepts](#-sql-concepts)
* [🗄️ SQL Query Challenges](#-sql-query-challenges)
* [📊 Statistics Concepts](#-statistics-concepts)
* [📊 Statistics Practice Bank](#-statistics-practice-bank)
* [🎲 Probability — Worked Problems](#-probability--worked-problems)
* [🎲 Probability Practice Bank](#-probability-practice-bank)
* [📚 Glossary](#-glossary)

---

## 🗄️ SQL Concepts

**What is a view?**
A **view** is a virtual table representing the result of a `SELECT`. It doesn't store data — it re-runs the query each time it's referenced — and it simplifies complex queries by encapsulating them into a single reusable object.

**Are SQL tables dynamic or static?**
**Static** — a fixed structure with a set number of columns and defined data types. Data persists and only changes when a user/app updates it.

**Primary key vs. foreign key**
- **Primary key** — unique identifier for each row; enforces *entity* integrity.
- **Foreign key** — links two tables; enforces *referential* integrity.

**INNER JOIN vs. LEFT JOIN**
- **INNER JOIN** — only rows where the join condition matches in both tables.
- **LEFT JOIN** — all rows from the left table, plus matching rows from the right (NULLs where no match).

**WHERE vs. HAVING**
- **WHERE** — filters rows *before* aggregation.
- **HAVING** — filters groups *after* aggregation (works on aggregate values).

**When would you use a subquery?**
When you need data from one table based on conditions in another, want one query's result as input to another, or want to break a complex query into readable parts. *Prefer CTEs for readability.*

**How would you speed up a slow query?**
- **Indexing** frequently-searched columns.
- **Efficient JOINs** — prefer `INNER` over `OUTER` where possible; avoid unnecessary joins.
- **Simplify** — drop unneeded columns, aggregates, and subqueries.
- **Good schema design** — normalized tables, proper relationships.
- **Appropriate data types** — smaller types = less data to scan.

---

## 🗄️ SQL Query Challenges

**Candidates with ALL required skills (Python, Tableau, PostgreSQL):**
```sql
SELECT candidate_id
FROM candidates
WHERE skill IN ('Python', 'Tableau', 'PostgreSQL')
GROUP BY candidate_id
HAVING COUNT(skill) = 3
ORDER BY candidate_id ASC;
```

**Pages with zero likes (anti-join):**
```sql
SELECT P.page_id
FROM pages AS P
LEFT JOIN page_likes AS PL ON P.page_id = PL.page_id
WHERE PL.page_id IS NULL
ORDER BY P.page_id ASC;
```

**Parts started but not finished:**
```sql
SELECT part
FROM parts_assembly
WHERE finish_date IS NULL
GROUP BY part;
```

**Laptop vs. mobile viewership (conditional aggregation):**
```sql
SELECT
  SUM(CASE WHEN device_type = 'laptop' THEN 1 ELSE 0 END) AS laptop_views,
  SUM(CASE WHEN device_type IN ('tablet', 'phone') THEN 1 ELSE 0 END) AS mobile_views
FROM viewership;
```

> Pro Tip: `COUNT(...) HAVING = N` for "has all N", `LEFT JOIN ... WHERE right IS NULL` for "has none", and `SUM(CASE WHEN ...)` for pivot-style counts are three patterns worth memorizing.

---

## 📊 Statistics Concepts

**Standard deviation vs. variance**
Variance is the average of squared deviations from the mean; standard deviation is its square root, so it's in the *same units* as the data — more interpretable.

**Explain a confidence interval to a non-technical audience**
A range likely to contain the true population value with a certain confidence (e.g., 95%). *"If we measured a sample of students' heights and got a 95% CI of 60–64 inches, we're 95% confident the true average of all students falls in that range."*

**Explain p-values in plain terms**
A measure of evidence against the null hypothesis. It's the probability of seeing results as extreme as yours *if the null were true*. Smaller p-value → stronger evidence against the null. Below the threshold (often 0.05) → statistically significant.

**Correlated predictors in multiple linear regression**
This is **multicollinearity** — it makes coefficients unstable and hard to interpret, and can inflate significance and cause overfitting. Fixes: (1) **variable selection** (drop one correlated predictor / stepwise), (2) **PCA** into uncorrelated components, (3) **regularization** (Ridge/Lasso), (4) inspect the **correlation matrix**.

**Statistical power**
The probability of correctly rejecting a false null (avoiding a Type II error). Increases with larger sample size, larger effect size, or a higher significance level. Used to determine the sample size needed to detect a given effect.

**A/B testing & common pitfalls**
Randomly assign subjects to treatment A or B and compare outcomes. Pitfalls: too-small **sample size**, uncontrolled **confounding variables**, **multiple comparisons** inflating false positives, **data biases** from sampling/measurement, and **testing too many variables** at once.

---

## 📊 Statistics Practice Bank

Try these cold (common at FAANG / quant interviews):

- Derive a confidence interval from a series of coin tosses.
- Estimate λ for an exponential lifetime model given *n* customers' histories.
- Derive the mean and variance of Uniform(a, b).
- E[min(X, Y)] for X, Y ~ Uniform(0, 1).
- Best estimate of *d* after sampling Uniform[0, d] *n* times.
- Expected days until N(0,1) draws exceed 2.
- Difference between **MLE and MAP** (mathematically).
- Blend the mean & standard deviation of two (then K) subsets.
- Sample a point uniformly from a unit circle.
- Turn Bernoulli trials into a normal-distributed sample.

---

## 🎲 Probability — Worked Problems

**Disease test (Bayes' rule):** 1/1000 have a disease; test is 98% correct if you have it, 1% false-positive if you don't. P(disease | positive)?
$$P(A\mid B)=\frac{P(B\mid A)P(A)}{P(B\mid A)P(A)+P(B\mid A')P(A')}=\frac{0.98(0.001)}{0.98(0.001)+0.01(0.999)}\approx 8.93\%$$
The takeaway: even an accurate test yields a low positive predictive value when the base rate is tiny.

**10 flips, 1 head — fair coin?** With n=10 you can't use the CLT/normal approximation, so compute exactly. Number of ways to get exactly 1 head = 10, total outcomes = 2¹⁰ = 1024:
$$p\text{-value}=\frac{10}{1024}\approx 0.0098 < 0.05 \Rightarrow \text{reject } H_0$$

**HH vs. TH game.** Toss until HH (you win) or TH (friend wins). Because *any* T before the final H guarantees "TH" appears first, HH only wins if the first two tosses are HH → the probability of winning works out to **2/3**.

---

## 🎲 Probability Practice Bank

- P(a 7-game series goes to 7 games)?
- Diligent-rater Bayes problem (4 "good" labels).
- Two random chords in a circle — P(they intersect)?
- 50 cards, 5 colors × 10 numbers — P(two picks differ in color *and* number)?
- Expected number of rolls to see all 6 die faces.
- Expected coin flips to get two consecutive heads.
- Expected cards drawn before the first ace.
- Generate fair odds from an unfair coin.
- Three friends say it's rainy (each lies w.p. 1/3; prior rain 0.25) — P(rainy)?

---

## 📚 Glossary

| Term | Definition | When it matters |
|------|------------|-----------------|
| View | Virtual table from a saved query | Simplifying SQL |
| Anti-join | Find rows with *no* match (`LEFT JOIN ... IS NULL`) | "Has none" queries |
| Multicollinearity | Correlated predictors in regression | Unstable coefficients |
| Statistical power | P(detecting a real effect) | Sample-size planning |
| Base rate | Underlying prevalence of an event | Bayes / test accuracy |
| p-value | Evidence against the null | Significance decisions |

---

🧠 **Pro Tips:**
* For SQL, **talk through the join logic** before writing — interviewers want your reasoning.
* For stats, always translate the concept into a **plain-language example**.
* For probability, name the tool first (**Bayes**, complement, linearity of expectation), then compute.

🔗 Helpful Links:
* https://www.stratascratch.com/ (SQL & Python practice)
* https://www.nicksingh.com/posts/40-probability-statistics-data-science-interview-questions-asked-by-fang-wall-street
* https://mode.com/sql-tutorial/
