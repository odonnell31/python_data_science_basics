# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 09:05:39 2019

@author: Michael O'Donnell
"""

# Question
# Sort two lists of words, A and B, into list A in alphabetical order



words_list = ['Sort', 'these', 'words', 'alphabetically', 'using', 'merge', 'sort']

# OK, going to employ merge sort, with a twist for alphabetical
def merge_sort_words(alist):
    # statment to avoid an infinite loop..    
    if len(alist)>1:
        
        # make all words to lowercase
        for i in range(len(alist)):
            alist[i] = alist[i].lower()
        
        print("splitting", alist, "into 2 pieces")
        
        # splitting the list in the middle
        middle = len(alist) // 2
        left_half = alist[:middle]
        right_half = alist[middle:]
        
        # make this function recursive
        merge_sort_words(left_half)
        merge_sort_words(right_half)
        
        # make three counters for the heavy lifting of this function
        i = 0
        j = 0
        k = 0
        
        # compare words and merge them back into alist
        while i < len(left_half) and j < len(right_half):
            # create a temporary list to quickly compare words alphabetically
            temp_list = [left_half[i], right_half[j]]
            if left_half[i] == sorted(temp_list)[0]:
                alist[k] = left_half[i]
                i = i+1
            else:
                alist[k] = right_half[j]
                j = j+1
            k = k+1
        
        # fill out list if right half is empty but left half isn't
        while i < len(left_half):
            alist[k] = left_half[i]
            i = i+1
            k = k+1
        
        # fill out list if left half is empty but right half isn't
        while j < len(right_half):
            alist[k] = right_half[j]
            j = j+1
            k = k+1
            
        print("merging", alist)
        
merge_sort_words(words_list)
print(words_list)