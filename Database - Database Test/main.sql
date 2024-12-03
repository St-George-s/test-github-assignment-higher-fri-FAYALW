-- DESCRIBE ALL TABLES;

-- 3.1)
-- SELECT episodeTitle, showName, maxViewers, episodeDate
-- FROM Episode, Show
-- WHERE Episode.showID = Show.showID;

-- 3.2)
-- SELECT showName AS 'Show', episodeTitle AS 'Episode'
-- FROM Episode, Show
-- WHERE Episode.showID = Show.showID
-- AND episodeDate like '%2024-12%';

--3.3)
-- UPDATE Timeslot
-- SET endTime = '19:30'
-- WHERE airDate = '2024-12-24'
-- AND showID = (
--     SELECT showName
--     FROM Show
--     WHERE showName = 'Star Cooks'
-- );

--5)
-- SELECT showName, COUNT(ratingID) AS 'TotalRatings'
-- FROM Show, ViewerRating, Episode
-- WHERE Show.showID = Episode.showID
-- AND Episode.episodeID = ViewerRating.episodeID
-- GROUP BY showName
-- ORDER BY TotalRatings DESC;