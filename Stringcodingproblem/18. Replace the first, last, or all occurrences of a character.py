s=input("enter a string")
ch=input("enter character you want to replace")
re=input("enter you want to replace with")
new=''
for i in range(len(s)):
    if s[i]==ch:
        new=new+re
    else:
        new=new+s[i]
print(new)
