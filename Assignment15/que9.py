num=int(input("enter number"))
i=1
while i<=num:
    j=1
    while j<=i:
        if j%2==1:
            print("1",end="")
        else:
            print("0",end="")
        j=j+1
    print()
    i=i+1