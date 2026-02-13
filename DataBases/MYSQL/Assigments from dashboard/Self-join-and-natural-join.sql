-- CREATE TABLES
CREATE TABLE Categories (
    category_id INT PRIMARY KEY AUTO_INCREMENT,
    category_name VARCHAR(100) NOT NULL,
    description TEXT
);

CREATE TABLE Customers (
    customer_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    phone_number VARCHAR(15),
    address TEXT,
    date_joined DATE
);

CREATE TABLE Products (
    product_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2),
    stock_quantity INT,
    category_id INT,
    FOREIGN KEY (category_id) REFERENCES Categories(category_id)
);

CREATE TABLE Orders (
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT NOT NULL,
    order_date DATE,
    total_amount DECIMAL(10, 2),
    shipping_address TEXT,
    payment_status VARCHAR(20),
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);

CREATE TABLE Order_Items (
    order_item_id INT PRIMARY KEY AUTO_INCREMENT,
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT,
    item_price DECIMAL(10, 2),
    FOREIGN KEY (order_id) REFERENCES Orders(order_id),
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
);

-- INSERT sample data
INSERT INTO Categories VALUES
(1, 'Electronics', 'Electronic devices and gadgets'),
(2, 'Clothing', 'Apparel and fashion items'),
(3, 'Books', 'Books and educational materials');

INSERT INTO Customers VALUES
(1, 'John', 'Doe', 'john@email.com', '9876543210', '123 Main St, New York', '2023-01-15'),
(2, 'Jane', 'Smith', 'jane@email.com', '9876543211', '456 Oak Ave, Los Angeles', '2023-02-20'),
(3, 'Mike', 'Johnson', 'mike@email.com', '9876543212', '789 Pine Rd, Chicago', '2023-03-10'),
(4, 'Sarah', 'Williams', 'sarah@email.com', '9876543213', '321 Elm St, Houston', '2023-04-05'),
(5, 'David', 'Brown', 'david@email.com', '9876543214', '654 Maple Dr, Phoenix', '2023-05-12');

INSERT INTO Products VALUES
(1, 'Laptop', 'High performance laptop', 999.99, 15, 1),
(2, 'Mouse', 'Wireless mouse', 29.99, 50, 1),
(3, 'T-Shirt', 'Cotton t-shirt', 19.99, 100, 2),
(4, 'Jeans', 'Blue denim jeans', 49.99, 75, 2),
(5, 'Python Book', 'Learn Python Programming', 39.99, 40, 3),
(6, 'Keyboard', 'Mechanical keyboard', 89.99, 25, 1),
(7, 'Headphones', 'Bluetooth headphones', 79.99, 30, 1),
(8, 'Sweater', 'Wool sweater', 59.99, 45, 2);

INSERT INTO Orders VALUES
(1, 1, '2024-01-10', 1109.98, '123 Main St, New York', 'Completed'),
(2, 2, '2024-01-15', 79.99, '456 Oak Ave, Los Angeles', 'Completed'),
(3, 1, '2024-02-05', 129.97, '123 Main St, New York', 'Pending'),
(4, 3, '2024-02-20', 39.99, '789 Pine Rd, Chicago', 'Completed'),
(5, 4, '2024-03-01', 69.98, '321 Elm St, Houston', 'Completed'),
(6, 2, '2024-03-10', 999.99, '456 Oak Ave, Los Angeles', 'Completed'),
(7, 5, '2024-03-15', 169.97, '654 Maple Dr, Phoenix', 'Pending'),
(8, 3, '2024-03-20', 199.97, '789 Pine Rd, Chicago', 'Completed');

INSERT INTO Order_Items VALUES
(1, 1, 1, 1, 999.99),
(2, 1, 2, 1, 29.99),
(3, 2, 7, 1, 79.99),
(4, 3, 2, 1, 29.99),
(5, 3, 5, 1, 39.99),
(6, 3, 3, 2, 19.99),
(7, 4, 5, 1, 39.99),
(8, 5, 4, 1, 49.99),
(9, 5, 3, 1, 19.99),
(10, 6, 1, 1, 999.99),
(11, 7, 6, 1, 89.99),
(12, 7, 8, 1, 59.99),
(13, 7, 5, 1, 39.99),
(14, 8, 2, 1, 29.99),
(15, 8, 4, 2, 49.99),
(16, 8, 7, 1, 79.99),
(17, 8, 3, 1, 19.99);


-- 20 Join Operation Questions for E-commerce:
-- Join the Customers table with the Orders table to list all orders made by a specific customer.
SELECT * FROM customers c 
INNER JOIN orders o ON c.customer_id = o.customer_id 
WHERE c.customer_id = 1;

-- Find all orders placed by customers who live in a specific city (using the address field in Customers table).
SELECT c.customer_id, c.first_name, c.address, o.order_id, o.order_date FROM customers c JOIN orders o ON c.customer_id = o.customer_id WHERE c.address LIKE '%New York%';

-- List the products and their categories by joining the Products and Categories tables.
SELECT p.product_id, p.name, p.price, c.category_name FROM products p JOIN categories c ON p.category_id = c.category_id;

-- Get a list of all products purchased by a particular customer, including their name, description, and quantity ordered (using Orders, Order_Items, and Products).
SELECT c.first_name, c.last_name, p.name, p.description, oi.quantity FROM customers c 
JOIN orders o ON c.customer_id = o.customer_id 
JOIN order_items oi ON o.order_id = oi.order_id 
JOIN products p ON oi.product_id = p.product_id WHERE c.customer_id = 1;

-- Join Order_Items with Orders to get a list of all products ordered along with the order's total amount.
SELECT oi.order_item_id, oi.quantity, oi.item_price, o.order_id, o.total_amount FROM order_items oi JOIN orders o ON oi.order_id = o.order_id;

-- Find the total number of items ordered for each product (using Order_Items and Products).
SELECT p.product_id, p.name, SUM(oi.quantity) as total_quantity FROM products p JOIN order_items oi ON p.product_id = oi.product_id GROUP BY p.product_id, p.name;

-- Find the customer who placed the highest value order (using Orders and Customers).
SELECT c.customer_id, c.first_name, c.last_name, o.order_id, o.total_amount FROM customers c JOIN orders o ON c.customer_id = o.customer_id ORDER BY o.total_amount DESC LIMIT 1;

-- Get a list of all customers who ordered a specific product (join Customers, Orders, and Order_Items).
SELECT DISTINCT c.customer_id, c.first_name, c.last_name FROM customers c JOIN orders o ON c.customer_id = o.customer_id JOIN order_items oi ON o.order_id = oi.order_id WHERE oi.product_id = 1;

-- Join Products and Order_Items to find the total revenue generated by each product.
SELECT p.product_id, p.name, SUM(oi.quantity * oi.item_price) as total_revenue FROM products p JOIN order_items oi ON p.product_id = oi.product_id GROUP BY p.product_id, p.name;

-- Find the most popular product in each category (using Products, Order_Items, and Categories).
SELECT c.category_id, c.category_name, p.product_id, p.name, SUM(oi.quantity) as total_ordered FROM categories c JOIN products p ON c.category_id = p.category_id JOIN order_items oi ON p.product_id = oi.product_id GROUP BY c.category_id, p.product_id ORDER BY c.category_id, total_ordered DESC;

-- Get a list of all orders with their corresponding products, including product name and quantity ordered (using Orders, Order_Items, and Products).
SELECT o.order_id, o.order_date, p.name, oi.quantity, oi.item_price FROM orders o JOIN order_items oi ON o.order_id = oi.order_id JOIN products p ON oi.product_id = p.product_id;

-- Find the average number of items ordered per customer (using Orders and Order_Items).
SELECT c.customer_id, c.first_name, AVG(oi.quantity) as avg_items_per_order FROM customers c JOIN orders o ON c.customer_id = o.customer_id LEFT JOIN order_items oi ON o.order_id = oi.order_id GROUP BY c.customer_id;

-- List customers who have not placed any orders (using Customers and Orders).
SELECT c.customer_id, c.first_name, c.last_name FROM customers c LEFT JOIN orders o ON c.customer_id = o.customer_id WHERE o.order_id IS NULL;

-- Find all orders that contain more than 5 items, including customer details (using Orders, Order_Items, and Customers).
SELECT c.customer_id, c.first_name, c.last_name, o.order_id, COUNT(oi.order_item_id) as item_count FROM customers c JOIN orders o ON c.customer_id = o.customer_id JOIN order_items oi ON o.order_id = oi.order_id GROUP BY o.order_id HAVING COUNT(oi.order_item_id) > 2;

-- List the total number of products sold per category (using Products, Order_Items, and Categories).
SELECT c.category_id, c.category_name, SUM(oi.quantity) as total_sold FROM categories c JOIN products p ON c.category_id = p.category_id JOIN order_items oi ON p.product_id = oi.product_id GROUP BY c.category_id, c.category_name;

-- Find all orders placed in the last 30 days along with the products purchased (using Orders, Order_Items, and Products).
SELECT o.order_id, o.order_date, p.name, oi.quantity FROM orders o JOIN order_items oi ON o.order_id = oi.order_id JOIN products p ON oi.product_id = p.product_id WHERE o.order_date >= DATE_SUB(CURDATE(), INTERVAL 30 DAY);

-- Get a list of products that are out of stock and were previously ordered (using Products and Order_Items).
SELECT DISTINCT p.product_id, p.name, p.stock_quantity FROM products p JOIN order_items oi ON p.product_id = oi.product_id WHERE p.stock_quantity = 0;

-- List the products that have not been sold in the last 6 months (using Products and Order_Items).
SELECT p.product_id, p.name FROM products p LEFT JOIN order_items oi ON p.product_id = oi.product_id LEFT JOIN orders o ON oi.order_id = o.order_id WHERE o.order_date IS NULL OR o.order_date < DATE_SUB(CURDATE(), INTERVAL 6 MONTH);

-- Find customers who have placed orders above a certain value threshold, with order details (using Orders, Customers).
SELECT c.customer_id, c.first_name, c.last_name, o.order_id, o.order_date, o.total_amount FROM customers c JOIN orders o ON c.customer_id = o.customer_id WHERE o.total_amount > 500;

-- Get the total sales amount for each customer, including their personal details (using Orders, Order_Items, and Customers).
SELECT c.customer_id, c.first_name, c.last_name, c.email, SUM(o.total_amount) as total_spent FROM customers c JOIN orders o ON c.customer_id = o.customer_id GROUP BY c.customer_id, c.first_name, c.last_name, c.email;

