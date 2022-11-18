













SELECT title, rating 
FROM movies JOIN ratings ON ratings.movie_id = movies.id 
WHERE year = 2010
ORDER BY rating DESC, title ASC;


-- List the names of all people who starred in Toy Story.





SELECT name FROM people JOIN stars ON stars.person_id = people.id JOIN movies ON movies.id = stars.movie_id WHERE title = 'Toy Story';