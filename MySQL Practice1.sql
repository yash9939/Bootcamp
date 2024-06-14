#Creating a Database
CREATE DATABASE store;

#Using the created database
USE store;

#Creating Tables for the database

#Creating the customer table
CREATE TABLE customer(
customer_id INT(6) PRIMARY KEY,
Customer_name VARCHAR(30) NOT NULL,
Age INT(3) CHECK(Age>18) NOT NULL,
Phone_no INT(11) UNIQUE
);

#Renaming the primary of customer table
ALTER TABLE customer RENAME COLUMN customer_id TO cid;

#Adding another column in the customer table
ALTER TABLE customer ADD Email_id VARCHAR(30) UNIQUE;

#Creating products table
CREATE TABLE products(
pid INT(6) PRIMARY KEY,
Product_name VARCHAR(50) NOT NULL,
Price DECIMAL(5,2) NOT NULL,
Stock INT(5) NOT NULL
);

#Dropping a column from the products table
ALTER TABLE products DROP COLUMN Price;

#Adding a Column to the products table
ALTER TABLE products ADD COLUMN Price INT(10) NOT NULL;

CREATE TABLE orders(
oid int(3) PRIMARY KEY,
cid int(3),
pid int(3),
amt int(10) NOT NULL,
FOREIGN KEY(cid) REFERENCES customer(cid) ON DELETE CASCADE ON UPDATE CASCADE, #Referening the foreign key to the original table
FOREIGN KEY(pid) REFERENCES products(pid) ON DELETE CASCADE ON UPDATE CASCADE #Referening the foreign key to the original table
);

#Renaming the amt column in the orders table
ALTER TABLE orders RENAME COLUMN amt TO Amount;

#Creating Payments table for the databse
CREATE TABLE payment(
pay_id INT(3) PRIMARY KEY,
oid INT(3),
Amount INT(10) NOT NULL,
mode VARCHAR(30) CHECK(MODE IN('upi','credit','debit')),
status VARCHAR(30),
FOREIGN KEY(oid) REFERENCES orders(oid) ON DELETE CASCADE ON UPDATE CASCADE
);

#Dropping a column in the paymnet table
ALTER TABLE payment DROP COLUMN mode; 

#Adding another mode(COD) in payment.mode column 
ALTER TABLE payment ADD COLUMN MODE VARCHAR(30) CHECK(MODE IN("upi", "credit", "debit", "cod"));

#Inserting Some values in the above made Tables

#Inserting values in customer table
INSERT INTO customer VALUES (1, "Rahul", 20, 458769047, "rahul@gmail.com");
INSERT INTO customer VALUES (2, "Suman", 24, 489564756, "suman@gmainl.com");
INSERT INTO customer VALUES (3, "Abhishek", 36, 364785690, "abhishek@gmail.com");
INSERT INTO customer VALUES (4, "Saumya", 44, 875690456, "saumya@gmail.com");

#Inserting values in products table
INSERT INTO products VALUES (101, "Boat Headphone", 12000, 26);
INSERT INTO products VALUES (102, "One Plus Ear phone", 2400, 18);
INSERT INTO products VALUES (103, "Mac Book", 116699, 69);
INSERT INTO products VALUES (104, "iPhone", 89999, 56);

#Inserting values in orders table
INSERT INTO orders VALUES (201, 3, 102, 2400);
INSERT INTO orders VALUES (202, 2, 104, 89999);
INSERT INTO orders VALUES (203, 1, 103, 116699);

#Inserting values in payments table 
INSERT INTO payment VALUES (301, 201, 2832, "credit", "Successful");
INSERT INTO payment VALUES (302, 202, 106198, "cod", "Successful");
INSERT INTO payment VALUES (303, 203, 137704, "upi", "Pending");


#Operators

#Arithmatic Sum Operator
SELECT SUM(Price) AS total_revenue 
FROM products;

# Arithmatic Division Operator
SELECT Price, (Price / (SELECT AVG(Price) FROM products)) AS Avg_Difference
FROM products;

#Comparison Greater than Operator
SELECT cid, Customer_name FROM customer
WHERE Age>30;

#Comparison Equal to Operator
SELECT pay_id FROM payment
WHERE status = "Successful";

#Logical AND operator
SELECT cid, Customer_name FROM customer
WHERE Age>18 AND Age<30;

#Logical OR operator
SELECT pay_id FROM paymnet
WHERE status="Successful" OR status="Pending";