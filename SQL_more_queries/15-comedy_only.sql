-- script that lists all Comedy shows in the database hbtn_0d_tvshows
SELECT n.title FROM tv_shows n JOIN tv_show_genres s ON n.id = s.show_id JOIN tv_genres gen ON gen.id = s.genre_id WHERE gen.name = 'Comedy' ORDER BY n.title;
