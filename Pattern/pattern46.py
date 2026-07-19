num=int(input("enter any number"))
i=1
c=num
while i<=num:
    j=1
    while j<=num-i:
        print(" ",end = " ")
        j+=1

    j=1
    while j<=i:
        print(chr(64+j), end =" ")
        j=j+1
    print()
    i=i+1