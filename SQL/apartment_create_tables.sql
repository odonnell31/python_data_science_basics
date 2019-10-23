SHOW VARIABLES LIKE "secure_file_priv";

DROP TABLE apartments;
DROP TABLE buildings;
DROP TABLE tenants;

CREATE TABLE apartments (apartment_id int, building_id int,
       vacant_status int, rent int, pet_friendly int,
       PRIMARY KEY (apartment_id));

LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\apartments.csv' 
INTO TABLE apartments 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

SELECT * FROM apartments;

CREATE TABLE buildings (building_id int, building_address VARCHAR(75),
		city VARCHAR(25), floors int, units int, built_year int,
        PRIMARY KEY (building_id));

LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\buildings.csv' 
INTO TABLE buildings 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

SELECT * FROM buildings;

CREATE TABLE tenants (tenant_id int, tenant_name VARCHAR(50), 
		apartment_id int, renter_income int,
        lease_start DATE, lease_end DATE,
        PRIMARY KEY (tenant_id));

LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\tenants.csv' 
INTO TABLE tenants
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

SELECT * FROM tenants;

SHOW TABLES;