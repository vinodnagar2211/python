-- use regex;


-- create database regex;
-- USE regex;
-- CREATE table S (
-- Stu_id INT PRIMARY KEY,
-- name VARCHAR (55) NOT NULL
-- );
-- DROP TABLE S;
DESC S;


 
 -- insert into s ( stu_id,name)
--  values
--  (1 , "ram"),
--  (2 , "syam"),
--  (3 , "rohan");
 
 select *
from s;

update s
set name = "rohan lal"
where name = "ram";


create table r (
id int primary key not null ,
name varchar (44),
()
type varchar (33) default "raja ram"
);

desc r;
use regex;
insert into r (id , name )
values
(1 , "ras"),
(2 , "mohan"),
(3 , "rohit") ;

select *
from r;

select Stu_id , concat (Stu_id, name)
from r;

use employees;
 
 select *
 from employees;
 
 select emp_no, concat(emp_no,first_name," @ ",last_name) as fullname
 from employees;
 
 select emp_no, concat_ws( " $ ", first_name,last_name,gender) as full_name
 from employees;
 
 select *
 from employees;
 
 select *
 from employees
 where emp_no between 10003 and 10008;
 
 use employees;
 select *
 from employees;

select first_name, count(*)          from employees       ;

select first_name, count(emp_no)     from employees       ;



select substring(first_name , -2,-5)
from employees;

select *, char_length(first_name)
from employees
where char_length(first_name) > 4  and char_length(first_name) > 6;

 select *
 from employees
 limit 4 , 5 ;
 
 use regex;
 create table ram ( id int primary key auto_increment, 
 marks int ,
 price decimal(5,3)
 );
 describe ram;
 insert into ram (id , marks, price)
 values
 (1,23,12.345),
 (2,34,54.321);
 
 select *
 from ram;
 
 select datediff(curdate() - curdate());
 

select *
from employees;

select emp_no , hire_date , date_add(hire_date , interval 1 month) ,date_sub(hire_date , interval 1 month) 
from employees;

use regex;
select *
from r;
alter table r
add column mob int unique;

alter table r;
rename table naveen to r;

use ig_clone
select *
from photos;

desc photo_tags;


use regex ;

delimiter $$
create procedure sss()
begin
select *
from r ; 
end $$
delimiter ;

call sss();

delimiter $$
create procedure namee ()
begin
select name
from r;
end $$
delimiter ;

call namee();


delimiter $$
create procedure h ( in id int)
begin
select *
from r
where most_id = id;
end $$
delimiter ;

call h(3);

select *
from r;

use employees;
 
--  Select all columns from a table:
 select *
 from employees;
 -- Select specific columns from a table:
 select first_name,last_name
 from employees;
 
--  Select distinct values from a column:
select distinct(first_name)
from employees;
 
--  Filter rows based on a condition:
select *
from employees
where hire_date = "1986-06-26";
 
--  Order rows in ascending order:
select *
from employees
order by hire_date ;

-- Order rows in descending order:
select *
from employees
order by hire_date desc;
 
--  Limit the number of rows returned:
select *
from employees
limit 4;
          -- OR
 SELECT *
 from employees
 limit 4,3;
 
--  Count the number of rows in a table:
select count(*)
from employees;

-- Sum of values in a column:
select sum(emp_no)
from employees;
 
--  Average of values in a column:
select avg(emp_no)
from employees;
 
--  Maximum value in a column:
select max(emp_no)
from employees;

-- Minimum value in a column:
 select min(emp_no)
from employees;

-- Filter rows with NULL values:
select *
from employees
where first_name is null;

-- Filter rows with non-NULL values:
select *
from employees
where first_name  is not null;

-- Join two tables based on a common column:
 
 select *
 from dept as d
 inner join
 emp as e
 on d.dept_id = e.dept_id;
 
 select e.name , d.city
 from dept as d
 inner join
 emp as e
 on d.dept_id = e.dept_id;
 
--  Group rows based on a column:
select gender, count(*)
from employees
group by gender;

-- Select rows with values within a range:
select *
from employees
where emp_no between 10001 and 10015 ;


-- Select rows with values outside a range:
select *
from employees
where emp_no not between 10001 and 10015 ;

select *
from employees;


 
 
 
 
 
 
