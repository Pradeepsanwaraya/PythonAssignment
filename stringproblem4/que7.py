
# 7. Remove Duplicate Words from a String

# Voice Assistant Noise Correction System

# A voice assistant records spoken commands from users.

# Due to microphone disturbance and network lag, some words are repeated multiple times.

# The company wants a Python program that removes duplicate words while maintaining the original order.

# ``
# hello hello how are are you
# ```

# Output:

# ```
# hello how are you
# ```

# #
s=input("Enter Sentence: ").split()
new=""
for i in s:
    if i not in new.split():
        new=new+i+" "
print(new)