s=input("enter a string")
sum=0

for i in s:
    if i>="0" and i<="9":
        sum=sum+int(i)

print(sum)