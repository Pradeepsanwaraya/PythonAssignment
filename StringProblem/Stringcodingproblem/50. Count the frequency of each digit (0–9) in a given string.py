s=input("enter a string")

d=""

for i in s:
    if i not in d:
        count=0

        for j in s:
            if i==j:
                count=count+1

        if i>="0" and i<="9":
            print(i,count)

        d=d+i