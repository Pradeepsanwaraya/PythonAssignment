num=int(input("enter any number"))
count=1
for i in range(1,num+1):
    for j in range(1,i+1):
        print(chr(96+count),end=" ")
        count=count+1
    print()