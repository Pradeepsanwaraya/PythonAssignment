s=input("enter a string")
high=-1
highch=''
done=''
for i in s:
    if i not in done:
        count=0
        for j in s:
            if i==j:
                count=count+1
    if count>high:
        high=count
        highch=i
    done=done+i
print(highch)
print(high)
