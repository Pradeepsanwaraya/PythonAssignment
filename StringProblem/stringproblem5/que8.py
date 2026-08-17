
# # 8. Intelligent Search Query Compressor

# A search engine company wants to compress user queries.

# ## Rules:

# * Count frequency of each character
# * Display characters in sorted order
# * Ignore spaces
# * Case insensitive

# ### Input:

# ```text
# Google Search
# ```

# ### Output:

# ```text
# a1c1e2g2h1l1o2r1s1t1
# ```
word=input("Enter string:").lower()

for i in range(len(word)):
    if word[i]!=" " and word[i] not in word[:i]:
        c=0
        for j in word:
            if word[i]==j:
                c=c+1
        print(word[i],c,sep="",end="")