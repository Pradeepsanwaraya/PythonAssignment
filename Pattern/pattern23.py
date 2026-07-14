# a
# bc
# d f
# g  j
# klmno	*

num=int(input("enter any number"))
c=1
for i in range(1,num+1):
    for j in range(1,i+1):
        if i==4 and j==2:
            print(" ", end=" ")
        elif i==4 and j==3:
            print(" ", end=" ")
        else:
            print(chr(96+c), end=" ")
        c=c+1   
    print()