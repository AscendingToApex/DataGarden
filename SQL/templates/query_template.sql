-- =====================================================================
-- Query title : <what this query answers>
-- Author      : <name>            Date: <YYYY-MM-DD>
-- Database    : <database/schema>
-- Purpose     : <one-line business purpose>
-- =====================================================================
-- See guides: ../guides/data_manipulation_language_ref.md
--             ../guides/sql_dialect_portability_ref.md

USE MyDatabase;   -- SQL Server context (omit/adjust on other engines)

-- Optional: reusable subset via a CTE for readability
WITH filtered AS (
    SELECT
        o.order_id,
        o.customer_id,
        o.order_date,
        o.amount
    FROM Sales.Orders AS o
    WHERE o.order_date >= '20240101'
      AND o.order_date <  '20250101'
)

SELECT
    f.customer_id,
    COUNT(*)          AS num_orders,
    SUM(f.amount)     AS total_spent,
    AVG(f.amount)     AS avg_order_value
FROM filtered AS f
GROUP BY f.customer_id
HAVING SUM(f.amount) > 1000
ORDER BY total_spent DESC;

-- Portability reminders (see sql_dialect_portability_ref.md):
--   TOP n  (SQL Server)   ->  LIMIT n  (Postgres/MySQL)
--   GETDATE()             ->  NOW() / CURRENT_TIMESTAMP
--   ISNULL(x, 0)          ->  COALESCE(x, 0)
