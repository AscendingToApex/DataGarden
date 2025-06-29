# 🧠 MS SQL Data Definition Language Reference Guide

## 📚 Table of Contents
* [🗂 Creating & Dropping Databases & Schemas](#-creating--dropping-databases--schemas)  
* [🧱 Creating & Modifying Tables](#-creating--modifying-tables)  
* [🔐 Defining Constraints & Indexes](#-defining-constraints--indexes)  
* [🔍 Views & Routines](#-views--routines)  
* [📐 Data Types & Collation](#-data-types--collation)  
* [🗄 Metadata Queries](#-metadata-queries)  

---

## 🗂 Creating & Dropping Databases & Schemas

1. Create a new database:
   ```sql
   CREATE DATABASE TSQLV4
     ON PRIMARY ( NAME = TSQLV4_data, FILENAME = 'TSQLV4.mdf' )
     LOG ON      ( NAME = TSQLV4_log,  FILENAME = 'TSQLV4.ldf' );
   ```
2. Alter database properties:
   ```sql
   ALTER DATABASE TSQLV4
     SET RECOVERY SIMPLE;
   ALTER DATABASE TSQLV4
     COLLATE Latin1_General_100_CI_AS_SC;
   ```
3. Drop an existing database:
   ```sql
   DROP DATABASE IF EXISTS TSQLV4;
   ```
4. Create a schema within the database:
   ```sql
   CREATE SCHEMA Reporting AUTHORIZATION dbo;
   ```
5. Drop a schema (must be empty):
   ```sql
   DROP SCHEMA IF EXISTS Reporting;
   ```

- Databases encapsulate data files and log files; schemas organize objects within them.  
> Pro Tip: Always include `IF EXISTS`/`IF NOT EXISTS` to make scripts idempotent.

---

## 🧱 Creating & Modifying Tables

1. Create a table with identity, defaults, and constraints:
   ```sql
   CREATE TABLE dbo.Products (
     ProductID   INT          IDENTITY(1,1) PRIMARY KEY,
     Name        NVARCHAR(100) NOT NULL,
     Price       MONEY        NOT NULL DEFAULT(0),
     CreatedDate DATETIME2    NOT NULL DEFAULT SYSUTCDATETIME()
   );
   ```
2. Add, alter, or drop a column:
   ```sql
   ALTER TABLE dbo.Products
     ADD Stock INT              NOT NULL DEFAULT(0);
   ALTER TABLE dbo.Products
     ALTER COLUMN Price DECIMAL(10,2);
   ALTER TABLE dbo.Products
     DROP COLUMN CreatedDate;
   ```
3. Rename a column or table:
   ```sql
   EXEC sp_rename 'dbo.Products.Stock', 'Quantity', 'COLUMN';
   EXEC sp_rename 'dbo.Products', 'Inventory';
   ```
4. Drop the table:
   ```sql
   DROP TABLE IF EXISTS dbo.Products;
   ```

- Always qualify table names with schema; plan column order and data types carefully.  
> Note: `sp_rename` can break dependencies—use sparingly.

---

## 🔐 Defining Constraints & Indexes

1. Add a primary key or unique constraint:
   ```sql
   ALTER TABLE dbo.Orders
     ADD CONSTRAINT PK_Orders_OrderID PRIMARY KEY (OrderID);
   ALTER TABLE dbo.Orders
     ADD CONSTRAINT UQ_Orders_CustID_OrderDate UNIQUE (CustID, OrderDate);
   ```
2. Add foreign key and check constraints:
   ```sql
   ALTER TABLE dbo.OrderDetails
     ADD CONSTRAINT FK_OD_Orders FOREIGN KEY (OrderID)
       REFERENCES dbo.Orders(OrderID);
   ALTER TABLE dbo.Products
     ADD CONSTRAINT CHK_Products_Price CHECK (Price >= 0);
   ```
3. Add a default constraint:
   ```sql
   ALTER TABLE dbo.Orders
     ADD CONSTRAINT DF_Orders_CreatedDate DEFAULT SYSUTCDATETIME() FOR CreatedDate;
   ```
4. Create clustered or nonclustered index:
   ```sql
   CREATE CLUSTERED INDEX IX_Orders_OrderDate
     ON dbo.Orders (OrderDate DESC);
   CREATE NONCLUSTERED INDEX IX_Orders_CustID
     ON dbo.Orders (CustID)
     INCLUDE (TotalDue);
   ```
5. Drop constraints or indexes:
   ```sql
   ALTER TABLE dbo.Orders DROP CONSTRAINT FK_OD_Orders;
   DROP INDEX IX_Orders_CustID ON dbo.Orders;
   ```

- Name constraints and indexes using clear, standardized conventions (e.g. PK_, FK_, IX_).  
> Pro Tip: Use filtered indexes to optimize queries on nullable columns.

---

## 🔍 Views & Routines

1. Create or alter a view:
   ```sql
   CREATE VIEW dbo.v_SalesSummary
   AS
   SELECT CustID, SUM(TotalDue) AS Total
     FROM dbo.Orders
    GROUP BY CustID;

   ALTER VIEW dbo.v_SalesSummary
   AS /* modified definition */
   ```
2. Drop a view:
   ```sql
   DROP VIEW IF EXISTS dbo.v_SalesSummary;
   ```
3. Create stored procedures and functions:
   ```sql
   CREATE PROCEDURE dbo.GetProductByID @ID INT
   AS
   BEGIN
     SELECT * FROM dbo.Products WHERE ProductID = @ID;
   END;

   CREATE FUNCTION dbo.ufn_GetOrderCount(@CustID INT)
     RETURNS INT
   AS
   BEGIN
     RETURN (SELECT COUNT(*) FROM dbo.Orders WHERE CustID = @CustID);
   END;
   ```
4. Drop procedures or functions:
   ```sql
   DROP PROCEDURE IF EXISTS dbo.GetProductByID;
   DROP FUNCTION IF EXISTS dbo.ufn_GetOrderCount;
   ```

- Views encapsulate queries for reuse; routines encapsulate logic for performance and security.  
> Note: Use `SCHEMABINDING` on views/functions to improve performance and prevent accidental column drops.

---

## 📐 Data Types & Collation

| Type             | Storage     | Range                          | Accuracy      | Entry Format                  |
|------------------|-------------|--------------------------------|---------------|-------------------------------|
| `CHAR(n)`        | n bytes     | Fixed length                   | Byte          | –                             |
| `VARCHAR(n)`     | ≤ n bytes   | Variable length                | Byte          | –                             |
| `NCHAR(n)`       | 2×n bytes   | Fixed Unicode                  | Byte          | –                             |
| `NVARCHAR(n)`    | ≤ 2×n bytes | Variable Unicode               | Byte          | –                             |
| `DATE`           | 3 bytes     | 0001-01-01 → 9999-12-31        | 1 day         | `YYYY-MM-DD`                  |
| `TIME`           | 3–5 bytes   | N/A                            | 100 ns        | `hh:mm:ss.nnnnnnn`            |
| `DATETIME2`      | 6–8 bytes   | 0001-01-01 → 9999-12-31        | 100 ns        | `YYYYMMDD hh:mm:ss.nnnnnnnn`  |
| `DATETIMEOFFSET` | 8–10 bytes  | 0001-01-01 → 9999-12-31        | 100 ns + TZ   | `YYYYMMDD hh:mm:ss.nnnnnnn±hh:mm` |
| `SMALLDATETIME`  | 4 bytes     | 1900-01-01 → 2079-06-06        | 1 minute      | `YYYYMMDD hh:mm:`             |
| `DATETIME`       | 8 bytes     | 1753-01-01 → 9999-12-31        | 3.33 ms       | `YYYYMMDD hh:mm:ss.nnn`       |

- Collation sets character sorting and comparison rules:
  ```sql
  ALTER DATABASE TSQLV4 COLLATE Latin1_General_100_CI_AS_SC;
  ```
> Pro Tip: Define collation at database creation to ensure metadata consistency.

---

## 🗄 Metadata Queries

1. List all tables and schemas:
   ```sql
   SELECT SCHEMA_NAME(schema_id) AS SchemaName, name AS TableName
     FROM sys.tables;
   ```
2. List columns and types for a table:
   ```sql
   SELECT name AS ColumnName,
          TYPE_NAME(system_type_id) AS DataType,
          max_length, is_nullable
     FROM sys.columns
    WHERE object_id = OBJECT_ID(N'dbo.Orders');
   ```
3. List indexes for a table:
   ```sql
   SELECT name, type_desc, is_unique
     FROM sys.indexes
    WHERE object_id = OBJECT_ID(N'dbo.Orders');
   ```
4. Use Information Schema views:
   ```sql
   SELECT TABLE_SCHEMA, TABLE_NAME
     FROM INFORMATION_SCHEMA.TABLES
    WHERE TABLE_TYPE = N'BASE TABLE';
   ```

- System catalog views and Information Schema provide metadata for automation and auditing.  
> Pro Tip: Use `sys.objects` to find object types and create dates.

---

## 🧠 Common MS SQL Data Definition Language Commands

| Command                               | Description                                    |
|---------------------------------------|------------------------------------------------|
| `CREATE DATABASE`                     | Define a new database                          |
| `ALTER DATABASE`                      | Modify database settings                       |
| `DROP DATABASE IF EXISTS`             | Remove a database                              |
| `CREATE SCHEMA`                       | Define a new schema                            |
| `CREATE TABLE`                        | Define a new table                             |
| `ALTER TABLE ... ADD/ALTER/DROP`      | Modify table schema                            |
| `DROP TABLE IF EXISTS`                | Remove a table                                 |
| `ALTER TABLE ... ADD CONSTRAINT`      | Add PK, FK, CHECK, DEFAULT, UNIQUE, etc.       |
| `CREATE INDEX`                        | Define clustered or nonclustered index         |
| `DROP INDEX`                          | Remove an index                                |
| `CREATE VIEW`                         | Define a view                                  |
| `CREATE PROCEDURE/FUNCTION`           | Define stored procedure or function            |
| `DROP PROCEDURE/FUNCTION/VIEW`        | Remove routines or views                       |
| `ALTER DATABASE ... COLLATE`          | Change database collation                      |
| `sp_rename`                           | Rename tables, columns, or other objects       |

---

## 📚 Glossary

| Term             | Definition                                                                 | When to Use                                    |
|------------------|-----------------------------------------------------------------------------|------------------------------------------------|
| Database         | Logical container for data files, log files, and objects                    | At database creation and configuration         |
| Schema           | Namespace within a database to group objects                                | Organizing tables, views, routines             |
| Table            | Structured object for storing rows and columns                              | Defining data entities                         |
| Constraint       | Rule enforced on table columns (PK, FK, CHECK, DEFAULT, UNIQUE)             | Ensuring data integrity                        |
| Index            | Physical structure for fast lookup                                          | Improving query performance                    |
| View             | Virtual table defined by a query                                            | Abstracting complex queries                    |
| Procedure        | Precompiled batch of SQL statements                                         | Encapsulating business logic                   |
| Function         | Precompiled routine returning a scalar or table                             | Encapsulating reusable calculations            |
| Collation        | Rules for character data sorting and comparison                             | Defining case/accent sensitivity on char types  |
| Metadata         | Data about database objects (tables, columns, indexes)                       | Auditing and automation                        |

---

🧠 **Pro Tips:**  
* Always script your DDL changes and version-control them for auditability.  
* Use meaningful, standardized naming conventions (schemas, tables, constraints).  
* Test schema changes in a staging environment to validate downstream dependencies.  

🔗 Helpful Links:  
* https://learn.microsoft.com/sql/t-sql/statements/create-table-transact-sql  
* https://learn.microsoft.com/sql/relational-databases/system-catalog-views/sys-tables-transact-sql  
* https://learn.microsoft.com/sql/relational-databases/sql-server-index-design-guide  