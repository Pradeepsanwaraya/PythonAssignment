s=input("enter a string")
count=0
sub="the"
sub2="is"
countis=0

for i in range(len(s)):
    new=""
    for j in range(i,len(s)):
        new=new+s[j]
        if new==sub:
            count=count+1
        if new==sub2:
            countis=countis+1
print(count,countis)