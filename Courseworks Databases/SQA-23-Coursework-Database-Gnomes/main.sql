-- DESCRIBE ALL TABLES;
-- SELECT gnomeName, SUM(quantity) AS "Total gnomes sold"
-- FROM Gnome G, GnomePurchase GP
-- WHERE 
    -- G.description like "%solar%"
    -- AND G.gnomeID = GP.gnomeID
-- GROUP BY gnomeName
-- ORDER BY "Total gnomes sold" DESC;

SELECT MAX(unitPrice)
FROM Gnome


SELECT emailAddress, CO.orderID, quantity
FROM Customer C, Orders O, GnomePurchase GP, Gnome G
WHERE price = (
    SELECT MAX(unitPrice)
    FROM Gnome
) quantity >= 3;