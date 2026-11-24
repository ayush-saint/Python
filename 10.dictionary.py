# Data Types 


""" Dictionary : is a built-in data type used to store data in key-value pairs. 
Each key is unique and is used to access its corresponding value.
"""
# Example : 
chai = dict(type="Masala chai", size= "Large", sugar=2) 
chai2 = {"type":"plain chai","size":"medium", "sugar":3} # can be written as this
print(f"Chai : {chai}")
print(f"Chai 2 : {chai2}")

chai_recipe = {} # empty dictionary
chai_recipe["base"]="black tea" # adding element to empty dictionary
chai_recipe["liquid"]="milk"
print(f"Recipe base: {chai_recipe['base']}") # accessing just the black tea
print(f"Recipe {chai_recipe}")

del chai_recipe["liquid"] # deleting just liquid
print(f"Recipe {chai_recipe}")

# Membership Testing in dictionary
print(f"Is sugar in the order:{"sugar" in chai }")

# Printing just the keys and value and both
print(f"Order details(Keys): {chai.keys()}")
print(f"Order details(values): {chai.values()}")
print(f"Order details(items): {chai.items()} ")

