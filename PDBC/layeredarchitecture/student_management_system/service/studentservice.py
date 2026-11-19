from dao.datadao import StudentDAO

class StudentService:
    def __init__(self):
        self.dao = StudentDAO()
        self.dao.create_table()

    def _is_valid(self, student):
        if not student.name.strip():
            return "Name khali nahi ho sakta"
        if not 0 <= student.marks <= 100:
            return "Marks 0 se 100 ke beech hone chahiye"
        if student.age <= 0:
            return "Age 0 se zyada honi chahiye"
        return None

    def add_student(self, student):
        error = self._is_valid(student)
        if error:
            return error
        self.dao.save(student)
        return "data inserted"

    def get_all(self):
        return self.dao.get_all()

    def get_by_name(self, name):
        return self.dao.get_by_name(name)

    def delete_by_name(self, name):
        return self.dao.delete_by_name(name)

    def update_student(self, student, old_name):
        if self._is_valid(student):
            return 0
        return self.dao.update(student, old_name)