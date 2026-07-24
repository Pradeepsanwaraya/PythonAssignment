num=int(input("enter any number"))
for i in range(num+1):
    c=1
    for j in range(1,i+1):
        if c%2==0:
            print("0",end=" ")
        else:
            print("1",end=" ")
        c=c+1
    print()