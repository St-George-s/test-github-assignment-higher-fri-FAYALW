-- DESCRIBE ALL TABLES;

-- PART A
-- 2a) 
-- A query to select customers who have placed orders in a particular month
-- A query to update customer information

-- PART B
-- 2b)
-- SELECT gnomeName, SUM(quantity) AS "Total gnomes sold"
-- FROM Gnome G, GnomePurchase GP
-- WHERE 
    -- G.description like "%solar%"
    -- AND G.gnomeID = GP.gnomeID
-- GROUP BY gnomeName
-- ORDER BY "Total gnomes sold" DESC;

-- 2c)
-- SELECT Customer.emailAddress, Orders.orderID, GnomePurchase.quantity
-- FROM Customer
-- JOIN Orders ON Customer.customerID = Orders.customerID
-- JOIN GnomePurchase ON Orders.orderID = GnomePurchase.orderID
-- JOIN Gnome ON GnomePurchase.gnomeID = Gnome.gnomeID
-- WHERE Gnome.unitPrice = (
   -- SELECT MAX(unitPrice)
   -- FROM Gnome
-- ) AND quantity >= 3;

-- 2d)
-- SELECT forename, surname, ROUND(SUM(quantity * unitPrice * 1.2),2) AS [Total to Pay £]
-- FROM Customer, Gnome, GnomePurchase, Orders
-- WHERE Orders.orderID="ord0024"
-- AND Customer.customerID=Orders.customerID
-- AND Orders.orderID=GnomePurchase.orderID
-- AND Gnome.gnomeID=GnomePurchase.gnomeID; 

-- 2ei)
-- The price may have been changed/updated, so the custoemr could have paid a 
-- different price when they bought it compared to the price it costs now

-- 2eii)
-- The database could keep a record of the transaction/keep a column of the price 
-- when ordered so that it can see how much was paid at the time, regardless of 
-- any prices changes/updates.