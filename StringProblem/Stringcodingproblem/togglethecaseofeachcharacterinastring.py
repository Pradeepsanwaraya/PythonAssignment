s=input("enter a string")
toggle=""
for i in range(len(s)):
    if s[i]>='a' and s[i]<='z':
        u=ord(s[i])
        toggle=toggle+chr(u-32)
    elif s[i]>='A' and s[i]<='Z':
        l=ord(s[i])
        toggle=toggle+chr(l+32)
    else:
        toggle=toggle+s[i]
print(toggle)