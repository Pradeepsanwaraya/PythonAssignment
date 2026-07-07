
# 5.

# Automorphic Number Lock

# A high-security digital locker validates access codes using a special mathematical rule.

# When a user enters a numeric code, the system squares the number and checks whether the last digits of the square match the original number.
#  If it matches, the code is considered valid.

# An Automorphic Number is a number whose square ends with the same number.

# Task:
# Write a Python program to check whether a given number is an Automorphic Number or not.

# Example:
# Input:
# 25

# Output:
# Automorphic Number
num=int(input("enter any number"))
sqr=num*num
temp=num
while temp>0:
    if temp%10 != sqr%10:
        print("not an automorphic")
        break
    temp=temp//10
    sqr=sqr//10
else:
    print("automorphic")