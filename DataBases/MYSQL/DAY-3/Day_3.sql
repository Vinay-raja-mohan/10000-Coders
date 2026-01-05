show DATABASES;

CREATE DATABASE demodb;

SHOW DATABASES;

USE demodb;

create table vinay(id int, name varchar(10));

desc vinay;

insert into vinay VALUES (1,'vinay'),(2,'kumar'),(3,'reddy');

alter table vinay add column gender varchar(6) Default 'MALE';

DESC vinay;

select * from vinay;

alter table vinay modify column id int primary key;

desc vinay;

