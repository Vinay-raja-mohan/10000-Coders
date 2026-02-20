-- after insert --> inserted succesfully
-- after update -->updated successfully
-- after delete --> deleted successfully

-- before salary < 60000 error
-- before update new bal > old bal
-- before delete age > 60 error

-- after insert --> inserted succesfully
-- after update -->updated successfully
-- after delete --> deleted successfully

-- before salary < 60000 error
-- before update new bal > old bal
-- before delete age > 60 error

use demodb;

create table  class(id int,name varchar(50),bal float,age int);


create table testing(tran varchar(100),dot datetime default now());

delimiter $$
create trigger t101 before insert on class
for each row
begin
if new.bal<60000 then
signal sqlstate "45000" set message_text= "balance is low than expected";
end if;
end $$

create trigger t102 before update on class
for each row
begin
if new.bal<old.bal then
signal sqlstate "45000" set message_text = "old bal is higher";
end if;
end $$

create trigger t103 before delete on class
for each row
begin
if old.age<61 then
signal sqlstate "45000" set message_text = "not eligible age";
end if;
end $$
delimiter ;

insert into class values(2,"Naga",70000,18);

select * from class;




