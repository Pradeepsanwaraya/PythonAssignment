# Assignment 1 — Age Calculator

# Create a program that accepts the user's date of birth and calculates:

# Current age in years
# Completed months
# Total number of days lived
# Next birthday date
# Number of days remaining for the next birthday

# Input:

# Enter DOB (DD-MM-YYYY): 15-08-1998

# Expected Output:

# Age: 28 years
# Total Days Lived: XXXXX days
# Next Birthday: 15-08-2027
# Days Remaining: XX days
# from datetime import datetime
# dob=map(int,input("Enter DOB (DD-MM-YYYY): ").split("-"))
# day,month,year=dob
# birth=datetime(year,month,day)
# today=datetime.now()
# age=today.year-year
# if (today.month,today.day)<(month,day):
#     age=age-1
# months=(today.year-year)*12+(today.month-month)
# if today.day<day:
#     months=months-1
# totaldays=(today-birth).days
# nextbirthday=datetime(today.year,month,day)
# if nextbirthday<today:
#     nextbirthday=datetime(today.year+1,month,day)
# daysremaining=(nextbirthday-today).days

# print("Age:",age,"years")
# print("Completed Months:",months,"months")
# print("Total Days Lived:",totaldays,"days")
# print("Next Birthday:",nextbirthday.strftime("%d-%m-%Y"))
# print("Days Remaining:",daysremaining,"days")


from datetime import datetime
dob=map(int,input("enter your date of birth").split())
day,month ,year=dob
birth=datetime(year,month,day)
print(birth)
today=datetime.now()
print(today)
age=today.year-year
print(age)
if (today.month,today.day)<(month,day):
    age=age-1
months=(today.year-year)*12+(today.month-month)
print(months)
print(today.month-month) 
if today.day<day:
    months=months-1
totaldays=(today-birth)
print(totaldays)
nextbirthday=datetime(today.year,month,day)
if nextbirthday<today:
    nextbirthday=datetime(today.year+1,month,day)
daysremaining=(nextbirthday-today).days
print(nextbirthday)
print(daysremaining)