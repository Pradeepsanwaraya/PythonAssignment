pw = input("Enter Password: ")

count = 0
scount = 0

if len(pw) >= 8 and len(pw) <= 15:

    if pw[0] >= 'A' and pw[0] <= 'Z':
        if pw[-1] >= '0' and pw[-1] <= '9':

            for ch in pw:
                if ch >= '0' and ch <= '9':
                    count = count + 1
                elif ch == "@" or ch == "#" or ch == "$" or ch == "%" or ch == "&" or ch == "*":
                    scount = scount + 1
                elif ch == " ":
                    print("Invalid Password")
                    break
            else:
                if count >= 2 and scount >= 1:
                    print("Secure Password")
                else:
                    print("Invalid Password")

        else:
            print("Invalid Password")
    else:
        print("Invalid Password")

else:
    print("Invalid Password")