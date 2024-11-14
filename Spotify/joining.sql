Predictions:

SELECT * 
FROM Tracks 
WHERE album_id IN(
  SELECT album_id 
  FROM Albums 
  WHERE release_year > 2018
);

I think that this will select all tracks from albums released after the year 2018.


 SELECT T.track_name, A.album_name 
 FROM Tracks T, Albums A
 WHERE T.album_id = A.album_id
   AND A.release_year > 2020;

I think that this will select all track names and their corresponding album names for albums released after the year 2020.


SELECT T.track_name, A.album_name 
FROM Tracks T 
JOIN Albums A ON T.album_id = A.album_id 
WHERE A.release_year > 2020;

I think that this will select track names along with their album names for tracks that are part of albums released after 2020.


SELECT A.artist_name, COUNT(T.track_id) 
FROM Artists A 
JOIN Tracks T ON A.artist_id = T.artist_id 
GROUP BY A.artist_name;

I think that this will count the number of tracks for each artist in the database.


Modifying:

• Use a different condition in the subquery of the first SQL statement.
SELECT * 
FROM Tracks 
WHERE album_id IN(
  SELECT album_id 
  FROM Albums 
  WHERE release_year > 2019
);


• Experiment with different aggregate functions in the equi join queries.
SELECT A.artist_name, MAX(T.track_id) 
FROM Artists A 
JOIN Tracks T ON A.artist_id = T.artist_id 
GROUP BY A.artist_name;


Making:

• Write a query to find all track names for Lizzo by using an equi join between Tracks and Artists.
SELECT T.track_name, Ar.artist_name
FROM Tracks T
JOIN Artists Ar ON T.artist_id = Ar.artist_id
WHERE Ar.artist_name = 'Lizzo';


• Select track names and their respective genres by using an equi join between Tracks and Genres.
SELECT T.track_name, G.genre_name
FROM Tracks T
JOIN Genres G ON G.genre_id = T.genre_id;


• Count the number of tracks in each genre for 2017 by using an equi join among Tracks, Albums, and Genres.
SELECT genre_name, COUNT(T.track_name) AS 'Track Count'
FROM Albums A
JOIN Tracks T ON T.album_id = A.album_id
JOIN Genres G ON T.genre_id = G.genre_id
WHERE A.release_year = 2017
GROUP BY genre_name;