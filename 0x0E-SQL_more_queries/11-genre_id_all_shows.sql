-- Import the database
-- Import the database dump from hbtn_0d_tvshows into MySQL server.
--Display tv_shows.title - tv_show_genres.genre_id in asc order
MySQL < hbtn_0d_tvshows
SELECT tv_shows.`title`,
tv_show_genres.`genre_id`
	FROM tv_shows LEFT JOIN `tv_show_genres`
		ON tv_shows.`id` = tv_show_genres.`show_id`
ORDER BY tv_shows.`title`, tv_show_genres.`genre_id` ASC