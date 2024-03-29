
use employees;

-- Sure, here are 10 basic SQL practical questions along with their solutions:

-- 1 Select all records from a table:
select *
from employees;

-- 2 Select specific columns from a table
select emp_no,first_name
from employees;

-- 3  Select distinct values from a column
select   distinct(first_name) , first_name as name
from employees;

-- 4 Filter records based on a condition
 select *
 from employees
 where first_name = "georgi";

-- 5 Order records in ascending order
select *
from employees
order by first_name , last_name;

-- 6 Order records in descending order
select *
from employees
order by first_name , last_name desc;

 --  7 Count the number of records in a table:
 
select count(first_name) , count(*)
from employees;

-- 8 find the maximum value in a column 
select max(emp_no)
from employees;

-- 9  Find the minimum value in a column
select min(emp_no)
from employees;

-- 10  Group records and apply aggregate functions
select gender ,count(*)
from employees
group by gender;