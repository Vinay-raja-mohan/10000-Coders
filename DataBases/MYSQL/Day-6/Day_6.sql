use demodb;

select *,sum(amount) over() total,rank() over(order by amount asc)  from bank;