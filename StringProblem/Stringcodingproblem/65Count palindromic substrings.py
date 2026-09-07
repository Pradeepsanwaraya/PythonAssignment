s=input("enter a string")
count=0

for i in range(len(s)):
    for j in range(i,len(s)):
        new=""
        for k in range(i,j+1):
            new=new+s[k]

        rev=""
        for k in range(len(new)-1,-1,-1):
            rev=rev+new[k]

        if new==rev:
            count=count+1

print(count)