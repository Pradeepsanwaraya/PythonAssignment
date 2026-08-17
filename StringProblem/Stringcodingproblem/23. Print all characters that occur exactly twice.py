s=input("enter a string")
twicech=''
done=''
for i in s:
    if i not in done:
        count=0
        for j in s:
            if i==j:
                count=count+1
        if count==2:
            twicech=twicech+i
    done=done+i
print(twicech)