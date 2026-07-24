# `
# 3. Find the First Non-Repeated Character

# Railway Ticket Fraud Detection System

# The railway department generates ticket reference IDs automatically.

# Sometimes, due to technical issues, many characters get repeated inside the ticket ID.

# The department wants a Python program that finds the first character that appears only once in the string.

# Example 1

# Input:
# aabbccddefg
# Output:

# ```
string=input("enter any string ")
done=''
for i in string:
    if i not in done:
        count=0
        for j in string:
            if j==i:
                count=count+1
        if count==1:
            print(i)
            break 
        done=done+i
