-- Database Show Karna 
show databases;
-- Database Create Karna 
create database if not exists collage;
-- Database ko Drop Karna 
drop database if exists student_db;
-- Database ko Use karna
use collage;
-- Database ki All Tables ko Dhekana
show tables;
-- Hum Kis Database me hai ye Cheak Karna
select database();
-- Table Create Karna
create table students(id int ,name varchar(66));
-- Hamare Database me kon-kon si Table hai cheak Karna
show tables;

desc students;

select *
from students;
-- Table me Data Insert Karana
insert into students(id,name)
values
(1,"ram"),
(2,"syam"),
(3,"mohan"),
(4,"sita"),
(5,"gita"),
(6,"seema");
 
insert into students  values (7,"mohan");
select *
from students;

-- Special Column ko hi dhekana 
 select name
 from students;
-- Special Condition ke Sath Kisi Column ko Dhekhana
select *
from students
where id = 4;
-- Old Data ko Update Karna
update students 
set name = "mohan lal"
where id = 3;
-- Data & Table ko Delete karna with Condition
 delete
 from students
 where id in(1,3,5) ;
 
--  full Table Drop Karna
drop table students;

show tables;

create table cus(id int,name varchar(555));

insert into cus(id,name)
values 
(1,"ram"),
(2,null),
(3,"mohan"),
(4,null),
(5,"gita"),
(6,"seema");
-- Column me Null Values ko Dhekhan 
select *
from cus
where  name is not null;

select *
from cus
where  name is null;

-- Column me Default Set Karna 
create table stu(id int,name varchar (55),address varchar(77)  default "kota");
desc stu;
select database();
insert into stu  
values 
(8,"mohan lal"),
(5,"mohan","jaipur");
 
 select*from stu;

