-- Active: 1767583816891@@127.0.0.1@3306@assignments
show tables;
show databases;
create DATABASE assignments;
use assignments;
show tables;

create table student(id int ,student_name varchar(50) not null,phone_number bigint not null);

create table employees(emp_name varchar(10) not null,department varchar(10) not null);

create table users(username varchar(10) unique);

create table customers(email varchar(10) unique);

create table orders(order_status varchar(10) DEFAULT "pending");

create table accounts(created_date date DEFAULT "2026-09-01");

create table products(product_id int auto_increment PRIMARY key);

alter table student auto_increment = 1;

alter table employees add column salary int;

alter table employees add constraint check_salary check (salary > 10000);
alter table employees modify column department varchar(40) default "english";

alter table accounts add column age int;
alter table accounts add constraint check_age check (age>=18);

create table login(email varchar(20) PRIMARY KEY);

alter table products add column price int;
alter table products modify column price int not null,
add constraint check_price check (price > 0);

create table tickets(status varchar(10) default "Open", priority int check (priority >= 1 and priority <= 5));

create table employee_details(emp_id int AUTO_INCREMENT PRIMARY KEY,email varchar(10) unique,emp_name varchar(10) not null);
alter table employee_details auto_increment = 10;


