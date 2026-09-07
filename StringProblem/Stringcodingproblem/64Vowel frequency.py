s=input("enter a string")
d={}
for i in s:
    if i in "aeiou":
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
print(d)