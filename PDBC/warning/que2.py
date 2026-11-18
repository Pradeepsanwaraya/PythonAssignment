class Students:
    college="infobeans"
    def __init__(self,name,rollno,marks):
        self.name=name
        self.rollno=rollno
        self.marks=marks
    def display(self):
        print(self.name)
        print(self.rollno)
        print(self.marks)
obj=Students("pradeep",12,85)
obj.display()
print(obj.college)
