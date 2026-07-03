# 3.
# Prime Number Range Checker

# A cyber security system generates prime numbers for encryption analysis.
# The user enters a starting number and ending number.
# The system checks and displays all prime numbers between the given range using nested loops.

# Input:
# Enter starting number: 10
# Enter ending number: 50

# Output:
# Prime Numbers are:
# 11
# 13.
# 17
# 19
# 23
# 29
# 31
# 37
# 41
# 43
# 47
num1=int(input("enter any number"))
num2=int(input("enter any number"))
print("prime number are:")
for i in range(num1,num2+1):
    if i<=1:
        continue
    for j in range(2,i):
        if i%j==0:
           
            break
    else:
        
        print(i)
   