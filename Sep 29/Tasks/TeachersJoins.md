# SQL Joins on SchoolDB
```sql
-- CREATE DATABASE
create database SchoolDB;
Use SchoolDB;
```
```sql
-- CREATE TABLES
create table Teachers (
teacher_id int auto_increment primary key,
teacher_name varchar(50),
subject_id int
);

create table subjects(
subject_id int auto_increment primary key,
subject_name varchar(50)
);
```
```sql
-- INSERTING VALUES WITH BAD DATA
INSERT INTO Subjects (subject_name) VALUES
('Mathematics'),   -- id = 1
('Science'),       -- id = 2
('English'),       -- id = 3
('History'),       -- id = 4
('Geography');     -- id = 5 (no teacher yet)

INSERT INTO Teachers (teacher_name, subject_id) VALUES
('Rahul Sir', 1),   -- Mathematics
('Priya Madam', 2), -- Science
('Arjun Sir', NULL),-- No subject assigned
('Neha Madam', 3);  -- English
```
```sql
-- INNER JOIN
select t.teacher_name,s.subject_name
from Teachers t
inner join Subjects s
on t.subject_id = s.subject_id;
```
```sql
-- LEFT JOIN
select t.teacher_name,s.subject_name
from Teachers t
Left join Subjects s
on t.subject_id = s.subject_id;
```sql
-- RIGHT JOIN
select t.teacher_name,s.subject_name
from Teachers t
right join Subjects s
on t.subject_id = s.subject_id;
```
```sql
-- FULL JOIN
select t.teacher_name,s.subject_name
from Teachers t
left join Subjects s
on t.subject_id = s.subject_id
union
select t.teacher_name,s.subject_name
from Teachers t
right join Subjects s
on t.subject_id = s.subject_id;
```
