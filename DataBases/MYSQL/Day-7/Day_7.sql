-- Active: 1767583816891@@127.0.0.1@3306@demodb
show DATABASEs;

create table department(d_id int PRIMARY KEY , dept_name VARCHAR(30));

desc department;

create table employee(e_id int PRIMARY KEY, e_name VARCHAR(50), e_salary float,fd_id int,constraint f_d_id FOREIGN key(fd_id) references department(d_id));

desc employee;

insert into department values(10,'sales'),(20,'hr'),(30,'it');

insert into employee values(101,'vinay',10000,20),(102,'kumar',20200,10);

select * from employee;

select * from employee inner join department on employee.fd_id = department.d_id;

select * from department inner join employee on employee.fd_id = department.d_id;

select e_id,e_name,e_salary,department.dept_name from employee inner join department on employee.fd_id = department.d_id;

select e_name, department.dept_name from employee inner join department on employee.fd_id = department.d_id;

select e_id,e_name,e_salary,department.dept_name from employee inner join department on employee.fd_id = department.d_id where department.dept_name = 'hr';

select count(*),department.dept_name from employee INNER JOIN department on employee.fd_id = department.d_id GROUP BY department.dept_name;
