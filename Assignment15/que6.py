# a
# ab
# abc
# abcd
# abcde
num=int(input("Enter rows:"))
i=1
while i<=num:
    j=97
    while j<97+i:
        print(chr(j),end="")
        j=j+1
    print()
    i=i+1