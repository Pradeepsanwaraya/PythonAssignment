# 1
# 12
# 123
# 1234
# 12345
num=int(input("enter any number"))
i=1
while num>=1:
    j=1
    while j<=num-1:
        print(" ",end = " ")
        j+=1
    j=1
    while j<=i:
        print(i, end = " ")
        j=j+1
    print()
    i=i+1
    num=num-1