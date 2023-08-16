#  0x0D. SQL - Introduction
# Database Basics and MySQL Guide

This README provides an introduction to database concepts, relational databases, SQL, and basic MySQL operations.

## What's a Database?

A **database** is a structured collection of data that allows for efficient storage, retrieval, and manipulation of information.

## What's a Relational Database?

A **relational database** organizes data into tables with rows and columns. It uses keys to define relationships between tables.

## What Does SQL Stand For?

**SQL** stands for Structured Query Language. It's used for managing and manipulating relational databases.

## What's MySQL?

**MySQL** is an open-source Relational Database Management System (RDBMS) that uses SQL for querying and management.

## Creating a Database in MySQL

To create a database, use the SQL command:
```sql
CREATE DATABASE database_name;
DDL and DML
DDL (Data Definition Language) deals with defining and managing database structures.
DML (Data Manipulation Language) deals with manipulating data stored in the database.
Creating and Altering Tables
To create a table:

sql
Copy code
CREATE TABLE table_name (
    column1 datatype,
    column2 datatype,
    ...
);
To alter a table:

sql
Copy code
ALTER TABLE table_name
    ADD column_name datatype;
Retrieving Data (SELECT)
To retrieve data from a table:

sql
Copy code
SELECT column1, column2
FROM table_name
WHERE condition;
Inserting, Updating, and Deleting Data
To insert data into a table:

sql
Copy code
INSERT INTO table_name (column1, column2)
VALUES (value1, value2);
To update data in a table:

sql
Copy code
UPDATE table_name
SET column1 = new_value
WHERE condition;
To delete data from a table:

sql
Copy code
DELETE FROM table_name
WHERE condition;
Subqueries
Subqueries are nested queries used within other queries to retrieve data based on the results of another query.

Using MySQL Functions
MySQL provides various built-in functions for calculations, string manipulation, date/time operations, etc. Example
