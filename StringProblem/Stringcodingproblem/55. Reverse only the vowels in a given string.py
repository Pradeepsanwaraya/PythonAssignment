s=input("enter a string")
rev=""
store=""
for i in s:
    if i in "aeiou":
        store=store+i
for i in store:
    rev=i+rev
print(rev)