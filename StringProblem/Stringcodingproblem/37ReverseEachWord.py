s=input("enter a string").split()

revword=""
for i in s:
    rev=""
    for j in i:
        rev=j+rev
    revword=revword+rev+" "
    
print(revword)