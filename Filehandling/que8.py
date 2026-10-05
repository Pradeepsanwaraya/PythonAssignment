f=open("article.txt","r")

ch=input("enter character: ")
count=0

for line in f:
    words=line.split()

    for word in words:
        if word.lower().startswith(ch.lower()):
            count=count+1

f.close()

print("words starting with",ch,":",count)