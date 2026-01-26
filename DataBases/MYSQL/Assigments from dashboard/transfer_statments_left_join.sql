CREATE TABLE customer (c_id INT PRIMARY KEY,c_name VARCHAR(50),city VARCHAR(50));

CREATE TABLE orders (o_id INT PRIMARY KEY,c_id INT,amount INT,order_date DATE);

INSERT INTO customer VALUES
(1, 'Amit', 'Hyderabad'),
(2, 'Ravi', 'Chennai'),
(3, 'Neha', 'Bengaluru'),
(4, 'Pooja', 'Mumbai'),
(5, 'Kiran', 'Delhi');

INSERT INTO orders VALUES
(101, 1, 2500, '2024-01-10'),
(102, 1, 4000, '2024-02-15'),
(103, 2, 1500, '2023-12-20'),
(104, 3, 5000, '2024-03-05'),
(105, 3, 3200, '2024-03-20');


select * from customer LEFT JOIN orders on customer.c_id=orders.c_id;

select c_name,orders.o_id from customer LEFT JOIN orders on customer.c_id = orders.c_id where o_id is  null;

select c_name,orders.amount from customer LEFT JOIN orders on customer.c_id = orders.c_id where orders.amount is null;

select c_name,orders.order_date from customer LEFT JOIN orders on customer.c_id = orders.c_id;

select c_name,count(orders.o_id) from customer LEFT JOIN orders on customer.c_id = orders.c_id GROUP BY customer.c_id;

select c_name,max(orders.order_date) from customer LEFT JOIN orders on customer.c_id = orders.c_id group by customer.c_id,customer.c_name;

select customer.c_name,count(orders.c_id) from customer LEFT join orders on customer.c_id = orders.c_id group by customer.c_id having  count(orders.c_id)>1;

select customer.c_name,orders.amount from customer left join orders on orders.c_id = customer.c_id where orders.amount > 3000 or orders.c_id is null;