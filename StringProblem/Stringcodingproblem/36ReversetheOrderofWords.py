s=input("enter a string").split()
rev=""
for i in range(len(s)-1,-1,-1):
    rev=rev+" "+s[i]
print(rev)

