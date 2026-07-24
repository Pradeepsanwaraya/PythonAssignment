
# 5.
# Cybercrime Log Analysis System

# A cybersecurity company monitors encrypted login activity stored as character-based security logs.

# During investigation, analysts need to identify the last character that repeats in the log sequence.
# This helps detect the most recent duplicated activity pattern before a possible security breach.

# Write a Python program to find the last repeating character in a given string.

# If no repeating character exists, print:

# No repeating character found
# Input:
# abccdbefga
# Output:
# a
word = input("Enter any word: ")

for i in range(len(word)-1, -1, -1):
    c = 0
    for j in word:
        if word[i] == j:
            c = c + 1
    if c > 1:
        print(word[i])
        break
else:
    print("No repeating character found")