s=input("enter a string")
ch=input("enter a character")
for i in range(len(s)):
    if s[i]==ch:
        break
print(i)