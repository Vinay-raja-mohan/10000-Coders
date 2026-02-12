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
 
