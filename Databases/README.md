# Programming Foundations: Databases.
# [*Course Certificate*](https://www.linkedin.com/learning/certificates/07173a747213041986bb49fd8d34ac47050da57afe9b349c48ad7add7b78c422)

### Benefits of spreadsheets:
- Stores data more efficiently.
- Collections of Rows and Columns => tables.
- **Database** : Collection of tables. 
    - Provides structure for data.
    - Allows enforecement of rules for data.
    - Protect data from unauthorized access or chages.
- **Schema**: The definition of how data in a database will be organized. 
### Relational Databases:
- Columns = Atrributes
- Rows = Instances.
- Relations = Tables. 
- Keys and unique values:
    - Unique value is a value that does not appear in any other row or column.
    - Primary key: Unique.
    - Composite key: Tow or more fields taken together to act as a unique identifier.
    - Foreign key: Refers to a primary key in another table. 
- Relationships:
    - One-to-Many.
    - One-to-One.
    - Many-to-Many.
- ACID: Atomic, Consistent, Isolated, Durable.
> Transactions in DB.
- ACID requirements are handled by DBMSs already. 
- SQL: Strucured Query Language. 
    - DML: Data Manipulation Language. Allowing statements to be written for DBMS to interpret how to interact with data.
        - Clause.
        - Predicate.
        - Expression.
        - Such as SELECT ...etc.
    - DDL: Data Definition Lanuage. Offerring features to manage the db itself, such as creating or modifying tables and controlling access to tables. 
    - DCL: Data Control Language = DDL.
### Tables:
- ER diagrams = Entity Relationship diagram. 
    - A diagram uses tables, fields, and relationships to plan a database.
- Data types: 
    - Varchar(number of characters.)
    - Date, Time, Datetime, Timesstamp.
    - Integers, Decimal.
    - Phone numbers are stored as characters. => varchar(200)
    - Null represents the absence of a value. 
    - Null = a data type. 
- Primary and Foreign keys: 
    - PK = unique value.
    - UUID = Universally Unique Identifier for more security measures.
    - Composite key: used when there is no primary key.
### Relationships:
- One-to-Many relatoinships: 
    - Foriegn key is on the many side.
    - One record is associated with many records.
- Many-to-Many relationship:
    - You need to create a new table and combine the primary keys of both tables in the new table. 
- One-to-One relationship:
    - Use it when you need to seperate information.
    - Not commonly used.
- Referential Integrity:
    - When the database is aware of relationships and won't allow a user to modify data in a way that violates those relationships.
    - Helps maintain the consistency of a table. 
    - Use it to delete records or prevent records from being deleted.
### Database Optimization:
- Normalization Rules:
    - 1NF, 2NF, 3NF.
    - Helps prevent problems when using database. 
- First Normal Form (1NF):
    - Values in each cell should be atomic and tables should have no repeating groups.
    - Order of rows is not important. 
    - No repeatition.
    - Voilations with 1NF are easy to spot at the ealy stages of design.
- Second Normal Form (2NF):
    - No value in a table should depend on only part of a key that can be used to uniquely identify a row.
    - Comes in context of composite keys. 
    - Create a new table. 
- Third Normal Form (3NF):
    - Values should not be stored if they can be calculated from another non-key field.
> If a database Satisfies the 1NF, 2NF, 3NF => then it is fully optimized. 
> Denormalization: is the process of intentionally duplicating information in a table, in violation of normalization rules. 
### More Topics on Databases:
- Stored Procedures:
    - Are a series of commands stored on the database.
    - Allow reuse of long or detailed queries instead of writing them for each use.
    - Provide a safe way to deal with sensitive data.
- Check Indexes, Transactions. 
- Access Control:
    - Column Permissions. 
    - Consider Business requirements when granting access to database and data.
    - Understand compliance regulations.
- SQL Injection:
    - Type of attack that includes part of a SQL command entered as a value to hijack query and change how it works.
- Software Options:
    - Microsoft SQL Server.
    - Oracle.
    - dBase.
    - FileMaker Pro.
    - Microsoft Access.
    - MySQL.
    - MariaDB.
    - SAP HANA.
    - SQLite.
    - Desktop Databases:
        - Used for smaller solutions.
        - Hosted on workstation.
        - Access.
    - Enterprise Databases:
        - Used by large number of people.
        - Services millions of interactions.
        - SQL Server, Oracle...
    - For Big Data you will need to use some frameworks. 
    - NoSQL:
        - Unstructured data.
        - Key-value pairs.
        - Graphs.
        - Objects.
        - Geographic data points.
        - Posts and comments => Streamed data.
        
        

