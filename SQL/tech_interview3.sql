CREATE TABLE customer_survey
(customer_id int, score float, submitted datetime);

INSERT INTO customer_survey
(customer_id, score, submitted)
VALUES
(501, 9, '2019-11-1 15:30:36'),
(502, 8, '2019-11-1 15:30:36'),
(503, 7, '2019-11-1 15:30:36'),
(504, 6, '2019-11-1 15:30:36'),
(505, 5, '2019-11-1 15:30:36'),
(501, 8, '2019-11-2 12:30:36'),
(502, 7, '2019-11-2 12:30:36'),
(503, 6, '2019-11-2 13:30:36'),
(504, 10, '2019-11-2 15:30:36'),
(501, 3, '2019-11-2 17:30:36');

SELECT * FROM customer_survey;

# select the most recent score from each customer_id
SELECT customer_id, score, max(submitted) 
FROM customer_survey
GROUP BY customer_id
ORDER BY submitted DESC;

TRUNCATE TABLE customer_survey;