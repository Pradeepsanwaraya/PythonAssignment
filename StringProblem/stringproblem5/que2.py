
# # 2. AI Auto-Correct Consecutive Word Remover

# An AI-powered typing assistant often captures duplicate consecutive words while converting speech into text.

# The company wants a Python program that removes only consecutive duplicate words while preserving the original sentence structure.

# ### Input:

# ```text
# hello hello hello team meeting meeting started
# ```

# ### Output:

# ```text
# hello team meeting started
# ```

# ---
word=input("Enter sentence:").split()

print(word[0],end=" ")

for i in range(1,len(word)):
    if word[i]!=word[i-1]:
        print(word[i],end=" ")