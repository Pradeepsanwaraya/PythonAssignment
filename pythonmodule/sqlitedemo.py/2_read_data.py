import sqlite3

db = sqlite3.connect("student.db")
cursor = db.cursor()

cursor.execute("select * from student")
rows = cursor.fetchall()

for row in rows:
    print(row)

db.close()
