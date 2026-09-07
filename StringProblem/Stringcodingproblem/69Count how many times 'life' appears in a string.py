s=input("enter a string")
count=0
sub="life"

for i in range(len(s)):
    new=""
    for j in range(i,len(s)):
        new=new+s[j]
        if new==sub:
            count=count+1

print(count)