password = input("Enter password: ")

digit = 0
special = 0

for ch in password:
    if ch.isdigit():
        digit += 1
    if ch in "@#$%&*":
        special += 1

if (8 <= len(password) <= 15 and
    password[0].isupper() and
    password[-1].isdigit() and
    digit >= 2 and
    special >= 1 and
    " " not in password):
    print("Secure Password")
else:
    print("Invalid Password")