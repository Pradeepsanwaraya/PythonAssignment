f=open("article.txt","r")

lines=0
words=0
characters=0

for line in f:
    lines=lines+1

    data=line.split()
    words=words+len(data)

    characters=characters+len(line)

f.close()

print("total lines:",lines)
print("total words:",words)
print("total characters:",characters)