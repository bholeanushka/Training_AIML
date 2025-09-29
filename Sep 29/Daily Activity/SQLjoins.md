```sql
create database companydb;
use companydb;
```
```sql
create table departments (
dept_id int auto_increment primary key,
dept_name varchar(50) not null
);
```
```sql
create table employees (
emp_id int auto_increment primary key,
emp_name varchar(50),
age int,
salary decimal(10,2),
dept_id int,
foreign key (dept_id) references departments(dept_id)
);
```
```sql
insert into departments(dept_name) values
('IT'),
('HR'),
('Finance'),
('Sales');
```
```sql
INSERT INTO Employees (emp_name, age, salary, dept_id) VALUES
('Rahul', 28, 55000, 1),   -- IT
('Priya', 32, 60000, 2),   -- HR
('Arjun', 25, 48000, 3),   -- Finance
('Neha', 30, 70000, 1),    -- IT
('Vikram', 35, 65000, 4);  --
```
```sql
SET FOREIGN_KEY_CHECKS = 0;
TRUNCATE TABLE departments;
TRUNCATE TABLE employees;
```
```sql
INSERT INTO Departments (dept_name) VALUES
('IT'),         -- id = 1
('HR'),         -- id = 2
('Finance'),    -- id = 3
('Sales'),      -- id = 4
('Marketing');  -- id = 5

INSERT INTO employees (emp_name, age, salary, dept_id) VALUES
('Rahul', 28, 55000, 1),   -- IT
('Priya', 32, 60000, 2),   -- HR
('Arjun', 25, 48000, NULL),-- 
('Neha', 30, 70000, 1),    -- IT
('Vikram', 35, 65000, 4);  -- Sales
```
```sql
select e.emp_name,e.salary,d.dept_name
from employees e 
inner join departments d
on e.dept_id = d.dept_id;

select e.emp_name,e.salary,d.dept_name
from employees e
left join departments d
on e.dept_id = d.dept_id;
```
```sql
select e.emp_name,e.salary,d.dept_name
from employees e
right join departments d
on e.dept_id = d.dept_id;
```
```sql
select e.emp_name,e.salary,d.dept_name
from employees e
left join departments d
on e.dept_id = d.dept_id
union
select e.emp_name,e.salary,d.dept_name
from employees e
right join departments d
on e.dept_id = d.dept_id;
```


 
