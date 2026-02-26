Predictions:
SELECT artist_name 
FROM Artists;


SELECT *
FROM Albums;


SELECT *
FROM Tracks 
WHERE duration_ms > 200000;


SELECT album_name 
FROM Albums 
WHERE release_year > 2018;


Modifying:
• Try selecting different columns from the Artists table.
SELECT artist_id 
FROM Artists;

SELECT * 
FROM Artists;


• Use the WHERE clause to filter Albums by different years.
SELECT album_name 
FROM Albums 
WHERE release_year < 2020;

SELECT album_name 
FROM Albums 
WHERE release_year < 2020 AND release_year > 2010;


• Experiment with different conditions in the WHERE clause for the Tracks table.
SELECT track_name
FROM Tracks 
WHERE artist_ID = 17;

SELECT *
FROM Tracks 
WHERE genre_ID = 18;


Making:
• Write a query to select all track names from the Tracks table.
SELECT track_names 
FROM Tracks;


• Write a query to display all albums released before the year 2010.
SELECT album_name 
FROM Albums 
WHERE release_year < 2010;


• Write a query to select artist names from the Artists table where the artist_id is less than 10.
SELECT artist_name
FROM Artists 
WHERE artist_ID < 10;