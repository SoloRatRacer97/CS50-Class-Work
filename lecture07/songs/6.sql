





1) need to get artist if for post malone
2) Then return the id and compare it to the id in songs
3) Then, we can use that id to get the name of the songs that contain that id



SELECT names FROM songs WHERE artist_id = (SELECT id FROM artists WHERE name = 'Post Malone')