class Employee:
    def __init__(self,name,salary,department):
        self.name=name
        self.salary=salary
        self.department=department
    def display(self):
        print(self.name)
        print(self.salary)
        print(self.department)
obj=Employee("pradeep",10000,"iit")
obj.display()