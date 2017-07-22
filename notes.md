https://www.udacity.com/course/intro-to-relational-databases--ud197

# Lesson 1: Data and Tables
- Learn about how relational databases let you structure data into tables.
- Learn about the importance of unique keys and relationships between tables.

## Why a database ?
In memory data is temporal, so it's not apporpriate for storing datas that we want to last.
A flat file is persistent but can't resolve conflicts if there's many changes at a time.
A database offers many advantages:
- Persistence
- Data structure for storing and searching (usually faster than flat files)
- Allow methods to modify datas at the same time without making conflicts
- Relational databases only: flexible query language and special constraints to protect data consistency

## Tables
Colums has names to identify what they contain. Every values in a same column have the same type and moreover, they should have the same meaning.

| country   | population  | literacy |
|:----------|:------------|:---------|
| Argentina | 43 million  | 98%      |
| Brazil    | 203 million | 91%      |
| Colombia  | 47 million  | 94%      |
| Ecuador   | 15 million  | 92%      |

## Aggregation
An aggregation summurize several rows in one. The **count** agregation groups the values of one specified column and "count" the numbers of rows that have the same value in that columns:

| Name   | Species |
|:-------|:--------|
| Max    | gorilla |
| Sue    | gorilla |
| Max    | moose   |
| Alison | lama    |

COUNT Species =>

| species | count |
|:--------|:------|
| gorilla | 2     |
| mose    | 1     |
| lama    | 1     |

## Table Structure
Bad: we can't know in advence how many food colums there will be

*diet*

| species    | food 1  | food 2  | food 3 |
|:-----------|:--------|:--------|:-------|
| llama      | plants  |         |        |
| brown bear | fish    | meat    | plants |
| orangutan  | plants  | insects |        |

Bad: we can't use `count` and others agregations.

*diet*

| species    | food               |
|:-----------|:-------------------|
| llama      | plants             |
| brown bear | fish, meat, plants |
| orangutan  | plants, insects    |

There's often several same values in one row, and it's not a bad practice. We shoud do that:

*diet*

| species    | food    |
|:-----------|:--------|
| llama      | plants  |
| brown bear | fish    |
| brown bear | meat    |
| brown bear | plants  |
| orangutan  | plants  |
| orangutan  | insects |

Then we can make a query on it. A query always returns a table:

```sql
select food from diet where species = 'orangutan'

# 2rows/1column
food
---
plants
insects
```

Even if we ask a simple calcul to the database, it will return an one row/ one column table:
```sql
select 2+2 as sum

# 1row/1column
sum
---
4
```

```sql
select 2+2, 4+4, 6+6

# 1rows/3columns
?columns? | ?columns? | ?columns? |
-----------------------------------
4         | 8         | 12        |
```


## Related Table
We can use databas to `join` the tables together and look up the data whe want.

*pictures*

| id | name    | filename           |
|:---|:--------|:-------------------|
| 1  | Fluffy  | fluffsocute.jpg    |
| 2  | Monster | monstie-basket.png |
| 3  | George  | george.jpg         |

*votes*

| left | right | winner |
|:-----|:------|:-------|
| 2    | 3     | 3      |
| 1    | 3     | 1      |
| 2    | 1     | 1      |
| 3    | 2     | 3      |
| 3    | 1     | 1      |
| 2    | 3     | 3      |

*joined*

| left_name | right_name | winner_name |
|:----------|:-----------|:------------|
| Monster   | George     | George      |
| Fluffy    | George     | George      |
| Monster   | Fluffy     | Fluffy      |
| George    | Monster    | George      |
| George    | Fluffy     | Fluffy      |
| Monster   | George     | George      |

## Primary Key
We very often want unique entries. I can make a unique number manually called **id**. It's so cummon that most databases makes it for me, it's called a **primary key**.

Sometimes I can add datas itself if I'm sure it will be unique:
- PostCode for cities
- Coutry code for countries
- Students ID for students

Be carefull of some primary keys that won't works:
- FirstName/LastName: two persons can have the same
- Home adress: two persons can live together
- Email Address: unique, but can change
- Driver's license: unique, but not everyine has a one


## Joining tables

Here's an exemple of how to retrieve the number of animals eating fish in the privous exemple.
```sql
select animals.name, animals.species, diet.food
from animals join diet
  on animal.species = diet.species # statement to specify how to match up the rows from one table to the rows of the other one
  where food = 'fish';

# The result will be a 2r/1c table:

count
---
20
```

# Lesson 2: Elements of SQL

https://udacity.atlassian.net/wiki/display/BENDH/RDB+Lesson+2+Reference+Notes
- Begin learning SQL, the Structured Query Language used by most relational databases.
- Learn about the select and insert statements, the basic operations for reading and writing data.
- Learn about the operators and syntax available to get the database to scan and join tables for you.

## Types in SQL
There are a lot of types in SQL for many purposes. They even differ from one database to another. For exemple there's many way to declare a string or an integer.
To beggin I can use `text`, `int`, `date`. Be carrefull if I need the quote or not (depending on the type).

## Select Where

basic fetch of datas:

```sql
select # keyword to fetch data out of the database
    name, birthdate # wich columns to see in the result
from # what table they come from
animals
Where # restriction
species = 'gorilla';
```

## Booleans and Comparaisons
We can use Booleans **and**, **not** and **or**. The three next exemple returns the same:

```sql
# 1
select name from animals where
(not species = 'gorilla') and (not name ='Max');

# 2
select name from animals where
not (species = 'gorilla' or name ='Max');

# 3
select name from animals where
species != 'gorilla' and name !='Max';
```

I also can use comparaison operators pretty much the same way as in Python, expect `==` is `=`.

## Introspection
SQL is very bad at listing it's own structure (table, columns name and colums type)! But there's tools, each database has it's own implementation (often from the database console and not inside itself).

## Experimentation

Experiment page and Zoo database reference:
https://classroom.udacity.com/courses/ud197/lessons/3423258756/concepts/33885287060923

An exemple where I join multiple tables and display their datas while grouping and ordering:

```sql
SELECT COUNT(animals.species) as num, animals.species as "specie", taxonomy.t_order as "taxonomy order", ordernames.name as "order name"
  FROM animals JOIN taxonomy, ordernames
  ON (animals.species = taxonomy.name) and (taxonomy.t_order = ordernames.t_order)
  GROUP BY animals.species
  ORDER BY "order name" ASC
```

## SELECT clauses

Modifyers I can add in the SELECT statement:

```sql
LIMIT count # only return the 'count' first rows
LIMIT count OFFSET skip # return 'count' rows starting at the 'skip' one.

ORDER BY column # Sort the rows by 'colums' value order
ORDER BY column ASC # same as ORDER BY
ORDER BY  column DESC  # Reverse sorting
ORDER BY column1, column2 # Sort by 'column1' first, then by 'column2'

GROUP BY column # return one row by distinct value in 'column'. Beware that it change the behavior of MAX, COUNT and SUM
```

Return each species and the numbers of animals of each. Sort them with in first the species that have the most animals:
```sql
SELECT species, count(*) as num # Columns to show
  FROM animals # Tables to search
  GROUP BY species # Aggregation
  ORDER BY num DESC # Sorting
```

    ## Insertion
    To insert a row in my table, I use `ÌNSERT`.

```sql
# Automatic insertion if the values are in the same order as table's column.
INSERT INTO table VALUES ("stuff", 42):

# Specifying which value goes in which column.
INSERT INTO table (col2, col1) VALUES (42, "stuff"):
```

## HAVING: After Aggregating
`where` applies to the rows *before* aggregation. Sometime I need to restrict with aggragated rows like COUNT() results, MAX or SUM. I should give this result a name with AS, and us `having` to aggregate on it.
Subselect can also do the job.

For exemple if I have a store and I want ot find all the items that have more sold than five units:
```sql
select name,
count(*) as num
from sales
having num > 5;
```


# Lesson 3: Python DB-API
- Learn how to access a relational database from Python code.
- Use a virtual machine (VM) to run a Python web application with a database.
- Common security pitfalls of database applications, including the famous Bobby Tables.

## Running a Virtual Machine
https://classroom.udacity.com/courses/ud197/lessons/3423258756/concepts/14c72fe3-e3fe-4959-9c4b-467cf5b7c3a0
[Virtual box](https://www.virtualbox.org/wiki/Downloads) is tool to run a virtual machine.
[Vagrant](https://www.vagrantup.com/) is a tool to ease the configuration of a virtual machine and re-run the same environement on different systems. I can compare it to docker, but with an entire virtual machine.

## Python DB-API
DB-API is a standart to connect python and a database library. There's a lot of differents libraries for differents databases that follow this standart, and adapting code from one to another is straitfoward. The standart specifies what function I cal to:
- connect to a database
- send queries
- get results

Databases and Libraries (= DB-API module) has sometimes a quite different names:

| BD System  | DB-API mudule   |
|:-----------|:----------------|
| SQLite     | sqlite3         |
| PostgreSQL | psycopg2        |
| ODBC       | pyodbc          |
| MySQL      | mysql.connector |

## DB-API flow
I usually need to follow the same flow anytime I use DB-API:

```python
import sqlite3 # Import the database library

conn = sqlite3.connect("Cookies") # Connect to the database. Here we connect to *Cookies*: Chrome and firefox use SQLite to store their cookies and web history. If I use a network, I need to specify here the hostname, username, password...

cursor = conn.cursor() # use the *connection* object to create a *cursor* that actually run the queries and fetches the results.

cursor.execute("SELECT host_key FROM cookies LIMIT 10") # use the *cursor* to run a query

results = cursor.fetchall() # use the *cursor* to fetch the results

connection.commit() # if I hadve performed an *INSERT*
# or
connection.rollback() # if I have performed an *INSERT*

print results #

conn.close() # Good to always close the connection to free memory, especially if the code is run in a loop!
```

git checkout --track origin/dev
git checkout -b dev origin/dev

## PSQL basic commands
https://classroom.udacity.com/courses/ud197/lessons/3483858580/concepts/35153985420923

## Attacks
### Bobby Tables
http://bobby-tables.com/

I should be carefull that come inputs may break my databases:
`'` or `"` may produce an error
`'); delete from posts; --` may delete all content!

I can prevent that by using the right syntax:
```sql
# BAD: input is inserted and interpreted
cur.execute("INSERT INTO posts VALUES ('%s')" % content)

# GOOD: input is inserted safely as a string
cur.execute("INSERT INTO posts VALUES (%s)", (content,))
```

### Script Injetion

Some inputs are not dangerous for the database itself but can execute dangerous script when rendered in the browser:
```html
<script>
  setTimeout(function() {
    var tt = document.getElementById('content');
    tt.value = "<h2 style='color: #FF6699; font-family: Comic Sans MS'>Spam, spam, spam, spam,<br>Wonderful spam, glorious spam!</h2>";
    tt.form.submit();
  }, 2500);
</script>
```
**Bleach** is a library to escape html code:
http://bleach.readthedocs.io/en/latest/

- **Input sanitization** : clean before storing in the BD. That way, any app/interface that use the database are protected without worring.
- **Output sanitization** : clean after storing in the DB. That way, I keep accurate record of what users sent. It's also necessary if I *already have* dangerous datas in my DB.

Perhaps the best way is to do both. To keep the accurate record, I could use one BD for raws data and one for sanitize one.

## Update
The `UPDATE` command update values in the database. I can use the `WHERE` clause to select the rows to update. If i leave it empty, all raws will be updated.

```sql
UPDATE table
  SET column = value
  WHERE restriction;
```
*Restriction* can be `content = '<script>DANGEROUS</script'` but it's painfull because we have to target each content precisely.
We can use the `like` operator with `%` to target content that include what we search for:
`content like '%<script>%'` will target all values that include `<script>`.

### % selector

The `%` means "anything", like the `.*` in regex or `*` in uniw shell.

```sql
| fish   |
|--------|
| salmon |

TRUE
fish like 'salmon'
fish like 'salmon%'
fish like 'sal%'
fish like '%n'
fish like 's%n'
fish like '%al%'
fish like '%'
fish like '%%%'

FALSE
fish like 'carp'
fish like 'salmonella'
fish like '%b%'
fish like 'b%'
fish like ''
```

## Delete

```sql
DELETE from table
  WHERE restriction
```


# Lesson 4: Deeper Into SQL
- Learn how to design and create new databases.
- Learn about normalized design, which makes it easier to write effective code using a database.
- Learn how to use the SQL join operators to rapidly connect data from different tables.

## Normalization
http://www.bkent.net/Doc/simple5.htm

Normalization is the process of organizing columns and tables to achieve these goals:
- Improve data integrity
- Reduce redondancy
- Have the optimum structure

In a **normalized** DB, the relashionships among the tables match the relationships that are really there among the data.

### Guidlines
#### Every row has the same number of columns
In practice, the database system won't let us *literally* have different numbers of columns in different rows. But if we have columns that are sometimes empty (null) and sometimes not, or if we stuff multiple values into a single field, we're bending this rule.

**BAD** because some columns are empty and that can cause problems in operations. Also, two columns for the same meaning *major*. Also, if we want to add other majors we have to change the table structure
| Student ID | Major 1 | Major 2 |
|------------|---------|---------|
| 11111      | Math    |         |
| 22222      | Bio     |         |
| 33333      | Math    | Bio     |

**GOOD**
| Student ID | Major 1 |
|------------|---------|
| 11111      | Math    |
| 22222      | Bio     |
| 33333      | Math    |
| 33333      | Bio     |

#### There is a unike *key*, and everything in a raw says something about the key
The "unike key" may be one column or multiple column, we call it *composite*. It even can be the whole row. But we shouldn't duplicate single ID, composite ID of whole row is a table.

More importantly, if we are storing non-unique facts — such as people's names — we distinguish them using a unique identifier such as a serial number. This makes sure that we don't combine two people's grades or parking tickets just because they have the same name.

**BAD** because *Warehouse-Address* is a fact about *Warehouse*, not about *Part*
| PART | WAREHOUSE | Quantity | Warehouse-Address |
|------|-----------|----------|-------------------|

**GOOD**
| PART | WAREHOUSE | Quantity |
|------|-----------|----------|

| WAREHOUSE | Warehouse-Address |
|-----------|-------------------|

*Note : If the key is composite, this rules is: "A non-key field is a fact about the composite keys, not a subset of them, i.e. one of them"* 

#### Facts that don't relate to the key belong in different tables
The example here is has *Employee*, their *departement*, and the *departement*'s *location*. The *lcoation* isn't a fact about the *Employee*; it's a fact about the *Departement*. Moving it to a separate table saves space and reduces ambiguity, and we can always reconstitute the original table using a join.

**BAD**
| EMPLOYEE | Department | Location |
|----------|------------|----------|

**GOOD**
| EMPLOYEE | Department |
|----------|------------|

| DEPARTMENT | Location |
|------------|----------|

#### Tables shouldn't imply relationships that don't exist
There should be relationships in any columns. Below *BAD* exemple make look like *Skills* and *Language* has something to do together. In fact there isn't any relation, so we should spleet the tables.

**BAD** because there isn't any relationship between Skill and Language, but filling the table will assiciate them in the same rows.
| Employee | Skill | Language |
|----------|-------|----------|

**GOOD**
| Employee | Skill |
|----------|-------|

| Employee | Language |
|----------|----------|

### Denormalization
It's an approach to making DB queries faster by avoiding joins. Modern advenced DB as **PostgreSQL** can meet the same goals  using tools as *Indexes* and *Materialized Views*.

## CREATE database
First I need to creane a DB and give it a name

```sql
```

## CREATE database, tables and Types

```sql
# First I need to create a DB
CREATE DATABASE dbName [options]

# Connect to a database in psql
\c dbName

# I can delete it if I'm not connected to it
DROP DATABASE dbName [options]

# Create a table
CREATE TABLE tableName (
  column1 type [constraints],
  column2 type [constraints],
  column3 type [constraints],
  [row constraints])

# Delete a table
DROP TABLE tableName [options]
```

I gave a name of the table, the name of each columns and the type of each columns. I aslo can set constraints on each columns and on the row as a whole.

There's a ton of different types. Some DB have a lot, others have few. When the desired type isn't available I can use another one instead usually `string` or `integer`.

Normally, creating the DB is done upfront as part of the installation procedure. It's not cummon at all to send `CREATE TABLE` commands from my app code, even if it's technically possible.

### Primary Keys
A primary key ensure we can uniquely identify each columns. It also define what the table datas are about. I should define myself the primary keys I want. Then if i try to insert a row that duplicate a primary key, psql will throw an error (and I'll have to rollback()).

Unique column for primary key : put `primary key` after the column definition:
```sql
CREATE TABLE students (
  id serial primary key,
  name text,
  birthdate text,
)
```

Multiple columns for primary key : use `primary key` followed by the columns name at the end of the table definition:
```sql
CREATE TABLE postalPlaces (
  postalCode integer,
  country text,
  name text,
  primary key (postalCode, country)
)
```

### Tables Relationships - Foreign Keys
Sometimes it's usefull to declare relationships constraints. For exemple, here's a table that list items in a store and another table that list sales of items:

*Products*
| ItemID | Price | Name         |
|--------|-------|--------------|
| 111    | 7$    | small object |
| 222    | 36$   | big object   |

*Sales*
| ItemID | SalesDate  | Count |
|--------|------------|-------|
| 111    | 2017-07-22 | 3     |
| 222    | 2017-07-21 | 1     |

The *ItemID* in the *Sales* table should already exist in the *product* table because we can't sell something not in stock! I can constraints *Sales*' *ItemID* to already exist in the *Products* table with `REFERENCE tableName(colName)`. `(colName)` is not needed if it has the same name:

```sql
CREATE TABLE sales (
  ItemID integer REFERENCE products, # or REFERENCE products(ItemID)
  SalesDate date,
  Count integer
)
```

*Sales*' *ItemID* is called a **Foreign Key**. It references to another table's column, often a primary key.

What happend if I delete an item in the product table taht break the reference ?
