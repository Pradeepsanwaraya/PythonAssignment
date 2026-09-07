s=input("enter a string : ")
result=""
for i in range(2,len(s)):
    result=result+s[i]
for i in range(2):
    result=result+s[i]
print(result)