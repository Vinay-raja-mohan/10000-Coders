Procedures : reuse a block of code again and again
            just like a function

delimiter $$
create Procedure procedure_name()
begin
commands
end$$
delimiter;

calling the procedure:
call procedure_name();
exec procedure_name() -- in sql server

delimiter $$
create PROCEDURE age()
begin
select * from emp where age > 35;
end$$
delimiter;


remove the proccedure
drop procedure procedure_name;


use demodb;

delimiter $$
create procedure selecting()
begin
select * from emp;
end$$
delimiter ;

call selecting();


delimiter $$
create procedure up(a int,b int)
begin
update emp set Empid = a where Empid = b;
end $$
delimiter ;

call up(32,34);

select * from emp;

delimiter $$
create procedure new(a int)
begin
delete from	emp where EmpId = a;
end $$
delimiter ;

call new(32);