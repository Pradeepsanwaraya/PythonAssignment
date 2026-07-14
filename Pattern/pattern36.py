
# AB
# A C
# A  D
# ABCDE
num=int(input("enter the number"))
for i in range(num,0,-1):
    for j in range(1,i+1):
        
        if i==4 and j==2:
            print(" ", end=" ")
        elif i==4 and j==3:
            print(" ", end=" ")
        else:
            print(chr(64+j), end=" ")
        
    print()