















SELECT AVG(rating) FROM ratings JOIN movies ON movies.id = ratings.movie_id WHERE year = '2012';




-- List all movies released in 2010 and their ratings, in descending order by rating. For movies with the same rating, order them alphabetically by title.

-- the first ORDER BY takes priority over the second ORDER BY



SELECT title, rating 
FROM movies JOIN ratings ON ratings.movie_id = movies.id 
WHERE year = 2010
ORDER BY rating DESC, title ASC;