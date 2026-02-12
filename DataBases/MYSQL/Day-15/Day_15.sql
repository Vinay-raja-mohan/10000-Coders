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