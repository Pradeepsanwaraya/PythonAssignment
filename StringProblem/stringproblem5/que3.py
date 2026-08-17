
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
uniqe='' 
count=0
done=''
for i in word:
    if i not in done:
        count=0
        for j in word:
            if j==i:
                count=1
                break
        if count==1:
            print(i)
            done=done+i
