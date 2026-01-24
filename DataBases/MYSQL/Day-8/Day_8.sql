show tables;

select count(*),department.dept_name from employee inner join department on employee.fd_id = department.d_id GROUP BY department.dept_name;

insert into employee values (103,"sai",30000,30),(104,"mohan",25000,10),(105,"raj",45000,20);

select * from employee;

select * from department;

select e_name,e_salary,department.dept_name from employee inner join department on employee.fd_id = department.d_id where e_salary > 20000;

select department.dept_name, max(e_salary) from employee INNER join department on employee.fd_id = department.d_id GROUP BY department.dept_name;


create table courses(c_id int PRIMARY KEY,c_name varchar(30),dura int);

create table students(s_id int PRIMARY KEY,s_name varchar(50),d_join date,fc_id int,constraint fc_id FOREIGN key(fc_id) REFERENCES courses(c_id));

insert into courses values(10,'python',6),(11,'java',7),(13,'c++',2),(16,'mern',3);

select * from courses;

desc students;

insert into students values(101,'sai','2025-12-20',10),(102,'kumar','2026-01-20',13),(103,'mohan','2025-07-20',11);

select * from students;

select * from students inner join courses on students.fc_id = courses.c_id;

select * from students right join  courses on students.fc_id = courses.c_id where students.fc_id is null;

select courses.c_name,count(s_id) from students right join courses on students.fc_id = courses.c_id group by courses.c_name;

insert into students values(104,'raj','2026-01-20',11);

update students set d_join = "2026-09-18" where s_id = 104;

select courses.c_name,max(d_join) from students right join courses on students.fc_id = courses.c_id group by courses.c_name;

select s_name , courses.c_name from students right join courses on students.fc_id = courses.c_id where d_join > "2020-01-01";

select courses.c_name,count(s_name) from students right join courses on students.fc_id = courses.c_id group by courses.c_name;



