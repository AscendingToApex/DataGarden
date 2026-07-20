# 📗 Spreadsheets Reference Guide (Excel & Google Sheets)

> 🟢 **Level:** Beginner  ·  **Prerequisites:** none  ·  **Related:** [SQL DML](../../SQL/guides/data_manipulation_language_ref.md) · [Pandas](../../Python/guides/pandas_ref.md) · [Data Cleaning](../../Data_Wrangling/guides/data_cleaning_ref.md)

Spreadsheets are where most data analysis *starts* — and often where it ships. This guide covers the everyday toolkit for **Microsoft Excel** and **Google Sheets**: essential formulas, **lookups**, **conditional logic**, **pivot tables**, **cleaning text**, and **Power Query** — with notes on where the two tools differ.

> Excel vs. Sheets: ~90% of formulas are identical. This guide flags the differences that matter; when nothing is noted, assume it works in both.

## 📚 Table of Contents

* [🧱 Spreadsheet Basics](#-spreadsheet-basics)
* [🔢 Everyday Formulas](#-everyday-formulas)
* [🔎 Lookups (VLOOKUP / XLOOKUP / INDEX-MATCH)](#-lookups-vlookup--xlookup--index-match)
* [🔀 Conditional Logic](#-conditional-logic)
* [🧮 Conditional Aggregation](#-conditional-aggregation)
* [🧹 Cleaning Text](#-cleaning-text)
* [📊 Pivot Tables](#-pivot-tables)
* [⚡ Power Query (Excel)](#-power-query-excel)
* [✅ Data Validation & Formatting](#-data-validation--formatting)
* [🆚 Excel vs. Google Sheets](#-excel-vs-google-sheets)
* [🧠 Common Functions](#-common-functions)
* [📚 Glossary](#-glossary)

---

## 🧱 Spreadsheet Basics

- A **cell** is referenced by column-letter + row-number: `A1`, `B7`.
- **References**: `A1` (relative — shifts when copied), `$A$1` (absolute — locked), `$A1` / `A$1` (mixed).
- A **range** spans cells: `A1:A10` (a column), `A1:D1` (a row), `A1:D10` (a block).
- Formulas start with `=`. Refer to whole columns as `A:A`.

> Pro Tip: Press **F4** (Excel) to cycle a reference through relative → absolute → mixed while editing a formula.

---

## 🔢 Everyday Formulas

```
=SUM(A1:A10)            ' total
=AVERAGE(A1:A10)        ' mean
=COUNT(A1:A10)          ' count numbers
=COUNTA(A1:A10)         ' count non-empty cells
=MIN(A1:A10)  =MAX(...) ' extremes
=ROUND(A1, 2)           ' round to 2 decimals
=TODAY()   =NOW()       ' current date / datetime
```

---

## 🔎 Lookups (VLOOKUP / XLOOKUP / INDEX-MATCH)

Look up a value in one column and return a matching value from another — the analyst's bread and butter.

```
' VLOOKUP — searches the FIRST column, returns a column to its right
=VLOOKUP(lookup_value, table_range, col_index, FALSE)   ' FALSE = exact match
=VLOOKUP("Widget", A2:D100, 3, FALSE)

' XLOOKUP — modern, flexible (Excel 365 & Google Sheets); can look left
=XLOOKUP(lookup_value, lookup_range, return_range, "Not found")

' INDEX + MATCH — the classic flexible combo (works everywhere)
=INDEX(return_range, MATCH(lookup_value, lookup_range, 0))
```

> Note: Prefer **XLOOKUP** (or **INDEX/MATCH**) over VLOOKUP — VLOOKUP breaks when columns are inserted and can't look to the left of the key.

---

## 🔀 Conditional Logic

```
=IF(A2>100, "High", "Low")
=IF(AND(A2>100, B2="Open"), "Escalate", "OK")
=IF(OR(A2="", B2=""), "Missing", "Complete")
=IFERROR(VLOOKUP(...), "Not found")     ' trap errors gracefully
=IFS(A2>=90,"A", A2>=80,"B", TRUE,"C")  ' multiple conditions
```

---

## 🧮 Conditional Aggregation

Sum/count/average only the rows that meet criteria — the spreadsheet version of SQL's `WHERE` + `GROUP BY`:

```
=SUMIF(range, ">100")
=SUMIFS(sum_range, crit_range1, "West", crit_range2, ">100")
=COUNTIF(range, "Open")
=COUNTIFS(range1, "West", range2, ">100")
=AVERAGEIF(range, "West", avg_range)
```

> Pro Tip: The `*IFS` versions (plural) let you stack multiple criteria — reach for them once you have more than one condition.

---

## 🧹 Cleaning Text

```
=TRIM(A2)                 ' remove extra spaces
=UPPER(A2)  =LOWER(A2)  =PROPER(A2)
=LEFT(A2,3)  =RIGHT(A2,4)  =MID(A2,2,5)
=LEN(A2)                  ' length
=SUBSTITUTE(A2,"-","")    ' replace text
=TEXTSPLIT(A2,",")        ' split into columns (Excel 365 / Sheets: SPLIT)
=CONCAT(A2," ",B2)  =TEXTJOIN(", ",TRUE,A2:A5)
```

> Note: For a one-time cleanup, Excel's **Data → Text to Columns** and both tools' **Find & Replace** are faster than formulas.

---

## 📊 Pivot Tables

The single most powerful analysis tool in a spreadsheet — drag-and-drop `GROUP BY`.

1. Select your data range (with headers).
2. **Excel:** Insert → PivotTable. **Sheets:** Insert → Pivot table.
3. Drag fields into four zones:
   - **Rows** — the categories to group by (e.g., Region)
   - **Columns** — a second grouping (e.g., Quarter)
   - **Values** — the number to aggregate (Sum, Count, Average…)
   - **Filters** — slice the whole table
4. Change a value field's aggregation (Sum → Average/Count) in its settings.

> Pro Tip: Keep source data **tidy** — one row per record, one column per variable, no blank rows — and pivot tables just work.

---

## ⚡ Power Query (Excel)

**Power Query** (Excel's *Get & Transform*) is a repeatable ETL tool — import, clean, and reshape data with steps you can refresh with one click.

- **Data → Get Data** to connect to files, folders, databases, or the web.
- Each transform (remove columns, filter, split, unpivot, merge) is a recorded **step**.
- **Refresh** re-runs every step on new data — no manual re-work.

> Note: Power Query is the spreadsheet gateway to real data pipelines. Google Sheets' rough equivalents are **IMPORTRANGE**, **QUERY**, and connected sheets.

---

## ✅ Data Validation & Formatting

- **Data Validation** — restrict a cell to a list, number range, or date (dropdowns, guardrails).
- **Conditional Formatting** — color cells by rules (highlight duplicates, heat-map values, flag outliers).
- **Freeze Panes / Freeze rows** — keep headers visible while scrolling.
- **Tables** (Excel: Ctrl+T) — structured ranges with auto-expanding formulas and named references.

---

## 🆚 Excel vs. Google Sheets

| Feature | Excel | Google Sheets |
|---------|-------|---------------|
| Collaboration | OneDrive/365 co-editing | Real-time, built-in |
| Scale | Millions of rows, faster | Slower on large data |
| ETL | Power Query | `QUERY`, `IMPORTRANGE`, connected sheets |
| Automation | VBA / Office Scripts | Apps Script (JavaScript) |
| Unique functions | `XLOOKUP`, `LAMBDA` | `QUERY`, `ARRAYFORMULA`, `IMPORTRANGE` |

> Pro Tip: Google Sheets' `=QUERY(range, "SELECT A, SUM(C) GROUP BY A")` brings SQL-like power right into a cell — great practice for the real SQL guides.

---

## 🧠 Common Functions

| Function | Purpose |
|----------|---------|
| `SUM/AVERAGE/COUNT` | Aggregate |
| `VLOOKUP/XLOOKUP/INDEX-MATCH` | Look up matching values |
| `IF/IFS/IFERROR` | Conditional logic |
| `SUMIFS/COUNTIFS` | Conditional aggregation |
| `TRIM/PROPER/SUBSTITUTE` | Clean text |
| `TEXTSPLIT/TEXTJOIN` | Split / combine text |
| `UNIQUE/SORT/FILTER` | Dynamic arrays |

---

## 📚 Glossary

| Term | Definition | When it matters |
|------|------------|-----------------|
| Absolute reference | `$A$1` — locked when copied | Reusing a constant/rate |
| Pivot table | Drag-and-drop grouping & aggregation | Summarizing data |
| Power Query | Excel's refreshable ETL tool | Repeatable cleaning |
| Dynamic array | Formula that spills into many cells | `UNIQUE`, `FILTER`, `SORT` |
| Tidy data | One row/record, one column/variable | Making pivots reliable |

---

🧠 **Pro Tips:**
* Keep raw data on its own tidy sheet; do analysis on separate sheets so you never overwrite the source.
* Learn **pivot tables** and **XLOOKUP/INDEX-MATCH** first — they cover the majority of analyst tasks.
* When a spreadsheet gets slow or repetitive, that's your signal to graduate to **SQL** or **Pandas**.

🔗 Helpful Links:
* https://support.microsoft.com/excel
* https://support.google.com/docs/topic/9054603
* https://exceljet.net/
