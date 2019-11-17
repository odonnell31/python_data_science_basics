CREATE TABLE movies
(movie_name VARCHAR(50), movie_id int,
genre VARCHAR(50));

CREATE TABLE movie_goers
(movie_id int, visitor_id int);

CREATE TABLE visitor_desc
(visitor_id int, visitor_name VARCHAR(50),
favorite_genre VARCHAR(50));

INSERT INTO movies
(movie_name, movie_id, genre)
VALUES
("Avengers", 1, "superhero"),
("Spiderman 2", 2, "superhero"),
("Forest Gump", 3, "adventure");

INSERT INTO movie_goers
(movie_id, visitor_id)
VALUES
(1, 10),
(1, 11),
(1, 12),
(1, 13),
(1, 14),
(1, 15),
(1, 16),
(2, 17),
(2, 18),
(2, 19),
(2, 11),
(3, 12),
(3, 13),
(3, 14),
(3, 15),
(3, 16);

INSERT INTO visitor_desc
(visitor_id, visitor_name, favorite_genre)
VALUES
(10, "Michael", "adventure"),
(11, "Cameryn", "adventure"),
(12, "Porter", "superhero"),
(13, "Kristin", "superhero"),
(14, "Lambert", "superhero"),
(15, "Kevin", "horror"),
(16, "Dubya", "adventure"),
(17, "Erin", "superhero"),
(18, "Garrett", "volleyball"),
(19, "Kat", "horror");

SELECT * FROM movies;
SELECT * FROM movie_goers;
SELECT * FROM visitor_desc;

# return all movies that have at least the average number of visitors
SELECT COUNT(*)/COUNT(DISTINCT movie_id) FROM movie_goers;

SELECT movies.movie_name, COUNT(movie_goers.visitor_id)
FROM movie_goers
LEFT JOIN movies
ON movie_goers.movie_id = movies.movie_id
GROUP BY movies.movie_name
HAVING COUNT(movie_goers.visitor_id) >= (SELECT COUNT(*)/COUNT(DISTINCT movie_id) FROM movie_goers);

SELECT movies.movie_name, COUNT(movie_goers.visitor_id)
FROM movie_goers
LEFT JOIN movies
ON movie_goers.movie_id = movies.movie_id
GROUP BY movies.movie_name
HAVING COUNT(movie_goers.visitor_id) >= 5;

