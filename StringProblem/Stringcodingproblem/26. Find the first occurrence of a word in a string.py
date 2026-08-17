s=input("enter a sentence").split()
word=input("enter a word")
for i in range(len(s)):
    if s[i]==word:
        print(i)
        break