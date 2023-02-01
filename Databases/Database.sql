-- DDL:
CREATE TABLE Customers(
    CustomerID INT(6) NOT NULL AUTO_INCREMENT,
    FirstName Varchar(200) NOT NULL, 
    City Varchar(50),
    FavoriteDish int(50) references Dishes(DishID)
    primary key (CustomerID)
);
-- DML:
-- Writing Queries:
SELECT * FROM Customers;

-- Use Where to narrow query results:
SELECT FirstName, City FROM CustomerID where FirstName = "Ahmed" and City like "%C";

-- Sorting Results:
SELECT * FROM  Customers ORDER BY FirstName ASC;

-- Aggregate Functions:
SELECT COUNT(FirstName) FROM Customers;
SELECT SUM(Price), AVG(Price), MIN(Price), MAX(Price) FROM Dishes;

-- Joining Tables:
SELECT FirstName, City FROM Customers JOIN Dishes
ON Customers.FavoriteDish = Dishes.DishID;

-- Modifying Data:
INSERT INTO Customers (FirstName, LastName) Values("Jane", "John");
SELECT * FROM Customers WHERE FirstName ="Taylor" AND LastName = "John";
UPDATE Customers SET Email = "Tahlaj@gmail.com" WHERE CustomerID = 1;
DELETE FROM Customers WHERE CustomerID = 23;






