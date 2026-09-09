s=input("enter a string")
long=""
for i in range(1,len(s)):
    sub=""
    for j in range(i):
        sub=sub+s[j]
    end=""
    for k in range(len(sub)-len(s),len(s)):
        end=end+s[k]
    if len(end)>len(long):
        long=sub
print(long)
    