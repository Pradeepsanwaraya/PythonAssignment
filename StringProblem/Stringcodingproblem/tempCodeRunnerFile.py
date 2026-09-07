s=input("enter a string")
d={}
long=0
ch=""
for i in s:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
for k,v in d.items():
    if v>long:
        long=v
        ch=k
print(long)