-- cities in the golden state
-- san fran etc.
SELECT id, name FROM cities 
WHERE state_id = 
(SELECT id FROM states
WHERE name = 'California')
ORDER BY cities.id ASC;
