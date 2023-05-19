-- script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter
SELECT gen.name AS name FROM tv_genres gen JOIN tv_show_genres s ON gen.id = s.genre_id JOIN tv_shows n ON n.id = s.show_id WHERE n.title = 'Dexter' 
