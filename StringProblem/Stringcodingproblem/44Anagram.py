s=input("enter a string")
s2=input("enter a strng2")
d1={}
d2={}
for i in range(len(s)):
    if i not in d1:
        d1[i]=1
    else:
        d1[i]+=1
for j in range(len(s2)):
    if j not in d2:
        d2[j]=1
    else:
        d2[j]+=1
if d1==d2:
    print("anagram")
else:
    print("not an anagram")
