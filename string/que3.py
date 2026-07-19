'''3.
Character Occurrence Checker in Product Review

An e-commerce website wants to know how many times a particular character appears in a product review.

Input: Enter product review: this product is really good Enter character to check: o

Output: Character 'o' occurs: 4 times
'''

msg=input("Enter product review: ")
ch=input("Enter Character  ")
count=0
for i in msg:
    if i.lower()==ch:
        count=count+1

print("Occurance of ",ch ,"in ",msg,"is : ",count)
        