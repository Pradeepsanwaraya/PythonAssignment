
# 6.

# Product Code Verification System

# An e-commerce company wants to verify whether two product codes are rearranged versions of each other.

# Conditions:
# - Ignore spaces
# - Ignore case sensitivity

# Input:
# Enter first product code: Dormitory
# Enter second product code: Dirty Room

# Output:
# Both Product Codes are Matching

code1 = input("Enter first product code: ")
code2 = input("Enter second product code: ")
for ch in code1:
    if ch not in code2:
        print("Both Product Codes are Not Matching")
        break
else:
    
    print("Both are Matching")