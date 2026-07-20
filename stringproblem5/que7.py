
# # 7. Enterprise Password Pattern Strength Analyzer

# A cybersecurity company wants to validate advanced passwords.

# ## Conditions:

# * Minimum 10 characters
# * At least:

#   * 1 uppercase letter
#   * 1 lowercase letter
#   * 1 digit
#   * 1 special character
# * No consecutive repeating characters
# * No spaces allowed

# ### Input:

# ```text
# Pyth@n1234
# ```

# ### Output:

# ```text
# Strong Password
# ```

# ### Input:

# ```text
# Paaass@12
# ```

# ### Output:

# ```text
# Weak Password
# ```

# ---
word=input("Enter password:")

u=l=d=s=0
r=0

if len(word)>=10 and " " not in word:
    for i in range(len(word)):
        if word[i].isupper():
            u=1
        elif word[i].islower():
            l=1
        elif word[i].isdigit():
            d=1
        else:
            s=1

        if i>0 and word[i]==word[i-1]:
            r=1

    if u==1 and l==1 and d==1 and s==1 and r==0:
        print("Strong Password")
    else:
        print("Weak Password")
else:
    print("Weak Password")