s=input("enter a string").split()
word=input("enter a word")
for i in range(len(s)):
    if s[i]==word:
        print(i)
