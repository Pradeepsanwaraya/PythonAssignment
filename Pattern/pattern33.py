num=int(input("enter the number"))
for i in range(num,0,-1):
    for j in range(1,i+1,1):
        print(chr(64+j), end=" ")
    print()