# 📊 Power BI & Data Analytics Reference Guide

> 🟡 **Level:** Intermediate  ·  **Prerequisites:** none

**Power BI** is Microsoft's suite for turning scattered data sources into interactive, shareable dashboards. This guide covers the **types of analytics**, the **roles** on a data team, the **six tasks** of a data analyst, and the **building blocks** and **workflow** of Power BI itself.

> Big idea: The value of data is unlocked by **telling a story** with it. Reports that tell that story help decision-makers act faster and more accurately.

## 📚 Table of Contents

* [🔎 What Is Data Analysis?](#-what-is-data-analysis)
* [🧠 The Five Types of Analytics](#-the-five-types-of-analytics)
* [👥 Roles on a Data Team](#-roles-on-a-data-team)
* [🛠️ The Six Tasks of a Data Analyst](#-the-six-tasks-of-a-data-analyst)
* [🧩 The Parts of Power BI](#-the-parts-of-power-bi)
* [🔄 The Flow of Work](#-the-flow-of-work)
* [🏗️ Building Blocks](#-building-blocks)
* [🔌 Connecting & Refreshing Data](#-connecting--refreshing-data)
* [🧠 Key Terms at a Glance](#-key-terms-at-a-glance)
* [📚 Glossary](#-glossary)

---

## 🔎 What Is Data Analysis?

Data analysis is the process of **identifying, cleaning, transforming, and modeling** data to discover meaningful, useful information — then crafting it into a **story** through reports that support decision-making.

---

## 🧠 The Five Types of Analytics

| Type            | Answers…                          | Example                                  |
|-----------------|-----------------------------------|------------------------------------------|
| **Descriptive** | What *happened*?                  | KPIs, ROI, dashboards of historical data |
| **Diagnostic**  | *Why* did it happen?              | Finding the cause of an anomaly          |
| **Predictive**  | What *will* happen?               | Forecasting future trends                |
| **Prescriptive**| What *should we do*?              | Recommending the next best action        |
| **Cognitive**   | What if circumstances change?     | Self-learning inferences from data       |

> Note: Diagnostic analytics generally go in three steps — (1) spot anomalies, (2) gather related data, (3) use statistics to explain them.

---

## 👥 Roles on a Data Team

- **Business Analyst** — closest to the business; interprets the *output* of visualizations.
- **Data Analyst** — profiles, cleans, transforms, models data and builds reports/dashboards (the core Power BI role).
- **Data Engineer** — provisions data platforms; manages secure flow of structured/unstructured data across sources.
- **Data Scientist** — advanced analytics (descriptive → predictive), forms hypotheses/experiments; most time goes to data wrangling and feature engineering.
- **Database Administrator (DBA)** — manages availability, performance, backups, and security of the databases.

> Note: In many organizations the **data analyst** and **business analyst** work is done by the same person.

---

## 🛠️ The Six Tasks of a Data Analyst

1. **Prepare** — profile, clean, and transform raw data into trusted, understandable information (including privacy/security like anonymizing PII).
2. **Model** — define relationships between tables. A poor model is often the cause of slow reports and refreshes.
3. **Visualize** — pick the right visuals, colors, and fonts to tell a compelling, accessible story.
4. **Analyze** — find insights, patterns, and trends; predict outcomes and communicate them clearly.
5. **Manage** — oversee reports, dashboards, workspaces, and datasets; control sharing and security.
6. *(Ongoing)* reduce data silos by reusing shared, certified datasets.

> Pro Tip: If a report is slow or refreshes take forever, revisit **Prepare** and **Model** first — that's usually where the bottleneck lives.

---

## 🧩 The Parts of Power BI

- **Power BI Desktop** — the Windows app where you build reports.
- **Power BI Service** — the online SaaS where you publish, build dashboards, and share.
- **Power BI Mobile** — apps (Windows/iOS/Android) for viewing on the go.

---

## 🔄 The Flow of Work

1. Bring data into **Power BI Desktop** and create a report.
2. **Publish** to the Power BI Service; build dashboards there.
3. **Share** dashboards with others.
4. Others **view and interact** in Power BI Mobile.

---

## 🏗️ Building Blocks

| Block            | What it is                                                        |
|------------------|------------------------------------------------------------------|
| **Visualization**| A visual representation of data (chart, map, etc.)               |
| **Dataset**      | The collection of data (often combined from many sources)        |
| **Report**       | A collection of visualizations across one or more pages          |
| **Dashboard**    | A single-page collection of visuals shared with others           |
| **Tile**         | A single visualization on a dashboard                            |

> Note: A **dashboard** must fit on one page (the "canvas"); a **report** can span many pages. When a dashboard is shared *with* you, you can interact but not rearrange the tiles.

---

## 🔌 Connecting & Refreshing Data

- Use **Get Data** (lower-left of the Service home page) to connect to Excel, SQL Server, Azure, Oracle, and SaaS services (Salesforce, MailChimp, etc.) via built-in **connectors**.
- Many SaaS sources ship a ready-made **app** — a preset bundle of dashboards/reports for the whole organization.
- Keep data current with **Scheduled refresh** (Settings → Datasets → Scheduled refresh), or refresh immediately with the refresh icon.

---

## 🧠 Key Terms at a Glance

| Term       | Meaning                                                     |
|------------|-------------------------------------------------------------|
| Connector  | Built-in link to a data source                              |
| Canvas     | The blank backdrop where you place visuals                  |
| App        | Preset, ready-made visuals/reports shared org-wide          |
| Workspace  | A container for related reports, dashboards, and datasets   |
| Certified dataset | An endorsed, trusted dataset for reuse               |

---

## 📚 Glossary

| Term          | Definition                                                    | When it matters                    |
|---------------|---------------------------------------------------------------|------------------------------------|
| KPI           | Key Performance Indicator tracking an objective               | Descriptive analytics              |
| Data modeling | Defining relationships between tables                         | Report performance                 |
| EDA           | Exploratory Data Analysis                                     | Understanding data before modeling |
| Data silo     | Isolated data not shared across an org                        | Managing/reusing datasets          |
| Scheduled refresh | Automatic dataset update on a set timetable               | Keeping dashboards current         |

---

🧠 **Pro Tips:**
* A clean **data model** matters more for performance than fancy visuals.
* Design for the **story**: accessible colors, sensible fonts, the right visual for the data.
* Reuse **shared/certified datasets** to cut duplicated effort and reduce silos.

🔗 Helpful Links:
* https://learn.microsoft.com/en-us/power-bi/
* https://learn.microsoft.com/en-us/training/powerplatform/power-bi
* https://learn.microsoft.com/en-us/power-bi/fundamentals/desktop-getting-started
