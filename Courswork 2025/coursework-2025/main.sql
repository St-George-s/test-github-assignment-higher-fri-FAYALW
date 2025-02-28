-- DESCRIBE ALL TABLES;

-- 2c
-- SELECT comicTitle, issue, publisherName, valuation
-- FROM Comic, Publisher
-- WHERE valuation > (
--     SELECT AVG(valuation)
--     FROM Comic

-- )


-- 2d
-- SELECT characterName, SUM(valuation) AS 'Total Valuation'
-- FROM CharacterInfo, Comic, ComicCharacter
-- WHERE CharacterInfo.characterID = comicCharacter.characterID
-- AND ComicCharacter.comicID = Comic.comic
-- AND characterName like '%Duck%'
-- GROUP BY characterName
-- ORDER BY 'Total Valuation' ASC;


-- 2e
SELECT comicTitle, issue, publisherName, (valuation * 2) AS [Double Price]
FROM Comic, Publisher, Series, CharacterInfo, ComicCharacter
WHERE Series.seriesName = "The OK Seven"
AND CharacterInfo.characterName = "Starlordly"
AND Comic.publisherID = Publisher.publisherID
AND Comic.seriesID = Series.seriesID
AND CharacterInfo.characterID = ComicCharacter.characterID
GROUP BY comicTitle
ORDER BY [Double Price] DESC;