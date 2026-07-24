no=int(input("enter the no"))
for i in range(1,no+1):
    for j in range(no,i,-1):
        print(" ",end=" ")
    c=no
    for k in range(1,i+1):
        print(c,end=" ")
        c=c-1
    print()