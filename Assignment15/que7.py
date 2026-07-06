
     *
    **
   ***
  ****
 *****
******
num=int(input("Enter rows:"))
i=1
while i<=num:
    s=1
    while s<=num-i:
        print(" ",end="")
        s=s+1
    j=1
    while j<=i:
        print("*",end="")
        j=j+1
    print()
    i=i+1