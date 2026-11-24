# conditionals 

# nested if else statement 
device_status = "active"
temperature = 38

if device_status == "active":
    if temperature> 35:
        print("high termperature alert")
    else :
        print("temperature is normal")
else:
    print("device is inactive")

# Ternary Operator or Conditional Expression
order_amount = int(input("Enter the order amount: "))
# int makes the input into integer 
delivery_fees = 0 if order_amount > 300 else 30
print(f"Delivery fees is : {delivery_fees}")