# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 08:33:26 2019

@author: Michael ODonnell
"""

# Question:
# Given a string, write a function to check if it is a permutation of a palindrome.
# A palindrome is a word or phrase that is the same forwards and backwards.
# A permutation is a rearrangement of the letters. The palindrome does not
# need to be limited to only dictionary words.
# ex: "Tact Coa" is True, permutation: "taco cat" and "atco cta"

def palindrome_perm(s):
    # first, remove spaces from s and convert to lowercase
    s = s.replace(' ', '')
    s = s.lower()
    
    
    # next, make a dict with a key for each char in s
    s_dict = {}
    for i in s:
        if i not in s_dict.keys():
            s_dict[i] = 1
        else:
            s_dict[i] = s_dict[i]+1
    print(s_dict)
    
    # next, make a dict for even and odd values of s_dict
    even_odd = {'even': 0, 'odd': 0}
    for j in s_dict.values():
        if j%2 == 0:
            even_odd['even'] = even_odd['even'] + 1
        else:
            even_odd['odd'] = even_odd['odd'] + 1
    
    if even_odd['odd'] <= 1 and len(s)>0:
        print("Yes, string is a permutation of a palindrome!")
    else:
        print("No, string is not a permutation of a palindrome")
        
        
palindrome_perm("Tact Coa")