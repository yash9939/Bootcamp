# Using the Database created earlier
USE store;

# Creating extra table Employee in the store Database for self join
CREATE TABLE employees(
eid INT(10) PRIMARY KEY,
Employee_name TEXT(60) NOT NULL,
Phone_no INT(11) NOT NULL UNIQUE,
Department VARCHAR(50) NOT NULL,
Manager_id INT(10) 
);

INSERT INTO employees VALUES (1001, "Roshan", 364832255, "Analytics", 1004);
INSERT INTO employees VALUES (1002, "Kartik", 853697413, "Delivery", NULL);
INSERT INTO employees VALUES (1003, "Sumaiya", 247850493, "Sales", 1002);
INSERT INTO employees VALUES (1004, "Neha", 402358931, "Sales", 1002);

# Joins
# Inner Join
# Displaying the customer names with there order id's
SELECT Customer_name, oid AS Orders_ID
FROM orders
INNER JOIN customer ON orders.cid = customer.cid;

# Displaying the customer names, Product id's, Product names with there order id's
SELECT Customer_name, products.pid AS Product_ID, Product_name, oid AS Orders_ID
FROM orders
INNER JOIN customer ON orders.cid = customer.cid
INNER JOIN products ON orders.pid = products.pid;

# Left Outer Join
# Displaying the Payment id's, Amount, order id's 
SELECT pay_id AS Payment_ID, Amount, oid AS Order_ID
FROM payment
LEFT JOIN orders ON payment.oid = orders.oid;

# Displaying the product id's, Product name, Order id's of the products ordered
SELECT products.pid AS Product_id, Product_name, oid AS Order_ID, Amount
FROM orders
LEFT JOIN products ON orders.pid = products.pid;

# Right Join
# Displaying the product id's, Product name, Order id's of the products ordered
SELECT products.pid AS Product_id, Product_name, oid AS Order_ID, Amount
FROM orders
RIGHT JOIN products ON orders.pid = products.pid;

# Full Join
# Displaying the product id's, Product name, Order id's of the products ordered
SELECT products.pid AS Product_id, Product_name, oid AS Order_ID, Amount
FROM orders
LEFT JOIN products ON orders.pid = products.pid
UNION
SELECT products.pid AS Product_id, Product_name, oid AS Order_ID, Amount
FROM orders
RIGHT JOIN products ON orders.pid = products.pid;

# Self Join
# Displaying the employees with managers
SELECT e1.Employee_name AS Employee, e2.Employee_name AS Manager 
FROM employees e1
INNER JOIN employees e2 ON e1.manager_id = e2.eid;

# Cross Join
# Displaying all the details of customer and orders
SELECT Product_name, oid AS Order_ID, Amount
FROM orders
CROSS JOIN products ON orders.pid = products.pid;
