'''vehicle = input("Enter vehicle number: ")

if (len(vehicle) == 10 and
    vehicle[:2].isalpha() and
    vehicle[2:4].isdigit() and
    vehicle[4:].isalnum()):
    print("Valid Vehicle Number")
else:
    print("Invalid Vehicle Number")

    7.
Vehicle Number Plate Checker
The traffic department wants to validate vehicle registration numbers.
Conditions:
- First 2 characters should be alphabets
- Next 2 should be digits
- Total length should be 10
Input:
Enter vehicle number: MP04AB1234
Output:
Valid Vehicle Number
'''

plate=input("Enter vehicle number: ")

if len(plate)==10:
     fir=plate[0].lower()
     sec=plate[1].lower()
     third=plate[2]
     four=plate[3]
     if fir>='a' and fir<='z' and sec>='a' and sec<='z':
      
         if  third>='0' and third<='9' and four>='0' and four<='9':
              print("Valid Number Plate ")
         else:
              print("Third and Fourt number must be Numeric  ")
     else:
          print("First and Second Letter Must be Alphabet ")
else:
    print("Invalid Number Plate ")

