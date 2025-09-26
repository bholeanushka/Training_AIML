# Employee Table and SQL Operations

## 1. Creating Table
``` sql
Create table Employees(
id int auto_increment primary key,
name varchar(50) not null,
age int,
department varchar(50),
salary decimal(10,2)
);
```

## 2. Insert Values
``` sql
Insert into Employees (name,age,department,salary)
values ('Priya',22,'HR',90000),
('Arjun',20,'Sales',78000),
('Prajakta',25,'Consulting',1500000),
('Rohit',22,'Consulting',680000)
;
select * from Employees;
```

## 3. Retriving Values
``` sql
select name from Employees
where salary > 90000;
```

## 4. Updating records
``` sql
Update Employees
Set salary = 950000, department = "HR"
where id = 2;
select *  from Employees;
```
## 5. Delelting Values
``` sql
Delete from Employees where id = 2;
select *  from Employees;
```
