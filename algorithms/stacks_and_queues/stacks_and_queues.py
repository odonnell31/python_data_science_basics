# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 08:44:29 2019

@author: Michael ODonnell
"""

# Stacks: Last in First out.
    # functions: pop() - remove top item
    # push(item) - add item to top of stack
    # peek() - return the top item of stack
    # isEmpty() - return true if stack is empty

# Queue: First in first out
    # add(item) - add item to the end of th elist
    # remove() - remove item from the end of the list
    # peek() - return last item in list
    # isEmpty() - return true if queue is empty
    
# ===================================

# Question: How would you design a stack which, in addition to push and pop,
# has a function which returns the minimum element?
    
# first, create class Stack with methods
class Stack:
    def __init__(self):
        Stack.top = None
    
    # returns True if Stack has no pancakes    
    def isEmpty(self):
        return(self.top == None)

    # returns the value of the pancake on top  
    def peek(self):
        return(self.top.value)

    # adds a pancake to the top, and sets the pancake underneath the top  
    def add_pancake(self, pancake_value):
        pancake_underneath = None
        if self.isEmpty() == False:
            pancake_underneath = self.top
            self.top = Pancake(pancake_value)
            self.top.set_under(pancake_underneath)
        else:
            self.top = Pancake(pancake_value)

    # removes pancake from the top, sets pancake underneath
    def pop_pancake(self):
        if self.isEmpty() == False:
            self.top = self.top.under
        else:
            print('cannot pop empty stack')
            
    # return the minimum element of the Stack
    def minimum_element(self):
        value_list = []
        
        def pop_and_append(self):
            if self.isEmpty() == False:
                value_list.append(self.top.value)
                self.pop_pancake()
                pop_and_append(self)
            else:
                pass
            
        if self.isEmpty() == False:
            pop_and_append(self)
        
        print(min(value_list))

        for p in reversed(value_list):
            self.add_pancake(p)            
        
# class Pancake to put in the Stack
class Pancake:
    def __init__(self, value):
        self.value = value
        self.under = None
     
    # method to set the pancake underneath
    def set_under(self, under_pancake):
        self.under = under_pancake

# create a test stack
test_stack = Stack()

# add five pancakes to the test stack
test_stack.add_pancake(10)
test_stack.add_pancake(11)
test_stack.add_pancake(12)
test_stack.add_pancake(13)
test_stack.add_pancake(14)

# remove a pancake from the test stack
test_stack.pop_pancake()

# print the value of the pancake on top, and the one underneath
print(test_stack.top.value)
print(test_stack.top.under.value)

# print the minimum value in the stack
test_stack.minimum_element()

# re-print the top value in the stack
print(test_stack.top.value)


# Question 2: write a program to sort a stack such that the smallest items are
# on top. You can use an additional temp stack, but you may not copy the elements
# into another data structure like an array.

    