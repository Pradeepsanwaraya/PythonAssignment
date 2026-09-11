
# 2.
#  Employee Joining & Experience System

# Create an employee experience calculator.

# Read:

# Employee name
# Joining date
# Current date

# Calculate:

# Total days worked
# Total years worked
# Total months approximately
# Experience in Years Months Days
# Whether employee has completed 1 year
# Whether employee has completed 5 years

# Example:

# Enter employee name: Rahul
# Enter joining date: 10-06-2021
# Enter current date: 10-09-2026

# Output:

# Employee: Rahul
# Joining Date: 10-06-2021
# Experience: 5 Years 3 Months 0 Days
# Total Days Worked: 1918
# # 5 Years Completed: Yes
# from datetime import datetime
# name=input("enter name of employ")
# joiningdate=map(int,input("enter a joining date").split())
# joiningday,joiningmonth,joiningyear=joiningdate
# joining=datetime(joiningyear,joiningmonth,joiningday)
# current=datetime.now()
# print(joining)
# print(current)
# totalyear=(current.year-joiningyear)
# print("total year he worked",totalyear)
# if (current.month,current.day)<(joiningmonth,joiningday):
#     totalyear=totalyear-1
# # ye ai ka he itana ni samaj aaya
# # month=current.month-joiningmonth
# print(totalyear,month,days)
# if totalyear>=5:
#     print("5 year experience completed ")
           