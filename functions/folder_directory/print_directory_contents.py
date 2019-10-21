# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 20:06:41 2019

@author: ODsLaptop
"""

# Question: create a function that takes a file directory and prints the paths within that directory

def print_directory_contents(path):
    import os
    for f in os.listdir(path):
        contents = os.path.join(path, f)
        if os.path.isdir(contents):
            print_directory_contents(contents)
        else:
            print(contents)
            
print_directory_contents("C:\\Users\\ODsLaptop\\Documents\\MO.work\\python_basics\\python_data_science_basics")