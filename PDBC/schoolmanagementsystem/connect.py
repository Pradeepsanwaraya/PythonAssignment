import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='pradeep@1670'
)
dbcursor=mydb.cursor()
# dbcursor.execute('create database schoolmanagement')
# print("database is created")
dbcursor.execute("use schoolmanagement")
# dbcursor.execute("create table student(sid int ,sname varchar(50),course varchar(50),fees decimal(10,2),city varchar(30))")
# # print("table is created")
# dbcursor.execute('alter table student add primary key(sid)')
# dbcursor.execute("DELETE FROM student")

# mydb.commit()

# print("Old records deleted successfully")
# dbdata="insert into student values(%s,%s,%s,%s,%s)"

# dblist = [
#     (101, 'Amit', 'Python', 15000, 'Indore'),
#     (102, 'Priya', 'Java', 18000, 'Bhopal'),
#     (103, 'Rahul', 'Python', 15000, 'Indore'),
#     (104, 'Neha', 'Java', 18000, 'Ujjain'),
#     (105, 'Karan', 'MERN', 20000, 'Indore')
# ]
# dbcursor.executemany(dbdata,dblist)
# mydb.commit()
# dbcursor.execute("select * from student")
# for i in  dbcursor:
#     print(i)

# dbcursor.execute("insert into student values(6,'anjali','python',15000,'dewas')")
# mydb.commit()
# dbcursor.execute("select * from student")
# result=dbcursor.fetchall()
# print(result)
# search_name=input("Enter student name:")
# pattern="%"+search_name+"%"
# sql = "SELECT * FROM student WHERE sname LIKE %s"
# dbcursor.execute(sql, (pattern,))
# result = dbcursor.fetchall()
# if result:
#     for row in result:
#         print(row)
# else:
#     print("No record found")
# dbcursor.execute('update student set fees=17000 where sid=101')
# dbcursor.execute("SELECT * FROM student WHERE sid=101")

# res = dbcursor.fetchone()
# print(res)
dbcursor.execute("DELETE FROM student WHERE sid= %s",(104,))
mydb.commit()
if dbcursor.rowcount > 0:
    print("Student deleted successfully!")
else:
    print("Student not found!")