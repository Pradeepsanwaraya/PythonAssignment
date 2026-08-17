
# # 5. Social Media Hashtag Trend Window

# A social media company wants to analyze the smallest substring containing all unique characters from a hashtag.

# ### Input:

# ```text
# aabcbcdbca
# ```

# ### Output:

# ```text
# dbca
# ```

# ### Explanation:

# `dbca` contains all unique characters: a,b,c,d

# ---
word=input("Enter string:")

u=""
for ch in word:
    if ch not in u:
        u=u+ch

ans=word
i=0
j=0

while i<len(word):
    while j<len(word):
        temp=word[i:j+1]
        ok=True
        for ch in u:
            if ch not in temp:
                ok=False
                break
        if ok:
            if len(temp)<len(ans):
                ans=temp
            break
        j=j+1
    i=i+1
    j=i

print(ans)