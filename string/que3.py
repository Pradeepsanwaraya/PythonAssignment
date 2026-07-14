review = input("Enter product review: ")
char = input("Enter character to check: ")

count = 0

for ch in review:
    if ch.lower() == char.lower():
        count += 1

print("Character", repr(char), "occurs:", count, "times")