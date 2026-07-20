# 🔀 SQL Dialect Portability Reference Guide

> 🟡 **Level:** Intermediate  ·  **Prerequisites:** [SQL DML basics](data_manipulation_language_ref.md)  ·  **Related:** [DDL](data_definition_language_ref.md) · [Spreadsheets QUERY](../../Spreadsheets/guides/spreadsheets_ref.md)

The DataGarden SQL guides are written for **Microsoft SQL Server (T-SQL)**, but analysts hop between engines — **PostgreSQL, MySQL, BigQuery, Snowflake, SQLite**. Core SQL (`SELECT/FROM/WHERE/GROUP BY/HAVING/ORDER BY/JOIN`) is identical everywhere; this guide maps the pieces that **differ** so you can move between them confidently.

> Rule of thumb: the query *logic* is portable; the *functions and limit syntax* are what change.

## 📚 Table of Contents

* [🚦 Limiting Rows](#-limiting-rows)
* [🔗 String Operations](#-string-operations)
* [📅 Dates & Times](#-dates--times)
* [❓ NULL Handling](#-null-handling)
* [🔠 Data Types](#-data-types)
* [🧩 Identifiers & Quoting](#-identifiers--quoting)
* [🪄 Other Common Differences](#-other-common-differences)
* [🧠 Quick Translation Table](#-quick-translation-table)
* [📚 Glossary](#-glossary)

---

## 🚦 Limiting Rows

The most common portability gotcha:

| Engine | Syntax |
|--------|--------|
| SQL Server | `SELECT TOP 10 * FROM t ORDER BY c` |
| PostgreSQL / MySQL / SQLite | `SELECT * FROM t ORDER BY c LIMIT 10` |
| Standard SQL / all modern | `... ORDER BY c OFFSET 0 ROWS FETCH NEXT 10 ROWS ONLY` |

> Note: `LIMIT 10 OFFSET 20` (Postgres/MySQL) skips 20 then returns 10 — the portable equivalent of T-SQL's `OFFSET ... FETCH`.

---

## 🔗 String Operations

| Task | SQL Server | PostgreSQL | MySQL |
|------|-----------|------------|-------|
| Concatenate | `a + b` or `CONCAT(a,b)` | `a \|\| b` or `CONCAT(a,b)` | `CONCAT(a,b)` |
| Length | `LEN(s)` | `LENGTH(s)` | `LENGTH(s)` / `CHAR_LENGTH(s)` |
| Substring | `SUBSTRING(s,1,3)` | `SUBSTRING(s FROM 1 FOR 3)` | `SUBSTRING(s,1,3)` |
| Upper/lower | `UPPER/LOWER` | `UPPER/LOWER` | `UPPER/LOWER` |

> Note: `+` for concatenation is **SQL Server only**. `||` is the ANSI standard (Postgres, SQLite, Oracle). `CONCAT()` is the safest cross-engine choice.

---

## 📅 Dates & Times

| Task | SQL Server | PostgreSQL | MySQL |
|------|-----------|------------|-------|
| Current timestamp | `GETDATE()` | `NOW()` / `CURRENT_TIMESTAMP` | `NOW()` |
| Add interval | `DATEADD(day,7,d)` | `d + INTERVAL '7 day'` | `DATE_ADD(d, INTERVAL 7 DAY)` |
| Difference | `DATEDIFF(day,a,b)` | `b - a` (days) / `AGE(b,a)` | `DATEDIFF(b,a)` |
| Extract part | `DATEPART(year,d)` / `YEAR(d)` | `EXTRACT(YEAR FROM d)` | `YEAR(d)` / `EXTRACT(...)` |
| Format | `FORMAT(d,'yyyy-MM-dd')` | `TO_CHAR(d,'YYYY-MM-DD')` | `DATE_FORMAT(d,'%Y-%m-%d')` |

---

## ❓ NULL Handling

| Task | SQL Server | PostgreSQL / Standard | MySQL |
|------|-----------|-----------------------|-------|
| Replace NULL | `ISNULL(x, 0)` | `COALESCE(x, 0)` | `IFNULL(x,0)` / `COALESCE` |
| First non-null | `COALESCE(a,b,c)` | `COALESCE(a,b,c)` | `COALESCE(a,b,c)` |

> Pro Tip: **`COALESCE`** is ANSI-standard and works everywhere — prefer it over `ISNULL`/`IFNULL` for portable code.

---

## 🔠 Data Types

| Concept | SQL Server | PostgreSQL | MySQL |
|---------|-----------|------------|-------|
| Auto-increment | `IDENTITY(1,1)` | `SERIAL` / `GENERATED ... AS IDENTITY` | `AUTO_INCREMENT` |
| Variable string | `VARCHAR(n)` / `NVARCHAR(n)` | `VARCHAR(n)` / `TEXT` | `VARCHAR(n)` / `TEXT` |
| Boolean | `BIT` | `BOOLEAN` | `TINYINT(1)` / `BOOLEAN` |
| Cast | `CAST(x AS INT)` / `CONVERT` | `CAST(x AS INT)` / `x::INT` | `CAST(x AS SIGNED)` |

---

## 🧩 Identifiers & Quoting

| Engine | Quote identifiers with | String literals |
|--------|-----------------------|-----------------|
| SQL Server | `[Order Details]` | `'text'` |
| PostgreSQL / Standard | `"Order Details"` | `'text'` |
| MySQL | `` `Order Details` `` (backticks) | `'text'` |

> Note: Double quotes mean an **identifier** in standard SQL, but a **string** in MySQL's default mode — a classic cross-engine bug.

---

## 🪄 Other Common Differences

- **Case sensitivity:** identifiers are case-insensitive in SQL Server/MySQL (Windows) but PostgreSQL folds unquoted names to lowercase.
- **`SELECT` without `FROM`:** `SELECT 1+1` works in most engines; Oracle needs `FROM DUAL`.
- **Temp tables:** `#temp` (SQL Server) vs. `CREATE TEMP TABLE` (Postgres) vs. `CREATE TEMPORARY TABLE` (MySQL).
- **Cloud warehouses** (BigQuery, Snowflake, Redshift) are mostly ANSI-standard: use `LIMIT`, `||`/`CONCAT`, `COALESCE`, and `EXTRACT`. BigQuery uses backticks for `` `project.dataset.table` ``.

---

## 🧠 Quick Translation Table

| Need | Portable / ANSI choice |
|------|------------------------|
| Limit rows | `LIMIT n` (or `FETCH NEXT n ROWS ONLY`) |
| Concatenate | `CONCAT(a, b)` |
| Replace NULL | `COALESCE(x, default)` |
| Current time | `CURRENT_TIMESTAMP` |
| Extract date part | `EXTRACT(YEAR FROM d)` |
| Cast | `CAST(x AS type)` |

---

## 📚 Glossary

| Term | Definition | When it matters |
|------|------------|-----------------|
| Dialect | An engine's specific SQL variant | Moving between databases |
| ANSI SQL | The cross-engine standard | Writing portable queries |
| T-SQL | Microsoft SQL Server's dialect | The DataGarden SQL guides |
| Warehouse | Analytics DB (BigQuery, Snowflake…) | Modern analyst work |

---

🧠 **Pro Tips:**
* Write to the **ANSI standard** by default (`LIMIT`, `COALESCE`, `CONCAT`, `EXTRACT`) — it ports the furthest.
* When a query fails on a new engine, suspect **row-limiting, string concat, or date functions** first.
* Keep the engine's official function reference bookmarked — that's where the differences live.

🔗 Helpful Links:
* https://www.postgresql.org/docs/current/functions.html
* https://dev.mysql.com/doc/refman/8.0/en/functions.html
* https://learn.microsoft.com/en-us/sql/t-sql/functions/functions
