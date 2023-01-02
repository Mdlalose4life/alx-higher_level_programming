-- Import the database
-- Import the database dump from hbtn_0d_tvshows into MySQL server.
-- Display tv_shows.title - tv_show_genres.genre_id in asc order
MySQL < hbtn_0d_tvshows
SELECT tv_shows.`title`,
tv_show_genres.`genre_id`
	FROM tv_shows
		INNER JOIN tv_show_genres.`genre_id`
		ON tv_shows.`id` = tv_show_genres.`show_id`
ORDER BY ASC tv_shows.`title`, tv_show_genres.`genre_id;
