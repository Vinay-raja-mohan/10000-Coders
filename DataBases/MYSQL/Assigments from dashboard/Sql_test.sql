-- 1.Write a SQL query to find the second highest salary from the Employees table?
select max(salary) from emp where salary <
(select max(salary) from emp);
-- 2.Write a SQL query to find employees who earn more than their manager?
select * from emp where salary >
(select salary from emp where name='manager');
-- 3.Write a SQL query to find the department with the highest average salary?
SELECT department FROM emp GROUP BY department ORDER BY AVG(salary) DESC LIMIT 1;

-- 4.Write a SQL query to find duplicate emails in the table?
SELECT email, COUNT(*) FROM employees GROUP BY email HAVING COUNT(*) > 1;

-- 5.Write a SQL query to rank employees based on salary within each department?
SELECT emp_id, name, department, salary, RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS rank FROM emp;