s=input("enter string")

upper=""
for i in s:
    if i>='a' and i<="z":
        u=ord(i)

        upper=upper+(chr(u-32))
    else:
        upper=upper+i
print(upper)