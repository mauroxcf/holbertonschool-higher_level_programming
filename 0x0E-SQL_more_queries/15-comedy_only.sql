-- script that lists all Comedy shows in the database

SELECT title FROM tv_shows
JOIN tv_show_genres ON tv_show_genres.show_id = id
JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
WHERE tv_genres.name = 'Comedy'
ORDER BY title;
