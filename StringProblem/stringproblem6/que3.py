
# 3.
# Replace Consecutive Duplicate Characters with Single Character
# Data Compression System

# A cloud storage company wants to reduce unnecessary repeated characters in text logs.

# Write a Python program that replaces consecutive duplicate characters with a single occurrence.

# Input:
# aaabbbccccdddaa
# Output:
# abcda
word = input("Enter any word: ")

for i in range(len(word)):
    if i == 0 or word[i] != word[i-1]:
        print(word[i], end="")