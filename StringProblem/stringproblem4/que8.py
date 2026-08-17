# .
# Find the Second Highest Repeating Character in a String

# Social Media Trend Analysis System

# A social media company analyzes hashtags and user comments to identify trending character patterns.

# The analytics team wants a Python program to find the character with the second highest frequency in a given string.

# This helps detect secondary trending patterns in user activity.

# Input:

# aaabbbbccddeee

# Output:

# e

# Explanation:

# b occurs 4 times → highest
# e occurs 3 times → second highest

# Condition:

# Program should work for both uppercase and lowercase letters.
# Spaces should be ignored.
# If no second highest frequency exists, print:
# Second highest repeating character not found
s=input("Enter any string ")
first=0
second=0
fchar=""
schar=""
for i in s:
    if i==" ":
        continue
    count=0
    for j in s:
        if i==j:
            count=count+1
    if count>first:
        second=first
        schar=fchar
        first=count
        fchar=i
    elif count>second and count!=first:
        second=count
        schar=i
if second==0:
    print("Second highest repeating character not found")
else:
    print(schar)