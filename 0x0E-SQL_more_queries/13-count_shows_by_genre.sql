-- Import the database
-- Import the database dump from hbtn_0d_tvshows into MySQL server.
-- A script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
MySQL < hbtn_0d_tvshows
SELECT tv_genres.`name`,
		COUNT(*) AS `number_of_shows`
	FROM tv_genres
		INNER JOIN tv_show_genres
	ON tv_genres.`id` = tv_show_genres.`genre_id`
    GROUP BY tv_genres.`name`
    ORDER BY `number_of_shows` DESC;