s=input("enter a string")
lower=""
for i in range(len(s)):
    if s[i]>='A' and s[i]<='Z':
        l=ord(s[i])
        lower=lower+(chr(l+32))
    else:
        lower=lower+i
print(lower)