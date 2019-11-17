CREATE TABLE customers
(customer VARCHAR(50), customer_id int);

INSERT INTO customers
(customer, customer_id)
VALUES ("cust one", 123);

INSERT INTO customers
(customer, customer_id)
VALUES ("cust two", 124);

INSERT INTO customers
(customer, customer_id)
VALUES ("cust three", 125);

INSERT INTO customers
(customer, customer_id)
VALUES ("cust four", 125);

SELECT * FROM customers;

CREATE TABLE transactions
(customer_id int, transaction_id int, amount int);

INSERT INTO transactions
(customer_id, transaction_id, amount)
VALUES (123, 001, 1000);

INSERT INTO transactions
(customer_id, transaction_id, amount)
VALUES (124, 002, 2000);

INSERT INTO transactions
(customer_id, transaction_id, amount)
VALUES (124, 003, 3000);

SELECT * FROM transactions;



SELECT customers.customer, COUNT(transactions.transaction_id) AS "cust_transactions"
FROM customers
LEFT JOIN transactions
ON customers.customer_id = transactions.customer_id
GROUP BY customers.customer
ORDER BY COUNT(transactions.transaction_id) DESC;

CREATE TABLE students
(student_name VARCHAR(100), score int, class int);

INSERT INTO students
(student_name, score, class)
VALUES ("Michael", 85, 2),
("Dwight", 91, 4),
("Phillis", 91, 4),
("Pam", 89, 4),
("Jim", 99, 7),
("Angela", 92, 2),
("Andy", 80, 5);

SELECT * FROM students;



SELECT students.student_name, students.score, students.class
FROM students
LEFT JOIN (SELECT max(score), class
FROM STUDENTS
GROUP BY class) AS table2
ON students.class = table2.class;


CREATE TABLE fsia
(company VARCHAR(50), marketCap int);

INSERT INTO fsia
(company, marketCap)
VALUES
("fiat", 100),
("ford", 200),
("jeep", 300);

SELECT * FROM fsia;

CREATE TABLE fsib
(company VARCHAR(100), share_price int,
share_volume int);

INSERT INTO fsib
(company, share_price, share_volume)
VALUES
("chevy", 10, 25),
("crysler", 12, 32),
("toyota", 15, 21);

SELECT * FROM fsib;

CREATE VIEW marketCap_b AS
SELECT company, (share_price * share_volume) AS "marketCap"
FROM fsib;

INSERT INTO fsia
SELECT * FROM marketCap_b;

SELECT * FROM fsia;