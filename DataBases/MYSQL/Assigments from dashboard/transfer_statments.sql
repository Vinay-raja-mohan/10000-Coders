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

--- RIGHT JOIN ---
create table course(c_id int PRIMARY key,c_name varchar(50),duration int);
insert into course values (101,"Python",3),(102,"java",4),(103,"Sql",2),(104,"AI",6),(105,"web dev",5);

create table student (s_id int PRIMARY key,s_name varchar(50),sc_id int,j_date date);

insert into student
values (1,"Amit",101,"2024-01-10"),
        (2,"Ravi",102,"2023-12-15"),
        (3,"Neha",101,"2024-02-05"),
        (4,"Pooja",103,"2024-03-01"),
        (5,"Kiran",102,"2024-01-25"),
        (6,"Anvi",106,"2024-10-10");

select * from course right join student on course.c_id = student.sc_id;

select course.c_name,s_name from student right join course on course.c_id = student.sc_id;

select c.c_name , s.s_name from student as s right join course as c on c.c_id = s.sc_id where s_name is null;

select course.c_name,s_name from student right join course on course.c_id = student.sc_id;

select course.c_name,count(student.s_id) from student right join course on course.c_id = student.sc_id group by course.c_name;

select course.c_name ,max(j_date) from student right join course on course.c_id = student.sc_id group by course.c_name;

select c_name,student.* from course RIGHT join student on student.sc_id = course.c_id where c_name is not null;

select course.c_name,s_name,j_date from student right join course
on course.c_id = student.sc_id where j_date > "2024-01-01";

select course.c_name, s_name from student right join course on course.c_id = student.sc_id 
where student.s_name is not null
order by course.c_name asc ;

show tables;


