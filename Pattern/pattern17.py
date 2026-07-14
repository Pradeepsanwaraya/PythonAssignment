num=int(input("enter any number"))
for i in range(num+1):
    for j in range(1,i+1):
        if i%2==0:
            print("#",end=" ")
        else:
            print("*",end=" ")
    print()