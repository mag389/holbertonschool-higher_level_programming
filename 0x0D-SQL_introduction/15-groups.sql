-- lists number of records with sanme scorein second table
-- displays score and number, sorted by number
SELECT score, count(score) AS `number` FROM second_table GROUP BY score
ORDER BY number DESC;
