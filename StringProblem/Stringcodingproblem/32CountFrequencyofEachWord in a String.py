s=input("enter a sentence").split()
done=""
for i in s:
    if i not in done.split():
        count=0
        for j in s:
            if i==j:
                count=count+1
        done=done+i+" "
        print(count,i)
