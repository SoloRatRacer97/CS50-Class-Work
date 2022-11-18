

















-- List the titles of all movies in which both Johnny Depp and Helena Bonham Carter starred.

SELECT title 
FROM movies 
JOIN stars ON stars.movie_id = movies.id JOIN people ON people.id = stars.person_id JOIN ratings ON ratings.movie_id = stars.movie_id 
WHERE name = 'Chadwick Boseman' ORDER BY rating DESC Limit 5;





SELECT title FROM movies JOIN stars ON stars.movie_id = movies.id JOIN people ON people.id = stars.person_id WHERE name = "Johhny Depp" INTERSECT SELECT title FROM people JOIN stars ON stars.person_id = people.id JOIN movies ON movies.id = stars.movie_id WHERE name = "Helena Bonham Carter";


