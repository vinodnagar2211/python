----------------------- Complite Tops ---------------------------
select concat_ws( "%", "name","address") fullname
from mohan;

select insert(address,2,1,"mohanlal")
from mohan;

select substring(address ,1,2)
from mohan;

select  replace(address ,"kota","jaipur")
from mohan;

create database software;
use regex;
show databases;
show tables;
-- kis database in work current time
select database();
drop database software;
use regex;
create table mohan
(id int primary key , 
name varchar(55), 
address varchar (55),
email varchar (55));

show tables;
drop table mohan;
desc r;
describe mohan ;
select *
from mohan;

create table mohan ( id int primary key , name varchar(55), m_numbe int);

insert into mohan ( id , name, m_numbe)
values
(1,"vijay", 234567),
(2,"vuuijay", 27734567),
(3,"vihhjay", 23554567);

use regex;

select *
from r;
 
use regex;
select *
from mohan;

drop table mohan;
update r
set name = "mom"
where most_id = 1;

delete 
from mohan
where id = 1;

delete 
from mohan;

create table mohan ( id int primary key ,
name  varchar (44) unique not null ,
address varchar (55) default  "jaipur");

select *
from mohan ;

insert into mohan ( id , name ,address)
values 
(1,"ram","kota"),
(2,"syam","kota"),
(3,"mohan","kota"),
(4,"nanu","jaipur");

select *
from mohan;

select concat(name , ":" , address)
from mohan;

select concat_ws( "%", "name","address") fullname
from mohan;

select insert(address,2,1,"mohanlal")
from mohan;

select substring(address ,1,2)
from mohan;

select  replace(address ,"kota","jaipur")
from mohan;

select reverse(address)
from mohan;

select char_length(address)
from mohan;

select insert(address,2,1,"mohanlal")
from mohan;

select left(address,3)
from mohan;

select right(name , 3)
from mohan;

select repeat(address ,4)
from mohan;

select trim("                                ram     ");

use employees;

select count(*)
from employees;

select count(distinct(first_name))
from employees;

select *
from employees;

select *
from employees
where first_name like "_a_%";

select first_name, count(emp_no)
from employees
group by first_name;

select first_name, count(emp_no)
from employees
group by first_name
having count(emp_no)>250;


select ifnull (first_name  , "5")
from employees;



select *
from employees
where first_name  is not null ;