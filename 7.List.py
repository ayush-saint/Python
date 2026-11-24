# Data Types 


"""
List : is a collection of multiple elements stored in a single variable. 
Lists are ordered and mutable (changeable)
"""

ingredients = ["water","milk","black tea"] #list

# adding to list
ingredients.append("sugar")
print(f"Ingredients are : {ingredients}")

# remove from list 
ingredients.remove("milk")
print(f"Ingredients are : {ingredients}")

# extending a list 
spice_options = ["ginger","cardamom"]
chai_ingredients = ["water", "milk"]

chai_ingredients.extend(spice_options)
print(f"chai : {chai_ingredients}")

# inserting 
chai_ingredients.insert(2,"black tea")
print(f"chai : {chai_ingredients}")

"""Poping : deletes the element from list and and return the removed element. 
Pop not only removes an element from the list but also gives that removed element back so you can use it somewhere else, 
if you don't gave any elemnt to pop it will remove last element"""
last_added = chai_ingredients.pop()
print(f"{last_added}")
print(f"chai : {chai_ingredients}")
print(f"chai poped element : {last_added}")

# reversing the list
chai_ingredients.reverse()
print(f"chai : {chai_ingredients}")

""" sorting : means arranging its elements in a particular order, either ascending or descending.
if you don't gave me order it will arrange the list in ascending"""
chai_ingredients.sort()
print(f"chai : {chai_ingredients}")
chai_ingredients.sort(reverse=True) # descending order

# Maximum and Minimum out of list 
sugar_level = [1,2,3,4,5]
print(f"maximum sugar level : {max(sugar_level)}")
print(f"maximum sugar level : {min(sugar_level)}")










