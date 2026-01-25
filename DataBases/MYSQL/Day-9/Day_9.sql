select courses.c_name,count(s_name) from students RIGHT join courses on students.fc_id = courses.c_id group by courses.c_name;

select s_id,s_name,d_join,courses.c_name from students RIGHT JOIN courses on students.fc_id = courses.c_id where d_join > "2025-10-01";

select s_name,courses.c_name from students RIGHT JOIN courses on students.fc_id = courses.c_id ORDER BY c_name asc;

create table customer(c_id int PRIMARY KEY,c_name varchar(50),city varchar(10));
create table orders(or_id int PRIMARY KEY,or_date date,ord_amount int,fc_id int,constraint frn_cid FOREIGN key(fc_id) REFERENCES customer(c_id));

insert into customer values(101,"sai","hyd"),(102,"mohan","knr"),(103,"kumar","sanga"),(104,"raj","ap");

insert into orders values
(201, '2026-01-05', 5000, 101),
(202, '2026-01-10', 12000, 102),
(203, '2026-01-15', 8000, 101),
(204, '2026-02-01', 15000, 103)
(205, '2026-02-10', 6000, 104);

delete from orders where or_id = 204;

select * from customer left join orders on customer.c_id = orders.fc_id;

select customer.* from customer left JOIN orders on customer.c_id = orders.fc_id where orders.fc_id is null;

select c_name,orders.ord_amount from customer LEFT JOIN orders on customer.c_id = orders.fc_id where orders.or_id is null;