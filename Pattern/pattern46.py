num=int(input("enter any number"))
for i in range(num,0,-1):
    for j in range(1,num+1):
        print(""*i, end=" ")
    for k in range(1,i+1):
        print(chr(64+k), end=" ")
    print()