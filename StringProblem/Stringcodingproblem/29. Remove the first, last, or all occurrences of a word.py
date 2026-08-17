s=input("enter a sentence").split()
word=input("enter a word")
new=""
for i in range(len(s)-1,-1,-1):
    if s[i]==word:
        pass
    else:
        new=new+" "+s[i]
print(new)
    
    