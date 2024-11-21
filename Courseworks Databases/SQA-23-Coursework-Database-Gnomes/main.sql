-- DESCRIBE ALL TABLES;
-- SELECT gnomeName, SUM(quantity) AS "Total gnomes sold"
-- FROM Gnome G, GnomePurchase GP
-- WHERE 
    -- G.description like "%solar%"
    -- AND G.gnomeID = GP.gnomeID
-- GROUP BY gnomeName
-- ORDER BY "Total gnomes sold" DESC;


SELECT emailAddress, CO.orderID, quantity, MAX(unitPrice)
FROM Customer C, CustOrder CO, GnomePurchase GP, Gnome G
WHERE quantity >= 3 AND 