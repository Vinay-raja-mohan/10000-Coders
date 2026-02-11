----------nesteed query-------------------------
--Second highest salary from the table
select * from emp where salary =
(select max(salary) from emp where salary <
(select max(salary) from emp));

--third higest salary
select * from emp where salary =
(select max(salary) from emp where salary <
(select max(salary) from emp where salary <
(select max(salary) from emp)));

--20th max salary
select distinct salary from emp order by salary desc limit 1 offset 19;


-----------Correlated Query------------------------
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

