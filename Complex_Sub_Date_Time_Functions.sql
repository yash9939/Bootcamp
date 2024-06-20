USE store;

# Sub Queries
SELECT cid AS Customer_ID, Customer_name, Age FROM customer 
WHERE cid IN (SELECT cid   
FROM orders 
WHERE Amount > 10000); 

SELECT pid AS Product_ID, Product_name, price AS Price FROM products 
WHERE price = (SELECT max(price)   
FROM products ); 

SELECT cid AS Customer_ID, Customer_name, Age FROM customer 
WHERE cid IN (SELECT cid   
FROM orders 
WHERE pid IN (SELECT pid FROM products 
WHERE Price > 10000)); 

# Correlated Queries
SELECT Product_name, price
FROM products p
WHERE price > (
    SELECT AVG(price)
    FROM products
    WHERE p.price > 1000 );
    
SELECT Customer_name
FROM customer c
WHERE EXISTS (
    SELECT 1
    FROM orders o
    WHERE o.cid = c.cid
    GROUP BY o.cid
    HAVING AVG(o.Amount) > (
        SELECT AVG(Amount)
        FROM orders
    )
);

# Joins
# Inner Join
SELECT p.Product_name, o.oid, o.Amount
FROM products p
INNER JOIN (
    SELECT *
    FROM orders
) o ON p.pid = o.pid
WHERE p.price > 1000;

# Left join
SELECT p.Product_name, SUM(o.Amount) AS total_orders_amount
FROM products p
LEFT JOIN orders o ON p.pid = o.pid
GROUP BY p.Product_name;

# Analytical Function / Advanced function
# RANK Function
SELECT pid AS Product_ID, Product_name, price, RANK() OVER (ORDER BY price DESC) AS price_rank
FROM products;

# DENSE RANK Function
SELECT pid AS Product_ID, Product_name, price,
DENSE_RANK() OVER (ORDER BY price DESC) AS price_rank
FROM products;

# ROW_NUMBER Function
SELECT ROW_NUMBER() OVER (ORDER BY age DESC) AS row_num, cid AS Customer_ID, Customer_name, Age
FROM customer;

# CUME_DIST Function
SELECT oid, Amount,
CUME_DIST() OVER (ORDER BY Amount) AS cumulative_distribution
FROM payment;

#LAG Function
SELECT Product_name, price, LAG(price) OVER (PARTITION BY location ORDER BY price) AS lag_price
FROM products;

# LEAD Function
SELECT Product_name, price, location, LEAD(price) OVER (PARTITION BY location ORDER BY price) AS lead_price
FROM products;