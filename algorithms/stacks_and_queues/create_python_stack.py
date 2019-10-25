# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 12:53:22 2019

@author: Michael ODonnell
"""

# Question:
# Create a Stack in python, with the following methods:
#   pop
#   peek
#   add
#   return minimum value


# first, create class Pancake to add and remove from a Stack
class Pancake:
    def __init__(self, value):
        self.underneath = None
        self.value = value

# create Class Stack with all the required methods
class Stack:
    def __init__(self):
        self.top = None
    
    # each added pancake is informed of the pancake underneath it
    def add_pancake(self, pancake):
        pancake.underneath = self.top
        self.top = pancake
        
    def pop(self):
        if self.top != None:
            self.top = self.top.underneath
            
    def peek(self):
        if self.top != None:
            print(self.top.value)
        else:
            print("Empty Stack")
    
    # remove all pancake from stack, find the min value, restack the pancakes:        
    def min_value(self):
        value_list = []
        while self.top != None:
            value_list.append(self.top.value)
            self.pop()
        
        for p in reversed(range(len(value_list))):
            self.add_pancake(Pancake(value_list[p]))
            
        print(min(value_list))
                
            
# Test the function!
        
# create a stack
python_stack = Stack()

# add 5 pancakes to the stack
python_stack.add_pancake(Pancake(10))
python_stack.add_pancake(Pancake(20))
python_stack.add_pancake(Pancake(40))
python_stack.add_pancake(Pancake(30))
python_stack.add_pancake(Pancake(50))

# peek at the top value of the stack
print("Peek at top value in stack:")
python_stack.peek()

# pop top pancake from the stack
print("Pop the top element from the stack")
python_stack.pop()

# print the minimum value in the stack
print("Find the minimum value in the stack")
python_stack.min_value()

# peek one more time at the top element of the stack
print("Again, peek at the top element of the stack")
python_stack.peek()