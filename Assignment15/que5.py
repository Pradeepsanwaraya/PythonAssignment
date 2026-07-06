# A
# AB
# ABC
# ABCD
# ABCDE
num=int(input("Enter rows: "))

i=1
while i<=num:
    j=1
    while j<=i:
        print(chr(64 + j), end="")
        j+=1
    print()
    i+=1