# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 22:48:26 2019

@author: Michael ODonnell
"""

# Question
# You are given two sorted arrays, A and B.
# Write a method to merge B into A in sorted order.
A = []
B = []

import random
for x in range(10):
    A.append(random.randint(1,100))
    B.append(random.randint(1,100))
    
print("A:", A)
print("B:", B)

def merge_sort(A):
    # for error checking, print each time we're splitting the list
    print("splitting", A, "into 2 pieces")
    
    if len(A)>1:
        # find the middle of the list
        middle = len(A) // 2
        left_half = A[:middle]
        right_half = A[middle:]
        
        # run this function on the halves recursively
        merge_sort(left_half)
        merge_sort(right_half)
        
        # create three counters
        i = 0
        j = 0
        k= 0
        
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                A[k] = left_half[i]
                i = i+1
            else:
                A[k] = right_half[j]
                j = j+1
            k = k+1
            
        while i < len(left_half):
            A[k] = left_half[i]
            i = i+1
            k = k+1
            
        while j < len(right_half):
            A[k] = right_half[j]
            j = j+1
            k = k+1
        
        print("Merging", A)
    

# add list B to list A
for y in B:
    A.append(y)
    
merge_sort(A)
print(A)
            