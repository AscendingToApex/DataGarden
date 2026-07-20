# 🎨 Dashboard Design & Data Storytelling Reference Guide

> 🟡 **Level:** Intermediate  ·  **Prerequisites:** [Data Literacy](../../Data_Literacy/guides/data_literacy_ref.md)  ·  **Related:** [Power BI](power_bi_ref.md) · [Matplotlib](matplotlib_ref.md) · [Seaborn](seaborn_ref.md)

A chart shows a number; a **dashboard tells a story** and a **narrative drives a decision**. This guide covers choosing the right chart, designing dashboards that people actually use, the principles of visual clarity, and how to structure an insight so stakeholders *act* on it.

> The goal of every visual is not to display data — it's to help someone **make a decision**.

## 📚 Table of Contents

* [📈 Choosing the Right Chart](#-choosing-the-right-chart)
* [🎯 Design Principles](#-design-principles)
* [🖥️ Dashboard Layout](#-dashboard-layout)
* [🌈 Color & Accessibility](#-color--accessibility)
* [🏷️ Labeling & Context](#-labeling--context)
* [📖 Data Storytelling](#-data-storytelling)
* [🚫 Common Pitfalls](#-common-pitfalls)
* [✅ Pre-Ship Checklist](#-pre-ship-checklist)
* [📚 Glossary](#-glossary)

---

## 📈 Choosing the Right Chart

Start from the **question**, not the chart type:

| You want to show… | Use | Avoid |
|-------------------|-----|-------|
| Comparison across categories | Bar chart | Pie (hard to compare) |
| Change over time | Line chart | Many-slice pie |
| Part-to-whole | Stacked bar, treemap | 3-D pie |
| Relationship between two variables | Scatter plot | — |
| Distribution of one variable | Histogram, box plot | — |
| A single key number | Big-number KPI tile | Gauge clutter |
| Geographic pattern | Map (choropleth) | Table of regions |

> Pro Tip: When in doubt, a **bar chart** is almost always clearer than a pie chart. Reserve pies for 2–3 slices at most.

---

## 🎯 Design Principles

- **Maximize the data-ink ratio** (Tufte) — remove anything that isn't conveying data: heavy gridlines, borders, 3-D effects, background images.
- **One message per chart** — if a chart needs a paragraph to explain, split it.
- **Start bar/area axes at zero** — truncated axes exaggerate differences and mislead.
- **Order intentionally** — sort bars by value (not alphabetically) unless the category has a natural order.
- **Direct labeling** beats a legend the eye has to hunt through.

---

## 🖥️ Dashboard Layout

- **Follow the reading path:** most important number **top-left**, supporting detail below/right (Western readers scan in a Z / F pattern).
- **Inverted pyramid:** headline KPIs → trends → granular breakdowns → raw detail.
- **Group related visuals** and leave whitespace between groups.
- **5–9 visuals max** per view — beyond that, split into tabs/pages.
- **Consistent everything** — same colors for the same categories, same date ranges, same number formats across every tile.

> Note: A dashboard is a *product*. Ask "what decision does the viewer need to make?" and design backward from that.

---

## 🌈 Color & Accessibility

- Use a **limited palette** — one accent color for "look here," neutral grays for context.
- **Color has meaning** — pick sequential palettes for magnitude, diverging for above/below a midpoint, categorical for unordered groups (see the [Seaborn guide](seaborn_ref.md)).
- **Don't rely on color alone** — ~8% of men have color-vision deficiency. Add labels, patterns, or position. Avoid red/green as the only distinction.
- Keep **sufficient contrast** between text and background.

---

## 🏷️ Labeling & Context

Every chart needs enough context to stand alone:

- A **descriptive title that states the takeaway** ("Sales fell 12% in Q3" beats "Sales by Quarter").
- **Axis labels and units** (%, $, thousands).
- A **reference point** — target line, prior period, or benchmark — so a number means something.
- **Source and as-of date**, so viewers trust and can reproduce it.

---

## 📖 Data Storytelling

Turn analysis into action with a simple narrative arc:

1. **Context** — what's the situation and why should the viewer care?
2. **Conflict / insight** — what changed, what's surprising, what's the problem?
3. **Resolution** — the recommended action and expected impact.

Structure the *delivery* like a news article — **BLUF (Bottom Line Up Front)**: lead with the answer, then support it. Executives read the headline; analysts read the appendix.

> Pro Tip: State the **"so what"** explicitly. "Churn rose to 8%" is a fact; "Churn rose to 8% — we should prioritize the onboarding fix" is a story that drives a decision.

---

## 🚫 Common Pitfalls

- **Truncated axes** that exaggerate change.
- **Dual axes** that imply a correlation that isn't there.
- **Too many colors** — the rainbow dashboard.
- **Vanity metrics** with no decision attached.
- **Overplotting** — thousands of scatter points as a solid blob (use transparency or aggregation).
- **Precision theater** — "42.7194%" when "43%" is all anyone needs.

---

## ✅ Pre-Ship Checklist

- [ ] Each chart answers one clear question
- [ ] Titles state the takeaway, not just the topic
- [ ] Axes labeled, units shown, bar/area axes start at zero
- [ ] Consistent colors/formats across all tiles
- [ ] Works for color-blind viewers (not color-only)
- [ ] A reference/benchmark gives each number meaning
- [ ] Source and as-of date present
- [ ] The recommended action / "so what" is explicit

---

## 📚 Glossary

| Term | Definition | When it matters |
|------|------------|-----------------|
| Data-ink ratio | Share of "ink" that shows real data | Removing clutter |
| KPI | Key Performance Indicator | Headline metrics |
| BLUF | Bottom Line Up Front | Structuring insights |
| Choropleth | Map shaded by a value | Geographic data |
| Diverging palette | Colors emphasizing a midpoint | Above/below target |

---

🧠 **Pro Tips:**
* Design **backward from the decision** the viewer must make.
* Put the **takeaway in the title** and the **action in the summary**.
* Less is more — remove a color, a gridline, and a decimal place, and clarity goes up.

🔗 Helpful Links:
* https://www.storytellingwithdata.com/
* https://www.tableau.com/learn/articles/data-visualization
* https://material.io/design/communication/data-visualization.html
