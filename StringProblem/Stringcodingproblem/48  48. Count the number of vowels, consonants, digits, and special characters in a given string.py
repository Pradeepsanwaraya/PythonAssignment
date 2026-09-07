s=input("enter a string")
vcount=0
Acount=0
lcount=0
dcount=0
scount=0
for i in s:
    if i in "aeiouAEIOU ":
        vcount=vcount+1
    elif i>='A' and i<='Z':
        Acount=Acount+1
    elif i>='a' and i<='z':
        lcount=lcount=1
    elif i>="0" and i<="9":
        dcount=dcount+1
    elif i in "@#$%&*":
        scount=scount+1
    else:
        pass
print("vowel",vcount)
print("upper",Acount)
print("lower",lcount)
print("digit",dcount)
print("special",scount)