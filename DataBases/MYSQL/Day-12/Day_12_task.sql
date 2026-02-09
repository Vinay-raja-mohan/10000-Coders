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

------------------------------------------------------------------------------------------------------------
--Practice
--Find employees whose salary is greater than Sneha’s salary.
select * from emp where salary > 
(select salary from emp where name = "sneha");

--Find employees who are older than the youngest employee in the HR department.
select * from emp where age >
(select min(age) from emp where department = 'HR');

--Find employees working in the same department as Nisha.
select * from emp where department = 
(select department from emp where name = "Nisha");

-- Find employees earning more than the average salary of the IT department.
select * from emp where salary >
(select avg(salary) from emp where department = "IT");

-- Find employees whose salary equals the maximum salary in the Sales department.
select * from emp where salary =
(select max(salary) from emp where department = "Sales");

-- Find employees who live in the same city as Ravi.
select * from emp where city = 
(select city from emp where name = "Ravi");

-- Find employees earning less than the highest salary in the HR department.
select * from emp where salary <
(select max(salary) from emp where department = "HR");

-- Find employees whose age is greater than the average age of all employees.
select * from emp where age>
(select avg(age) from emp);

----------------------------------------------------------------------------------------------------------------

-- Find employees working in departments where at least one employee earns more than 70,000.
select * from emp where department in
(select department from emp where salary > 70000);

-- Find employees who live in cities where Finance department employees live.
select * from emp where city in
(select city from emp where department = "Finance");

--Find employees earning more than all employees in the HR department.
select * from emp where salary >
(select max(salary) from emp where department = 'HR');

-- Find employees whose salary is greater than any employee in the Sales department.
select * from emp where salary >
(select min(salary) from emp where department = "Sales");

-- Find employees working in departments that have more than one employee.
select * from emp where department in
(select department from emp group by department having count(*)>1);

-- Find employees whose city appears in more than one department.
select * from emp where city in
(select city from emp group by city having count(distinct department)>1);

-- Find employees who earn the same salary as someone in a different department.
(select salary from emp );