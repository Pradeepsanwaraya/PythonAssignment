
import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='pradeep@1670'
)
dbcursor=mydb.cursor()
dbcursor.execute("use employeemanagement")
# dbcursor.execute("create table if not exists employee(eid int primary key,ename varchar(50),department varchar(40),salary decimal(10,2),city varchar(30))")

while True:
    print("\n===== employee management system =====")
    print("1. add employee")
    print("2. display all employees")
    print("3. search employee by name")
    print("4. update employee salary")
    print("5. delete employee")
    print("6. exit")

    choice=int(input("enter your choice:"))

    match choice:
        case 1:
            empid=int(input("enter employee id:"))
            ename=input("enter employee name:")
            department=input("enter employee department:")
            salary=float(input("enter employee salary:"))
            city=input("enter employee city:")
            sql="insert into employee values(%s,%s,%s,%s,%s)"
            val=(empid,ename,department,salary,city)
            dbcursor.execute(sql,val)
            mydb.commit()
            print("employee inserted successfully.")

        case 2:
            dbcursor.execute("select * from employee")
            result=dbcursor.fetchall()
            if result:
                for row in result:
                    print(row)
                print("records displayed successfully.")
            else:
                print("no records found.")

        case 3:
            search_name=input("enter employee name to search:")
            pattern="%"+search_name+"%"
            sql="select * from employee where ename like %s"
            dbcursor.execute(sql,(pattern,))
            result=dbcursor.fetchall()
            if result:
                print("matching employees:")
                for row in result:
                    print(row)
            else:
                print("no record found.")

        case 4:
            empid=int(input("enter employee id:"))
            salary=float(input("enter new salary:"))
            sql="update employee set salary=%s where eid=%s"
            dbcursor.execute(sql,(salary,empid))
            mydb.commit()
            if dbcursor.rowcount>0:
                print("employee salary updated successfully.")
            else:
                print("employee not found.")

        case 5:
            empid=int(input("enter employee id:"))
            sql="delete from employee where eid=%s"
            dbcursor.execute(sql,(empid,))
            mydb.commit()
            if dbcursor.rowcount>0:
                print("employee deleted successfully.")
            else:
                print("employee not found.")

        case 6:
            print("thank you for using employee management system.")
            break

        case _:
            print("invalid choice. please try again.")

dbcursor.close()
mydb.close()
