-------Views--------
-- Creates a virtual table for the main table, 
-- So that we can easily access the table
-- Save the time
-- Provide security by giving names

-- create view view_name as
-- command

-- select * from view_name


create view new_view as
select * from emp where department = 'it';

select * from new_view where age>30 order by age desc;

create view hr as
select * from emp where department = 'hr';

select * from hr;

create view salary as
select * from emp where salary > 70000;

select * from salary order by salary asc;

insert into emp values (31,'Vinay','HR',80000,33,'Hyderabad');

select * from hr;

show databases;

use information_schema;

show tables;

select * from views where table_schema = 'demodb';
