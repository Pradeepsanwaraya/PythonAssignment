

# 3.

# Fibonacci Population Growth Tracker

# A wildlife research team is studying the growth of a rare species.  
# They observe that the population follows a Fibonacci pattern:

# - Month 1 → 0 animals  
# - Month 2 → 1 animal  
# - Every next month → sum of previous two months  

# The researchers want to analyze the growth pattern.

# Write a program to:

# - Read number of months n
# - Generate Fibonacci series up to n months using loop
# - Print population for each month
# - Find total population observed
# - Count how many months population exceeded 5

# Input:
# 8

# Output:
# Population Growth:
# 0 1 1 2 3 5 8 13

num=int(input("enter any number"))
a=0
b=1
while num>0:
    print(a)
    temp=a
    a=b
    b=temp+b
    num=num-1