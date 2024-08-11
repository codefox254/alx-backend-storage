-- SQL script that creates a view named 'need_meeting' 
-- that lists all students who have a score strictly under 80
-- and either have no last meeting date or their last meeting date is more than one month ago.

DELIMITER $$

DROP VIEW IF EXISTS need_meeting;

CREATE VIEW need_meeting AS
SELECT name
FROM students
WHERE score < 80
AND (last_meeting IS NULL OR last_meeting < DATE_SUB(NOW(), INTERVAL 1 MONTH));

DELIMITER ;
