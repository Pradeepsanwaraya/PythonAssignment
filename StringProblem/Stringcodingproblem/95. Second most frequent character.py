s=input("enter a string")
d={}
long=0
ch=""
ch2=""
secondl=0
for i in s:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
for k,v in d.items():
    if v>long:
        
        secondl=long 
        ch2=ch
        long=v
        ch=k
    elif v>secondl and v!=long:
        secondl=v
        ch2=k  
print(secondl,ch2)
