# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 11:42:29 2021

@author: ODsLaptop
"""

# coding in the pythonic way

mantra = "beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex."

# importing modules

from collections import defaultdict, OrderedDict, Counter



# functions

def print_whitespace():
    print_whitespace.counter += 1
    
    print("\n")
    print("function number:", print_whitespace.counter)
print_whitespace.counter = 0

print_whitespace()


def doubler(x: int) -> int:
    return x*2

print(doubler(6))

print_whitespace()


def most_common_words(text: str):
    all_words = Counter(text.lower().split())
    
    for word, count in all_words.most_common():
        if count > 1:
            print(word, count)
            
most_common_words(mantra)

print_whitespace()

# default argument

def default_set(message = "default message") -> str:
    print(message)
    
default_set()

print_whitespace()

# strings

tab_string = '\t'
new_line_string = '\n'
raw_string = r'\n'

multi_line_string = """first line.
second line.
third line."""

def test_f_strings(first_name:str, last_name:str):
    output_sentance = f"My first name is {first_name} and last is {last_name}."
    print(output_sentance)
    
test_f_strings("Scooby", "Doo")

print_whitespace()

# exceptions

def exceptions_testing(number:int):
    try:
        print(number/0)
    except:
        print("cannot divide by zero")
              
exceptions_testing(10)

print_whitespace()

# lists

integer_list = [10, 3, 6, 2]
mixed_list = ["python", 0.1, True, 100]
list_of_lists = [[0,1,2,3], ["ten", 10], []]

def list_length(lst:list):
    print(len(lst))
    
for l in [integer_list, mixed_list, list_of_lists]:
    list_length(l)
    
print_whitespace()

def elements_of_a_list(lst:list):
    
    try:
        print("first element", lst[0])
        print("last element", lst[-1])
        print("second to last element", lst[-2])
        print("first three elements", lst[:3])
        print("last three elements", lst[-3:])
        print("without first and last", lst[1:-1])
        print("every third element", lst[::3])
        print("is 1 in the list?", 1 in lst)
        
    except:
        print("list not adequate")
        
elements_of_a_list([1,4,76,54,23,56,"ten", 1, 109, 2349, 314])

print_whitespace()

def concat_lists(x, y):
    print(x, y)
    x.extend(y)
    print(x)

concat_lists(x=[1,2,3], y=[10,11,12])

print_whitespace()

# tuples

def explore_tuples(x, y, z):
    first_tuple = x, y, z
    print(first_tuple[1])
    
explore_tuples(7, 8, 9)

print_whitespace()

# dictionaries

empty_dict = {}
grades = {"Kim": 80, "Jim": 70}

print(grades.get("Kim", 0))
print(grades.get("Bob"))

grades["Bob"] = 75

print("num students:", len(grades))

print(grades.keys()) # values, items

print_whitespace()

# count words in a document
def count_words(document:str):
    
    word_counts = {}
    for word in document:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts

word_count_test = count_words(mantra.lower().split())
print(word_count_test)

print_whitespace()

# defaultdict

def dd_word_count(document:str):
    
    from collections import defaultdict
    
    word_counts = defaultdict(int)
    
    for word in document:
        word_counts[word] += 1
        
    return word_counts

word_count_test2 = dd_word_count(mantra.lower().split())
print(word_count_test2)

print_whitespace()

# counters

def counter_word_count(document:str):
    
    from collections import Counter
    
    word_counts = Counter(document)
    
    for word, count in word_counts.most_common():
        print(word, count)
        
counter_word_count(mantra.lower().split())

print_whitespace()

# sets

set_of_words = set(mantra.lower().split())
print(set_of_words)
print("unique words in matra:", len(set_of_words))

print_whitespace()

# control flow

def if_statement(x:int):
    
    if x > 1:
        print(f"{x} is a positive integer")
    elif x > 0:
        print("counting number")
    else:
        print("negative number")
        
if_statement(22)

def if_one_line(x):
    parity = "even" if x % 2 == 0 else "odd"
    print(parity)
    
if_one_line(10)

print_whitespace()

def continue_and_break():
    
    for x in range(10):
        
        if x == 3:
            continue
        
        if x == 5:
            break
        
        print(x)

continue_and_break()

print_whitespace()

# truthiness

def is_true(x:list):
    
    print(all(x))
    
    print(any(x))
    
is_true([0, True, {}])

print_whitespace()

# sorting

## .sort sorts in-place
## sorted() returns a new list

lst = [1,4,19,0,-5,100]

sorted_list = sorted(lst)

lst.sort(reverse = True)

print(lst, sorted_list)

print_whitespace()

# list comprehensions

even_numbers = [x for x in range(20) if x%2 ==0]
squares = [x*x for x in range(4)]
even_squares = [x*x for x in even_numbers]

square_dict = {x:x*x for x in range(5)}

pairs = [(x,y)
        for x in range(10)
        for y in range(10)]

print(pairs)

print_whitespace()

# assert!

def smallest_number(num_list: list):
    return min(num_list)

assert smallest_number([1,2,3,-4]) == -4

#assert smallest_number([1,3,5]) == 3, "assertion shows incorrect"

# object oriented programming

class CountingClicker:
    """ string to describe the class here """
    
    def __init__(self, count = 0):
        self.count = count
        
    def click(self, num_times = 1):
        self.count += num_times
        
    def read(self):
        return self.count
    
    def reset(self):
        self.count = 0
       
# creating a subclass! This inherits the functionality of a class
class NoResetClicker(CountingClicker):
    
    def reset(self):
        pass

clicker = CountingClicker()
clicker.click()
clicker.click()
print("clicker reads:", clicker.read())

print_whitespace()

# iterables and generators

def generate_range(n:int):
    i = 0
    while i < n:
        yield i
        i += 1
        
for i in generate_range(7):
    print(f"i: {i}")
    
print_whitespace()

names = ["Tom", "Keith", "Cindy", "Aunt Martha"]

for i, name in enumerate(names):
    print(f"{i}: {name}")
    
print_whitespace()

# randomness

import random

four_randoms = [random.random() for x in range(4)]
print(four_randoms)

print_whitespace()

range_randoms = [random.randrange(100,200) for x in range(5)]
print(range_randoms)

print_whitespace()

random_numbers = [1,2,3,4,5,6,7,8,9]
random.shuffle(random_numbers)
print(random_numbers)

print_whitespace()

best_friend = random.choice(names)
print("random best friend:", best_friend)

print_whitespace()

    # random smaple without replacement
random_sample = random.sample(random_numbers, 3)
print(random_sample)

print_whitespace()

# args and kwargs

def magic(*args, **kwargs):
    print("unnamed args:", args)
    print("keyword args:", kwargs)
    
magic(1, 2, "seven", [1, 7], key = "keyword!", key2 = 9)

print_whitespace()

