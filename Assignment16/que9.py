
# 9.
# Abundant Number Detector

# A financial system analyzes surplus numbers.

# An Abundant Number:
# Sum of proper factors > number

# Write a program to check Abundant Number.

# Input:
# 12

# Output:
# Abundant Number

num=int(input("Enter any number:"))

sum=0

for i in range(1,num):
    if num%i==0:
        sum=sum+i

if sum>num:
    print("Abundant Number")
else:
    print("Not Abundant Number")