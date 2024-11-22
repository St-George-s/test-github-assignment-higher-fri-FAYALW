--DESCRIBE ALL TABLES;

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