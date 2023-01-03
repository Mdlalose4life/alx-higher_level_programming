-- Import the database
-- Import the database dump from hbtn_0d_tvshows into MySQL server.
--  A script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
MySQL < hbtn_0d_tvshows
SELECT tv_genres.`name`	
	FROM tv_genre
		INNER JOIN tv_show_genres
		ON tv_genres.`id` = tv_show_genres.`genre_id`
    
		INNER JOIN tv_shows
		ON tv_shows.`id` = tv_show_genres.`show_id`
		WHERE tv_shows.`tittle` = "Dexter"
	ORDER BY tv_genres.`name`