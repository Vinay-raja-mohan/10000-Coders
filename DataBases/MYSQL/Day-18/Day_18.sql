-- TCL -- Transaction control language
-- transaction :-- which will perform operations on the table data {insert\update\delete}

-- commit -- will store the data permanenatly
-- rollback -- recover the data which store as temporarily
-- savepoint -- will store the data temporarily

--syntaxes

--commit;
--rollback;
--savepoint reference_name;

use demodb;

create table bank(id int, name varchar(100), amount int);

select * from bank;

insert into bank values (1,'sai',1000);

rollback;

insert into bank values(2,'mohan',2000);

set autocommit = 1;

delete from bank where id = 2;

rollback;

update bank set amount = 1000 where id = 1;
commit;
rollback;

insert into bank values(3,'venkat',3000);
rollback;

begin;
insert into bank values (4,'naga',4000),(5,'venkata',5000);
commit;
rollback;

begin;
delete from bank where id = 5;
savepoint a;
rollback;

begin;
set autocommit = 1;
insert into bank values (6,'vinay',6000);
rollback;


