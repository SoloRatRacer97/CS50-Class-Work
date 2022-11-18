










SELECT name 
FROM people 
JOIN stars ON stars.person_id = people.id JOIN movies ON movies.id = stars.movie_id 
WHERE title = 'Toy Story';

-- We cannot do distinct here.... Need to do group by? No, we would still just end up with one Tom

-- Use GROUP BY Tom, person_id


-- List the names of all people who starred in a movie released in 2004, ordered by birth year.


SELECT DISTINCT(name) FROM people JOIN stars ON stars.movie_id = people.id JOIN movies ON movies.id = stars.movie_id WHERE year = '2004' GROUP BY name, person_id ORDER BY birth;