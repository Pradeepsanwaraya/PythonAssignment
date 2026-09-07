s=input("enter a string")
new=""
for i in range(len(s)):
    if s[i] in s[:i]:
        new=new+"$"
    else:
        new=new+s[i]
print(new)