
num=int(input("enter any number"))
for i in range(1,num+1):
    for j in range(1,i+1):
        print(""*i, end=" ")
    for k in range(num,0,-1):
        print(num, end=" ")
    print()