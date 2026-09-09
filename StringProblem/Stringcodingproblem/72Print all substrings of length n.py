s=input("enter a string")
length=int(input("enter a length of string"))
for i in range(len(s)):
    sub=""
    for j in range(i,len(s)):
        sub=sub+s[i]
        if len(sub)==length:
            print(sub)