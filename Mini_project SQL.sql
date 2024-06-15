 
 -- ============================== MINI PROJECT IN SQL ===============================

create database bank_db;

select database ();

create database if not exists bank_db;

use bank_db;

drop table employees;

create table employees(emp_id int Primary key Auto_increment,
name varchar(66) not null ,
desing varchar(44) default "Probition" ,
dept varchar(66));

desc employees;

insert into employees(emp_id,name,desing,dept)
values
(101,"Raju","Manager","Loan");

insert into employees(name,desing,dept)
values
("Sham","Cashier","Cash"),
("Paul","Associate","Loan"),
("Alex","Accountant","Account"),
("Victor","Associate","Deposit");

select *
from employees;

select emp_id,name
from employees;

select *
from employees
where emp_id  in (101,103);

select *
from employees
where emp_id = 101;

select emp_id,name
from employees
where emp_id = 101;

select *
from employees;

update employees 
set dept = "IT"
where emp_id = 103;

delete
from employees
where emp_id = 102;

-- concat
-- cocat_ws

select substr(name,2,4),substring(name,2,4)
from employees;

select replace(desing,"a","D"),desing
from employees;

select upper(name),lcase(reverse(name)),desing
from employees;

use employees;

select length(first_name), char_length(first_name)
from employees;

select  insert(first_name ,3,0,":ram:")
from employees;

select  first_name,left(first_name,3) ,right(first_name,3)
from employees;


use regex;

show tables;

create table  if not exists coll(emp_id int Primary key Auto_increment,
fname varchar(66) not null ,
lname varchar(44) not null,
desing varchar(44) default "Probition" ,
dept varchar(66));


desc coll;
insert into coll(emp_id,fname,lname, desing,dept) 
values
(101,"Raju","Rastogi","Manager","Loan"),
(102,"Sham","Mohan","Cashier","Cash"),
(103,"Baburao","Apte","Associate","Loan"),
(104,"Paul","Philip","Accountant","Account"),
(105,"Alex","Watt","Associate","Deposit");

select *
from coll;

select concat(emp_id,":",lname,":",desing,":",dept)
from coll;

select concat(emp_id,":",fname ," ",lname,":",desing,":",dept)
from coll;

select concat(emp_id,":",fname,":",upper(desing),":",dept)
from coll;

select concat(upper(left(dept,1)),emp_id," ",fname)
from coll;
select *
from coll;

select distinct(dept)
from coll;

select *
from coll
order by emp_id desc;

select *
from coll
order by emp_id
limit 3;

select *
from coll
where fname like "A%";

select *
from coll
where lname like "____";

select emp_id,fname,lname,desing,dept,length(lname)
from coll 
where length(lname) = 4;


-- sub query 
use employees;

select * 
from salaries
where  salary = (select max(salary)
from salaries);

use regex;

select *
from coll;

select count(emp_id)
from coll;

select dept,count(*)
from coll
group by dept;

select min(emp_id)
from coll;

create view max_query as
select emp_id,fname,lname
from coll
where emp_id = (select max(emp_id)
from coll);

select *
from max_query;

select dept,
count(*),sum(emp_id),avg(emp_id)
from coll
group by dept;
select database();

select *
from cow;
insert into cow(id,name,slary)
values 
(5,"",66),
(6,"null",99);

use regex;
select name, ifnull (name,"5")
from cow;
SELECT name, IFNULL(name, 'No Department') FROM cow;

64








