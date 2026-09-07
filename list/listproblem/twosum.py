l=list(map(int,input("enter a list").split()))
target=int(input("enter the target"))
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]+l[j]==target:
            print(l[i],l[j])
        