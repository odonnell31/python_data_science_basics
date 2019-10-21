# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 22:00:40 2019

@author: ODsLaptop
"""

import urllib.request
from bs4 import BeautifulSoup
import pandas as pd



# URL of page we will scrape
url = "https://www.baseball-reference.com/leagues/MLB/2019.shtml"

html = urllib.request.urlopen('https://www.google.com/')

soup = BeautifulSoup(html,features="lxml")

# get the column headers
soup.findAll('tr', limit=2)

# extract text we need into a list, important to use [1] here
headers = [th.getText() for th in soup.findAll('tr', limit=2)[0].findAll('th')]
headers = headers[1:]
print(headers)