# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 08:29:45 2019

@author: Michael ODonnell
"""

# Question:
# First, create a method isSubstring which checks if one word is a substring of another.
# Then given two strings, s1 and s2, write code to check if s2 is a rotation
# of s1 using only one call to isSubstring.
# example: "waterbottle" is a rotation of "erbottlewat"

def isSubstring(word, sub):
    # check is the sub is in the word.. return as boolean value
    if sub in word:
        return True
    else:
        return False
        
print(isSubstring("test", "es"))

def string_rotation(s1, s2):
    # ok, this is an unusual solution to this problem
    # but, I'm going to write out s1 three times
    # then, check if s2 is a substring of that elongated s1
    
    # so first, extend s1 to be 3 consecutive s1's
    s1_three_times = s1*3
    
    # then, check if s2 is a substring of the elongated s1
    if isSubstring(s1_three_times, s2) == True:
        print("yes,", s2, "is a rotation of", s1)
    else:
        print("no,", s2, "is not a rotation of", s1)
    
    
string_rotation("waterbottle", "erbottlewat")    