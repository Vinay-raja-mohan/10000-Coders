--- 11. Find employees whose salary is greater than the average salary of their department.
select * from emp as e where salary >
(select avg(salary) from emp where Department = e.Department);

--12. Find employees earning the maximum salary in their department.
select * from emp as e where salary =
(select max(salary) from emp where department = e.department);

select count(empid),department from emp group by department;
