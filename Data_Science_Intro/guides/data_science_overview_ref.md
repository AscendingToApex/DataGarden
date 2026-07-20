# 🌐 Data Science Overview Reference Guide

A big-picture introduction to **what data science is** and **how data science work actually gets done** — the interdisciplinary skill set, the end-to-end process, the analytics maturity path, how to choose projects, and two classic frameworks (**Tom Khabaza's Nine Laws** and **CRISP-DM**).

> Data science is inherently **interdisciplinary** — take away domain knowledge, computer science, *or* statistics, and the rest falls apart.

## 📚 Table of Contents

* [🤔 What Is Data Science?](#-what-is-data-science)
* [🧩 The Three Pillars](#-the-three-pillars)
* [🔄 The Data Science Process](#-the-data-science-process)
* [📈 The Analytics Maturity Path](#-the-analytics-maturity-path)
* [❓ Types of Analytics Questions](#-types-of-analytics-questions)
* [💼 Choosing Projects Strategically](#-choosing-projects-strategically)
* [⚖️ Khabaza's Nine Laws of Data Mining](#-khabazas-nine-laws-of-data-mining)
* [🔁 CRISP-DM Lifecycle](#-crisp-dm-lifecycle)
* [📚 Glossary](#-glossary)

---

## 🤔 What Is Data Science?

A few complementary definitions:

- *"The cross-disciplinary set of skills that are becoming increasingly important in many applications across industry and academia."* — Jake VanderPlas
- *"Using data to achieve specified goals by designing or applying computational methods for inference or prediction."* — Fayyad & Hamutcu

---

## 🧩 The Three Pillars

Data science sits at the intersection of three areas — and **domain knowledge** ties them together:

| Pillar | Why it matters |
|--------|----------------|
| **Statistics** | Overlaps heavily with what data scientists do — rigor and inference |
| **Computer Science** | The programming/engineering base to work with data at scale |
| **Data Visualization / Communication** | Turning technical findings into something non-technical audiences can act on |

> Note: Without **domain knowledge**, even strong stats and code produce answers to the wrong questions.

---

## 🔄 The Data Science Process

A repeatable pipeline (from *Introducing Data Science*):

1. **Set the research goal** — define the goal and create a project charter.
2. **Retrieve data** — internal (with ownership/access sorted) and external sources.
3. **Prepare data** — clean (entry errors, impossible values, missing values, outliers, typos), transform (aggregate, derive measures, dummies, reduce variables), and combine (merge/join, set operators, views).
4. **Explore data** — simple and combined graphs, link-and-brush, non-graphical techniques.
5. **Model data** — model/variable selection, execution, diagnostics, and comparison.
6. **Present & automate** — communicate results and automate the analysis.

> Pro Tip: **Data preparation is more than half** of most projects — budget your time accordingly.

---

## 📈 The Analytics Maturity Path

Organizations climb this ladder from hindsight to foresight:

| # | Stage | Question it answers |
|---|-------|---------------------|
| 1 | Standard Report | What happened? |
| 2 | Ad-hoc Reports | How many, how often, where? |
| 3 | Query Drilldown | Where exactly is the problem? |
| 4 | Alerts | What actions are needed? |
| 5 | Statistical Analysis | Why is this happening? |
| 6 | Forecasting | What if these trends continue? |
| 7 | Predictive Modeling | What will happen next? |
| 8 | Optimization | What's the best that can happen? |

---

## ❓ Types of Analytics Questions

| Classification | Method | Question |
|----------------|--------|----------|
| **Describe** | Standard / Ad-hoc reporting | What happened? How many, how often, where? |
| **Explore** | Query/drilldown, visualization, clustering | Where's the problem? What groupings exist? |
| **Explain** | Correlation, inference, causal | What's related? What can a sample tell me? What causes this? |
| **Predict** | Forecasting, predictive modeling, alerts/scores | What's the trend? What will happen? Which predictions prompt action? |
| **Prescribe** | Optimization, optimization under uncertainty | How do we achieve the best outcome (with variability)? |

---

## 💼 Choosing Projects Strategically

- Projects typically run **4–6 months** from concept to pre-deployment.
- The **best first project is not the easiest** — low-hanging fruit worth less than a team member's salary is rarely worth it and is never as easy as it looks. Weigh **potential payoff**.
- Aim to **clear seven figures** after project expenses; treat the data science team as a **profit center**, not a cost center.
- Keep **5+ projects in the queue**, ranked by ROI, and **re-vet/re-sequence quarterly**.

> Note: It usually takes ~three projects to hit a good rhythm — as a data steward, then an active data scientist, then leading a project.

---

## ⚖️ Khabaza's Nine Laws of Data Mining

1. **Business objectives** are the origin of every data mining solution.
2. **Business knowledge** is central to every step.
3. **Data preparation** is more than half of every process.
4. The right model can only be found by **experiment** (No Free Lunch).
5. There are **always patterns** (Watkins' Law).
6. Data mining **amplifies perception** in the business domain.
7. Prediction increases information locally by **generalization**.
8. Value isn't determined by model accuracy alone — it's found in **more effective action** and improved strategy.
9. **All patterns are subject to change** — data mining is never once-and-done.

---

## 🔁 CRISP-DM Lifecycle

The **Cross-Industry Standard Process for Data Mining** — the classic, iterative ML/analytics lifecycle:

1. **Business Understanding** — objectives, situation assessment, data-mining goals, project plan.
2. **Data Understanding** — identify sources, collect, describe, explore, verify quality (data dictionaries help).
3. **Data Preparation** — select, clean, construct, integrate, format.
4. **Modeling** — select techniques, design tests, build and assess models.
5. **Evaluation** — evaluate results, review the process, determine next steps.
6. **Deployment** — plan deployment, monitoring & maintenance; final report; project review.
7. **Monitoring** — continual evaluation and improvement.

> Pro Tip: CRISP-DM is a **loop**, not a line — you'll cycle back (e.g., new data understanding → more prep) throughout a project.

---

## 📚 Glossary

| Term | Definition | When it matters |
|------|------------|-----------------|
| CRISP-DM | Standard iterative data-mining lifecycle | Structuring any DS project |
| Analytics maturity | Progression from reporting to optimization | Assessing an org's capability |
| Project charter | Document defining a project's goal & scope | Kicking off work |
| Profit vs. cost center | Team that generates vs. consumes value | Justifying a DS team |
| Data dictionary | Reference describing each data field | Data understanding |

---

🧠 **Pro Tips:**
* Anchor every project to a **business objective** — that's law #1 for a reason.
* Expect to spend **most of your time on data prep**, not modeling.
* Value is measured by **better action**, not just model accuracy.

🔗 Helpful Links:
* https://www.datascience-pm.com/crisp-dm-2/
* https://jakevdp.github.io/PythonDataScienceHandbook/
* https://en.wikipedia.org/wiki/Cross-industry_standard_process_for_data_mining
