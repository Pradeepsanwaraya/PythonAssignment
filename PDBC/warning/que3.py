class Employee:
    company="infobeans"
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def display(self):
        print(self.name)
        print(self.salary)
    @classmethod
    def change_company(cls,name):
        cls.company=name
    @staticmethod
    def message():
        print("i have learnt class and all")
obj=Employee("pradeep",10000)
obj.display()
Employee.change_company("Abc Technology")
print(Employee.company)
Employee.message()