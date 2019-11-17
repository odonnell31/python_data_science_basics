SELECT buildings.building_id, buildings.city, COUNT(*)
FROM buildings
JOIN apartments
ON buildings.building_id = apartments.building_id
WHERE apartments.rent > 1000
GROUP BY buildings.building_id
ORDER BY COUNT(*) DESC;

CREATE VIEW richest_tenants AS
SELECT tenants.tenant_name, tenants.renter_income, apartments.pet_friendly
FROM tenants
JOIN apartments
ON tenants.apartment_id = apartments.apartment_id
WHERE apartments.pet_friendly = 1
ORDER BY tenants.renter_income DESC
LIMIT 5;

SELECT * FROM richest_tenants;

SELECT * FROM tenants
LIMIT 1;
