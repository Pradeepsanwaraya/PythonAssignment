s=input("enter a string:")

for i in range(len(s)):
    sub=""
    for j in range(i,len(s)):
        sub=sub+s[j]
        print(sub)
