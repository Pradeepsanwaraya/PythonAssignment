f=open("article.txt","r")

search=input("enter word to search: ")
count=0

for line in f:
    words=line.split()

    for word in words:
        if word.lower()==search.lower():
            count=count+1

f.close()

print(search,"occurs",count,"times in the file.")