-- default 
-- update data
-- not null
-- primary key / Foreign key
-- subquery
-- if null
-- is null
-- ========================== Constraint (Primary key,feroign key ,not null, unique, cheak)
-- create table ramu (id int primary key ,name  varchar (55) not null unique ,mob varchar unique  check length(mob) >=10);
-- =========================full outer not commen data[inner join opposit ]
select *
from mohan
cross join ram
where mohan.id is null or ram.id is null;
-- ===========================================================================

-- database create karna
create database regex;

-- database use karana
use regex;

-- Table and database dekhana
show tables;
show databases;  

-- kis database ke in ho ye dekhana
select database();
use regex;

-- table create karna
create table mohan (id int primary key , name varchar(65) not null,address varchar (67));
create table ram (id int primary key , name varchar (54) , email varchar (75));

-- table ki Details dikhna 
desc mohan;

-- database  and Table Drop karna
drop database mohan_lal;
drop table ram;

-- Table me Data insert karna
insert into mohan(id,name,address)
values
(1,"ram","kota"),
(2,"sya","jaipur"),
(3,"sohan","jhalawar");
insert into ram(id,name,email)
values
(1,"ram","ram@gmail.com"),
(2,"sya","sya@gmail.com"),
(3,"sohan","sohan@gmail.com");

-- One Row insert in Table
insert into mohan (id,name,address)
values 
(1,"ram","kota");

-- Data Delete on Tables in condition baseed
delete 
from mohan
where id =1;

-- ===============Concate Functon 
select id,concat(name , "   :   ", address)
from mohan;

-- ===================Concat_WS
select id,concat_ws("  :  ",name,address,id ,name,address)
from mohan;

-- =============================substring  column me se select part nikalna
select id, name, substring(address ,2, 3)
from mohan;

-- =======================Reverse Column ke Reverse karna
select id,name, reverse(name)
from mohan; 

-- ======================Replace give colomn ko Replace 
select id, name ,replace(name,"a","d") as replace_columns
from mohan;

-- ====================== Upper Lower case
select id,name, upper(name), lower(address)
from mohan;

-- ======================Char_length
select id,name, char_length(name), char_length(address)
from mohan;

-- ======================give Column me se Left ye Rigth se Word Nikalna
select id,name ,left(address,2),right(address,2)
from mohan; 

-- ======================Column ke Repeat karana
select id,repeat(id,5)
from mohan;

-- ======================Column me data insert karana
select id,name,insert(name,2,1,"::moooo::")
from mohan;

-- ===============================Distinct
select distinct(name)
from mohan;

-- ===============================like
select *
from mohan
where name like "r%";

-- ===============================order by

-- ===============================count(*)
select count(*)
from mohan;

-- ===============================Limit

-- ===============================Group by/ Having
select name
from mohan
group by name;

-- ===============================Aggregat Functon (Sum,subtract,Avg,min,max)

-- ===============================Relational Operators (>,<,>=,<=,!=)

-- ===============================LOgical Operators (and,or, in, not in,Between,like,is null)
select *
from mohan
where name = "ram" and address = "kota";

select *
from mohan
where name = "ram" or address = "jaipur";

select *
from mohan
where name in ("ram","sya");

select *
from mohan
where name not in ("ram","sya");

select *
from mohan
where id between 1 and 2;
 
 
-- ============================= Case Statement
select id,name,
case
when id = 1 then 5
when id = 2 then 6
else 7
end as count
from mohan;

-- =========== Alter Commend==== (add Column,  remove column,  update Row Data,  table name Rename,column Rename,change Data Type)
 
 -- =================add Column
alter table mohan
add column email varchar(66);

-- =================remove column
alter table mohan 
drop column email;

-- =================update Row Data
update mohan
set address = "jhunjhunu"
where id = 1 ;

-- =================table name Rename
alter table ram_singh
rename mohan; 

-- ==============================column Rename
alter table mohan
rename column address to patta; 

alter table mohan
rename column patta to address; 

-- ================================change Data Type
alter table mohan
modify id varchar (55);

alter table mohan
modify id int;

-- ========================Joins(Corss_Join, Inner_join,full outer not commen data,Natural_join, [outer_join ==>> Left_Join,Right_join,Full outer_Join] only for right not comment,only for right not comment )
select *
from mohan;

select *
from ram;
-- ================Corss_Join Every Product Muliply
select *
from mohan
cross join ram;


-- ================Inner_join 
select *
from mohan as m
inner join ram as r
on m.id = r.id;
-- ===============================================================================================
-- =========================full outer not commen data[inner join opposit ]
select *
from mohan
cross join ram
where mohan.id is null or ram.id is null;
-- ====================================================================================================
===============================Natural join [Commen Entry]
select *
from mohan as m
natural join ram as r
where id ;


select m.id,r.name,m.address,r.email
from mohan as m
inner join ram as r
where m.id = r.id;

-- ================ Right_join
select *
from mohan as m
right join ram as r
on m.id = r.id; 

-- ================Left_Join
select *
from mohan as m
left join ram as r
on m.id = r.id;

-- ================ Full outer_Join [union and union all]
select *
from mohan as m 
right join ram as r
on m.id = r.id
union
select *
from mohan as m 
left join ram as r
on m.id = r.id;

select *
from mohan as m 
right join ram as r
on m.id = r.id
union all
select *
from mohan as m 
left join ram as r
on m.id = r.id;

-- ===================================only for right not commen
select *
from mohan as m
right join ram as r
on m.id = r.id
where m.id is null;
-- ===================================only for left not commen
select *
from mohan as m
left join ram as r
on m.id = r.id
where m.id is null;