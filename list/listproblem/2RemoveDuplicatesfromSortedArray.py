l=[1,1,2,2,3,3]
r=1
for i in range(len(l)):
    if l[i]!=l[r-1]:
        l[r]=l[i]
        r=r+1
print(r)
print(l)
