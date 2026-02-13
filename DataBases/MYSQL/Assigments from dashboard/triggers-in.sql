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