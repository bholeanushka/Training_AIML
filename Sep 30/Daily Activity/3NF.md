``` sql
CREATE TABLE Cities (
city_id INT PRIMARY KEY,
city_name VARCHAR(50),
state VARCHAR(50)
);

CREATE TABLE Customers_3NF (
customer_id INT PRIMARY KEY,
customer_nmae VARCHAR(50),
city_id INT,
FOREIGN KEY (city_id) REFERENCES Cities (city_id)
);

CREATE TABLE Products_3NF LIKE Product_2NF;

CREATE TABLE Orders_3NF LIKE Orders_2NF;

CREATE TABLE OrdersItems_3NF LIKE OrderItems_2NF;
```
``` sql
INSERT INTO Products_3NF SELECT * FROM Product_2NF;

INSERT INTO Cities VALUES 
(10,'Mumbai','Maharashtra'),
(20,'Delhi','Delhi');

INSERT INTO Customers_3NF VALUES
(1,'Rahul',10),
(2,'Priya',20);

INSERT INTO Orders_3NF SELECT * FROM Orders_2NF

INSERT INTO OrdersItems_3NF SELECT * FROM OrderItem_2NF
```
