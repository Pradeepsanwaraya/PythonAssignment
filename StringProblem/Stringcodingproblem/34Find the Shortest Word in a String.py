s=input("enter a steing").split()
short=s[0]
for i in s:
    if len(i)<len(short):
        short=i
print(short)