
# 4.
# Armstrong Number Finder

# A digital number analysis system checks for Armstrong numbers within a range.
# The user enters starting and ending numbers.
# The system finds all Armstrong numbers using nested loops.

# Input:
# Enter starting number: 1
# Enter ending number: 500

# Output:
# Armstrong Numbers are:
# 1
# 153
# 370
# 371
# 407
num1=int(input("enter starting number"))
num2=int(input("enter ending number"))

print("Armstrong Numbers are:")

for i in range(num1,num2+1):
    temp=i
    l=len(str(i))
    sum=0

    while temp>0:
        digit=temp%10
        sum=sum+digit**l
        temp=temp//10

    if sum==i:
        print(i)
