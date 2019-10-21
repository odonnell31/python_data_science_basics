# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 20:06:41 2019

@author: ODsLaptop
"""

# Question: create a function that takes a file directory and prints the paths within that directory

def print_directory_contents(path):
    
    # import os library to operate with our operating system
    import os
    
    # loop through all names of contents in the path
    for f in os.listdir(path):
        # use .join() to add name onto end of path
        contents = os.path.join(path, f)
        # use .isdir() to check if contents is a non-empty folder
        if os.path.isdir(contents):
            #if contents is a non-empty folder, run this function on it recursively!
            print("within folder:", contents)  
            print_directory_contents(contents)
        else:
            print(contents)
            
print_directory_contents("C:\\Users\\ODsLaptop\\Documents\\MO.work\\python_basics\\python_data_science_basics\\functions")