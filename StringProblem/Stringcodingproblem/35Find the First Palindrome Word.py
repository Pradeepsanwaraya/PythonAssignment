s=input("enter string").split()
palindrome=""
for i in s:
    rev=''
    for j in i:
        rev=rev+j
    if rev==i:
        print("palindrome",i)
        break
