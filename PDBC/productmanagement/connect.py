import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='pradeep@1670'
)
cursor=mydb.cursor()
# cursor.execute('create database productmanagement')
# print("database is created")
cursor.execute('use productmanagement')
while True:
    print("\n----- product management system -----")
    print("1. add product")
    print("2. view all products")
    print("3. search product")
    print("4. update product")
    print("5. delete product")
    print("6. exit")

    choice = int(input("enter your choice: "))
    match choice:
        case 1:
            print("add product")
            name=input("enter product name")
            price=float(input("enter product price"))
            quantity=int(input("enter product quantity"))
            sql='insert into products(name,price,quantity) values(%s,%s,%s)'
            val=(name,price,quantity)
            cursor.execute(sql,val)
            mydb.commit()
        case 2:
            cursor.execute("select * from products")
            result=cursor.fetchall()
            print(result)
        case 3:
            print("search product")
            pid = int(input("enter product id: "))

            sql = "select * from products where id=%s"
            val = (pid,)

            cursor.execute(sql, val)
            result = cursor.fetchone()

            if result:
                print(result)
            else:
                print("product not found")     
        case 4:
            print("update product")
            pid = int(input("enter product id: "))
            name = input("enter new product name: ")
            price = float(input("enter new product price: "))
            quantity = int(input("enter new product quantity: "))

            sql = "update products set name=%s, price=%s, quantity=%s where id=%s"
            val = (name, price, quantity, pid)

            cursor.execute(sql, val)
            mydb.commit()

            if cursor.rowcount > 0:
                print("product updated successfully")
            else:
                print("product not found")
        case 5:
            print("delete product")
            pid = int(input("enter product id: "))

            sql = "delete from products where id=%s"
            val = (pid,)

            cursor.execute(sql, val)
            mydb.commit()

            if cursor.rowcount > 0:
                print("product deleted successfully")
            else:
                print("product not found")       
        case 6:
            print("thank you!")
            break