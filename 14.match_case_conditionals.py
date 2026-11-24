# conditionals 

# match case statement

seat = input("enter the seat type sleeper/AC/2s : ").lower()

match seat:
    case "sleeper":
        print("no AC, beds available")
    case "AC":
        print("AC, beds available")
    case "2s":
        print("no AC, seats available")
    case _:# underscore for default case 
        print("invalid statement")
