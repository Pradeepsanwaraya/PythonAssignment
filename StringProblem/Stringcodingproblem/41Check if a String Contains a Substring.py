s=input("enter a string")
word=input("enter a word")
for i in range(len(s)-len(word)+1):
    flag=True
    for j in range(len(word)):
        if s[i+j]!=word[j]:
            flag=False
            break
    else:
        print("word found",word)

