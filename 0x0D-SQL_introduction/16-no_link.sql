-- lists all records with constraints
-- no null names, score and name, desc order
SELECT score, name FROM second_table WHERE name <> '' ORDER BY score DESC;
