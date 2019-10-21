# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 17:06:32 2019

@author: Michael ODonnell

SQL Practice
"""

# three tables: salespeople, orders, customers

"""
table: salespeople

    sales_id |    name    |   city   | commission 
-------------+------------+----------+------------
        5001 | James Hoog | New York |       0.15
        5002 | Nail Knite | Paris    |       0.13
        5005 | Pit Alex   | London   |       0.11
        5006 | Mc Lyon    | Paris    |       0.14
        5007 | Paul Adam  | Rome     |       0.13
        5003 | Lauson Hen | San Jose |       0.12
        
table: orders

ord_no    | purch_amt | ord_date   | customer_id | sales_id
----------  ----------  ----------  -----------  -----------
70001     | 150.5     | 2012-10-05 | 3005        | 5002
70009     | 270.65    | 2012-09-10 | 3001        | 5005
70002     | 65.26     | 2012-10-05 | 3002        | 5001
70004     | 110.5     | 2012-08-17 | 3009        | 5003
70007     | 948.5     | 2012-09-10 | 3005        | 5002
70005     | 2400.6    | 2012-07-27 | 3007        | 5001
70008     | 5760      | 2012-09-10 | 3002        | 5001
70010     | 1983.43   | 2012-10-10 | 3004        | 5006
70003     | 2480.4    | 2012-10-10 | 3009        | 5003
70012     | 250.45    | 2012-06-27 | 3008        | 5002
70011     | 75.29     | 2012-08-17 | 3003        | 5007
70013     | 3045.6    | 2012-04-25 | 3002        | 5001

table: customers

customer_id  |   cust_name    |    city    | grade |    sales_id 
-------------+----------------+------------+-------+-------------
        3002 | Nick Rimando   | New York   |   100 |        5001
        3007 | Brad Davis     | New York   |   200 |        5001
        3005 | Graham Zusi    | California |   200 |        5002
        3008 | Julian Green   | London     |   300 |        5002
        3004 | Fabian Johnson | Paris      |   300 |        5006
        3009 | Geoff Cameron  | Berlin     |   100 |        5003
        3003 | Jozy Altidor   | Moscow     |   200 |        5007
        3001 | Brad Guzan     | London     |   100 |        5005
"""
#import MySQLdb
import pandas as pd


db = MySQLdb.connect(host="localhost",    # host
                     user="michael1991",  # username
                     passwd="password1",  # password
                     db="student_data")   # name of the database

# create a Cursor object to execute SQL queries
cursor = db.cursor()




# Question 1: get all information from 'salesmen'
sql_query = cursor.execute("SELECT * FROM salespeople;")

# print all the first cell of all the rows
for row in cursor.fetchall():
    print(row[0])
    
    
    
# Question 2: get sales_id, name from 'salesmen'
sql_query = cursor.execute("SELECT sales_id, name FROM salespeople;")

# print all the first cell of all the rows
for row in cursor.fetchall():
    print(row[0])



# Question 3: retrieve the value of sales_id of all salespeople,
# getting orders from the customers in orders table without any repeats
sql_query = cursor.execute("SELECT DISTINCT sales_id FROM orders;")

# print all the first cell of all the rows
for row in cursor.fetchall():
    print(row[0])
    
    
# Question 4: display names and city of salespeople based in Paris
sql_query = cursor.execute("SELECT sales_id, name FROM salespeople
                               WHERE city='Paris';")

# print all the first cell of all the rows
for row in cursor.fetchall():
    print(row[0])
    
    
# Question 5: display customer names with a grade of at least 200 and from NY
sql_query = cursor.execute("SELECT cust_name FROM customers
                               WHERE grade>=200
                               AND city='New York')

# print all the first cell of all the rows
for row in cursor.fetchall():
    print(row[0])
    

# Question 6: display customer names, city of customers with first name 'Brad'
sql_query = cursor.execute("SELECT cust_name, city FROM customers
                               WHERE cust_name LIKE 'Brad%')

# print all the first cell of all the rows
for row in cursor.fetchall():
    print(row[0])
    

# Question 7: display all customers not from 'New York' or 'London' ordered by grade
sql_query = cursor.execute("SELECT cust_name, city FROM customers
                               WHERE city NOT IN('New York', 'London')
                                ORDER BY grade DESC;)

# print all the first cell of all the rows
for row in cursor.fetchall():
    print(row[0])
    

# Question 8: display all salespeople with commission greater than 0.12 but less than 0.16
sql_query = cursor.execute("SELECT name, commission FROM salespeople
                               WHERE commission BETWEEN 0.12 AND 0.15
                               ORDER BY commission DESC;)

# print all the first cell of all the rows
for row in cursor.fetchall():
    print(row[0])


# Question 9: calculate the average grade of each city from customers table
sql_query = cursor.execute("SELECT city, avg(grade) FROM customers
                               GROUP BY city
                               ORDER BY avg(grade) DESC;)

# print all the first cell of all the rows
for row in cursor.fetchall():
    print(row[0])
    
    
# Question 10: calculate the average grade of each city from customers table
sql_query = cursor.execute("SELECT city, avg(grade) FROM customers
                               GROUP BY city
                               ORDER BY avg(grade) DESC;)

# print all the first cell of all the rows
for row in cursor.fetchall():
    print(row[0])

db.close()