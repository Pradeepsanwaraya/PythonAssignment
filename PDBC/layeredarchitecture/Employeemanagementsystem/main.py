from service.employeeservice import EmployeeService
from model.Employee import Employee

print("Welcome to our software")

service=EmployeeService()
while True:
    print("1.Add Employee")
    print("2.Display Employees ")
    print("3.Search Employee by ID")
    print("4.update employee")
    print("5.delete employee")
    print("6 Exit")
    choice=int(input("Enter your choice: "))
    match choice:
        case 1:
            eid=int(input("Enter ID: "))
            name=input("Enter Name: ")
            salary=float(input("Enter Salary: "))
            employee=Employee(eid,name,salary)
            service.addemployee(employee)
        case 2:
            service.display_all_employees()
        case 3:
            id=int(input("Enter Employee ID to search: "))
            service.search_employee(id)
        case 4:
            id=int(input("Enter ID: "))
            name=input("Enter Name: ")
            salary=float(input("Enter Salary: "))
            employee=Employee(id,name,salary)
            service.modify_employee(employee)
        case 5:
            id=int(input("Enter ID: "))
            service.deleteemployee(id)
        case 6:
            print("application closed")
        case __:
            print("invalid choice")