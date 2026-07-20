
# # 3. Secure Banking Transaction Analyzer

# A banking server generates encrypted transaction IDs using letters and digits.

# The fraud detection team wants a Python program to find the first digit that does not repeat in the transaction ID.

# If no unique digit exists, print:

# ```text
# No unique digit found
# ```

# ### Input:

# ```text
# A122334455667789
# ```

# ### Output:

# ```text
# 8
# ```

# ---
word=input("Enter transaction ID:")

for i in range(len(word)):
    if word[i].isdigit():
        c=0
        for j in word:
            if word[i]==j:
                c=c+1
        if c==1:
            print(word[i])
            break
else:
    print("No unique digit found")