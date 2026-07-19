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
        if j==1 or i==num or j==i:
            print("1",end=" ")
        else:
            print("@",end=" ")
        c=c+1 
        j=j+1
    print()
    i=i+1