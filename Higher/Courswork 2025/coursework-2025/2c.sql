SELECT comicTitle, issue, publisherName, valuation
FROM Comic, Publisher
WHERE Comic.publisherID = Publisher.publisherID
AND valuation >= (
    SELECT AVG(valuation)
    FROM Comic) + 300;