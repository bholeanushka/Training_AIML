Create table Students (
id int auto_increment primary key,
name varchar(50),
age int,
course varchar(50),
marks int);

Insert into Students (name,age,course,marks)
values ('Rahul',21,'AI',85);
Insert into Students (name,age,course,marks)
values ('Priya',22,'ML',90),('Arjun',20,'DS',78);

select * from Students;
