# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 16:26:45 2019

@author: MabuXayda
"""

# %% FOR LOOPS
"""===========================================================================
FOR LOOPS

- A for loop is used for iterating over a sequence (that is either a list, 
a tuple, a dictionary, a set, or a string).
- With the for loop we can execute a set of statements, once for each item 
in a list, tuple, set etc.
"""
fruits = ["apple", "banana", "cherry"]

for x in fruits:
    x = x + "le"
    print(x)

for x in "banana":
    print(x.upper())

"""===========================================================================
- With the break statement we can stop the loop before it has looped through 
all the items
- With the continue statement we can stop the current iteration of the loop, 
and continue with the next
"""
fruits = ["apple", "banana", "cherry", "orange"]

for x in fruits:
    if x == "cherry":
        print("Day la cherry")
        break
    print(x)

for x in fruits:
    if x == "cherry":
        print("Day la cherry")
        continue
    print(x)

for x in fruits:
    if x == "cherry":
        print("Day la cherry")
        pass
    print(x)

"""===========================================================================
- A nested loop is a loop inside a loop.
- The "inner loop" will be executed one time for each iteration of the 
"outer loop"
"""
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)

# %% WHILE LOOPS
"""===========================================================================
WHILE LOOPS

- With the while loop we can execute a set of statements as long as a 
condition is true.
- While loops also have break and continue statement like for loops
- With the else statement we can run a block of code once when the condition 
no longer is true
"""

i = 0
while i < 10:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")

# %% TRY...EXCEPT
"""===========================================================================
TRY...EXCEPT

- The try block lets you test a block of code for errors.
- The except block lets you handle the error.
- The finally block lets you execute code, regardless of the result of the 
try and except blocks.
"""
p = "123"
try:
    print(int(p))
except:
    print("Something went wrong")
finally:
    print("The 'try except' is finished")



