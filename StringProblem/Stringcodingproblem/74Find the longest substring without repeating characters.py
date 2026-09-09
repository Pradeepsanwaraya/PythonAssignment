s=input("enter a string")

done=""
long=""

for i in range(len(s)):
    sub=""

    for j in range(i,len(s)):
        sub=sub+s[j]
        done=""

        for k in sub:
            if k not in done:
                done=done+k
            else:
                break

        if len(done)==len(sub):
            if len(sub)>len(long):
                long=sub

print(long)