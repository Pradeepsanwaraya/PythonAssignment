
# 6.Buzz Number Detector 

# A gaming system includes a special feature to identify “Buzz Numbers” for unlocking bonus rewards. Whenever a player enters a number, the system evaluates it using a predefined mathematical rule before granting access to hidden features.

# A number is considered a Buzz Number if it satisfies at least one of the following conditions:

# * The number is divisible by 7, OR
# * The number ends with the digit 7

# If the number satisfies any one of these conditions, it is treated as a valid Buzz Number and the player receives a reward. Otherwise, the system rejects the number.

# Task:
# Write a Python program to check whether a given number is a Buzz Number or not.

# Example:
# Input:
# 27

# Output:
# Buzz Number
num=int(input("enter any number"))
sum=0
temp=num
while temp>0:
  
    if temp%7==0 or temp%10==7:
        print("buzz number")
        break
    temp=temp//10
else:
    print("not a buzz nom")