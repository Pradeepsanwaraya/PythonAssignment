# 4.Spy Number Detector

# A cybersecurity system flags special numeric codes.

# A number is called a Spy Number if:
# Sum of digits = Product of digits

# Write a program to check whether the entered number is Spy Number or Not.

# Input:
# 1124

# Output:
# Spy Number
num=int(input("enter any number"))
sum=0
product=1
while num>0:
    rem=num%10
    sum=sum+rem
    product=product*rem
    num=num//10
if product==sum:
    print("spy number")
else:
    print("not a spy number")