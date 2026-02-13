delimiter $$
create procedure P1 (a int)
begin
insert into vinay(id) values(a);
end$$
delimiter ;

call P1(9);

select * from vinay;

delimiter $$
create procedure P2(n varchar(50),a int)
begin
update vinay set name = n where id = a;
end$$
delimiter ;

call P2('hello',9);

delimiter $$
create PROCEDURE P3 (i int)
begin
delete from vinay where id = i;
end$$
delimiter ;

call P3(9)

