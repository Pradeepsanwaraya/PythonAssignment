s1=input("enter string")
s2=input("enter string")
if len(s1)==len(s2) and s2 in s1+s1:
    print("Rotation")
else:
    print("Not Rotation")