s=input("enter string")
target=input("enter target")

for i in range(len(s)-1,-1,-1):
    if s[i]==target:
        break
print(i)
        