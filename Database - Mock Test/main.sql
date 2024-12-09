-- DESCRIBE ALL TABLES;

-- PART B

-- 3.1)
-- SELECT eventName AS 'Event Name', name AS 'Shop Name', maxAttendees AS 'Max Attendees', eventDate AS 'Event Date'
-- FROM Event, Shop
-- WHERE Event.shopID = Shop.shopID;

-- 3.2)
-- SELECT name AS 'Shop Name', eventName AS 'Event Name'
-- FROM Shop, Event
-- WHERE Event.shopID = Shop.shopID AND eventDate = '2024-12-25';

-- 3.3)
-- UPDATE OpeningTime 
-- SET closeTime = '19:00'
-- WHERE date = '2024-12-24'
-- AND shopID = (
--    SELECT shopID
--    FROM Shop
--    WHERE name = 'Zara'
-- );

-- PART C

-- SELECT name AS 'Shop Name', COUNT(bookingID) AS 'Total Bookings'
-- FROM Shop, Booking, event
-- WHERE Shop.shopID = Event.eventID
-- AND Event.eventID = Booking.eventID
-- GROUP BY name;