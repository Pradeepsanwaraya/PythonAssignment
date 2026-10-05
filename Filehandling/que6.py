f=open("article.txt","r")

longest=""

for line in f:
    words=line.split()

    for word in words:
        if len(word)>len(longest):
            longest=word

f.close()

print("longest word:",longest)
print("length:",len(longest))