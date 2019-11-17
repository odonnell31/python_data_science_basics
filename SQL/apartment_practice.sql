SELECT * FROM apartments
LIMIT 5;

SELECT * FROM buildings
LIMIT 5;

SELECT * FROM tenants
LIMIT 5;

SELECT tenant_name, lease_end
FROM tenants
WHERE lease_end BETWEEN '2019-11-01' AND '2019-11-30'
ORDER BY lease_end;

ALTER TABLE apartments
DROP COLUMN apartment_notes;

DROP TABLE apartments;

CREATE TABLE practice_table (col1 int,
col2 VARCHAR(10), col3 DATE, col4 binary,
PRIMARY KEY (col1));

INSERT INTO practice_table
VALUES(1, 'temp', '2019-10-10', 1, 1000);

TRUNCATE TABLE practice_table;

ALTER TABLE practice_table
ADD col5 int;

INSERT INTO practice_table
VALUES(1, 'temp', '2019-10-10', 1, 1000);

UPDATE practice_table
SET col1 = 20
WHERE col1 = 1;




