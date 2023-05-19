-- script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows
SELECT n.title, gen.name FROM tv_shows n LEFT JOIN tv_show_genres s ON n.id = s.show_id LEFT JOIN tv_genres gen ON gen.id = s.genre_id ORDER BY n.title, gen.name;
