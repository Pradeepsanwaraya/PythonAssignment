s=input("enter a string")
target=input("enter a character")
new=""
for i in range(len(s)):
    if s[i]!=target:
        new=new+s[i]
print(new)
        