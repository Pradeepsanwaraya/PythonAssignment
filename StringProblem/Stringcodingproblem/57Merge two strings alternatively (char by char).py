s=input("enter a string 1:")
l=input("enter a string 2 :")
i=0
j=0
mg=""
while i<len(s) and j<len(l):
    mg=mg+s[i]+l[j]
    i=i+1
    j+=1
while i<len(s):
    mg=mg+s[i]
    i=i+1
while j<len(l):
    mg=mg+l[j]
    j=j+1
print(mg)