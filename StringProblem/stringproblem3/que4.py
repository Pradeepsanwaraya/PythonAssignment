
# A messaging application wants to temporarily encrypt messages during
# transmission. The encryption rule is to reverse every word individually
# while keeping the word positions unchanged.

# Input: Enter message: java is powerful

# Output: Encrypted Message: avaj si lufrewop
msg=input("enter any number").split()
for i in msg:
    rev=''
    for j in i:
        rev=j+rev

    print(rev, end=' ')