from database.connection import conn
def savestudent(name,marks,age):
    db=conn()
    cursor=db.cursor()
    # cursor.execute("create database summer")
    # cursor.execute("use summer")
    cursor.execute("create table if not exists students(sid int primary key auto_increment,name varchar(50),marks int,age int)")
    sql="insert into students(name,marks,age) values(%s,%s,%s)"

    value=(name,marks,age)
    cursor.execute(sql,value)
    db.commit()
    return
def select():
    db=conn()
    db=conn()
    cursor=db.cursor()
    # cursor.execute("create database summer")
    # cursor.execute("use summer")
    cursor.execute("select * from students")
    result=cursor.fetchall()
    return result
def getbyname(name):
    db=conn()
    cursor=db.cursor()
    sql="select * from students where name=%s"
    value=((name),)
    cursor.execute(sql,value)
    res=cursor.fetchone()
    return res
def deletebyname(name):
    db=conn()
    cursor=db.cursor()
    sql="delete from students where name=%s"
    value=((name),)
    cursor.execute(sql,value)
    db.commit()
    affectedrow=cursor.rowcount
    return affectedrow
def update(name,marks,age,sname):
    db=conn()
    cursor=db.cursor()
    sql="update students set %s,%s,%s where name=%s"
    value=(name,marks,age,sname)
    cursor.execute(sql,value)
    affectedrow=cursor.rowcount
    return affectedrow