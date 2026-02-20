use demodb;

delimiter $$
create trigger t5 after delete on trigger1
for each row
begin
insert into trigger2(tran) values("bye byee"); 
end$$
delimiter ;

delete from trigger1 where  id = 2;

select * from trigger2;

delimiter $$
create trigger t4 before update on trigger1
for each row
begin
if old.bal>new.bal then
signal sqlstate '45000' set message_text = "old balance is higher";
end if;
end $$
delimiter ;

select * from trigger1;

update trigger1 set bal = 100 where id = 1;



delete from trigger1 where id =2;