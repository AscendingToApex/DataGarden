
# 🧠 T-SQL Reference Guide

## 📚 Table of Contents

* [🛠 Getting Started with T-SQL](#-getting-started-with-t-sql)
* [📋 Selecting & Filtering Data](#-selecting--filtering-data)
* [🧮 Aggregations & Grouping](#-aggregations--grouping)
* [🔗 Joins & Relationships](#-joins--relationships)
* [🛠 Temporary Tables & CTEs](#-temporary-tables--ctes)
* [⏳ Window Functions](#-window-functions)
* [🧱 Creating & Modifying Tables](#-creating--modifying-tables)
* [🔁 Stored Procedures & Functions](#-stored-procedures--functions)
* [🚨 Error Handling & Transactions](#-error-handling--transactions)
* [🧠 Common T-SQL Commands](#-common-t-sql-commands)
* [📚 Glossary](#-glossary)



## 🛠 Getting Started with T-SQL

1. Connect to SQL Server with SSMS or Azure Data Studio.  
2. Set your database context:
   ```sql
   USE [YourDatabase];
   GO
   ```
3. Run a test query:
   ```sql
   SELECT TOP 10 * FROM sys.objects;
   ```

> Note: T-SQL is Microsoft's extension of SQL for SQL Server.

---

## 📋 Selecting & Filtering Data

1. Basic SELECT:
   ```sql
   SELECT column1, column2
   FROM schema.table;
   ```
2. Filter rows with WHERE:
   ```sql
   SELECT *
   FROM Sales.Orders
   WHERE OrderDate >= '2024-01-01';
   ```
3. Sort results with ORDER BY:
   ```sql
   SELECT *
   FROM Production.Products
   ORDER BY Price DESC;
   ```

> Pro Tip: Use table aliases for readability and performance hints.

---

## 🧮 Aggregations & Grouping

1. Use aggregate functions:
   ```sql
   SELECT COUNT(*) AS TotalCount,
          SUM(Amount) AS TotalAmount
   FROM Sales.Invoices;
   ```
2. Group rows:
   ```sql
   SELECT CustomerID, SUM(Amount) AS Revenue
   FROM Sales.Invoices
   GROUP BY CustomerID;
   ```
3. Filter grouped results with HAVING:
   ```sql
   SELECT EmployeeID, COUNT(*) AS OrdersCount
   FROM Sales.Orders
   GROUP BY EmployeeID
   HAVING COUNT(*) > 10;
   ```

> Note: WHERE filters before grouping; HAVING filters after.

---

## 🔗 Joins & Relationships

1. INNER JOIN:
   ```sql
   SELECT c.Name, o.OrderDate
   FROM Customers c
   INNER JOIN Orders o
     ON c.CustomerID = o.CustomerID;
   ```
2. LEFT JOIN:
   ```sql
   SELECT p.Name, s.Quantity
   FROM Products p
   LEFT JOIN SalesOrderDetail s
     ON p.ProductID = s.ProductID;
   ```
3. CROSS APPLY:
   ```sql
   SELECT e.EmployeeID, e.Name, d.DepartmentName
   FROM Employees e
   CROSS APPLY dbo.fn_GetDepartments(e.EmployeeID) d;
   ```

> Pro Tip: Always fully specify join predicates to avoid unintended cartesian joins.

---

## 🛠 Temporary Tables & CTEs

1. Create a temp table:
   ```sql
   SELECT * INTO #TempCustomers
   FROM Customers
   WHERE Country = 'USA';
   ```
2. Use a CTE:
   ```sql
   WITH RecentOrders AS (
     SELECT * FROM Sales.Orders
     WHERE OrderDate >= '2024-01-01'
   )
   SELECT * FROM RecentOrders;
   ```
3. Recursive CTE:
   ```sql
   WITH Hierarchy AS (
     SELECT EmployeeID, ManagerID, 0 AS Level
     FROM Employees
     WHERE ManagerID IS NULL
     UNION ALL
     SELECT e.EmployeeID, e.ManagerID, h.Level + 1
     FROM Employees e
     JOIN Hierarchy h
       ON e.ManagerID = h.EmployeeID
   )
   SELECT * FROM Hierarchy;
   ```

> Note: Temp tables persist for your session; CTEs are scoped to a single statement.

---

## ⏳ Window Functions

1. Assign row numbers:
   ```sql
   SELECT Name, Salary,
          ROW_NUMBER() OVER (ORDER BY Salary DESC) AS Rank
   FROM Employees;
   ```
2. Calculate running totals:
   ```sql
   SELECT OrderDate, Amount,
          SUM(Amount) OVER (ORDER BY OrderDate) AS RunningTotal
   FROM Sales.Invoices;
   ```
3. Partitioned ranking:
   ```sql
   SELECT CustomerID, OrderDate, Amount,
          RANK() OVER (
            PARTITION BY CustomerID
            ORDER BY Amount DESC
          ) AS CustRank
   FROM Sales.Invoices;
   ```

> Pro Tip: Window functions never collapse rows—combine with SELECT or subqueries for filtered results.

---

## 🧱 Creating & Modifying Tables

1. Create a new table:
   ```sql
   CREATE TABLE dbo.Products (
     ProductID INT IDENTITY(1,1) PRIMARY KEY,
     Name NVARCHAR(100) NOT NULL,
     Price MONEY DEFAULT 0
   );
   ```
2. Add a column:
   ```sql
   ALTER TABLE dbo.Products
   ADD Stock INT NOT NULL DEFAULT 0;
   ```
3. Drop a table:
   ```sql
   DROP TABLE dbo.Products;
   ```

> Note: Always back up data before altering or dropping tables.

---

## 🔁 Stored Procedures & Functions

1. Create a stored procedure:
   ```sql
   CREATE PROCEDURE dbo.GetSalesByCustomer
     @CustomerID INT
   AS
   BEGIN
     SELECT OrderID, Total
     FROM Sales.Orders
     WHERE CustomerID = @CustomerID;
   END;
   ```
2. Execute it:
   ```sql
   EXEC dbo.GetSalesByCustomer @CustomerID = 123;
   ```
3. Create an inline TVF:
   ```sql
   CREATE FUNCTION dbo.GetTopCustomers(@MinTotal MONEY)
   RETURNS TABLE
   AS
   RETURN
     SELECT CustomerID, SUM(Total) AS TotalSales
     FROM Sales.Orders
     GROUP BY CustomerID
     HAVING SUM(Total) > @MinTotal;
   ```

> Pro Tip: Inline TVFs often outperform scalar functions in set-based queries.

---

## 🚨 Error Handling & Transactions

1. Basic transaction:
   ```sql
   BEGIN TRAN;
     UPDATE Accounts
     SET Balance = Balance - 100
     WHERE AccountID = 1;
     UPDATE Accounts
     SET Balance = Balance + 100
     WHERE AccountID = 2;
   COMMIT;
   ```
2. TRY…CATCH with rollback:
   ```sql
   BEGIN TRY
     BEGIN TRAN;
       -- your statements
     COMMIT;
   END TRY
   BEGIN CATCH
     ROLLBACK;
     SELECT ERROR_NUMBER() AS ErrNum,
            ERROR_MESSAGE() AS ErrMsg;
   END CATCH;
   ```

> Pro Tip: Always handle errors to avoid uncommitted transactions hanging locks.

---

## 🧠 Common T-SQL Commands

| Command                 | Description                             |
|-------------------------|-----------------------------------------|
| SELECT                  | Retrieve data                           |
| INSERT                  | Add new rows                            |
| UPDATE                  | Modify existing rows                    |
| DELETE                  | Remove rows                             |
| CREATE TABLE            | Define a new table                      |
| ALTER TABLE             | Change table schema                     |
| DROP TABLE              | Remove a table                          |
| CREATE PROCEDURE        | Define a stored procedure               |
| EXEC                    | Execute a procedure or statement        |
| WITH (CTE)              | Define a Common Table Expression        |
| ROW_NUMBER() OVER()     | Assign row numbers to result set        |
| SUM(...) OVER()         | Calculate running totals                |
| BEGIN TRANSACTION       | Start a transaction                     |
| COMMIT                  | Save a transaction                      |
| ROLLBACK                | Undo a transaction                      |

---

## 📚 Glossary

| Term               | Definition                                             | When to Use                              |
|--------------------|--------------------------------------------------------|------------------------------------------|
| CTE                | Named temporary result set within a single query       | Modular queries or recursion             |
| Temp Table         | Session-scoped table for intermediate results          | Multi-step data transformations          |
| Window Function    | Performs calculations across sets of rows without GROUP| Rankings, running totals, moving averages|
| Inline TVF         | Table-valued function returning a set of rows          | Encapsulating reusable logic             |
| Stored Procedure   | Precompiled SQL code block                             | Batch operations, encapsulate logic      |
| Transaction        | Ensures atomic execution of multiple statements        | Financial updates, critical batch jobs   |
| TRY…CATCH          | Error handling construct                               | Trap and handle runtime errors           |
| Partition By       | Divides result set for window functions                | Group-specific calculations              |
| Identity Column    | Auto-incrementing integer column                       | Primary key generation                   |
| CROSS APPLY        | Apply a table-valued function per row                  | Advanced joins with functions            |

---

🧠 **Pro Tips:**

* Always specify schema (e.g., dbo) to avoid ambiguity and improve performance.  
* Favor set-based operations over cursors or loops for scalability.  
* Regularly update statistics and rebuild indexes for optimal query plans.

🔗 Helpful Links:

* https://learn.microsoft.com/en-us/sql/t-sql/language-reference  
* https://learn.microsoft.com/en-us/sql/relational-databases  
* https://mode.com/sql-tutorial/sql-window-functions  