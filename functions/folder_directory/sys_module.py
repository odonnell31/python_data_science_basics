# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 21:52:45 2019

@author: ODsLaptop
"""

# Question: what is the sys module in python?

# Answer: the sys module allows you to interact with the command line from python

import sys

#print(sys.version)
#print(sys.path)
#print(sys.modules)

sys.stderr.write('This is stderr text\n')
sys.stderr.flush()
sys.stdout.write('This is stdout text\n')