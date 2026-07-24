# User se string lo
word = input("Enter string: ")

# Isme longest repeating substring store hogi
ans = ""

# -----------------------------------
# Outer loop
# i substring ka starting index batata hai
# -----------------------------------
for i in range(len(word)):

    # -----------------------------------
    # Inner loop
    # j substring ka ending index batata hai
    # Slicing me last index include nahi hota,
    # isliye len(word)+1 likha hai.
    # -----------------------------------
    for j in range(i+1, len(word)+1):

        # Substring banao
        sub = word[i:j]

        # -------------------------------
        # Dry Run
        #
        # word = "abcabcbb"
        #
        # i=0
        #
        # j=1 → sub="a"
        # j=2 → sub="ab"
        # j=3 → sub="abc"
        # j=4 → sub="abca"
        # j=5 → sub="abcab"
        # j=6 → sub="abcabc"
        # ...
        #
        # i=1
        #
        # j=2 → sub="b"
        # j=3 → sub="bc"
        # j=4 → sub="bca"
        # ...
        # -------------------------------

        # Check karo substring ek se zyada baar aa rahi hai ya nahi
        if word.count(sub) > 1:

            # -----------------------------
            # Dry Run
            #
            # sub="a"
            # word.count("a") = 2
            # Condition True
            #
            # sub="ab"
            # word.count("ab") = 2
            #
            # sub="abc"
            # word.count("abc") = 2
            #
            # sub="abca"
            # word.count("abca") = 1
            # Condition False
            # -----------------------------

            # Agar current substring pehle wali answer se badi hai
            if len(sub) > len(ans):

                # To answer update kar do
                ans = sub

                # -------------------------
                # Dry Run
                #
                # ans=""
                #
                # sub="a"
                # len("a") > len("")
                # ans="a"
                #
                # sub="ab"
                # ans="ab"
                #
                # sub="abc"
                # ans="abc"
                #
                # sub="abca"
                # Repeat nahi hui
                #
                # Final ans="abc"
                # -------------------------

# Final answer print karo
print(ans)