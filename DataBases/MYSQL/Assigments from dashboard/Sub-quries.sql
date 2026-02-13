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