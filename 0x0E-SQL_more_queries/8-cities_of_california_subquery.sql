-- cities in the golden state
-- san fran etc.
SELECT * FROM cities 
WHERE state_id = 
(SELECT id FROM states
WHERE name = 'California')
ORDER BY id ASC;
