
#  A company wants to analyze customer feedback messages by counting how many vowels are present in the feedback.

# Input: Enter feedback message: Hello Customer Service

# Output: Total vowels: 8

# msg = input("Enter feedback message: ")
# count = 0

# for ch in msg:
#     if ch.lower() in "aeiou":
#         count += 1

# print("Total vowels:", count)

msg=input("Enter Message : ")
count=0
c=0

for ch in msg:
    if ch.lower() in 'aeiou':
        count=count+1
    else:
        c=c+1

print("Vowel count ",count)
print("Consonant Count : ",c)