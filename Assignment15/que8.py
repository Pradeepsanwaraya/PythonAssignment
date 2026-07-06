num=int(input("enter number"))
i=0
while i<num:
    s=1
    while s<=i:
        print(" ",end="")
        s=s+1
    j=num
    while j>i:
        print(j,end="")
        j=j-1
    print()
    i=i+1