-- normalaization -> using a unstructured format of a table and converting it into a structured format of a table;

use demodb;

select * from pa;

alter table pa add column sno int first;

set sql_safe_updates =0;

UPDATE pa SET sno = 
CASE
    WHEN name = 'vinay' THEN 1
    WHEN name = 'raj' THEN 2
    WHEN name = 'mohan' THEN 3
    WHEN name = 'gelli' THEN 4
END;

create view subpa as
select distinct sno,name from pa;

select * from subpa;

create view subskill as
select distinct sno,skills from  pa;

select * from subskill;

select * from subpa as sp inner join subskill as sk on sp.sno = sk.sno where sk.skills = 'sql';

alter table pa add column prof varchar(50);

update pa set prof = 
case
when skills = 'java' then 'Ravi'
when skills = 'sql' then 'gopi'
when skills = 'python' then 'ajay'
when skills = 'php' then 'praveen'
end;

create view subprof as
select distinct skills,prof from pa;

select * from subpa as sp inner join subskill as sk on sp.sno = sk.sno inner join subprof as sf on sk.skills = sf.skills;

alter table pa add column psno int;

update pa set psno =
case 
when prof = 'ravi' then 101
when prof = 'gopi' then 102
when prof = 'ajay' then 103
when prof = 'praveen' then 104
end;
