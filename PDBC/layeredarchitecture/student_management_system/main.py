from service.studentservice import StudentService
from model.student import Student

class Student:
    def __init__(self):
        self.service = StudentService()

    def show_menu(self):
        print("1. insert")
        print("2. show all data")
        print("3. get by name")
        print("4. delete by name")
        print("5. update")
        print("6. exit")

    def run(self):
        while True:
            self.show_menu()
            choice = int(input("enter your choice: "))

            if choice == 1:
                name = input("enter name: ")
                marks = int(input("enter marks: "))
                age = int(input("enter age: "))
                student = Student(name, marks, age)
                print(self.service.add_student(student))

            elif choice == 2:
                for s in self.service.get_all():
                    print(s)

            elif choice == 3:
                name = input("enter name: ")
                s = self.service.get_by_name(name)
                if s is None:
                    print("student nahi mila")
                else:
                    print(s)

            elif choice == 4:
                name = input("enter name: ")
                print(self.service.delete_by_name(name), "record affected")

            elif choice == 5:
                old_name = input("enter old name: ")
                name = input("enter new name: ")
                marks = int(input("enter new marks: "))
                age = int(input("enter new age: "))
                student = Student(name, marks, age)
                print(self.service.update_student(student, old_name), "record affected")

            elif choice == 6:
                break

res= Student()
res.run()