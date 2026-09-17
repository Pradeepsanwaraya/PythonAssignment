import sqlite3

db = sqlite3.connect("student.db")
cursor = db.cursor()

cursor.execute("create table if not exists student (name text, marks integer)")
cursor.execute("insert into student values ('Ajay', 80)")

db.commit()
db.close()

print("Table created and data inserted")
