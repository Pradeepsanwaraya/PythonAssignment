s=input("enter a string")
l=0
count=0
for i in s:
    if i>='a' and i<='z':
        l=l+1
    elif i>='A' and i<='Z':

        count=count+1
    else:
        pass
print("lower",l)
print("upper",count)