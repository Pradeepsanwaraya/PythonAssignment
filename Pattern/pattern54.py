no=int(input("enter the no"))
for i in range(1,no+1):
    for j in range(no,i,-1):
        print(" ",end=" ")
    
    for k in range(1,i+1):
        if k==1 or i==no or k==i:
            print("1",end=" ")
        else:
            print("@",end=" ")
        
    print()