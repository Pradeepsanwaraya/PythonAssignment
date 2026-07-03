
# 2.
# Perfect Number Analyzer

# A mathematics research system analyzes special numbers within a given range.
# The user enters a starting number and ending number.
# The system checks every number in that range and displays all Perfect Numbers using nested loops.

# (A Perfect Number is a number whose sum of proper divisors is equal to the number itself.)

# Input:
# Enter starting number: 1
# Enter ending number: 1000

# Output:
# Perfect Numbers are:
# 6
# 28
# 496
num1=int(input("enter first number"))
num2=int(input("enter second number"))
for i in range(num1,num2):
    count=0
    for j in range(num1,num2//2+1):
        if i%j==0:
            count = count+j
    if count==num:
        print("perfect number ")
    else:
        print("not a perfect number")