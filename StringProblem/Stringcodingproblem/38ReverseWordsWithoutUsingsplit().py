s = input("enter a string")

words = ""
og = ""

for i in s:
    if i == " ":
        og = words + " " + og
        words = ""
    else:
        words = words + i

og = words + " " + og

print(og)