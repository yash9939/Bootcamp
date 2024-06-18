# In-Built Functions in MySQL

#Using the Database created earlier
USE store;

# String Functions
# Char_Length Function
SELECT CHAR_LENGTH("Hello, My name is Bruce !"); #Output: 25
SELECT CHAR_LENGTH("Bruce Wayne"); #Output: 11

# ASCII Function
SELECT ASCII("Y"); #Output: 89
SELECT ASCII("Batman"); #Output: 66
SELECT ASCII("Bruce Wayne"); #Output: 66

# Concat Function
SELECT CONCAT("Artificial", " ", "Intelligence"); #Output: Artificial Intelligence

#INSTr Function
SELECT INSTR("Bruce Wayne", "a"); #Output: 8
SELECT INSTR("Artificial Intelligence", "e"); #Output: 15

# LCASE or LOWER Function
SELECT LCASE('BATMAN'); #Output: batman
SELECT LOWER('DarKnighT'); #Output: darknight

# UCASE or UPPER Function
SELECT UCASE("batman"); #Output: BATMAN
SELECT UPPER("DarKnighT"); #Output: MYFUNCTION

#SUBSTR Function
SELECT SUBSTR("Bruce Wayne", 4, 7); #Output: ce Wayn
SELECT SUBSTR("Batman, The Dark Knight", 2, 10); #Output: atman, The

#LPAD Function
SELECT LPAD("Batman", 4, "*"); #Output: Batm

#RPAD Function
SELECT RPAD("Batman", 3, "*"); #Output: Bat

# TRIM, RTRIM, LTRIM Function
SELECT TRIM('   The BATMAN!   ');
SELECT RTRIM('   The BATMAN!   ');
SELECT LTRIM('   The BATMAN!   ');


# Date and Time Functions
# CURRENT_DATE Function
SELECT CURRENT_DATE(); #Output: 2024-06-18

# DATEDIFF Function
SELECT DATEDIFF("2024-08-18", "2024-06-14"); #Output: 65

# CURRENT_TIME Function
SELECT CURRENT_TIME() AS Present; 

# LAST_DAY Function
SELECT LAST_DAY("2024-06-18") AS Last_Date; #Output: 2024-06-30

# SYSDATE Function
SELECT SYSDATE() AS Month_and_Time;

# ADDDATE Function
SELECT ADDDATE("2024-06-18", INTERVAL 32 DAY); #Output: 2024-07-20


# Numeric Functions
# AVG Function
SELECT AVG(Amount) AS Avg_transaction 
FROM orders;

# COUNT Function
SELECT COUNT(cid) AS No_of_Customer
FROM customer;

# POW Function
SELECT POW(5,3) AS Output; #Output: 65

# MIN Function
SELECT MIN(Price) AS Lowest_Price_Product 
FROM products;

# MAX Function
SELECT MAX(Amount) AS Highest_Order
FROM orders;

# ROUND Function
SELECT ROUND(2.8963, 1) AS Output; #Output: 2.9
SELECT ROUND(2.8963) AS Output; #Output: 3
SELECT ROUND(-2.8963) AS Output; #Output: -3

# SQRT Function
SELECT SQRT(144) AS Output; #Output: 12

# FLOOR Function
SELECT FLOOR(2.9) AS Output; #Output: 2
SELECT FLOOR(-2.9) AS Output; #Output: -3
