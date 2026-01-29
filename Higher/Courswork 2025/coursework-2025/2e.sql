SELECT comicTitle, issue, publisherName, (valuation * 2) AS [Double Price]
FROM Comic, Publisher, Series, CharacterInfo, ComicCharacter
WHERE Series.seriesName = "The OK Seven"
AND CharacterInfo.characterName = "Starlordly"
AND Comic.publisherID = Publisher.publisherID
AND Comic.seriesID = Series.seriesID
AND Comic.comicID = ComicCharacter.comicID
AND CharacterInfo.characterID = ComicCharacter.characterID;