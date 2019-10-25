# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 20:30:10 2019

@author: Michael ODonnell
"""

# Question
# Implement a method to perform basic string compression using the counts
# of repeated characters. For example, the string aabcccccaaa would become
# a2b1c5a3. If the compressed string is longer than the original string,
# return the original string

def compress_string(s):
    # attempting to complete in <10 mins
    
    # first, create an empty dictionary to store indexes of each new char
    char_dict = {}
    # create counter i to count number of consecutive occurences of char
    i = 0
    
    # loop through the string and add each non-repeated char index to dict
    for c in range(len(s)):
        if s[c] != s[c-1]:
            char_dict[c] = 1
            i = 1
        else:
            char_dict[c-i] = char_dict[c-i]+1
            i = i + 1
    
    # make empty list to add char_dict keys and values
    compressed_s = []
    
    for d in char_dict:
        compressed_s.append(s[d])
        compressed_s.append(char_dict[d])
    
    # turn list into string (pretty nifty statement)
    compressed_s = ''.join(str(x) for x in compressed_s)
    
    # print the compressed string if its shorter than the original
    if len(compressed_s) >= len(s):
        print(s)
    
    else:
        print(compressed_s)
        

# test it!            
compress_string("aaabcdeeefggggg")

# much more difficult than expected!
                
    