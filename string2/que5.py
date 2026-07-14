code = input("Enter product code: ")

if code.lower() == code[::-1].lower():
    print("Palindrome Code")
else:
    print("Not a Palindrome Code")