```sql
-- CREATE DATABASE
CREATE DATABASE RetailINF;
USE RetailINF;
```
```sql
-- BAD TABLE
CREATE TABLE BadOrders (
order_id INT PRIMARY KEY,
order_date DATE,
customer_id INT,
customer_name VARCHAR(50),
customer_city VARCHAR(50),
-- repeating groups(comma-separated)
product_ids VARCHAR(200),
product_names VARCHAR(200),
unit_prices VARCHAR(200),
quantities VARCHAR(200),
order_total DECIMAL(10,2) -- derivable sum
```
```sql
-- INSERTING BAD VALUES
INSERT INTO BadOrders VALUES
-- order_id,data,cust_id,name,city,pids,pnames
(101,'2025-09-01',1,'Rahul','Mumbai','1,3','Laptop,Headphones','20000,48900','1,1',68900),
(102,'2025-09-02',2,'Priya','Delhi','2','Smartphone','24890','1',24890);
```
```sql
-- CREATING TABLES IN 1NF FORM
CREATE TABLE  Orders_1NF(
order_id INT PRIMARY KEY,
order_date DATE,
customer_id INT,
customer_name VARCHAR(50),
customer_city VARCHAR(50)
);

CREATE TABLE OrderItems_1NF (
order_id INT,
line_no INT,
product_id INT,
product_name VARCHAR(50),
unit_price DECIMAL(10,2),
quantity INT,
PRIMARY KEY(order_id,line_no),
FOREIGN KEY (order_id) REFERENCES Orders_1NF (order_id)
);
```
```sql
-- INSERTING DATA INTO 1NF FORM
INSERT INTO Orders_1NF
SELECT order_id,order_date,customer_id,customer_name,customer_city
FROM BadOrders;

INSERT INTO OrderItems_1NF VALUES 
(101,1,1,'Laptop',60000,1),
(101,2,3,'Headphones',2000,2),
(102,1,2,'Smartphone',30000,1);
```
