# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 11:05:56 2021

@author: ODsLaptop
"""

from collections import defaultdict

users = defaultdict(list)

for i in ["tom", "jane", "fred", "sara"]:
    users[i].append(len(i))

#print(users)
#print(users["tom"])
#print(users["michael"])

from collections import Counter

sentance = "Coffee is a brewed drink prepared from roasted coffee beans, the seeds of berries from certain Coffea species. All fruit must be further processed from a raw material—the fruit and seed—into a stable, raw product; un-roasted, green coffee. To process the berries, the seed is separated from the fruit to produce green coffee. Green coffee is then roasted, a process which transforms the raw product (green coffee) into a consumable product (roasted coffee). Roasted coffee is ground into a powder and mixed with water to produce a cup of coffee."

letters = Counter(sentance)

#for e in letters.elements():
#    print((e, letters[e]), end="\n")
    
print(letters)
print(letters.most_common(3))
print(letters.items())
print(letters.keys())
print(letters.values())

words = Counter(sentance.lower().split())
print(words)

for word, count in words.most_common():
    if count > 1:
        print(word, count)