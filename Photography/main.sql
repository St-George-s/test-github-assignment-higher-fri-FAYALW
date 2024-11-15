-- DESCRIBE ALL TABLES;

Subqueries

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
