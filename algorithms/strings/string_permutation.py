# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 08:29:06 2019

@author: Michael ODonnell
"""

# Question:
# Given two strings, write a method to decide if one is a permutation of the other.

def string_permutation(s1, s2):
    # simply, compare the two strings as sorted lists
    if sorted(s1) == sorted(s2):
        print("the strings are permutations of one another!")
    else:
        print("not permutations!")
    
string_permutation("test", "etst")