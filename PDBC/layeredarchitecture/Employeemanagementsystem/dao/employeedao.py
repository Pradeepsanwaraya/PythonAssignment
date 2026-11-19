from database.connection import Database
from model.Employee import Employee
class EmployeeDao:
    def saveemployee(self,employee):
        print("DAO:saving employee")

        db=Database()
        connection=db.connect()
        cursor=connection.cursor()
        query="insert into emp(id,name,salary) values(%s,%s,%s)"
        values=(employee.id,employee.name,employee.salary)
        cursor.execute(query,values)
        connection.commit()
        cursor.close()
        connection.close()
        print("employee saved successfully")


    def getallemployees(self):
        db=Database()
        connection=db.connect()
        cursor=connection.cursor()
        query="select id,name ,salary from emp"
        cursor.execute(query)
        records=cursor.fetchall()
        employees=[]
        for row in records:
            employee=Employee(row[0],row[1],row[2])
            employees.append(employee)
            cursor.close()
            connection.close()
            return employees



    def getemployeebyid(self,id):
        db=Database()
        connection=db.connect()
        cursor=connection.cursor()
        query="select * from emp where id=%s"
        cursor.execute(query,(id,))
        row=cursor.fetchone()
        cursor.close()
        connection.close()
        if row is not None:
            employee=Employee(row[0],row[1],row[2])
            return employee
        return None

    def updateemployee(self,employee):
        db=Database()
        connection=db.connect()
        cursor=connection.cursor()
        query="update emp set name=%s,salary=%s where id=%s"
        values=(employee.name,employee.salary,employee.id)
        cursor.execute(query,values)
        connection.commit()
        affectedrows=cursor.rowcount
        cursor.close()
        connection.close()
        return affectedrows
    def deleteemployee(self,id):
        db=Database()        
        connection=db.connect()        
        cursor=connection.cursor()
        query="delete from emp where id=%s"
        cursor.execute(query,(id,))
        connection.commit()
        affectedrows=cursor.rowcount
        cursor.close()
        connection.close()
        return affectedrows