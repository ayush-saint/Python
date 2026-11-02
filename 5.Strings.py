# Strings are immutable 

chai_type = "ginger chai"
customer_name = "priya"

print(f"Order for {customer_name} : {chai_type} please!")

chai_description = "Aromatic and bold"

# indexing : each String character has its own indexing (number)

print(f"First word : {chai_description[0:8]}")

# reversing the string(by negative indexing)
print(f"Last word : {chai_description[::-1]}")


# encoding in python
label_text = "chai speciãl"
encoded_label = label_text.encode("utf-8")
print(f"non encoded text : {label_text}")
print(f"encoded text : {encoded_label}")
decoded_label = encoded_label.decode("utf-8")
print(f"decoded label : {decoded_label}")