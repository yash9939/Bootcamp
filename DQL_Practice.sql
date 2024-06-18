# Using the store Databa
USE store;

# DQL Goup By Clause
# The amount of transaction done on each order
SELECT oid, SUM(Amount)
FROM orders
GROUP BY oid;

# Viewing and Grouping the list of customers on the basis of AGE 
SELECT GROUP_CONCAT(Customer_name) AS Customer_Names, Age
FROM customer
GROUP BY Age;

# DQL Order By
# Viewing each products on the basis of number of stock
SELECT Product_name, Price, Stock
FROM products
ORDER BY Stock;

# Viewing each products on the basis of Price in ascending order
SELECT Product_name, Price, Stock
FROM products
ORDER BY Price ASC;

# DQL Having Clause
# The list of Orders which are having Amount less than 5000
SELECT oid, Amount
FROM orders
GROUP BY oid
HAVING Amount > 5000;

# Viewing the total products Where Stock is less than 20 
SELECT Product_name, Price, Stock
FROM products
GROUP BY Product_name, Price, Stock
HAVING Stock < 20;

# DQL Select Command
# Select with Distinct
SELECT DISTINCT Customer_name, AGE, Phone_no FROM customer;

# Viewing Everything in products table
SELECT * FROM payment;

#Selecting by column name
SELECT cid, Customer_name FROM customer;

# Select command with if statement
SELECT cid,
	   Customer_name,
       IF(cid > 2, 'Pass', 'Fail')AS 'Remark'
FROM customer;

# Select command with case statement
SELECT pid,
	   Product_name,
       CASE WHEN pid > 102 THEN 'Pass' ELSE 'Fail' END AS 'Remark'
FROM products;

# Select command with Like statement
SELECT * FROM Products WHERE Product_name LIKE "%one%";