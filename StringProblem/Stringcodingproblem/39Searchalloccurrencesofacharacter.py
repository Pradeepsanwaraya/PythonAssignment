s=input("Enter string: ")
ch=input("Enter character: ")
index=""
for i in range(len(s)):
    if s[i]==ch:
        print(i)