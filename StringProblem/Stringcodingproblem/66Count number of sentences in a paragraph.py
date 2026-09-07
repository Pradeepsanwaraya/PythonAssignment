s=input("enter a paragraph")
count=0
for i in s:
    if i=="." or i=="!" or i=="?":
        count=count+1
print(count)