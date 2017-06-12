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

Bad: we can't use `count` and others agregations
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

--> 2rows/1column
food
---
plants
insects
```

Even if we ask a simple calcul to the database, it will return an one row/ one column table:
```sql
select 2+2 as sum

--> 1row/1column
sum
---
4
```

```sql
select 2+2, 4+4, 6+6

--> 1rows/3columns
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
    on animal.species = diet.species -- statement to specify how to match up the rows from one table to the rows of the other one
where food = 'fish';

-- The result will be a 2r/1c table:
count
---
20
```

##




# Lesson 2: Elements of SQL
- Begin learning SQL, the Structured Query Language used by most relational databases.
- Learn about the select and insert statements, the basic operations for reading and writing data.
- Learn about the operators and syntax available to get the database to scan and join tables for you.


# Lesson 3: Python DB-API
- Learn how to access a relational database from Python code.
- Use a virtual machine (VM) to run a Python web application with a database.
- Common security pitfalls of database applications, including the famous Bobby Tables.

# Lesson 4: Deeper Into SQL
- Learn how to design and create new databases.
- Learn about normalized design, which makes it easier to write effective code using a database.
- Learn how to use the SQL join operators to rapidly connect data from different tables.
