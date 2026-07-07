# 1.Leap Year Event Scheduler – Multi-Year Analysis System

# A city event management system schedules special festivals only in leap years.

# To plan future events, the system analyzes multiple years instead of just one.

# Write a program to:

# - Read start year and end year from user
# - For every year in the range, check whether it is a Leap Year or Not 
# - Apply rules:
#     - Divisible by 4 → Leap Year candidate  
#     - Divisible by 100 → Not Leap Year  
#     - Divisible by 400 → Leap Year  

# - If leap year → print year with "Event Scheduled"
# - Else → print year with "No Event"

# - After checking all years:
#     - Count total leap years
#     - Print total events scheduled

# Input:
# 2000
# 2005

# Output:
# 2000 → Event Scheduled
# 2001 → No Event
# 2002 → No Event
# 2003 → No Event
# 2004 → Event Scheduled
# 2005 → No Event
start=int(input("Enter start year:"))
end=int(input("Enter end year:"))

count=0

for year in range(start,end+1):

    if(year%400==0)or(year%4==0 and year%100!=0):
        print(year,"Event Scheduled")
        count=count+1
    else:
        print(year,"No Event")

print("Total Leap Years=",count)
print("Total Events Scheduled=",count)