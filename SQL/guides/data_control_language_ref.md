# 🧠 MS SQL Data Control Language Reference Guide

## 📚 Table of Contents

* [👤 GRANT Permissions](#-grant-permissions)  
* [🚫 DENY Permissions](#-deny-permissions)  
* [❌ REVOKE Permissions](#-revoke-permissions)  
* [🔐 Roles & Role Management](#-roles--role-management)  
* [🔄 Permission Inheritance & Hierarchy](#-permission-inheritance--hierarchy)  

---

## 👤 GRANT Permissions

1. Connect to your database in SSMS or Azure Data Studio.  
2. Execute a GRANT statement:
   ```sql
   GRANT SELECT, INSERT
     ON dbo.Orders
     TO SalesUser;
   ```
3. (Optional) Enable delegation:
   ```sql
   GRANT UPDATE
     ON dbo.Orders
     TO SalesManager
     WITH GRANT OPTION;
   ```
4. Verify the grant:
   ```sql
   SELECT * 
     FROM sys.database_permissions
    WHERE grantee_principal_id = DATABASE_PRINCIPAL_ID('SalesUser');
   ```

- GRANT explicitly assigns permissions on securables.  
- `WITH GRANT OPTION` lets the principal pass permissions to others.

> Pro Tip: Always qualify objects (`schema.object`) to avoid ambiguity.

---

## 🚫 DENY Permissions

1. Connect to your database.  
2. Issue a DENY statement:
   ```sql
   DENY DELETE
     ON dbo.Orders
     TO SalesUser;
   ```
3. Confirm the denial:
   ```sql
   SELECT *
     FROM sys.database_permissions
    WHERE permission_name = 'DELETE'
      AND state_desc      = 'DENY';
   ```

- DENY supersedes GRANT and inherited permissions.  
- Use sparingly to avoid complex permission logic.

> Note: Excessive DENY rules can make permission troubleshooting difficult.

---

## ❌ REVOKE Permissions

1. Connect to your database.  
2. Execute a REVOKE statement:
   ```sql
   REVOKE SELECT
     ON dbo.Orders
     FROM SalesUser;
   ```
3. Check effective permissions:
   ```sql
   SELECT *
     FROM fn_my_permissions('dbo.Orders','OBJECT');
   ```

- REVOKE removes explicit GRANT or DENY.  
- Inherited grants from roles or PUBLIC may still apply.

> Pro Tip: Log revocations in a change history for auditing clarity.

---

## 🔐 Roles & Role Management

1. Create a custom database role:
   ```sql
   CREATE ROLE db_Reporting;
   ```
2. Add users to the role:
   ```sql
   ALTER ROLE db_Reporting
     ADD MEMBER SalesAnalyst;
   ```
3. Grant object permissions to the role:
   ```sql
   GRANT SELECT ON dbo.SalesReport
     TO db_Reporting;
   ```
4. Remove a member:
   ```sql
   ALTER ROLE db_Reporting
     DROP MEMBER SalesAnalyst;
   ```
5. Drop the role:
   ```sql
   DROP ROLE db_Reporting;
   ```

- Roles simplify permission management across many users.  
- Use fixed server roles for server-level tasks (`sysadmin`, `securityadmin`) and custom roles for object-level.

> Pro Tip: Assign permissions to roles—not individuals—to follow least-privilege principles.

---

## 🔄 Permission Inheritance & Hierarchy

1. Permission evaluation order:
   - Explicit DENY  
   - Explicit GRANT  
   - Role-based GRANT  
   - PUBLIC role grants  
2. Scope levels:
   - Server-level  
   - Database-level  
   - Schema-level  
   - Object-level  
3. Precedence:
   - DENY > GRANT  

- A principal’s effective permissions combine all applicable grants minus any DENY.  
- PUBLIC role provides baseline permissions for every principal.

> Note: Use `sys.server_permissions`, `sys.database_permissions`, and `fn_my_permissions` to trace effective rights.

---

## 🧠 Common MS SQL DCL Commands

| Command                                           | Description                                          |
|---------------------------------------------------|------------------------------------------------------|
| `GRANT <perm> ON <securable> TO <principal>`      | Grant one or more permissions                        |
| `GRANT ... WITH GRANT OPTION`                     | Grant permission and allow delegation                |
| `DENY <perm> ON <securable> TO <principal>`       | Explicitly deny permission                           |
| `REVOKE <perm> ON <securable> FROM <principal>`   | Remove a GRANT or DENY                               |
| `CREATE ROLE <role_name>`                         | Create a new database role                           |
| `ALTER ROLE <role> ADD/DROP MEMBER <user>`        | Modify role membership                               |
| `DROP ROLE <role_name>`                           | Delete a database role                               |
| `fn_my_permissions(<name>, <scope>)`              | List effective permissions for current principal     |
| `HAS_PERMS_BY_NAME(<name>,<scope>,<perm>)`        | Check specific permission for a principal            |

---

## 📚 Glossary

| Term                 | Definition                                                              | When to Use                                          |
|----------------------|--------------------------------------------------------------------------|------------------------------------------------------|
| Securable            | Entity (server, database, schema, object) on which permissions can be set | In all GRANT/DENY/REVOKE statements                  |
| Principal            | User, database role, or server role                                      | In permission assignment clauses                     |
| Role                 | A grouping of permissions that can be assigned to multiple principals     | To simplify and standardize permission management    |
| WITH GRANT OPTION    | Clause allowing the grantee to grant the same permission to others        | When delegation of permissions is needed             |
| PUBLIC               | Default database role every principal is a member of                      | To audit baseline permissions across all users       |
| Inherited Permission | Permission granted via role membership or PUBLIC role                     | When assessing effective access                      |

---

🧠 **Pro Tips:**  
* Document each GRANT, DENY, and REVOKE operation for audit trails.  
* Use role-based security instead of direct user grants for scalability.  
* Periodically review and clean up unused permissions and roles.  

🔗 Helpful Links:  
* https://learn.microsoft.com/sql/t-sql/statements/grant-object-permissions-transact-sql  
* https://learn.microsoft.com/sql/t-sql/statements/deny-object-permissions-transact-sql  
* https://learn.microsoft.com/sql/t-sql/statements/revoke-object-permissions-transact-sql