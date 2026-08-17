
# 4.
# Employee ID Validator

# A company wants to validate employee IDs before storing them in the database.

# Conditions:
# - ID must start with "EMP"
# - Total length should be 8
# - Remaining characters should be digits only

# Input:
# Enter Employee ID: EMP10234

# Output:
# Valid Employee ID
id=input("Enter Employee ID: ")

if len(id)<=8:
    if id[0]=='E' and id[1]=='M' and id[2]=='P':
        print("Valid Employee ID")
    else:
        print("Invalid Employee ID")
else:
    print("Invalid Employee ID")