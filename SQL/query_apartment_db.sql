# find the average rent of an apartment in each city:

SELECT buildings.city, apartments.rent
FROM apartments
JOIN buildings ON apartments.building_id = buildings.building_id
GROUP BY buildings.city
ORDER BY apartments.rent DESC;


# Find the top 10 tenants with the largest income to rent ratio:

SELECT tenants.tenant_name, (tenants.renter_income / apartments.rent) AS “Rent_Ratio”,
apartments.rent, tenants.renter_income AS "income"
FROM tenants
JOIN apartments on tenants.apartment_id = apartments.apartment_id
ORDER BY “Rent_Ratio” DESC
LIMIT 10;

# Which city has the greatest number of vacant apartments?

SELECT buildings.city, COUNT(apartments.vacant_status) AS “Vacants”
FROM buildings
JOIN apartments
ON buildings.building_id = apartments.building_id
WHERE apartments.vacant_status = 1
GROUP BY buildings.city
ORDER BY “Vacants” DESC;


# Which city has the most pet friendly apartments?

SELECT buildings.city, COUNT(apartments.apartment_id) AS "Pet_Friendly_Apts"
FROM buildings
JOIN apartments ON buildings.building_id = apartments.building_id
WHERE apartments.pet_friendly = 0
GROUP BY buildings.city
ORDER BY "Pet_Friendly_Apts" DESC;

SELECT * FROM apartments;