# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 13:38:39 2021

@author: ODsLaptop
"""

# operators

def modulus(x:int, y:int) -> str:
    print(f"{x} goes into {y}:", y // x, "times")
    print("with remainder", y % x)
    
modulus(2, 11)

def python_case(words:str):
    print(f"the camelcase of \'{words}\' looks like this:", words.title().replace(' ', ''))
    print(f"the underscore PEP-specified version of \'{words}\' is:", words.lower().replace(' ', '_'))
    
python_case("this is a set of words")

def ask_for_input() -> str:
    color = input("what is your favorite color?")
    print(f"your answer is {color}")
    
#ask_for_input()

def true_or_false(x = 5, y = 5) -> bool:
    print(x == y)
    
true_or_false(x = 10, y = 10.00)

def break_vs_continue(x:int):
    for i in range(x):
        if i == 3:
            break
        else:
            print(i)
            
    print('='*20)
        
    for i in range(x):
        if i == 3:
            continue
        else:
            print(i)
            
break_vs_continue(x = 6)
print('*'*25)

def counting_backwards(starting_num:int):
    starting_num = abs(starting_num)
    for i in range(starting_num, 0, -1):
        print(i)
        
counting_backwards(10)

global_var = 10

def update_global_var():
    global global_var
    global_var = 11

update_global_var()
print(global_var)

# pause a program
import time

def pause_test(x:int):
    for i in range(x):
        print(f"pausing for {i} seconds...")
        time.sleep(i)
        print("done")
    print("sleep test complete.")
    
pause_test(2)

def list_index_loop(x:list):
    for i in range(len(x)):
        print(f"The index {i} has list value", x[i])
        
list_index_loop(["one", "two", "three"])

def enumerate_list(x:list):
    for index, value in enumerate(x):
        print(f"index {index} has value {value}")
        
enumerate_list(["one", "two", "three"])