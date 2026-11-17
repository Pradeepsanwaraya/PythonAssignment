import mysql.connector as db
class Employee_Management:
    def __init__(self):
        self.mydb=db.connect(
            host="localhost",
            port=3306,
            user="root",
            password="pradeep@1670",
            database="as2pdbc"
            )
        self.cursor=self.mydb.cursor()
        print("database connected successfully")

    def closed_connection(self):
        self.cursor.close()
        self.mydb.close()
        print("database Closed successfully")
    def add_department(self):
        dept_id=int(input("Enter Department ID:: "))
        dept_name=input("Enter Department Name: ")

    def add_employee(self):
        pass

    def display_all_employees(self):
        pass

    def search_employee_by_name(self):
        pass

    def update_employee_salary(self):
        pass

    def update_employee_department(self):
        pass

    def delete_employee(self):
        pass

    def department_wise_employee_count(self):
        pass

    def department_wise_average_salary(self):
        pass

    def employees_above_company_average(self):
        pass

    def employees_above_department_average(self):
        pass

    def display_it_department_employees(self):
        pass

    def departments_with_multiple_employees(self):
        pass

    def display_employee_manager(self):
        pass

    def departments_without_employees(self):
        pass

    def test_foreign_key_constraint(self):
        pass



    def menu(self):
      while True:
        print("\n===== COMPANY EMPLOYEE MANAGEMENT SYSTEM =====")
        print("1. Add Department")
        print("2. Add Employee")
        print("3. Display All Employees with Department")
        print("4. Search Employee by Name")
        print("5. Update Employee Salary")
        print("6. Update Employee Department")
        print("7. Delete Employee")
        print("8. Display Department-wise Employee Count")
        print("9. Display Department-wise Average Salary")
        print("10. Display Employees Earning More Than Average Salary")
        print("11. Display Employees Earning More Than Their Department Average")
        print("12. Display Employees Working in the IT Department")
        print("13. Display Departments Having More Than One Employee")
        print("14. Display Employee and Manager Names using Self Join")
        print("15. Display Departments with No Employees")
        print("16. Test Foreign Key Constraint")
        print("17. Exit")
        print("==============================================")
        choice=int(input("Enter your choice:"))
        match choice:
            case 1:
              pass
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
                pass
            case 7:
                pass
            case 8:
                pass
            case 9:
                pass
            case 10:
                pass
            case 11:
                pass
            case 12:
                pass
            case 13:
                pass
            case 14:
                pass
            case 15:
                pass
            case 16:
                pass
            case 17:
                pass