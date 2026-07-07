
# 8.
# Trimorphic Number Analyzer

# A coding system checks cube-based patterns.

# A Trimorphic Number:
# Cube of number ends with the same number.

# Example:
# 4³ = 64

# Write a program to check Trimorphic Number.

# Input:
# 4

# Output:
# Trimorphic Number

# Automorphic Number
num=int(input("enter any number"))
sqr=num*num*num
temp=num
while temp>0:
    if temp%10 != sqr%10:
        print("not an trimorphic")
        break
    temp=temp//10
    sqr=sqr//10
else:
    print("trimorphic")