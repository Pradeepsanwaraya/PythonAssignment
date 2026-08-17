s=input("enter a sentence").split()
word=input("enter a word")
for i in range(len(s)-1,-1,-1):
    if s[i]==word:
        print(i)
        break