num = input("Enter contact number: ")

count = 0

for ch in num:
    if ch.isdigit():
        count += 1

print("Total digits:", count)