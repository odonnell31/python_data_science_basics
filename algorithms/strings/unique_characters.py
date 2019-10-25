# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 12:16:01 2019

@author: Michael ODonnell
"""

# Question
# write an algorithm to determine if a string has all unique characters

def unique_chars(word):
    # plan of attack: append each character to a list, if it is not in list already
    
    # create empty list to append new characters to
    char_list = []
    
    # loop through the word once
    for i in word:
        # if character not in char_list, add it to the list
        if i not in char_list:
            char_list.append(i)
        # if character is already in char_list, return False
        else:
            return(word, "does not have all unique characters")
    return(word, "contains all unique characters")

# test the method
for w in ['test', 'multiple', 'words', 'with', 'this', 'function']:
    print(unique_chars(w))