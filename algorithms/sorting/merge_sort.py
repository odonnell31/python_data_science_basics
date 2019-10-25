# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 21:02:27 2019

@author: Michael ODonnell
"""

# create a method to sort a list with merge sort

def merge_sort(alist):    
    print("Splitting", alist, "into 2 pieces...")
    
    if len(alist)>1:
        middle = len(alist) // 2
        # split list a into left and right
        left = alist[:middle]
        right = alist[middle:]
        
        # now comes the recusive element of merge sort..
        merge_sort(left)
        merge_sort(right)
        
        i = 0
        j = 0
        k = 0
        
        while i < len(left) and j < len(right):
            
            if left[i] < right[j]:
                alist[k] = left[i]
                i = i+1
            else:
                alist[k] = right[j]
                j = j+1
            k = k+1

        while i < len(left):
            alist[k]=left[i]
            i=i+1
            k=k+1

        while j < len(right):
            alist[k]=right[j]
            j=j+1
            k=k+1

    print("Merging ",alist)

alist = []

import random
for i in range(10):
    alist.append(random.randint(1,100))
merge_sort(alist)
print(alist)
            