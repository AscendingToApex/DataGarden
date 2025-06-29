# 🧠 MS SQL Transaction Control Language Reference Guide

## 📚 Table of Contents
* [📦 Begin, Commit & Rollback](#-begin-commit--rollback)  
* [🎯 Savepoints](#-savepoints)  
* [💥 TRY…CATCH Error Handling](#-trycatch-error-handling)  
* [🕵️ XACT_STATE & Diagnostics](#-xact_state--diagnostics)  

---

## 📦 Begin, Commit & Rollback

1. **Begin a transaction**  
   ```sql
   BEGIN TRANSACTION TransactionName;
   ```
2. **Make changes**  
   ```sql
   UPDATE dbo.Accounts
     SET Balance -= 100
     WHERE AccountID = 1;
   ```
3. **Commit the transaction**  
   ```sql
   COMMIT TRANSACTION TransactionName;
   ```
4. **Rollback the transaction**  
   ```sql
   ROLLBACK TRANSACTION TransactionName;
   ```

- Controls atomic units of work: commit to persist, rollback to undo.  
- Named transactions help manage nested scopes.  

> Pro Tip: Always name your transactions to avoid ambiguity in nested or distributed contexts.  
> Note: An uncommitted transaction will hold locks until commit/rollback.

---

## 🎯 Savepoints

1. **Set a savepoint**  
   ```sql
   SAVE TRANSACTION SavePointName;
   ```
2. **Perform operations**  
   ```sql
   INSERT INTO dbo.Log (Message) VALUES ('Step 1 done');
   ```
3. **Rollback to savepoint**  
   ```sql
   ROLLBACK TRANSACTION SavePointName;
   ```
4. **Continue or commit**  
   ```sql
   -- further operations
   COMMIT TRANSACTION TransactionName;
   ```

- Savepoints allow partial rollbacks within a larger transaction.  
- Useful for multi-step processes where only part may need undo.  

> Pro Tip: Use meaningful savepoint names (e.g., ‘BeforeCharge’) for readability.  
> Note: SAVE TRANSACTION does not support nested transaction counts—only marks points in the active transaction.

---

## 💥 TRY…CATCH Error Handling

1. **Start TRY…CATCH block**  
   ```sql
   BEGIN TRY
     BEGIN TRANSACTION;
       -- risky statements here
     COMMIT TRANSACTION;
   END TRY
   BEGIN CATCH
     -- error handling below
   END CATCH;
   ```
2. **In CATCH: rollback and capture error**  
   ```sql
   BEGIN CATCH
     IF XACT_STATE() <> 0
       ROLLBACK TRANSACTION;
     SELECT
       ERROR_NUMBER()   AS ErrorNumber,
       ERROR_MESSAGE()  AS ErrorMessage,
       ERROR_LINE()     AS ErrorLine;
   END CATCH;
   ```
3. **Optionally rethrow or log**  
   ```sql
   THROW;  -- rethrows original error
   ```

- Ensures transactions do not remain open on errors.  
- Captures error details for diagnostics or logging.  

> Pro Tip: Use `THROW` inside CATCH to preserve error context and state.  
> Note: `TRY…CATCH` only traps errors of severity ≥ 11 in T-SQL.

---

## 🕵️ XACT_STATE & Diagnostics

1. **Check transaction state**  
   ```sql
   SELECT XACT_STATE() AS TranState;
   ```
2. **Interpret `XACT_STATE()`**  
   - `1` = active, can commit  
   - `0` = no transaction  
   - `-1` = uncommittable, must rollback  
3. **Use in CATCH**  
   ```sql
   IF XACT_STATE() = -1
     ROLLBACK TRANSACTION;
   ELSE IF XACT_STATE() = 1
     COMMIT TRANSACTION;
   ```

- Helps decide proper cleanup in error handling.  
- Avoids committing a doomed transaction.  

> Pro Tip: Always test `XACT_STATE()` before issuing COMMIT in a CATCH block.  
> Note: Do not mix `@@TRANCOUNT` with `XACT_STATE()` for commit/rollback logic.

---

## 🧠 Common MS SQL Transaction Control Language Commands

| Command                                      | Description                                    |
|----------------------------------------------|------------------------------------------------|
| `BEGIN TRANSACTION [name]`                   | Start a new transaction (optional name)        |
| `COMMIT TRANSACTION [name]`                  | Commit the current transaction                 |
| `ROLLBACK TRANSACTION [name|savepoint]`      | Roll back the transaction or to a savepoint    |
| `SAVE TRANSACTION [savepoint_name]`          | Create a savepoint within an active transaction|
| `XACT_STATE()`                               | Returns transaction state (1, 0, -1)           |
| `ERROR_NUMBER()/ERROR_MESSAGE()/ERROR_LINE()`| Retrieve error details in CATCH block          |
| `TRY…CATCH`                                  | Structured error handling in T-SQL             |
| `THROW`                                      | Rethrow caught error preserving context        |

---

## 📚 Glossary

| Term             | Definition                                                                 | When to Use                                 |
|------------------|----------------------------------------------------------------------------|---------------------------------------------|
| Transaction      | A unit of work that is committed or rolled back as a whole                 | To group related DML operations             |
| Savepoint        | A marker within a transaction to allow partial rollback                    | When you need rollback to a specific point  |
| XACT_STATE()     | Function that returns the state of the current transaction                 | In error handling to decide commit/rollback |
| TRY…CATCH        | Block to trap and handle T-SQL errors                                      | To manage errors and ensure cleanup         |
| THROW            | Statement to rethrow an error preserving original error context            | After logging or cleanup in CATCH block     |

---

🧠 **Pro Tips:**  
* Always wrap your transactions in TRY…CATCH to avoid open transactions on errors.  
* Use named transactions and savepoints for complex multi-step processes.  

🔗 Helpful Links:  
* https://learn.microsoft.com/sql/t-sql/language-elements/transactions-transact-sql  
* https://learn.microsoft.com/sql/t-sql/language-elements/try-catch-transact-sql  
* https://learn.microsoft.com/sql/t-sql/functions/xact-state-transact-sql  