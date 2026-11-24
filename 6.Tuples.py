# Data Types 

"""
Tuples: Immutable, 
is a collection of multiple element, data types stored in a single variable, 
one Tuples can contain multiple data types elements
and Tuples can contain different data tyoes elements
ex: fruits = ("apple", "banana", "mango", "orange")
"""
fruits = ("apple", "banana", "mango", "orange") # Tuples

# Unpacking : means extracting elements from a collection (such as a list or tuple)
masala_spices = ("cardomon", "cloves", "cinamon")
(spices1,spices2,spices3) = masala_spices 
print(f"manin masala :{spices1},{spices2},{spices3}")

# Membership testing : in tuples means checking whether a particular element exists inside a tuple.
print(f"Is cinamon in masala spices ? {'cinamon' in masala_spices}")