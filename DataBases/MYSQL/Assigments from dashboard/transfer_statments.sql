-- Active: 1767583816891@@127.0.0.1@3306@assignments
show tables;

create table department(d_id int PRIMARY key,d_name varchar(50));

create table employee (e_id int PRIMARY KEY,e_name varchar(30),e_salary  float,fd_id int,constraint fd_key FOREIGN KEY(fd_id) REFERENCES department(d_id));

INSERT INTO department (d_id, d_name) VALUES
(10, 'HR'),
(20, 'IT'),
(30, 'Finance'),
(40, 'Marketing');


INSERT INTO employee (e_id, e_name, e_salary, fd_id) VALUES
(1, 'Amit', 30000, 10),     
(2, 'Ravi', 45000, 20),     
(3, 'Neha', 50000, 20),     
(4, 'Pooja', 40000, 30),    
(5, 'Kiran', 35000, 40),    
(6, 'Sonal', 38000, 20);    


select * from department;

select * from employee;

select department.d_name,e_name from employee inner join department on employee.fd_id = department.d_id;

select employee.*,department.d_name from employee inner join department on employee.fd_id = department.d_id;

select e_name,department.d_name from employee INNER join department on employee.fd_id= department.d_id where department.d_name = "IT";

select d_name, count(d_name) from department INNER join employee on employee.fd_id= department.d_id GROUP BY d_name;

select e_name,department.d_name,e_salary from employee INNER JOIN department on employee.fd_id= department.d_id where e_salary >= 40000 ORDER BY employee.e_salary ASC;

select e_name,department.d_name,e_date from employee INNER JOIN department on employee.fd_id= department.d_id where e_date > "2020-01-01";

select department.d_name,max(e_salary) from employee inner join department on employee.fd_id= department.d_id group by department.d_name;

select  e_name,department.d_name from employee INNER JOIN department on employee.fd_id= department.d_id where department.d_name like "h%";

select e_name,e_salary,department.d_name from employee INNER JOIN department on employee.fd_id= department.d_id ORDER BY department.d_name desC;





