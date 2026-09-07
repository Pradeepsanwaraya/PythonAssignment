s=input("enter a string")
new=""
for i in s:
    if (i>="a" and i<="z") or (i>="A" and i<="Z") or (i>="0" and i<="9") or i==" ":
        new=new+i
print(new)