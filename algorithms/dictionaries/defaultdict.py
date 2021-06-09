# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 11:05:56 2021

@author: ODsLaptop
"""

from collections import defaultdict

users = defaultdict(list)

for i in ["tom", "jane", "fred", "sara"]:
    users[i].append(len(i))

print(users)
print(users["tom"])
print(users["michael"])
