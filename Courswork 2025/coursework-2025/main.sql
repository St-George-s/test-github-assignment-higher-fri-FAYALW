-- DESCRIBE ALL TABLES;


-- 2c
-- SELECT comicTitle, issue, publisherName, valuation
-- FROM Comic, Publisher
-- WHERE Comic.publisherID = Publisher.publisherID
-- AND valuation >= (
--     SELECT AVG(valuation)
--     FROM Comic) + 300
-- ORDER BY comicTitle ASC;


-- 2d
SELECT mainCharacter, characterName, SUM(valuation) AS 'Total Valuation'
FROM CharacterInfo, ComicCharacter, Comic
WHERE ComicCharacter.characterID = CharacterInfo.characterID
AND ComicCharacter.comicID = Comic.comicID
AND characterName like '%Duck%';


-- 2e
-- SELECT comicTitle, issue, publisherName, (valuation * 2) AS [Double Price]
-- FROM Comic, Publisher, Series, CharacterInfo, ComicCharacter
-- WHERE Series.seriesName = "The OK Seven"
-- AND CharacterInfo.characterName = "Starlordly"
-- AND Comic.publisherID = Publisher.publisherID
-- AND Comic.seriesID = Series.seriesID
-- AND Comic.comicID = ComicCharacter.comicID
-- AND CharacterInfo.characterID = ComicCharacter.characterID;