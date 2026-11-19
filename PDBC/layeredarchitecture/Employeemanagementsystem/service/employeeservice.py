from dao.employeedao  import EmployeeDao
class EmployeeService:
    def addemployee(self,employee):
        if employee.id<=0:
            print("Employee id must be positive")
            return 
        if employee.name.strip()=="":
            print("Employee name cannot be empty")
            return
        print("service : processing employee ")
        dao=EmployeeDao()
        dao.saveemployee(employee)

    def display_all_employees(self):
        dao=EmployeeDao()
        employees=dao.getallemployees()
        if len(employees)==0:
            print("No employee found")
            return 
        for employee in employees:
            print("ID:",employee.id)
            print("Name",employee.name)
            print("Salary:",employee.salary)


    def search_employee(self,id):
        dao=EmployeeDao()
        employee=dao.getemployeebyid(id)
        if employee is None:
            print("Employee Not found")
        else:
            print("ID:",employee.id)
            print("Name",employee.name)
            print("Salary:",employee.salary)

    def modify_employee(self,employee):
        dao=EmployeeDao()
        if employee.name.strip()=="":
            print("employee name can  not empty")
            return
        affectedrows=dao.updateemployee(employee)
        if affectedrows>0:
            print("employee updated successfully")
        else:
            print("employee not found")


    def deleteemployee(self,id):
        dao=EmployeeDao()
        affectedrows=dao.deleteemployee(id)
        if affectedrows>0:
            print("employee deleted successfully")
        else:
            print("employee not found")
