class Employee:
    company = "Infobeans"
    def __init__(self,name,salary,department):
        self.name=name
        self.salary=salary
        self.department=department
    def display(self):
        print(self.name)
        print(self.salary)
        print(self.department)
    @classmethod
    def change_class(cls,name):
        cls.company=name
    @staticmethod
    def check_salary(salary):
        if salary>30000:
            print("High salary")
        else:
            print("Normal salary")
obj=Employee("pradeep",30000,'it')
obj.display()
obj.check_salary(obj.salary)
print()
Employee.change_class("ABC")
print(Employee.company)

print()
obj1=Employee("rajdeep",35000,'fi')
obj1.display()
obj1.check_salary(obj1.salary)
print()

obj2=Employee("deep",20000,'it')
obj2.display()
obj2.check_salary(obj2.salary)
print()
