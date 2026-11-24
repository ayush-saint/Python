# Data Types 

# Operator overloading : Combining, Multiplicating, comparing two lists, Example

base_liquid = ["water", "milk"]
extra_flavor = ["ginger"] 

full_liquid_mix = base_liquid + extra_flavor
print(f"Liquid mix :{full_liquid_mix}")

strong_brew = ["black tea", "water"] * 3
print(f"{strong_brew}")

""" bytearray : is a built-in data type used to store a sequence of bytes (values from 0 to 255). It is mutable, meaning you can modify its elements,
              : Bytearray is used to store and modify binary data, such as image data, file contents, and network data.
              : You can change individual bytes without creating a new bytearray.
    (not a type of array)
              """

data = bytearray([65, 66, 67])

print(data)
data[0] = 68
print(data)