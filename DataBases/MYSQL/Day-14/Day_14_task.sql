-- Active: 1767583816891@@127.0.0.1@3306@demodb
-- 17. Find employees whose salary equals the second-highest salary in the company.
select * from emp where salary =
(select max(salary) from emp where salary<
(select max(salary) from emp));

-- 18. Find employees whose salary equals the third-highest salary in the company.
select * from emp where salary =
(select max(salary) from emp where salary <
(select max(salary) from emp where salary<
(select max(salary) from emp)));

-- 19. Find employees whose salary is greater than the average salary of employees in Delhi.
select * from emp where salary >
(select avg(salary) from emp where city = 'Delhi')

-- 20. Find employees who earn more than the average salary of employees who are older than 30
select * from emp where salary>
(select avg(salary) from emp where age > 30);

-- 22. Find employees whose salary is greater than the average salary of Finance employees but less than the maximum salary of IT employees.
select * from emp where salary >
(select avg(salary) from emp where department = "finance") and salary < (select max(salary) from emp where department = "IT");

-- 23. Find employees who belong to the department that has the least number of employees.
(select max(s) from emp
(select count(*) as s from emp group by department));

-- 24.( Find employees whose city has more employees than the city of Priya.
select * from emp where city in
(select city from emp group by city having count(*) >
(select count(*) from emp where city = 
(select distinct city from emp where name = "Rohit")));

-- 25. Find employees who belong to the department where the average salary is greater than 55,000.
select * from emp where department in
(select department from emp group by department having avg(salary)>55000);

-- 26. Find employees who earn more than the average salary of all employees but less than the maximum salary of their department.
select * from emp as e where salary > (select avg(salary) from emp) and salary < (select max(salary) from emp as e2 where e.department = e2.department);

-- 27. Find employees whose salary is above the company average and age is below the company average.
select * from emp where salary > (select avg(salary) from emp) and age < (select avg(age) from emp);

