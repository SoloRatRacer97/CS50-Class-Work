


















-- List the names of all people who starred in a movie in which Kevin Bacon also starred.

SELECT name
FROM people 
WHERE name = 
(SELECT title 
FROM movies JOIN stars ON stars.movie_id = movies.id JOIN people ON stars.person_id = people.name
WHERE name = "Kevin Bacon" AND year = 1958)



SELECT DISTINCT name
FROM stars ON stars.person_id = people.id
WHERE movie_id IN
(SELECT movie_id
FROM people JOIN stars ON stars.person_id = people.id
WHERE birth = 1958 AND name = "Kevin Bacon")
AND name <> "Kevin Bacon";


