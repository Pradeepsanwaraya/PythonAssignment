class Student:
    def __init__(self,name,marks,age):
        self.name=name
        self.marks=marks
        self.age=age
    def __str__(self):
        return f"Name={self.name},Marks={self.marks},Age={self.age}"