
# # 6. AI Chat Toxic Pattern Detector

# An AI moderation system wants to detect whether a sentence contains three consecutive repeating characters.

# If found:

# ```text
# Spam Pattern Found
# ```

# Else:

# ```text
# Clean Message
# ```

# ### Input:

# ```text
# heyyy broooo welcome
# ```

# ### Output:

# ```text
# Spam Pattern Found
# ```

# ---
word=input("Enter message:")

for i in range(len(word)-2):
    if word[i]==word[i+1] and word[i]==word[i+2]:
        print("Spam Pattern Found")
        break
else:
    print("Clean Message")