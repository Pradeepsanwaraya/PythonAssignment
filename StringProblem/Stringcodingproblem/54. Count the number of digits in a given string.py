s=input("enter a string")
count=0
for i in s:
    if i>='0' and i<="9":
        count=count+1
print("digit count is :",count)