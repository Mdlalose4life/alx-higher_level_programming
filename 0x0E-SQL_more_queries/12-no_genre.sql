-- Import the database
-- Import the database dump from hbtn_0d_tvshows into MySQL server.
-- A script that lists all shows contained in hbtn_0d_tvshows without a genre linked.
MySQL < hbtn_0d_tvshows
SELECT tv_shows.`tittle`,
tv_show_genres.`genre_id`
	FROM tv_shows
    LEFT JOIN tv_show_geners.`genre_id`
        ON tv_shows.`id` = tv_show_geners.`show_id`
        WHERE tv_show_geners.`genre_id` = NULL
ORDER BY tv_shows.`title`, tv_show_genres.`genre_id` ASC;