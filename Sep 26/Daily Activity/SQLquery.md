# School Database Setup and SQL Operations

## 1. Creating the Database
``` sql
CREATE DATABASE schooldb;
USE schooldb;
```
## 2. Creating Table
``` sql
Create table Students (
id int auto_increment primary key,
name varchar(50),
age int,
course varchar(50),
marks int);
```

## 3. Insert Values
``` sql
Insert into Students (name,age,course,marks)
values ('Rahul',21,'AI',85);
```
``` sql
Insert into Students (name,age,course,marks)
values ('Priya',22,'ML',90),('Arjun',20,'DS',78);
```

## 4. Retriving Values
``` sql
select * from Students;
```
## 5. Selecting Specific column
``` sql
select name , marks from Students;
```
## 6. selecting records based on condition
``` sql
select name from Students
where marks > 80;
```

## 7. Updating records
``` sql
Update Students
Set marks = 95, course = "Advance AI"
where id = 2;
select *  from Students;
```
