USE store;

# DELIMITER
DELIMITER //

# PROCEDURE
CREATE PROCEDURE display_customer_details()
BEGIN 
      SELECT * FROM customer;
END //
DELIMITER ;

# Calling the procedure (display_customer_details)
CALL display_customer_details();

# Dropping the the procedure (display_customer_details)
DROP PROCEDURE  display_customer_details;


# Function
DELIMITER ,
CREATE FUNCTION customer_who_ordered()
RETURNS TEXT
DETERMINISTIC 
BEGIN
DECLARE details TEXT;
SELECT c.Customer_name INTO details	
FROM orders o
INNER JOIN customer c ON o.cid = c.cid;
RETURN details;
END,
DELIMITER ;

# Calling the created function (customer_who_ordered)
CALL customer_who_ordered();

# Dropping the function (customer_who_ordered)
DROP FUNCTION IF EXISTS customer_who_ordered;

# IN Parameter
DELIMITER @
CREATE PROCEDURE get_customer_details(IN customer_id INT)
BEGIN
SELECT * FROM customer;
END @
DELIMITER ;	

# Calling the procedure
CALL get_customer_details;

# OUT Parameter
DELIMITER @
CREATE PROCEDURE get_product_count(OUT product_count INT)
BEGIN
SELECT COUNT(*) INTO product_count FROM products;
END @
DELIMITER ;

# Calling the Procedure
CALL get_product_count(@product_count);


# Cursor
DELIMITER !
DECLARE @customer_count INT;
SELECT @customer_count = COUNT(*)
FROM customer;
PRINT 'Number of customers: ' + CAST(@customer_count AS VARCHAR(10));
DELIMITER ;