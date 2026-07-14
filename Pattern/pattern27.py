# 1
# 10
# 1 1
# 1  0
# 10101
num=int(input("enter any number"))
for i in range(1,num+1):
    for j in range(1,i+1):
        if i==4 and j==2:
            print(" ", end=" ")
        elif i==4 and j==3:
            print(" ", end=" ")
        else:     
            if (i+j)%2==0:
                print("0",end=" ")
            else:
                print("1",end=" ")
    print()