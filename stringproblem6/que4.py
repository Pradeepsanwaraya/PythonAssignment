
# 4.

# Find All Characters with Maximum Frequency
# Website Traffic Analysis System

# A web analytics company tracks user activity symbols in server logs.

# The company wants to identify all characters having the maximum frequency in the given string.

# Input:
# aabbbccddd
# Output:
# b d
word = input("Enter any word: ")

maxi = 0

for ch in word:
    c = 0
    for i in word:
        if ch == i:
            c = c + 1
    if c > maxi:
        maxi = c

for i in range(len(word)):
    c = 0
    for j in word:
        if word[i] == j:
            c = c + 1

    if c == maxi and word[i] not in word[:i]:
        print(word[i], end=" ")