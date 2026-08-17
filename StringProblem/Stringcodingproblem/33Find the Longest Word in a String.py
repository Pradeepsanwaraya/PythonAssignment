s=input("enter a sentence").split()
long=s[0]
for i in s:
    if len(i)>len(long):
        long=i

print(long)