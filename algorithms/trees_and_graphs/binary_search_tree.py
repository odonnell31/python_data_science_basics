# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 15:21:34 2019

@author: Michael ODonnell
"""

# first question: build a binary search tree

class Node:
    def __init__(self,value):
        self.value = value
        self.left_child = None
        self.right_child = None
        
def insert(root, node):
    # if their is no root, this is the root. done.
    if root == None:
        root = node
        
    # else, lets figure out where to place this node
    else:
        
        # so, if the node is greater than the root, diert it to right child
        if node.value > root.value:
            if root.right_child == None:
                root.right_child = node
            else:
                insert(root.right_child, node)
        
        # if the node is <= root, direct it to the left child
        if node.value <= root.value:
            if root.left_child == None:
                root.left_child = node
            else:
                insert(root.left_child, node)               

# A utility function to do inorder tree traversal 
def print_tree_in_order(root): 
    if root != None:
        print_tree_in_order(root.left_child) 
        print(root.value) 
        print_tree_in_order(root.right_child) 
        
        
        
# second question: implement a function to determine is a binary tree is a binary seach tree.
                    
def isBST(root):
    # an empty tree is a BST
    if root == None:
        return True
    
    def check_node(node, lower = -100000000, upper = 100000000):
        
        if node == None:
            return True
        
        value = node.value
    
        if value >= upper or value <= lower:
            return False
        
        if check_node(node.right_child, value, upper) != True:
            return False
        
        if check_node(node.left_child, lower, value) != True:
            return False
        
        return True
    
    return check_node(root)
            

root = Node(10)
insert(root, Node(12))
insert(root, Node(15))
insert(root, Node(19))
insert(root, Node(21))
insert(root, Node(8))
insert(root, Node(6))
insert(root, Node(4))
insert(root, Node(2))

print_tree_in_order(root)

print(isBST(root))
            