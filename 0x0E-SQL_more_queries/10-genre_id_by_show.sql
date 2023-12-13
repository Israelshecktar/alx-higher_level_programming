-- Use the database hbtn_0d_tvshows
USE hbtn_0d_tvshows;

-- List the shows by genre
SELECT tv_shows.title, tv_show_genres.genre_id
-- Join the tv_shows and tv_show_genres tables on the id column
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
-- Sort the results by the tv_shows.title and tv_show_genres.genre_id columns
ORDER BY tv_shows.title, tv_show_genres.genre_id;
