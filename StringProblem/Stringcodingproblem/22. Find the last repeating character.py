s=input("enhter a string")
last=''
done=""
for i in range(len(s)-1,-1,-1):
    if s[i] not in done:
        count=0
        for j in range(len(s)-1,-1,-1):
            if s[i]==s[j]:
                count=count+1
                
        if count==1:
            last=s[i]
            break
print(last)