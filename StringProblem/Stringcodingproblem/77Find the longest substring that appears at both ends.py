s=input("enter a string")
long=""
for i in range(1,len(s)):
    sub=""
    for j in range(i):
        sub=sub+s[j]
    end=""
    for k in range(len(s)-len(sub),len(s)):
        end=end+s[k]
    if sub==end:
        if len(sub)>len(long):
            long=sub
print(long)
    