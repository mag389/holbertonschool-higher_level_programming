-- all the genres of dexter
SELECT ts.title
FROM tv_shows ts
LEFT JOIN
(SELECT ts.title
FROM tv_genres tg
 JOIN tv_show_genres tsg
ON tg.id = tsg.genre_id


 JOIN tv_shows ts
 ON ts.id = tsg.show_id

WHERE tg.name = "Comedy"
ORDER BY ts.title ASC) o
ON o.title = ts.title
WHERE o.title IS NULL
ORDER BY ts.title ASC;
