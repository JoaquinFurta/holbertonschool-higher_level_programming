-- script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows
SELECT n.title, gen.name FROM tv_shows n JOIN tv_show_genres s ON n.id = s.show_id JOIN tv_genres gen ON gen.id = s.genre_id WHERE gen.name IS NOT NULL OR gen.name IS NULL ORDER BY n.title, gen.name;
