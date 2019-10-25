# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 08:45:14 2019

@author: Michael ODonnell
"""

# Goal: generate puesdo-data for a mySQL database that has three tables:
    # table 1: apartments
    # table 2: buildings
    # table 3: tenants

import pandas as pd
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import random
    
### First, building puesdo-dataset for table: apartments ###

# build empty dataframe to match apartments table headers:
apt_columns = ['apartment_id', 'building_id', 'vacant_status',
               'rent','pet_friendly']
apartments = pd.DataFrame(columns = apt_columns)


# create 1,000 records in apartments dataframe
for r in range(1,1000):
    
    new_record = {'apartment_id': r,
                  'building_id': random.randint(1,10),
                  'vacant_status': random.randint(0,1),
                  'rent': random.randint(750,5500),
                  'pet_friendly': random.randint(0,1)}
    
    new_record_df = pd.DataFrame(columns = apt_columns,
                                 data = [new_record])
    apartments = apartments.append(new_record_df)

### Second, building puesdo-dataset for table: buildings ###

# build empty dataframe to match buildings table headers:
buildings_columns = ['building_id', 'building_address', 'city',
                     'floors', 'units', 'built_year']
buildings = pd.DataFrame(columns = buildings_columns)

# streets and cities to create addresses
street = ["Pearl", "Peach", "Gordon", "2nd", "Yellowstone",
          "Winners", "El Camino Real", "Bluestone",
          "Green", "Astor", "6th"]

street_suffix = ["St", "Ave", "Ln", "Ct", "Rd",
                 "Way", "Dr", "Pl", "Drive", "Road",
                 "Street"]

city = ["Orlando", "Los Angeles", "Seattle", "San Francisco", "Chicago",
        "Portland", "Wilmington", "Miami", "Denver", "Boulder", "New York"]

# fill buildings table with 10 buildings (lots of data generated randomly)
for b in range(1,11):
    new_building = {'building_id': b,
                    'building_address': str(str(random.randint(1,1000))+" "+
                                            street[b]+" "+street_suffix[random.randint(1,10)]),
                    'city': city[random.randint(0,10)],
                    'floors': random.randint(3,12),
                    'units': apartments[apartments.building_id == b].apartment_id.count(),
                    'built_year': random.randint(1904, 1995)}
    new_building_df = pd.DataFrame(columns = buildings_columns,
                                 data = [new_building])
    buildings = buildings.append(new_building_df)


### Third, building puesdo-dataset for table: tenants ###

# build empty dataframe to match tenants table headers:
tenants_columns = ['tenant_id', 'tenant_name', 'apartment_id',
                   'renter_income', 'lease_start', 'lease_end']
tenants = pd.DataFrame(columns = tenants_columns)

# scrape list of common first and last names to create puesdo-names
# https://www.codementor.io/dankhan/web-scrapping-using-python-and-beautifulsoup-o3hxadit4
"""
url = "https://www.weddingvendors.com/baby-names/popular/1993/"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
tb = soup.find('table', class_='wikitable')

for link in tb.find_all('b'):
    first_name = link.find('a')
    print(name)
"""

# create random names
first_name = ['Michael', 'John', 'Adam', 'Kelly', 'Keith', 'Chuck', 'Samantha',
              'Emily', 'Cameryn', 'Julia', 'Cassy', 'Joel', 'Valerie', 'Jim']

# set all first names to uppercase, to match last names
for n in range(len(first_name)):
    first_name[n] = first_name[n].upper()

# https://names.mongabay.com/most_common_surnames.htm
last_name = ['SMITH','JOHNSON','WILLIAMS','JONES','BROWN','DAVIS','MILLER',
             'WILSON','MOORE','TAYLOR','ANDERSON','THOMAS','JACKSON','WHITE',
             'HARRIS','MARTIN','THOMPSON','GARCIA','MARTINEZ','ROBINSON',
             'CLARK','RODRIGUEZ','LEWIS','LEE','HERNANDEZ']

for t in range(apartments[apartments.vacant_status == 0].apartment_id.count()):
    new_tenant = {'tenant_id': str(5)+str(t),
                  'tenant_name': str(first_name[random.randint(0,len(first_name)-1)]+
                                                " "+last_name[random.randint(0,len(last_name))-1]),
                  'apartment_id': t+1,
                  'renter_income': random.randint(32000, 221000),
                  'lease_start': str(str(random.randint(1999, 2018))+
                                     "-"+str(random.randint(10, 12))+
                                     "-"+str(random.randint(10, 28))),
                  'lease_end': str(str(2019)+
                                     "-"+str(random.randint(10, 12))+
                                     "-"+str(random.randint(10, 28)))}
    new_tenant_df = pd.DataFrame(columns = tenants_columns,
                                 data = [new_tenant])
    tenants = tenants.append(new_tenant_df)

# change dataframe indexes for mySQL
apartments = apartments.set_index('apartment_id')
buildings = buildings.set_index('building_id')
tenants = tenants.set_index('tenant_id')

# export all three dataframes as csv's
apartments.to_csv("apartments.csv")
buildings.to_csv("buildings.csv")
tenants.to_csv("tenants.csv")