CREATE TABLE people
(id int, motherId int,
fatherId int, first_name VARCHAR(50),
age int);

INSERT INTO people
(id, motherId, fatherId, first_name, age)
VALUES
(1, NULL, NULL, "Adam", 50),
(2, NULL, NULL, "Eve", 50),
(3, 2, 1, "Cain", 30),
(4, 2, 1, "Abel", 20);

SELECT * FROM people;

ALTER TABLE people
ADD COLUMN childId int;

UPDATE people pt1, people pt2
SET pt2.childId = pt1.id
WHERE pt2.id = pt1.motherId
OR pt2.id = pt1.fatherId;

SELECT * FROM people;


CREATE VIEW parents AS
SELECT * FROM people
WHERE motherId IS NOT NULL
AND fatherId IS NOT NULL;



SELECT * FROM parents;
