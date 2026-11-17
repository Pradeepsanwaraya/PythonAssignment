import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password='pradeep@1670'
)
cursor=mydb.cursor()
# cursor.execute("create database online_shopping")
cursor.execute("use online_shopping")
cursor.execute("create table if not exists customer_order(customer_id int primary key,customer_name varchar(60),city varchar(40),email varchar(80))")
while True:
    print("Online shopping management system")