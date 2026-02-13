-- 1. Find employees whose salary is greater than the average salary of all employees.
select * from emp where salary >
(select avg(salary) from emp);

-- 2. Find employees whose age is less than the youngest employee in the HR department.
select * from emp where age <
(select min(age) from emp where department = "HR");

-- 3. Find employees living in the same city as Ravi
select * from emp where city = 
(select city from emp where name = 'ravi');

-- 4. Find employees with the same salary as Karan
select * from emp where salary = 
(select salary from emp where name='karan');

-- 5. Find employees earning more than Sneha
select * from emp where salary >
(select salary from emp where name = 'sneha');

-- 6. Find employees working in the same department as Nisha
select * from emp where Department = 
(select department from emp where name = 'Nisha');

--7. Find employees who live in the same cities as Finance department employees.
select * from emp where city in
(select city from emp where department = "Finance");

--8. Find employees older than any employee in the Sales department.
select * from emp where age >
(select min(age) from emp where department = 'Sales');

--9. Find employees earning more than all employees in HR.
select * from emp where salary >
(select max(salary) from emp where department = "HR");

--10. Find employees working in a department where at least one employee earns more than 70,000.
select * from emp where department in 
(select department from emp where salary > 70000);

----------------------Correlated queries----------------------

--- 11. Find employees whose salary is greater than the average salary of their department.
select * from emp as e where salary >
(select avg(salary) from emp where Department = e.Department);

--12. Find employees earning the maximum salary in their department.
select * from emp as e where salary =
(select max(salary) from emp where department = e.department);

-- 13. Find employees earning the minimum salary in their department.
select * from emp as e where salary =
(select min(salary) from emp where department = e.department)

-- 14. Find employees older than the average age of their department.
select * from emp as e where age >
(select avg(age) from emp where department = e.department);

-- 15. Find employees who have the same city as at least one of their department colleagues.
SELECT * FROM emp e WHERE EXISTS
(SELECT 1 FROM emp WHERE department = e.department AND city = e.city AND EmpID != e.EmpID);

-- 16. Find the city with the maximum number of employees.

select city from emp group by city having count(*) = 
(SELECT MAX(cnt) FROM 
(SELECT COUNT(*) AS cnt FROM emp GROUP BY city) y);


--------------------------nested subqueries--------------
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


