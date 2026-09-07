s=input("enter a string")
sub=input("enter substring")
count=0

for i in range(len(s)-len(sub)+1):
    new=""
    for j in range(len(sub)):
        new=new+s[i+j]
    if new==sub:
        count=count+1

print(count)