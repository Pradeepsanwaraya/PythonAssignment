emp = input("Enter Employee ID: ")

if len(emp) == 8 and emp.startswith("EMP") and emp[3:].isdigit():
    print("Valid Employee ID")
else:
    print("Invalid Employee ID")