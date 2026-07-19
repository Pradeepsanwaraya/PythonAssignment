num=int(input("enter any number"))
i=1
c=1
while i<=num:
    j=1
    while j<=num-i:
        print(" ",end = " ")
        j+=1
    j=1
    while j<=i:
        if c%2==0:
            print("0",end=" ")
        else:
            print("1",end=" ")
        c=c+1 
        j=j+1
    print()
    i=i+1