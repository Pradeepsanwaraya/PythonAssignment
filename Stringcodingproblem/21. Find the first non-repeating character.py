s=input("enter a string")
low=''
done=''
for i in s:
    if i not in done:
        count=0
        for j in s:
            if i==j:
                count=count+1
        if count==1:
            low=low+i
            break
        done=done+i
print(low)