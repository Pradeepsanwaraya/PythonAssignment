from database.connection import Database
from model.student import Student

class StudentDAO:
    def __init__(self):
        self.database = Database()

    def create_table(self):
        db = self.database.get_connection()
        cursor = db.cursor()
        cursor.execute(
            "create table if not exists students("
            "sid int primary key auto_increment,"
            "name varchar(50), marks int, age int)"
        )
        db.commit()
        db.close()

    def save(self, student):
        db = self.database.get_connection()
        cursor = db.cursor()
        sql = "insert into students(name, marks, age) values(%s, %s, %s)"
        cursor.execute(sql, (student.name, student.marks, student.age))
        db.commit()
        db.close()

    def get_all(self):
        db = self.database.get_connection()
        cursor = db.cursor()
        cursor.execute("select sid, name, marks, age from students")
        rows = cursor.fetchall()
        db.close()
        students = []
        for r in rows:
            students.append(Student(r[1], r[2], r[3], sid=r[0]))
        return students

    def get_by_name(self, name):
        db = self.database.get_connection()
        cursor = db.cursor()
        cursor.execute("select sid, name, marks, age from students where name=%s", (name,))
        r = cursor.fetchone()
        db.close()
        if r is None:
            return None
        return Student(r[1], r[2], r[3], sid=r[0])

    def delete_by_name(self, name):
        db = self.database.get_connection()
        cursor = db.cursor()
        cursor.execute("delete from students where name=%s", (name,))
        db.commit()
        count = cursor.rowcount
        db.close()
        return count

    def update(self, student, old_name):
        db = self.database.get_connection()
        cursor = db.cursor()
        sql = "update students set name=%s, marks=%s, age=%s where name=%s"
        cursor.execute(sql, (student.name, student.marks, student.age, old_name))
        db.commit()
        count = cursor.rowcount
        db.close()
        return count