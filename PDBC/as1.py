import mysql.connector as db
class Online_Shopping:
    def __init__(self):
        self.mydb=db.connect(
            host="localhost",
            port=3306,
            user="root",
            password="Shreya@123",
            database="as2pdbc"
        )
        self.cursor=self.mydb.cursor()

    #connection close program   
    def connection_close(self):
        self.cursor.close()
        self.mydb.close()

        print("Database Closed Successfully")
    def add_customer(self):
        customer_id=int(input("Enter Customer ID: "))
        customer_name=input("Enter Customer Name: ")
        city=input("Enter City: ")
        email=input("Enter Email: ")
        query=("insert into customer_order_pdbc(customer_id,customer_name,city,email)values(%s,%s,%s,%s)")
        details=(customer_id,customer_name,city,email)
        self.cursor.execute(query,details)
        self.mydb.commit()
        print("Customer Added Successfully")



    def add_product(self):
        product_id=int(input("Enter product ID: "))
        product_name=input("Enter Product Name: ")
        category=input("Enter Category: ")
        price=int(input("Enter Price: "))
        stock=int(input("Enter Stock: "))
        query=("insert into product_order_pdbc(product_id,product_name,category,price,stock)values(%s,%s,%s,%s,%s) ")
        details=(product_id,product_name,category,price,stock)
        self.cursor.execute(query,details)
        self.mydb.connect()
        print("product Inserted Succesfully")



    def place_order(self):
        order_id=int(input("Enter Order ID: "))
        customer_id=int(input("Enter Customer ID: "))
        product_id=int(input("Enter Product ID: "))
        quantity=int(input("Enter Quantity: "))
        status=input("Enter Order Status: ")
        query="insert into customer_order_details(order_id,customer_id,product_id,quantity,status)values(%s,%s,%s,%s,%s)"
        details=(order_id,customer_id,product_id,quantity,status)
        self.cursor.execute(query,details)
        self.mydb.commit()
        print("----------------")
        print("Order Placed Successfully")



    def display_all_order(self):
        query="select o.order_id,c.customer_name,p.product_name,o.quantity,p.price,(o.quantity * p.price) AS amount from customer_order_pdbc AS c inner join customer_order_details AS o on c.customer_id=o.customer_id inner join product_order_pdbc AS p on p.product_id=o.product_id "

        self.cursor.execute(query)
        records=self.cursor.fetchall()
        print("Order ID Customer Name Product name Quantity Price Amount Status ")
        print("-----------------------------------------")
        for rows in records:
                print(rows[0],rows[1],rows[2],rows[3],rows[4],rows[5])

    def search_customer(self):
        search_name=input("Enter customer name to search: ")
        query="select customer_id,customer_name,city from customer_order_pdbc where customer_name like %s "
        self.cursor.execute(query,('%' + search_name + '%',))
        records=self.cursor.fetchall()
        for row in records:
                print(row)

        
    def update_product_price(self):
        product_id=int(input("Enter Product ID: "))
        new_price=int(input("Enter New Price: "))
        query="update product_order_pdbc price=%s where product_id=%s"
        self.cursor.execute(query,(new_price,product_id))
        print("Product price updated successfully.")


                
    def update_order_status(self):
            order_id=int(input("Enter Product ID: "))
            status=input("Enter New Price: ")
            query="update customer_order_pdbc status=%s where order_id=%s"
            self.cursor.execute(query,(status,order_id))
            print("Order status updated successfully.")




    def delete_order(self):
           order_id=int(input("Enter Product ID: "))        
           query="delete product_order where order_id=%s"
           self.cursor.execute(query,(order_id)) 
           print("Order deleted successfully.")
    
    def total_purchase_amt(self):
            query=" select c.customer_id,c.customer_name,sum(p.price*od.quantity) from customer_order_pdbc as c inner join customer_order_details  as od on c.customer_id=od.customer_id inner join product_order_pdbc as p on p.product_id=od.product_id group by c.customer_id,c.customer_name order by c.customer_id"
            self.cursor.execute(query)
            records=self.cursor.fetchall()
            print("Customer ID  Customer Name  Total Purchase Amount")
            for row in records:
                    print(row[0],row[1],row[2] )

            
    def avg_product_price(self):
      query="select p.product_id,p.product_name,p.price from product_order_pdbc as p where p.price>(select avg(p.price) from product_order_pdbc as p);"
      self.cursor.execute(query)
      records=self.cursor.fetchall()
      print("Product ID  product Name  Price")
      for row in records:
        print(row[0],row[1],row[2] )
    
    def display_atleast_one_order(self):
        query="select c.customer_id ,c.customer_name from customer_order_pdbc AS c where c.customer_id in (select od.customer_id from customer_order_details as od );"
        self.cursor.execute(query)
        records=self.cursor.fetchall()
        print("Customer ID  Customer Name ")
        for row in records:
                print(row[0],row[1] )
            
    def display_not_placed(self):
            query="select c.customer_id ,c.customer_name from customer_order_pdbc AS c where c.customer_id not in (select od.customer_id from customer_order_details as od );"
            self.cursor.execute(query)
            records=self.cursor.fetchall()
            print("Customer ID  Customer Name ")
            for row in records:
                print(row[0],row[1] )


    def menu(self):
        print("===== ONLINE SHOPPING ORDER MANAGEMENT =====")
        print("1. Add Customer")
        print("2. Add Product")
        print("3. Place Order")
        print("4. Display All Orders with Customer and Product Details")
        print("5. Search Customer by Name")
        print("6. Update Product Price")
        print("7. Update Order Status")
        print("8. Delete Order")
        print("9. Display Customer-wise Total Purchase Amount")
        print("10. Display Products Costing More Than Average Product Price")
        print("11. Display Customers Who Have Placed at Least One Order")
        print("12. Display Customers Who Have Not Placed Any Order")
        print("13. Exit")
        choice=int(input("Enter your choice: "))
        match choice :
            case 1:
                    self.add_customer()
            case 2:
                    self.add_product()
            case 3:
                  self.place_order()
            case 4:
                self.display_all_order()
            case 5:
                self.search_customer()
            case 6:
                self.update_product_price()
            case 7:
                 self.update_order_status()
            case 8:
                self.delete_order()
            case 9:
                self.total_purchase_amt()                                                         
            case 10:
              self.avg_product_price()
            case 11:
                self.display_atleast_one_order()
            case 12:
                self.display_not_placed(self)    
            case 13:
                print("Thankyou for visiting")
            case __:
                print("Invalid Choice")

c1=Online_Shopping()
c1.menu()
c1.connection_close()