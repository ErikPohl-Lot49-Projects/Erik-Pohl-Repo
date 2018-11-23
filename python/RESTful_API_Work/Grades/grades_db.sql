 create table courses (
 course_id int primary key,
 course_name varchar2(1000),
 prereq_id int, 
 createdby int,
 creationdate date
 );
 
  create table students (
 student_id int primary key,
 student_lname varchar2(1000),
  student_fname varchar2(1000),
 createdby int,
 creationdate date
 );
 
create table grades (
grade_id int primary key,
student_id int,
course_id int,
numeric_grade int,
createdby int,
creationdate date
);

 
 
 
 
