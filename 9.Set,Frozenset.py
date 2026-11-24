# Data Types 


""" Sets : 
is a built-in data type used to store multiple unique elements in a single variable. 
It is unordered, does not allow duplicate values, and is mutable (can be modified).
"""
# Example : 
A = {10,20,30,40}
B = {30,40,50,60}
print(A|B) # union
print(A&B) # intersection
print(A-B) # difference/minus

# Membership testing : checks whether an element exists in a set
print(20 in A)
print(50 not in A)

""" Frozen Set :
A frozenset is a built-in data type used to store multiple unique elements, 
just like a set, but it is immutable, meaning you cannot add, remove, or modify its elements after creation.
"""
# Example :
A = frozenset([10, 20, 30, 20, 40])
print(A)