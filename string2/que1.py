username = input("Enter username: ")

if (5 <= len(username) <= 12 and
    username[0].isalpha() and
    " " not in username):

    valid = True

    for ch in username:
        if not (ch.isalnum() or ch == "_"):
            valid = False
            break

    if valid:
        print("Valid Username")
    else:
        print("Invalid Username")
else:
    print("Invalid Username")