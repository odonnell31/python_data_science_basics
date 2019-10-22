# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 08:33:23 2019

@author: 432663
"""

# Linked List basics:

# linked lists are a sequence of nodes.
# singly linked lists have a pointer from each node to the next node.
# doubly linked lists have two pointers from each node, one in each direction
# con of linked list: not constant time like a list, must iterate through
# pro of linked list: can add or remove items from the beginning in constant time

# Question: build a linked list!

# building out a linked list class
class LinkedList:
    
    def __init__(self):
        self.head = None
        self.linked_nodes = []
    
    # method to link nodes together into a linked list    
    def link_nodes(self, nodes):
        self.head = nodes[0].data
        for n in range(len(nodes)):
            self.linked_nodes.append(nodes[n].data)
            if n < len(nodes)-1:
                nodes[n].next = nodes[n+1].data
            
    # method to see the linked list, in order
    def print_linked_list(self):
        linked_list = []
        for n in self.linked_nodes:
            linked_list.append(n)
        print(linked_list)

# class for each node
class Node:
    def __init__(self, data):
        self.next = None
        self.data = data
        
# create a LinkedList object
LL = LinkedList()

# create four node objects
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

# link the four nodes just created
LL.link_nodes([node1, node2, node3, node4])

# print the linked list
LL.print_linked_list()