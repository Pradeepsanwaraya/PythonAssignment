
# 2.
# Find the Most Frequently Occurring Word
# News Channel Keyword Analyzer

# A news agency analyzes breaking news headlines to identify the most repeated keyword in a report.

# Write a Python program to find the word with the highest frequency.

# Input:
# india won the match and india created history
# Output:
# india


word=input("enter any word").split()
c=0
for ch in word:
    c=0
    for i in word:
        if ch==i:
            c=c+1
    if c>1:
       
        res=ch
print(res) 