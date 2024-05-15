-- 1. Write a SQL query to fetch “FIRST_NAME” from the Student table in upper case and use ALIAS name as STUDENT_NAME
select UPPER(FIRST_NAME) AS STUDENT_NAME from student;

-- 2. Write a SQL query to fetch unique values of MAJOR Subjects from Student table.
select distinct(major)
from student;

select *
from student
group by (major);

use employees;
select *
from employees;
select distinct(first_name)
from employees;

select first_name
from employees
group by first_name;

-- 3. Write a SQL query to print the first 3 characters of FIRST_NAME from Student table.
select first_name,upper(right(first_name, 3)) , left(first_name , 3);
                -- or
select substring(first_name ,1,4)
from employees;


SELECT first_name, RIGHT(first_name, 3), LEFT(first_name, 3) 
FROM employees;

-- ==================================================================================================
-- Write a SQL query to find the position of alphabet (‘a’) int the first name column ‘Shivansh’ from Student table.
-- SELECT INSTR(FIRST_NAME, 'a') FROM Student WHERE FIRST_NAME = 'Shivansh'; 
-- =========================================================================================

--  Write a SQL query that fetches the unique values of MAJOR Subjects from Student table and print its length.

select first_name, length(first_name)
from employees;

--  Write a SQL query to print FIRST_NAME from the Student table after replacing ‘a’ with ‘A’.
select first_name , replace(first_name ,"a" , "@@@@@")
from employees;

-- Write a SQL query to print the FIRST_NAME and LAST_NAME from Student table into single column COMPLETE_NAME.
select concat(first_name , " : ", last_name),concat_ws(" %% ",first_name , last_name)
from employees;

-- 8. Write a SQL query to print all Student details from Student table order by FIRST_NAME Ascending and MAJOR Subject descending .
select *
from employees
order by first_name asc , last_name desc ;


-- 9. Write a SQL query to print details of the Students with the FIRST_NAME as ‘Prem’ and ‘Shivansh’ from Student table.
select *
from employees
where first_name  in( 'prem','shivansh');

-- 10. Write a SQL query to print details of the Students excluding FIRST_NAME as ‘Prem’ and ‘Shivansh’ from Student table.
select *
from employees
where first_name in ("prem" , "shivansh");

-- 11. Write a SQL query to print details of the Students whose FIRST_NAME ends with ‘a’.
select *
from employees
where first_name like  "%a";
-- @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@    
-- 12. Write an SQL query to print details of the Students whose FIRST_NAME ends with ‘a’ and contains six alphabets.

select first_name, length(first_name) 
from employees
where first_name like "%a" and length(first_name) = 6 ;

-- what is different both are code tell me wirte now

-- book ===============SELECT * FROM Student WHERE FIRST_NAME LIKE '%_____a';

-- @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@    

-- 13. Write an SQL query to print details of the Students whose GPA lies between 9.00 and 9.99.
select *
from employees
where first_name between 'b' and 'd' ;
-- where hire_date between '1989-06-02' and '1991-06-02';
-- where  emp_no between 100005 and 100010;

-- 14. Write an SQL query to fetch the count of Students having Major Subject ‘Computer Science’.
 select last_name, count(*)
 from employees
 where last_name = "Simmel";

-- 15. Write an SQL query to fetch Students full names with GPA >= 8.5 and <= 9.5.
 select emp_no, concat(first_name,"  ",last_name) as full_name
 from employees
 where emp_no >= 10005 and emp_no <= 10009  ;
 
--  16. Write an SQL query to fetch the no. of Students for each MAJOR subject in the descending order.
select first_name , count(*)
from employees
group by first_name 
order by count(*) desc;

-- Display the details of students who have received scholarships, including their names, scholarship amounts, and scholarship dates.

select e.emp_no,e.first_name,e.last_name,e.gender,s.salary,e.birth_date
from employees as e
inner join 
salaries as s
on e.emp_no = s. emp_no;

-- 18. Write an SQL query to show only odd rows from Student table.
select *
from employees
where emp_no % 2 != 0;

-- 19. Write an SQL query to show only even rows from Student table.
select *
from employees
where emp_no % 2 = 0;
-- @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@    
-- 20. List all students and their scholarship amounts if they have received any. If a student has not received a scholarship, display NULL for the scholarship details.
 
 SELECT 
    Student.FIRST_NAME,
    Student.LAST_NAME,
    COALESCE(Scholarship.SCHOLARSHIP_AMOUNT, NULL) AS SCHOLARSHIP_AMOUNT,
    COALESCE(Scholarship.SCHOLARSHIP_DATE, NULL) AS SCHOLARSHIP_DATE
FROM 
    Student
LEFT JOIN 
    Scholarship ON Student.STUDENT_ID = Scholarship.STUDENT_REF_ID;
-- @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@    

-- 21. Write an SQL query to show the top n (say 5) records of Student table order by descending GPA.
select *
from employees
order by emp_no desc
limit 5;

-- @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
-- 22. Write an SQL query to determine the nth (say n=5) highest GPA from a table.
SELECT * FROM Student ORDER BY GPA DESC LIMIT 5, 1;

-- 23. Write an SQL query to determine the 5th highest GPA without using LIMIT keyword.
SELECT * FROM Student s1 
WHERE 4 = (
    SELECT COUNT(DISTINCT (s2.GPA)) 
    FROM Student s2
    WHERE s2.GPA >= s1.GPA
);

-- @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

-- 24. Write an SQL query to fetch the list of Students with the same GPA.
select *
from employees
where first_name = "Parto";

select first_name
from employees
group by first_name 
having first_name = "parto";

SELECT s1.* FROM Student s1, Student s2 WHERE s1.GPA = s2.GPA AND s1.Student_id != s2.Student_id;

-- @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
-- 25. Write an SQL query to show the second highest GPA from a Student table using sub-query.

select max(salary)
from salaries
where salary not in (
select max(salary)
from salaries
);

select salary
from salaries
order by salary desc
limit 1,1;

-- 26. Write an SQL query to show one row twice in results from a table.

SELECT * FROM employees 
UNION ALL
SELECT * FROM employees ORDER BY emp_no
limit 2;

-- 27. Write an SQL query to list STUDENT_ID who does not get Scholarship.
select *
from salaries
where salary not in (38623,38735,38786);

-- @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ 
-- 28. Write an SQL query to fetch the first 50% records from a table.
SELECT * FROM employees WHERE emp_no <= (SELECT COUNT(emp_no)/2 FROM employees);


SELECT * FROM Student WHERE STUDENT_ID <= (SELECT COUNT(STUDENT_ID)/2 FROM Student);
-- @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

-- 29. Write an SQL query to fetch the MAJOR subject that have less than 4 people in it. 
select first_name,count(*)
from employees
group by first_name
having count(*)<250;

-- 30. Write an SQL query to show all MAJOR subject along with the number of people in there.
select first_name,count(*)
from employees
group by first_name;

-- 31. Write an SQL query to show the last record from a table.
select *
from employees
order by emp_no desc
limit 1;

SELECT * FROM employees WHERE emp_no = (SELECT MAX(emp_no) FROM employees);

-- 32. Write an SQL query to fetch the first row of a table.
-- @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
-- 33. Write an SQL query to fetch the last five records from a table.
select *
from employees
order by emp_no desc
limit 5;

SELECT * 
FROM (
    SELECT * 
    FROM Student 
    ORDER BY STUDENT_ID DESC 
    LIMIT 5
) AS subquery
ORDER BY STUDENT_ID;
-- @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
-- 34. Write an SQL query to fetch three max GPA from a table using co-related subquery.

SELECT DISTINCT GPA FROM Student S1 
WHERE 3 >= (SELECT COUNT(DISTINCT GPA) FROM Student S2 WHERE S1.GPA <= S2.GPA) ORDER BY S1.GPA DESC;
-- @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

-- https://www.geeksforgeeks.org/sql-query-interview-questions/

