num=int(input("enter the number"))
for i in range(1,num+1):
    for j in range(1,i+1):
        
        if i==4 and j==2:
            print(" ", end=" ")
        elif i==4 and j==3:
            print(" ", end=" ")
        else:
            print(i, end=" ")
        
    print()