<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> d38a6b7 (Mock DB Test)
SELECT name
FROM Clients
WHERE client_id IN (
    SELECT client_id
    FROM Bookings
    WHERE event_type = 'Wedding'
);
<<<<<<< HEAD
=======
-- DESCRIBE ALL TABLES;

Subqueries

<<<<<<< HEAD
-- SELECT name
-- FROM Clients
-- WHERE client_id IN 
--     (SELECT client_id 
--     FROM Bookings 
--     WHERE event_type = 'Wedding');
>>>>>>> df4ceeb (.)
=======
SELECT title, date_taken
FROM Photos
WHERE date_taken = 
    (SELECT MAX(date_taken)
    FROM Photos);


SELECT photographer_id, name
FROM Photographers
WHERE photographer_id NOT IN 
    (SELECT photographer_id
    FROM Bookings);


SELECT name
FROM Clients
WHERE client_id IN 
    (SELECT client_id 
    FROM Bookings 
    WHERE event_type = 'Wedding');


SELECT COUNT(*) AS [Photo count]
FROM Photos
WHERE photographer_id IN 
    (SELECT photographer_id 
    FROM Photographers 
    WHERE experience_years > 5);
>>>>>>> a97e74f (.)
=======
>>>>>>> d38a6b7 (Mock DB Test)
