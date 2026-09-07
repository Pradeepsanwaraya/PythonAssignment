s1=input("enter a string")
s2=input("enter a string")

new=s1+s2

result=""

for i in new:
    if result=="" or i!=result[-1]:
        result=result+i

print(result)