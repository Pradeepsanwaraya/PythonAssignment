
# 5.
# Strong Number Detector

# A banking security system uses Strong Numbers for special authentication testing.
# The user enters a range of numbers.
# The system identifies all Strong Numbers between the given range using nested loops.

# A Strong Number is a number in which the sum of factorials of its digits is equal to the original number.

# Example:
# 145

# 1! + 4! + 5!
# = 1 + 24 + 120
# = 145
num1=int(input("enter starting number"))
num2=int(input("enter ending number"))

print("Strong Numbers are:")

for i in range(num1,num2+1):
    temp=i
    sum=0
    while temp>0:
        digit=temp%10
        fact=1
        for j in range(1,digit+1):
            fact=fact*j
        sum=sum+fact
        temp=temp//10
    if sum==i:
        print(i)
