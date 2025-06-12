Predictions:

SELECT COUNT(*)
FROM Tracks;

I think that this will count the total number of tracks in the Tracks table.


SELECT genre_id, COUNT(*)
FROM Tracks 
GROUP BY genre_id;

I think that this will count the number of tracks for each genre_id in the Tracks table, showing how many tracks belong to each genre.


SELECT genre_id, AVG(duration_ms)
FROM Tracks 
GROUP BY genre_id;

I think that this will calculate the average duration (in milliseconds) of tracks within each genre in the Tracks table.


Modifying:

• Change the COUNT(*) to COUNT(track_id) and observe any differences.

It changes the heading of the table to COUNT(track_id) rather than COUNT(*).


• Group tracks by album_id instead of genre_id and count them.


• Use a different aggregate function (SUM, AVG, COUNT, MAX or MIN), with the GROUP BY clause.
SELECT album_id, MAX(genre_id)
FROM Tracks 
GROUP BY album_id;


Making:

• Calculate the total duration of tracks in each album.
SELECT SUM(duration_ms) AS Tracks
FROM Tracks
GROUP BY album_id;


• Find the album with the longest average track duration.
SELECT AVG(duration_ms)
FROM Tracks
GROUP BY album_id
ORDER BY duration_ms DESC
LIMIT 1;

SELECT MAX(Average)
FROM (
    SELECT AVG(duration_ms) AS 'Average'
    FROM Tracks
    GROUP BY album_id
);