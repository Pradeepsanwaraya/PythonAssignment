s=input("enter a string")
sec=input("enter  a string")
flag=True
if len(s)!=len(sec):
    flag=False
else:
    for i in range(len(s)):
        if s[i]!=sec[i]:
            flag=False
print(flag)