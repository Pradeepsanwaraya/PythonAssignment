s=input("enter a string")
ch=input("enter a character")
count=0
for i in range(len(s)):
    if s[i]==ch:
        count=count+1
print(count)