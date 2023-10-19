-- sql
SELECT name
FROM tv_genres
WHERE id NOT IN
(
 SELECT tv_show_genres.genre_id
 FROM tv_show_genres
 INNER JOIN tv_shows
 ON tv_show_genres.show_id = tv_shows.id
 WHERE tv_shows.title = 'Dexter'
)
ORDER BY name ASC
