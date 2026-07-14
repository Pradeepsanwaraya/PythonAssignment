num=int(input("enter any number"))
c=1
space=" "
for i in range(1,num+1):
    for j in range(1,i+1):
        if j==1 or i==num or j==i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
        c=c+1   
    print()