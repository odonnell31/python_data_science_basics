# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 11:25:14 2019

@author: Michael O'Donnell
"""

# Hypothetically, let's say there's multiple tables in mySQL data warehouse

"""
table: applied_students

    id | student_name     | high_school  |  gpa 
-------------+------------+----------+------------
     1 | John Doe         | Finley       |  3.15
     2 | Jane Green       | Smithtown    |  3.13
     3 | Max Rielly       | Long Beach   |  3.11
     4 | Adam Lyons       | Sachem North |  2.14
     5 | Samantha Rose    | Sachem East  |  3.13
     6 | Nicholas Johnson | San Jose     |  4.12


table: all_high_schools

 high_school_ID | high_school  |    city     | state | state_rank 
-------------+------------+----------+----------------------------
           5001 | Smithtown    | Long Island |    NY | 31
           5002 | Long Beach   | Long Island |    NY | 12
           5005 | Sachem North | Long Island |    NY | 75
           5006 | Sachem East  | Long Island |    NY | 56
           5007 | Finley       | Wilmington  |    DE | 15
           5003 | San Jose     | NorCal      |    CA | 101


# To get the needed data from mySQL into python, use MySQLdb library
#import MySQLdb
import pandas as pd


db = MySQLdb.connect(host="localhost",    # host
                     user="michael1991",  # username
                     passwd="password1",  # password
                     db="student_data")   # name of the database

# create a Cursor object to execute SQL queries
cursor = db.cursor()

# grab needed data with SQL query
sql_query = cursor.execute("SELECT id, student_name, high_school, gpa
                           FROM applied_students
                           RIGHT JOIN all_high_schools
                           ON applied_students.high_school = all_high_schools.high_school")

# store all rows from sql_query in pandas dataframe
students_df = pd.read_sql(sql_query, db)

db.close()
"""

# now, to visualize and clean student_df

# not actually connected to SQL database, so building the needed dataframe
import pandas as pd
students_dict = {'id': [1, 2, 3, 4, 5,
                        6, 7, 8, 9, 10],
        'student_name': ['John Doe', 'Jane Green',
                         'Maxie Rielly', 'Maxi Rielly',
                         'Nicholas House', 'Sarah Wagner',
                         'Nolan Gerald', 'Katie Flynn',
                         'Edguardo Bovia', 'Nick House',
                         ],
        'high_school': ['Finley', 'Smithtown',
                        'Long Beach', 'Long Beach',
                        'Sachem East', 'Sachem North',
                        'Smithtown', 'Long Beach',
                        'Finley', 'Sachem East'],
        'gpa': [3.15, 3.13, 3.11, 3.11, 2.09,
                2.19, 1.95, 2.42, 2.51, 2.09],
        'high_school_ID': [5001, 5002, 5003, 5003, 5002,
                           5007, 5002, 5003, 5004, 5007],
        'city': ['Santa Clara', 'Long Island',
                 'Long Island', 'Long Island',
                 'Long Island', 'Long Island',
                 'Long Island', 'Long Island',
                 'Santa Clara', 'Long Island'],
        'state': ['CA','NY','NY','NY', 'NY',
                  'NY','NY','NY','CA', 'NY'],
        'state_rank': [31, 12, 75, 75, 10,
                       34, 12, 56, 35, 10]}

students_df = pd.DataFrame(data = students_dict)

# printing some general numbers
print("number of applicants:", len(set(students_df['id'])))
print("number of high schools applied from:", len(set(students_df['high_school'])))
print("number of states applied from:", len(set(students_df['state'])))
print("breakdown of gpa's:")
# plot the breakdown of gpas
import matplotlib.pyplot as plt
plt.hist(students_df['gpa'], range = [0,4])


# make a function to detect name similarity
from difflib import SequenceMatcher
def similar_names(n1, n2):
    return SequenceMatcher(None, n1, n2).ratio()

# function to find possible duplicates
def possible_duplicate_students():
    duplicate_records = []
    for index, row in students_df.iterrows():
        for check_i, check_row in students_df.iterrows():
            if index != check_i and ([check_i, index]) not in duplicate_records:
                if similar_names(row['student_name'], check_row['student_name']) > 0.6:
                    duplicate_records.append([index, check_i])
                    print("found similar records:", (index, row['student_name']),
                          (check_i, check_row['student_name']))
                
possible_duplicate_students()