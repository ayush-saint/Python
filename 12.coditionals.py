# conditionals 

# if statement 
age = 22
if age>=18:
    print("you are eligible to vote")

# if else statement 
# example 1
age2 = 9
if age2>=18:
    print("you are eligible to vote")
else:
    print("you are not eligible to vote ") 

# example 2 
snack = input("Enter the snack you want to order: ").lower() 
# taking input from the user, .lower() makes the input in lower case 

if snack == "cookies" or snack == "samosa":
    print(f"your order ({snack}) will be served soon ")
else :
    print(f"this ({snack}) is not available")

# if else if statement 
cup = input("enter the size(small, medium, large) of the cup: ").lower()
if cup == "small":
    print("the bill is 10 rupees")
elif cup == "medium":
    print("the bill is 15 rupees")
elif cup == "large":
    print("the bill is 20 rupees")
else:
    print("invalid input") 