SELECT characterName, SUM(valuation) AS [Total Valuation]
FROM CharacterInfo, ComicCharacter, Comic
WHERE ComicCharacter.characterID = CharacterInfo.characterID
AND ComicCharacter.comicID = Comic.comicID
AND characterName like '%Duck%'
AND mainCharacter = 1
GROUP BY characterName
ORDER BY [Total Valuation] DESC;