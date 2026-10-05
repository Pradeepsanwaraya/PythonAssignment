f=open("paragraph.txt","r")

vowels=0
consonants=0

for line in f:
    for ch in line.lower():
        if ch in "aeiou":
            vowels=vowels+1
        elif ch.isalpha():
            consonants=consonants+1

f.close()

print("total vowels:",vowels)
print("total consonants:",consonants)