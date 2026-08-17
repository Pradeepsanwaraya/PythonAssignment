text = input("Enter citizen information: ")

result = ""
newword = True

for ch in text:
    if ch == " ":
        result=result+ch
        newword = True
    else:
        if newword:
            result=result+ch.upper()
            newword = False
        else:
            result=result+ch

print("formatted information:")
print(result)