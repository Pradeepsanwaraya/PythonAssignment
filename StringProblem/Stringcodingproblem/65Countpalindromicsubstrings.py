s=input("enter a string")

for i in range(len(s)):
    sub=""
    for j in range(i+1,len(s)):
        sub=sub+s[j]
    rev=""
    for k in sub:
        rev=k+rev
    if sub==rev:
        print(sub)
