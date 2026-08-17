s=input("enter a sentence").split()
word=input("enter a word")
new=input("new enter new word")
empty=""
for i in range(len(s)-1,-1,-1):
    if s[i]==word:
        empty=empty+" "+new
    else:
        empty=empty+" "+s[i]
print(empty)
    
    