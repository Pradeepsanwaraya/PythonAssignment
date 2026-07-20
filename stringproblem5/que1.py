# 1. Smart Log File Error Pattern Detector

# A cybersecurity company stores server logs containing repeated system activity characters.

# To detect suspicious looping behavior, the analytics team wants a Python program that finds the longest repeating substring present in the log file.

# If multiple substrings have the same length, print the first one found.

#  Input:

# ```text
# abcabcbb
# ```

# Output:

# ```text
# abc
# ```

# ---
word=input("Enter string:")

res=""

for i in range(len(word)):
    for j in range(i+1,len(word)):
        k=0
        temp=""
        while j+k<len(word) and word[i+k]==word[j+k]:
            temp=temp+word[i+k]
            k=k+1
        if len(temp)>len(res):
            res=temp

print(res)