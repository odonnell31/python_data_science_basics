# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 22:24:33 2019

@author: ODsLaptop
"""

# Question: Implement an algorithm to determine is a string has all unique characters.

def all_unique_chars(string):
    # dict of characters in string
    char_dict = {}
    
    for i in string:
        if i in char_dict.keys():
            char_dict[i] = char_dict[i]+1
        else:
            char_dict[i] = 1
    
    if max(char_dict.values()) > 1:
        print("not unique")
    else:
        print("unique!")
    
all_unique_chars("testing..")
        