name = input("Enter student name: ")
count = 0

for ch in name:
    if ch.isalpha():
        if ch.lower() not in "aeiou":
            count += 1

print("Total consonants:", count)