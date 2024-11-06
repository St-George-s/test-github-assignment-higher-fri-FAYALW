Predictions:

DELETE FROM Tracks 
WHERE track_id = 5;

I think that this will delete the tracks which have track IDs that are equal to 5 from the Tracks table.


DELETE FROM Artists 
WHERE artist_id BETWEEN 20 AND 25;

I think that this will delete the artists which have artist IDs between 20 and 25 from the Artists table.


INSERT INTO Genres (genre_id, genre_name) 
VALUES (21, 'Jazz');

I think that this will add a record with a genre ID of 21 and a genre name of Jazz


INSERT INTO Tracks (track_id, track_name, artist_id, album_id, genre_id, duration_ms) 
VALUES (54, 'New Track', 4, 4, 1, 180000), 
       (55, 'Another Track', 5, 5, 2, 200000);

I think that this will add two new records. One record will have a track ID of 54, a track name called New Track, an artist ID of 4, an album ID of 4, a genre ID of 1, and a duration in milliseconds of 180000. The other record will have a track ID of 55, a track name called Another Track, an artist ID of 5, an album ID of 5, a genre ID of 2, and a duration in milliseconds of 200000.


UPDATE Albums 
SET release_year = 2021 WHERE album_id =3;

I think that this will update the release year of album IDs of 3 to 2021


UPDATE Artists 
SET artist_name = 'New Artist Name' WHERE artist_id IN (1, 2, 3);

I think that this will set the artist names to New Artists Name for artists with artist IDs of 1, 2, or 3.



Modifying:

• Try deleting records from Albums using different conditions.
DELETE FROM Albums 
WHERE album_id = 11;

DELETE FROM Albums 
WHERE release_year = 2019;


• Insert a new artist into the Artists table.
INSERT INTO Artists (artist_id, artist_name) 
VALUES (34, 'Don Toliver');

INSERT INTO Artists (artist_id, artist_name) 
VALUES (35, 'Drake');


• Update the duration of a track in the Tracks table.
UPDATE Tracks 
SET duration_ms = 100000 WHERE artist_id = 7;

UPDATE Tracks 
SET duration_ms = 430000 WHERE duration_ms = 198000;


Making:

• Write a query to delete tracks that are shorter than 2 minutes.
DELETE FROM Tracks 
WHERE duration_ms < 120000;


• Insert a new album with your choice of album_id, album_name, and release_year.
INSERT INTO Albums (album_id, album_name, and release_year) 
VALUES (56, 'SOS', 6, 6, 3, 240000), 
    

• Update the genre of a track in the Tracks table to a new genre.
UPDATE Tracks 
SET genre_name = 'Jazz' WHERE album_id = 2;