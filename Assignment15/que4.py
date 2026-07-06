num=int(input("Enter the number: "))

i=1
while i<=num:
    print()
    j=1
    while j<=i:
        if i%2==0:
            print("0", end=" ")
        else:
            print("1", end=" ")
        j+=1
    i+=1