# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 08:31:46 2019

@author: Michael ODonnell
"""

# Question:
# write a method to replace all spaces in a string with '%20'
# You may assume that the string has sufficient space at the end to
# hold the addition characters, and that you are given the "true"
# length of the string.

def replace_spaces(s):
    # using python's built-in replace function to replace spaces
    # this question may be more difficult in other languages..
    s = s.replace(' ', '%20')
    print(s)
    
replace_spaces("test string here..")