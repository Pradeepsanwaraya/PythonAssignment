# 7.
# Neon Number Detector

# Scenario:
# A smart calculator system checks special numbers used in mathematical testing.
# The user enters a range of numbers.
# The system identifies all Neon Numbers using nested loops.

# Theory:
# A Neon Number is a number where the sum of digits of its square is equal to the original number.

# Example:
# 9

# Square of 9 = 81

# 8 + 1 = 9

# Since the sum is equal to the original number, 9 is called a Neon Number.

# Input:
# Enter starting number: 1
# Enter ending number: 100

# Output:
# Neon Numbers are:
# 1
# 9
num1=int(input("enter any number"))
num2=int(input("enter any number"))
for i in range(num1,num2+1):
    square=i*i
    temp=square
    sum=0
    rev=0
    while temp>0:
        rev=temp%10
        sum=sum+rev
        temp=temp//10
    if sum==i:
        print(i)
