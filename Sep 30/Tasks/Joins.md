``` sql
-- CREATE DATABASE
CREATE DATABASE practiceDB;
USE practiceDB;
```
``` sql
-- CREATING TABLES
CREATE TABLE Students (
student_id INT AUTO_INCREMENT PRIMARY KEY,
student_name VARCHAR(50),
city VARCHAR(50)
);

CREATE TABLE Courses (
course_id INT AUTO_INCREMENT PRIMARY KEY,
course_name VARCHAR(100)
);

CREATE TABLE Enrollments (
enrollment_id INT auto_increment primary key,
student_id INT,
course_id INT,
grade DECIMAL(10,2),
FOREIGN KEY(student_id) REFERENCES Students (student_id),
FOREIGN KEY(course_id) REFERENCES Courses(course_id)
);
```
``` sql
-- INSERTING VALUES IN TABLES
INSERT INTO Students (student_name,city) VALUES
('Rohit','Pune'),
('Shreya','Pune'),
('Anushka','Mumbai'),
('Soham', 'Delhi');

INSERT INTO Courses(course_name) VALUES 
('AI'),
('DS'),
('ML');

INSERT INTO Enrollments(student_id ,course_id ,grade) VALUES
(1,2,80),
(3,1,90),
(2,1,70),
(4,3,85);
```
``` sql
-- RETRIVING VALUES
SELECT * FROM Students;
SELECT * FROM Courses;
SELECT * FROM Enrollments;
```
``` sql
-- LIST ALL STUDENTS
DELIMITER //
CREATE PROCEDURE ListAllStudents()
BEGIN
SELECT * FROM Students;
END //
DELIMITER ;
```
``` sql
-- LIST ALL COURSES
DELIMITER //
CREATE PROCEDURE ListAllCourses()
BEGIN
SELECT * FROM Courses;
END //
DELIMITER ;
```
``` sql
--  FIND STUDNET BASED ON CITY
DELIMITER //
CREATE PROCEDURE FindStudentsByCity(IN cityname VARCHAR(50))
BEGIN
SELECT * FROM Students
WHERE city = cityname;
END //
DELIMITER ;
```
``` sql
CALL ListAllStudents();
CALL ListAllCourses();
CALL FindStudentsByCity('Pune');
```
``` sql
-- STUDNETS WITH ENROLLED COURSES
DELIMITER //
CREATE PROCEDURE ListStudnetsWithCourses()
BEGIN
SELECT s.student_name,c.course_name FROM Students s
JOIN Enrollments e ON s.student_id = e.student_id
JOIN Courses c ON e.course_id = c.course_id;
END //
DELIMITER ;

CALL ListStudnetsWithCourses();
```
``` sql
-- STUDENTS ENROLLED IN PARTICULAR COURSE
DELIMITER //
CREATE PROCEDURE ListStudnetsByCourses(IN cid INT)
BEGIN
SELECT s.student_name,c.course_name FROM Students s
JOIN Enrollments e ON s.student_id = e.student_id
JOIN Courses c ON e.course_id = c.course_id
WHERE c.course_id = cid;
END //
DELIMITER ;

CALL ListStudnetsByCourses(1);
```
``` sql
-- NUMBER OF STUDENTS IN A COURSE
DELIMITER //
CREATE PROCEDURE CountStudnetsInCourse()
BEGIN
SELECT c.course_name, COUNT(e.student_id)
FROM Courses c
LEFT JOIN Enrollments e ON c.course_id = e.course_id
GROUP BY c.course_id , c.course_name;
END //
DELIMITER ;

CALL CountStudnetsInCourse();
```
``` sql
-- STUDENTS ALONG WITH GRADES
DELIMITER //
CREATE PROCEDURE ListStudnetsWithCoursesGrades()
BEGIN
SELECT s.student_name,c.course_name , e.grade FROM Students s
JOIN Enrollments e ON s.student_id = e.student_id
JOIN Courses c ON e.course_id = c.course_id;
END //
DELIMITER ;

CALL ListStudnetsWithCoursesGrades()
```
``` sql
-- FIND COURSES STUDENT IS ENROLLED IN
DELIMITER //
CREATE PROCEDURE ListCoursesByStudnets(IN sid INT)
BEGIN
SELECT s.student_name,c.course_name FROM Students s
JOIN Enrollments e ON s.student_id = e.student_id
JOIN Courses c ON e.course_id = c.course_id
WHERE s.student_id = sid;
END //
DELIMITER ;

CALL ListCoursesByStudnets(2);
```
``` sql
-- AVERAGE GRADES PER COURSE
DELIMITER //
CREATE PROCEDURE AverageGradeperCount()
BEGIN
SELECT c.course_name, AVG(e.grade) AS avg_grade
FROM Courses c
LEFT JOIN Enrollments e ON c.course_id = e.course_id
GROUP BY c.course_name;
END //
DELIMITER ;

CALL AverageGradeperCount();
```



