    # A
    # AB
    # ABC
    # ABCD
    # ABCDE
no=int(input("enter the no"))
for i in range(1,no+1):
    for j in range(no,i,-1):
        print(" ",end=" ")
    
    for k in range(1,i+1):
        print(chr(64+k),end=" ")
       
    print()