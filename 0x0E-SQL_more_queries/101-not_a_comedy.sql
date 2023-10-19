-- sql
SELECT title
FROM tv_shows
WHERE id NOT IN
(
 SELECT tv_show_genres.show_id
 FROM tv_show_genres
 INNER JOIN tv_genres
 ON tv_show_genres.genre_id = tv_genres.id
 WHERE tv_genres.name = 'Comedy'
)
ORDER BY title ASC
