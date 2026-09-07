l=[0,1,2,2,3,0,4,2]
k=2
r=0
for i in range(len(l)):
    if l[i]!=k:
        l[r]=l[i]
        r=r+1
print(l)
print(r)