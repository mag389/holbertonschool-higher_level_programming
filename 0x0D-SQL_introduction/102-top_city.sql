-- show top 3 cities during summer months
-- order by tmep grouped by city
SELECT city, AVG(value) AS `avg_temp` 
FROM temperatures 
where month >6 and month < 9 
GROUP BY city 
Order by avg_temp DESC 
LIMIT 3;
