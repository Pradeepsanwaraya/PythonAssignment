vehicle = input("Enter vehicle number: ")

if (len(vehicle) == 10 and
    vehicle[:2].isalpha() and
    vehicle[2:4].isdigit() and
    vehicle[4:].isalnum()):
    print("Valid Vehicle Number")
else:
    print("Invalid Vehicle Number")