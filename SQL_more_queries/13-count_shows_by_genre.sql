-- script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each
SELECT gen.name AS genre, COUNT(*) AS number_of_shows FROM tv_genres gen JOIN tv_show_genres j ON gen.id = j.show_id GROUP BY genre ORDER BY number_of_shows DESC;
