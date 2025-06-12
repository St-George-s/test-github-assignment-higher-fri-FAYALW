Predictions:

SELECT artist_name 
FROM Artists 
WHERE artist_name LIKE 'T%';

I think that this will select the artist names from the Artists table if the artist name starts with a T.


SELECT album_name, release_year 
FROM Albums 
WHERE release_year >= 2015 ORDER BY release_year DESC;

I think that this will select the album name and release year from the Albums table if the release year is more than or equal to 2015 in descending order.


SELECT a.album_name AS Album, a.release_year Year 
FROM Albums a 
WHERE a.release_year > 2010 
ORDER BY a.release_year;

I think that this will select album names and release years, with aliases Album and Year respectively, from the Albums table for albums released after 2010 in ascending order.


SELECT artist_name, LENGTH(artist_name) AS Name_Length 
FROM Artists 
WHERE artist_name LIKE '_a%';

I think that this will select artist names and the length of each name from the Artists table where the second letter of the artist's name is a.


Modifying:

• Use a different wildcard pattern ( % or _ ) in the LIKE clause.

SELECT artist_name 
FROM Artists 
WHERE artist_name LIKE '__a%';


• Change the ORDER BY clause to sort by a different field or in ascending order.

SELECT album_name, release_year 
FROM Albums 
WHERE release_year >= 2015 ORDER BY release_year ASC;


• Experiment with different aliases and calculated values in your queries.

SELECT a.album_name AS Album, a.release_year AS Year
FROM Albums a
WHERE a.release_year > 2010
ORDER BY a.release_year;

SELECT artist_name, LENGTH(artist_name) - 5 AS Name_Length_Minus_Five
FROM Artists;


Making:

• Write a query to select track names that start with 'S' and end with 'e'.

SELECT track_name 
FROM Tracks 
WHERE track_name LIKE 'S%e'


• Select albums released after 2010, displaying the album name and a calculation of how many years ago they were released.

SELECT album_name,
       2024 - release_year AS years_since_release
FROM Albums
WHERE release_year > 2010;


Write a query to display artist names with their name lengths, only for artists whose names are longer than 5 characters.

SELECT artist_name, LENGTH(artist_name) AS Name_Length
FROM Artists
WHERE Name_Length > 5;