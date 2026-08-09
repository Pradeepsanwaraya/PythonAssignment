s=input("enter a string").split()
count=0
for i in s:
    if i>='a' and i<='z':
        count=count+1
    elif i>='A' and i<='Z':
        count=count+1
    else:
        print("no character")
print(count)