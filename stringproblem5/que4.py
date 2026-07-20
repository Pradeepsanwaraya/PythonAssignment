
# # 4. Cloud Storage Duplicate File Name Resolver

# A cloud storage company stores uploaded filenames from users.

# Sometimes multiple duplicate filenames are uploaded.

# The system should:

# * Keep the first occurrence unchanged
# * Add (1), (2), (3)... for duplicates

# ### Input:

# ```text
# file file image file image data
# ```

# ### Output:

# ```text
# file file(1) image file(2) image(1) data
# ```

# ---
word=input("Enter file names:").split()

for i in range(len(word)):
    c=0
    for j in range(i):
        if word[i]==word[j]:
            c=c+1
    if c==0:
        print(word[i],end=" ")
    else:
        print(word[i]+"("+str(c)+")",end=" ")