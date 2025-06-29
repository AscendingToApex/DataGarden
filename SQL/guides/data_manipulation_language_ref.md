# 🧠 T-SQL Reference Guide

## 📚 Table of Contents

* [🛠 Getting Started with T-SQL](#-getting-started-with-t-sql)  
* [🛡️ Best Practices](#️-best-practices)  
* [📌 USE Statement](#-use-statement)  
* [🔍 SELECT Statement](#-select-statement)  
* [📖 FROM Clause](#-from-clause)  
* [🔎 WHERE Clause](#-where-clause)  
* [🗂️ GROUP BY Clause](#-group-by-clause)  
* [📏 HAVING Clause](#-having-clause)  
* [↕️ ORDER BY Clause](#-order-by-clause)  
* [🚦 TOP Filter](#-top-filter)  
* [⏭️ OFFSET-FETCH Filter](#-offset-fetch-filter)  
* [🔣 Predicates & Operators](#-predicates--operators)  
* [❓ NULLs](#-nulls)  
* [⚡ All-at-Once Operations](#-all-at-once-operations)  
* [🔠 Working with Character Data](#-working-with-character-data)  
* [📅 Working with Date & Time Data](#-working-with-date--time-data)  
* [🔀 CASE Expression](#-case-expression)  
* [🔀 Cross Joins](#-cross-joins)  
* [🔄 Self Cross Joins](#-self-cross-joins)  
* [🔢 Producing Tables of Numbers](#-producing-tables-of-numbers)  
* [🔗 Inner Joins](#-inner-joins)  
* [🛳️ Outer Joins](#-outer-joins)  
* [🏗️ Beyond Outer Joins](#-beyond-outer-joins)  
* [🧩 Composite Joins](#-composite-joins)  
* [⚖️ Non-Equi Joins](#-non-equi-joins)  
* [➕ Multi-Join Queries](#-multi-join-queries)  
* [🛠 Temporary Tables & CTEs](#-temporary-tables--ctes)  
* [⏳ Window Functions](#-window-functions)  
* [🧱 Creating & Modifying Tables](#-creating--modifying-tables)  
* [🔁 Stored Procedures & Functions](#-stored-procedures--functions)   
* [🗄️ Querying Metadata](#-querying-metadata)  
* [🧠 Common T-SQL Commands](#-common-t-sql-commands)  
* [📚 Glossary](#-glossary)  

---

## 🛠 Getting Started with T-SQL

1. Install and open SSMS or Azure Data Studio; connect to your SQL Server.  
2. Set your database context:
   ```sql
   USE TSQLV4;
   GO;
   ```
3. Run a quick test:
   ```sql
   SELECT TOP 5 name, create_date
     FROM sys.objects;
   ```

> Note: Verify permissions before executing scripts.

---

## 🛡️ Best Practices

- Terminate every statement with `;` for readability and future compatibility.  
- Always prefix columns with table aliases—even if unambiguous—for clarity.  
- Use parentheses and consistent indentation for complex logic.  
- Express dates/times as `'YYYYMMDD'` character strings.  
- Stick to ISO/ANSI SQL-92 syntax for portability.

> Pro Tip: Enforce naming conventions (schema, table, column) across your team.

---

## 📌 USE Statement

1. Begin scripts with `USE` to set context:
   ```sql
   USE TSQLV4;
   GO;
   ```
2. Ensures subsequent commands run against the intended database.

---

## 🔍 SELECT Statement

Retrieves and projects data. Aliases in `SELECT` aren’t visible to earlier clauses.

Logical processing order:  
1. FROM  
2. WHERE  
3. GROUP BY  
4. HAVING  
5. SELECT  
6. ORDER BY  

### Example
```sql
USE TSQLV4;
SELECT empid,
       YEAR(orderdate) AS orderyear,
       COUNT(*)      AS numorders
  FROM Sales.Orders
 WHERE custid = 71
 GROUP BY empid, YEAR(orderdate)
 HAVING COUNT(*) > 1
 ORDER BY empid, orderyear;
```

> Pro Tip: Use `DISTINCT` to remove duplicates:
> ```sql
> SELECT DISTINCT empid, YEAR(orderdate) AS orderyear
>   FROM Sales.Orders
>  WHERE custid = 71;
> ```

---

## 📖 FROM Clause

Specifies source tables and operators.

- Table references:
  - `Sales.OrderDetails`
  - `"Sales"."Order Details"`
  - `[Sales].[Order Details]`

> Note: Always qualify schema to avoid ambiguity.

---

## 🔎 WHERE Clause

Filters rows after `FROM`.

### Example
```sql
USE TSQLV4;
SELECT orderid, empid, orderdate, freight
  FROM Sales.Orders
 WHERE custid = 71;
```

> Pro Tip: Combine predicates with `AND`/`OR` for precise filtering.

---

## 🗂️ GROUP BY Clause

Groups rows for aggregation. Non-grouped columns must be aggregated.

- `COUNT(*)` counts all rows (including NULLs).  
- `COUNT(col)` ignores NULLs.  
- `COUNT(DISTINCT col)` counts unique non-NULLs.

### Example
```sql
USE TSQLV4;
SELECT empid,
       YEAR(orderdate) AS orderyear,
       SUM(freight)   AS totalfreight
  FROM Sales.Orders
 WHERE custid = 71
 GROUP BY empid, YEAR(orderdate);
```

---

## 📏 HAVING Clause

Filters groups based on aggregates.

### Example
```sql
USE TSQLV4;
SELECT empid,
       YEAR(orderdate) AS orderyear
  FROM Sales.Orders
 WHERE custid = 71
 GROUP BY empid, YEAR(orderdate)
 HAVING COUNT(*) > 1;
```

---

## ↕️ ORDER BY Clause

Sorts final output. Last in processing.

- Default `ASC`; specify `DESC` for descending.  
- With `DISTINCT`, you can only sort by selected columns.

### Example
```sql
USE TSQLV4;
SELECT empid, YEAR(orderdate) AS orderyear
  FROM Sales.Orders
 WHERE custid = 71
 GROUP BY empid, YEAR(orderdate)
 HAVING COUNT(*) > 1
 ORDER BY empid ASC, orderyear DESC;
```

---

## 🚦 TOP Filter

Limits row count or percent. Optional ties.

### Examples
```sql
SELECT TOP (5) orderid, orderdate FROM Sales.Orders ORDER BY orderdate DESC;
SELECT TOP (1) PERCENT orderid, orderdate FROM Sales.Orders ORDER BY orderdate DESC;
SELECT TOP (5) WITH TIES orderid, orderdate FROM Sales.Orders ORDER BY orderdate DESC;
```

> Note: `TOP` is non-standard and cannot skip rows.

---

## ⏭️ OFFSET-FETCH Filter

Standard, supports skipping. Requires `ORDER BY`.

### Example
```sql
SELECT orderid, orderdate
  FROM Sales.Orders
 ORDER BY orderdate, orderid
 OFFSET 50 ROWS FETCH NEXT 25 ROWS ONLY;
```

---

## 🔣 Predicates & Operators

Logical expressions yield TRUE/FALSE/UNKNOWN.

- Logical: `AND`, `OR`, `NOT`  
- Set: `IN`, `BETWEEN`, `LIKE` (use `N'…'` for Unicode)  
- Comparison: `=, >, <, >=, <=, <>`  
- Arithmetic: `+, -, *, /, %`

### Examples
```sql
SELECT orderid FROM Sales.Orders WHERE orderid IN (10248,10249,10250);
SELECT orderid FROM Sales.Orders WHERE orderid BETWEEN 10300 AND 10310;
SELECT empid, lastname FROM HR.Employees WHERE lastname LIKE N'D%';
SELECT CAST(col1 AS NUMERIC(12,2))/CAST(col2 AS NUMERIC(12,2)) AS ratio FROM dbo.MyTable;
```

Operator precedence (high→low):  
1. `()`  
2. `*`, `/`, `%`  
3. `+`, `-`  
4. Comparisons  
5. `NOT`  
6. `AND`  
7. `BETWEEN`, `IN`, `LIKE`, `OR`

---

## ❓ NULLs

1. Expressions on NULL yield UNKNOWN, not TRUE/FALSE.  
2. `NOT UNKNOWN` remains UNKNOWN.  
3. `NULL = NULL` evaluates to UNKNOWN.  
4. To include NULLs in filters, add `OR col IS NULL`.  
5. WHERE filters accept only TRUE; UNKNOWN rows are excluded.  
6. UNIQUE constraints in T-SQL treat two NULLs as equal—only one allowed.

> Pro Tip: Always explicitly test `IS NULL` or `IS NOT NULL` when needed.

---

## ⚡ All-at-Once Operations

1. SQL evaluates all expressions in the same logical phase simultaneously.  
2. You cannot reference a SELECT alias within the same SELECT clause.  
3. The optimizer chooses evaluation order; you can’t rely on short-circuit.

---

## 🔠 Working with Character Data

### Data Types
- Non-Unicode: `CHAR(n)`, `VARCHAR(n)`  
- Unicode: `NCHAR(n)`, `NVARCHAR(n)`

### Collation
```sql
SELECT name, description FROM sys.fn_helpcollations();
```
- On-prem: instance, database, column, expression.  
- Azure: database, column, expression.  
- Database collation sets metadata collation (object/column names).

### String Concatenation
```sql
SELECT empid, firstname + N' ' + lastname AS fullname FROM HR.Employees;
SELECT custid,
       country + COALESCE(N','+region, N'') + N',' + city AS location
  FROM Sales.Customers;
SELECT custid, CONCAT(country, ',', city) AS location FROM Sales.Customers;
```

> Pro Tip: Use `COALESCE` or `CONCAT` to handle NULLs gracefully.

---

## 📅 Working with Date & Time Data

### Data Types Overview

| Data Type       | Storage (bytes) | Date range                    | Accuracy             | Entry format              |
|-----------------|-----------------|-------------------------------|----------------------|---------------------------|
| DATETIME        | 8               | 1753-01-01 → 9999-12-31       | 3.33 ms              | YYYYMMDD hh:mm:ss.nnn     |
| SMALLDATETIME   | 4               | 1900-01-01 → 2079-06-06       | 1 minute             | YYYYMMDD hh:mm:          |
| DATE            | 3               | 0001-01-01 → 9999-12-31       | 1 day                | YYYY-MM-DD               |
| TIME            | 3–5             | N/A                           | 100 ns               | hh:mm:ss.nnnnnnn         |
| DATETIME2       | 6–8             | 0001-01-01 → 9999-12-31       | 100 ns               | YYYYMMDD hh:mm:ss.nnnnnnnn|
| DATETIMEOFFSET  | 8–10            | 0001-01-01 → 9999-12-31       | 100 ns               | YYYYMMDD hh:mm:ss.nnnnnnn(±)hh:mm |

> Pro Tip: Use `DATE` or `TIME` when only date or time is needed.

---

### Filtering Date Ranges

Avoid wrapping the column in functions so indexes can be used.

#### Example
```sql
SELECT orderid, custid, empid, orderdate
  FROM Sales.Orders
 WHERE orderdate >= '20150101'
   AND orderdate <  '20160101';
```

---

### Current Date & Time Functions

| Function             | Return Type     | Description                          |
|----------------------|-----------------|--------------------------------------|
| GETDATE()            | DATETIME        | Current date and time                |
| CURRENT_TIMESTAMP    | DATETIME        | ANSI-compliant same as GETDATE()     |
| GETUTCDATE()         | DATETIME        | Current UTC date and time            |
| SYSDATETIME()        | DATETIME2       | Current date and time                |
| SYSUTCDATETIME()     | DATETIME2       | Current UTC date and time            |
| SYSDATETIMEOFFSET()  | DATETIMEOFFSET  | Current date/time with UTC offset    |

#### Example
```sql
SELECT
  CAST(SYSDATETIME()       AS DATE) AS current_date,
  CAST(SYSDATETIME()       AS TIME) AS current_time;
```

---

### CAST, CONVERT, PARSE & TRY_ Functions

- `CAST(value AS type)` / `TRY_CAST(value AS type)`  
- `CONVERT(type, value[, style])` / `TRY_CONVERT(type, value[, style])`  
- `PARSE(value AS type [USING culture])` / `TRY_PARSE(value AS type [USING culture])`

> Pro Tip: Prefer `CAST` unless you need style or culture.

---

### SWITCHOFFSET

Adjusts a DATETIMEOFFSET to a target UTC offset.

#### Example
```sql
SELECT SWITCHOFFSET(SYSDATETIMEOFFSET(), '-05:00');
```

---

### TODATETIMEOFFSET

Combines a local datetime and offset into a DATETIMEOFFSET.

```sql
SELECT TODATETIMEOFFSET('2023-07-01 08:00:00', '+02:00');
```

---

### AT TIME ZONE

Converts a datetime to a DATETIMEOFFSET in a named time zone.

```sql
SELECT '2023-07-01 12:00:00' AT TIME ZONE 'Pacific Standard Time';
```

---

### DATEADD

Adds a number of date parts to a datetime.

#### Example
```sql
SELECT DATEADD(year, 1, '20210212');
```

---

### DATEDIFF & DATEDIFF_BIG

Calculates difference between two datetimes.

#### Example
```sql
SELECT DATEDIFF(day, '20150212','20160212');       -- 366
SELECT DATEDIFF_BIG(ms, '20200101','20200102');    -- uses BIGINT
```

---

### DATEPART / YEAR / MONTH / DAY

```sql
SELECT DATEPART(month, '20160212');    -- 2
SELECT YEAR('20160212');               -- 2016
SELECT MONTH('20160212');              -- 2
SELECT DAY('20160212');                -- 12
```

---

### DATENAME

Returns the name of the date part.

```sql
SELECT DATENAME(month, '20160212');    -- 'February'
```

---

### ISDATE

Tests if a string is a valid datetime.

```sql
SELECT ISDATE('2020-02-30');           -- 0
SELECT ISDATE('2020-02-29');           -- 1
```

---

### FROMPARTS

Builds date/time from parts.

```sql
SELECT DATEFROMPARTS(2023,7,1);  
SELECT DATETIMEFROMPARTS(2023,7,1,8,0,0,0);
SELECT DATETIMEOFFSETFROMPARTS(2023,7,1,8,0,0,0,'-05:00',7);
SELECT TIMEFROMPARTS(8,0,0,0,7);
```

---

### EOMONTH

Returns end-of-month date.

```sql
SELECT EOMONTH('2023-02-15');          -- '2023-02-28'
SELECT EOMONTH('2023-02-15', 1);       -- '2023-03-31'
```

---

## 🔀 CASE Expression

Returns a scalar based on conditions.

```sql
SELECT
  CASE
    WHEN score >= 90 THEN 'A'
    WHEN score >= 80 THEN 'B'
    ELSE 'C'
  END AS grade
  FROM Exams;
```
Shortcuts: `ISNULL`, `COALESCE`, `IIF(expr,val1,val2)`, `CHOOSE(idx,val1,val2,…)`.

---

## 🔀 Cross Joins

1. Cartesian product.  
2. Example:
   ```sql
   SELECT C.custid, E.empid
     FROM Sales.Customer AS C
   CROSS JOIN HR.Employees    AS E;
   ```

---

## 🔄 Self Cross Joins

1. Alias same table twice.  
2. Example:
   ```sql
   SELECT E1.empid, E2.empid
     FROM HR.Employees AS E1
   CROSS JOIN HR.Employees    AS E2;
   ```

---

## 🔢 Producing Tables of Numbers

1. Seed `Digits` (0–9).  
2. Triple cross-join to get 1–100:
   ```sql
   SELECT D3.digit*100 + D2.digit*10 + D1.digit +1 AS n
     FROM dbo.Digits AS D1
   CROSS JOIN dbo.Digits    AS D2
   CROSS JOIN dbo.Digits    AS D3
    ORDER BY n;
   ```

---

## 🔗 Inner Joins

1. Default join: product + filter.  
2. Example:
   ```sql
   SELECT E.empid, O.orderid
     FROM HR.Employees AS E
   JOIN Sales.Orders          AS O
     ON E.empid = O.empid;
   ```

---

## 🛳️ Outer Joins

1. Preserve unmatched rows with `LEFT/RIGHT/FULL [OUTER] JOIN`.  
2. Phases: product → filter → include outer rows as NULLs.

#### Example
```sql
SELECT C.custid, O.orderid
  FROM Sales.Customers AS C
LEFT JOIN Sales.Orders      AS O
  ON C.custid = O.custid;
```

---

## 🏗️ Beyond Outer Joins

### Missing Values
```sql
SELECT DATEADD(day,n-1,'20140101') AS orderdate,
       O.orderid
  FROM dbo.Nums AS N
LEFT JOIN Sales.Orders    AS O
  ON DATEADD(day,N.n-1,'20140101')=O.orderdate
 WHERE N.n<=DATEDIFF(day,'20140101','20161231')+1
 ORDER BY orderdate;
```

### Filtering & Multi-Join Effects
- `WHERE` on non-preserved side drops outer rows.  
- Inner/right after outer on non-preserved side removes outer rows.  
- `COUNT(*)` counts outer rows; use `COUNT(col)` to ignore NULLs.

---

## 🧩 Composite Joins

```sql
SELECT *
  FROM Table1 AS T1
JOIN Table2        AS T2
  ON T1.col1 = T2.col1
 AND T1.col2 = T2.col2;
```

---

## ⚖️ Non-Equi Joins

```sql
SELECT E1.empid, E2.empid
  FROM HR.Employees AS E1
JOIN HR.Employees    AS E2
  ON E1.empid < E2.empid;
```

---

## ➕ Multi-Join Queries

```sql
SELECT C.custid, O.orderid, OD.productid
  FROM Sales.Customers     AS C
JOIN Sales.Orders          AS O ON C.custid=O.custid
JOIN Sales.OrderDetails    AS OD ON O.orderid=OD.orderid;
```

---

## 🛠 Temporary Tables & CTEs

1. Temp table:
   ```sql
   SELECT * INTO #Temp
     FROM Sales.SalesOrderHeader
    WHERE OrderDate >= '2024-01-01';
   ```
2. Simple CTE:
   ```sql
   WITH Recent AS (
     SELECT * FROM Sales.SalesOrderHeader
     WHERE OrderDate >= '2024-01-01'
   )
   SELECT * FROM Recent;
   ```
3. Recursive CTE:
   ```sql
   WITH Hierarchy AS (
     SELECT ID, ManagerID, 0 AS lvl FROM HR.Employees WHERE ManagerID IS NULL
     UNION ALL
     SELECT e.ID, e.ManagerID, h.lvl+1
       FROM HR.Employees AS e
     JOIN Hierarchy      AS h ON e.ManagerID=h.ID
   )
   SELECT * FROM Hierarchy;
   ```

---

## ⏳ Window Functions

```sql
SELECT Name, Salary,
  ROW_NUMBER() OVER (ORDER BY Salary DESC) AS Rank
  FROM HR.Employees;

SELECT OrderDate, Amount,
  SUM(Amount) OVER (ORDER BY OrderDate) AS RunningTotal
  FROM Sales.Invoices;
```

---

## 🔁 Stored Procedures & Functions

```sql
CREATE PROCEDURE dbo.GetSalesByCustomer @CustomerID INT AS BEGIN
  SELECT OrderID, TotalDue FROM Sales.SalesOrderHeader WHERE CustomerID=@CustomerID;
END;

EXEC dbo.GetSalesByCustomer @CustomerID=42;

CREATE FUNCTION dbo.TopCustomers(@MinTotal MONEY) RETURNS TABLE AS RETURN
  SELECT CustomerID, SUM(TotalDue) AS Total
    FROM Sales.SalesOrderHeader
   GROUP BY CustomerID
  HAVING SUM(TotalDue)>@MinTotal;
```

---

## 🗄️ Querying Metadata

### Catalog Views
1. List tables with schema names:
   ```sql
   USE TSQLV4;
   SELECT SCHEMA_NAME(schema_id) AS table_schema,
          name                   AS table_name
     FROM sys.tables;
   ```
2. List columns for a table:
   ```sql
   SELECT name                 AS column_name,
          TYPE_NAME(system_type_id) AS column_type,
          max_length,
          collation_name,
          is_nullable
     FROM sys.columns
    WHERE object_id = OBJECT_ID(N'Sales.Orders');
   ```

### Information Schema Views
1. List user tables:
   ```sql
   SELECT TABLE_SCHEMA, TABLE_NAME
     FROM INFORMATION_SCHEMA.TABLES
    WHERE TABLE_TYPE = N'BASE TABLE';
   ```
2. Column details for Sales.Orders:
   ```sql
   SELECT COLUMN_NAME, DATA_TYPE, CHARACTER_MAXIMUM_LENGTH,
          COLLATION_NAME, IS_NULLABLE
     FROM INFORMATION_SCHEMA.COLUMNS
    WHERE TABLE_SCHEMA = N'Sales'
      AND TABLE_NAME   = N'ORDERS';
   ```

### System Stored Procedures & Functions
- `EXEC sys.sp_tables;`  
- `EXEC sys.sp_help   @objname=N'Sales.Orders';`  
- `EXEC sys.sp_columns @table_name=N'Orders', @table_owner=N'Sales';`  
- `EXEC sys.sp_helpconstraint @objname=N'Sales.Orders';`

### SERVERPROPERTY
```sql
SELECT SERVERPROPERTY('ProductLevel');
```

### DATABASEPROPERTYEX
```sql
SELECT DATABASEPROPERTYEX(N'TSQLV4','Collation');
```

### OBJECTPROPERTY
```sql
SELECT OBJECTPROPERTY(OBJECT_ID(N'Sales.Orders'),'TableHasPrimaryKey');
```

### COLUMNPROPERTY
```sql
SELECT COLUMNPROPERTY(OBJECT_ID(N'Sales.Orders'),'orderdate','Precision');
```

---

## 🧠 Common T-SQL Commands

| Command                         | Description                             |
|---------------------------------|-----------------------------------------|
| SELECT                          | Retrieve rows                           |
| INSERT                          | Add new rows                            |
| UPDATE                          | Modify existing rows                    |
| DELETE                          | Remove rows                             |
| CREATE PROCEDURE                | Define a stored procedure               |
| EXEC                            | Execute a procedure or statement        |
| WITH (CTE)                      | Define a CTE                            |
| ROW_NUMBER() OVER()             | Assign row numbers to result set        |
| SUM(...) OVER()                 | Calculate running totals                |

---

## 📚 Glossary

| Term                   | Definition                                               | When to Use                             |
|------------------------|----------------------------------------------------------|-----------------------------------------|
| Cartesian Product      | All-row combinations of two tables                       | Cross joins                             |
| CTE                    | Common Table Expression scoped to one statement          | Modular logic, recursion                |
| Temp Table             | Session-scoped table for intermediate results            | Multi-step transformations              |
| Window Function        | Calculation over sets of rows without `GROUP BY`         | Rankings, running totals                |
| Inline TVF             | Table-valued function returning a rowset                 | Reusable set-based logic                |
| Partition BY           | Divides window function result set by group              | Group-specific analytics                |
| Non-Equi Join          | Join on non-equality conditions                          | Range or inequality-based joins         |
| Composite Join         | Join matching multiple columns                           | Multi-column PK-FK relationships        |
| Outer Join             | Preserves unmatched rows from one/both sides             | Missing-data detection, calendar tables |

---

🧠 **Pro Tips:**  
* Label scripts with schema, purpose & date for auditing.  
* Favor set-based operations over row-by-row loops.  
* Keep statistics current and rebuild indexes to optimize plans.  

🔗 Helpful Links:  
* https://learn.microsoft.com/en-us/sql/t-sql/language-reference  
* https://learn.microsoft.com/en-us/sql/sql-server/  
* https://mode.com/sql-tutorial/sql-window-functions 