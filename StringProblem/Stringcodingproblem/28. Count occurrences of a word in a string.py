s=input("enter a sentence").split()
word=input("enter a word")
count=0
for i in range(len(s)-1,-1,-1):
    if s[i]==word:
        count=count+1
print(count)
    