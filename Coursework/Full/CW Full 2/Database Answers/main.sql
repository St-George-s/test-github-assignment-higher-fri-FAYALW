DESCRIBE ALL TABLES;

-- 2b)
-- SELECT Planner.forename, Planner.surname, Planner.plannerNo, COUNT(Walk.walkID) AS 'Total participants'
-- FROM Planner, Route, Walk
-- WHERE Planner.plannerNo = Route.plannerNo AND Route.routeID = Walk.routeID
-- GROUP BY Planner.forename, Planner.surname, Planner.plannerNo
-- ORDER BY COUNT(Walk.walkID) DESC;

-- 2c)
-- SELECT Walker.walkerNo, forename, surname, telNo
-- FROM Walker, Walk, Route
-- WHERE Walker.walkerNo = Walk.walkerNo 
--     AND Walk.routeID = Route.routeID 
--     AND Route.distance = (
--         SELECT MAX(distance)
--         FROM Route
--         )
-- GROUP BY telNo
-- ORDER BY Walker.walkerNo ASC;