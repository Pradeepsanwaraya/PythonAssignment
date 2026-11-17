
import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='pradeep@1670'
)
dbcursor=mydb.cursor()
dbcursor.execute("use schoolmanagement")

while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Search Student by Name")
    print("4. Update Student Fees")
    print("5. Delete Student")
    print("6. Exit")

    choice=int(input("Enter your choice:"))

    match choice:
        case 1:
            sid=int(input("Enter Student ID:"))
            sname=input("Enter Student Name:")
            course=input("Enter Course:")
            fees=float(input("Enter Fees:"))
            city=input("Enter City:")

            sql="INSERT INTO student VALUES(%s,%s,%s,%s,%s)"
            val=(sid,sname,course,fees,city)
            dbcursor.execute(sql,val)
            mydb.commit()
            print("Student inserted successfully.")

        case 2:
            dbcursor.execute("SELECT * FROM student")
            result=dbcursor.fetchall()

            if result:
                for row in result:
                    print(row)
                print("Records displayed successfully.")
            else:
                print("No records found.")

        case 3:
            search_name=input("Enter name to search:")
            pattern="%"+search_name+"%"
            sql="SELECT * FROM student WHERE sname LIKE %s"
            dbcursor.execute(sql,(pattern,))
            result=dbcursor.fetchall()

            if result:
                print("Matching students:")
                for row in result:
                    print(row)
            else:
                print("No record found.")

        case 4:
            sid=int(input("Enter Student ID:"))
            fees=float(input("Enter New Fees:"))
            sql="UPDATE student SET fees=%s WHERE sid=%s"
            dbcursor.execute(sql,(fees,sid))
            mydb.commit()

            if dbcursor.rowcount>0:
                print("Student fees updated successfully.")
            else:
                print("Student not found.")

        case 5:
            sid=int(input("Enter Student ID:"))
            sql="DELETE FROM student WHERE sid=%s"
            dbcursor.execute(sql,(sid,))
            mydb.commit()

            if dbcursor.rowcount>0:
                print("Student deleted successfully!")
            else:
                print("Student not found!")

        case 6:
            print("Thank you for using Student Management System.")
            break

        case _:
            print("Invalid choice. Please try again.")

dbcursor.close()
mydb.close()
