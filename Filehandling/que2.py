n=int(input("enter number of employees: "))

f=open("employees.txt","w")

for i in range(n):
    empid=input("enter employee id: ")
    name=input("enter employee name: ")
    dept=input("enter department: ")
    salary=input("enter salary: ")

    f.write(empid+","+name+","+dept+","+salary+"\n")

f.close()

f=open("employees.txt","r")

total=0
count=0

for line in f:
    data=line.strip().split(",")

    salary=int(data[3])

    total=total+salary
    count=count+1

    if salary>50000:
        print(data[0],data[1],data[2],salary)

f.close()

average=total/count

print("average salary:",average)