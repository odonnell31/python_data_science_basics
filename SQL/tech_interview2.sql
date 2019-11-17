CREATE TABLE stores
(store_name VARCHAR(50), store_id int,
city VARCHAR(50));

INSERT INTO stores
(store_name, store_id, city)
VALUES
("store123", 1, "Philly"),
("store126", 2, "New York"),
("store213", 3, "Seattle"),
("storeX", 4, "Mountain View");

CREATE TABLE store_desc
(store_id int, store_size int,
tier int, year_built int);

INSERT INTO store_desc
(store_id, store_size, tier, year_built)
VALUES
(1, 500, 200, 1986),
(2, 750, 100, 2008),
(3, 2000, 100, 2017),
(4, 1250, 100, 1999);

CREATE TABLE sales
(store_id int, transaction_id int,
customer_id int, purch_amt float,
purch_date date);

INSERT INTO sales
(store_id, transaction_id, customer_id, purch_amt, purch_date)
VALUES
(1, 1, 65, 78.97, '2019-11-01'),
(2, 2, 34, 890.12, '2019-11-01'),
(3, 3, 57, 31.31, '2019-11-01'),
(4, 4, 98, 91.91, '2019-11-01'),
(1, 5, 35, 78.34, '2019-11-01'),
(2, 6, 96, 71.98, '2019-11-01'),
(3, 7, 82, 205.00, '2019-11-06'),
(4, 8, 43, 19.95, '2019-11-06'),
(1, 9, 12, 1.95, '2019-11-06'),
(2, 10, 19, 210.11, '2019-11-06'),
(3, 11, 30, 39.95, '2019-11-06'),
(4, 12, 43, 71.55, '2019-11-06'),
(1, 13, 100, 43.99, '2019-11-06'),
(2, 14, 91, 99.99, '2019-11-06'),
(3, 15, 58, 109.14, '2019-11-06'),
(4, 16, 42, 25.00, '2019-11-07'),
(1, 17, 43, 75.10, '2019-11-07'),
(2, 18, 96, 50.00, '2019-11-07'),
(3, 19, 101, 0.99, '2019-11-07'),
(4, 20, 102, 204.95, '2019-11-07');

SELECT * FROM stores;
SELECT * FROM store_desc;
SELECT * FROM sales;

# get average sales of all stores by date
SELECT purch_date AS "s_date", AVG(purch_amt) AS "Average Sales"
FROM sales
GROUP BY s_date
ORDER BY s_date;

# return sum of sales by day in each store
SELECT stores.store_name, sales.purch_date, SUM(sales.purch_amt)
FROM sales
LEFT JOIN stores
ON sales.store_id = stores.store_id
GROUP BY stores.store_name, sales.purch_date
ORDER BY sales.purch_date, SUM(sales.purch_amt) DESC;