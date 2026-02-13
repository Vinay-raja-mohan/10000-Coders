-- triggers:- will store the action which operation will done in  another table;

delimiter $$
create trigger trigger_name
[before | after] [insert|update|delete] on table_name
for each row
begin
-- command
end$$
delimiter ;


use demodb;

create table trigger1(
id int,
name varchar(50),
bal int
);

create table trigger2(
tran varchar(100),
dot datetime default now()
);

select * from  trigger1;
select * from  trigger2;

-- t1
delimiter $$
create trigger t1 after insert on trigger1
for each row
begin
insert into trigger2(tran) values('Credited Sucessfully');
end$$
delimiter ;

-- t2
delimiter $$
create trigger t2 before insert on trigger1
for each row
begin
if new.bal<0 then
signal sqlstate '45000' set message_text = 'low balance';
end if;
end$$
delimiter ;

-- t3
delimiter $$
create trigger t3 after update on trigger1
for each row
begin
insert into trigger2(tran) values("Updated Successfully");
end$$
delimiter ;



insert into trigger1 values (1,'naidu',200);

update trigger1 set bal = 500 where id =2;

