# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 08:43:43 2019

@author: 432663
"""

# Question: Implement a function to check if a linked list is a palindrome

def linked_list_palindrome(linked_list):
    # loop through the linked list and store each value in a val_list
    val_list = []
    
    currrent_node = linked_list.head
    while current_node is not None:
        val_list.append(current_node.data)
        current_node = current_node.next
        
    # now, check if val_list is a palindrome
    reverse_val_list = val_list[::-1]
    
    if val_list == reverse_val_list:
        return True
    else:
        return False