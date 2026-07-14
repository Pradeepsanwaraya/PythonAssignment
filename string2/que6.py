code1 = input("Enter first product code: ")
code2 = input("Enter second product code: ")

a = code1.replace(" ", "").lower()
b = code2.replace(" ", "").lower()

if sorted(a) == sorted(b):
    print("Both Product Codes are Matching")
else:
    print("Product Codes are Not Matching")