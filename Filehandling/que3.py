n=int(input("enter number of orders: "))

f=open("orders.txt","w")

for i in range(n):
    orderid=input("enter order id: ")
    name=input("enter customer name: ")
    product=input("enter product: ")
    quantity=input("enter quantity: ")
    price=input("enter price: ")

    f.write(orderid+","+name+","+product+","+quantity+","+price+"\n")

f.close()

f=open("orders.txt","r")

highest=0
highestid=""
highestname=""

for line in f:
    data=line.strip().split(",")

    quantity=int(data[3])
    price=int(data[4])

    total=quantity*price

    print(data[0],data[1],data[2],"quantity:",quantity,"total:",total)

    if total>highest:
        highest=total
        highestid=data[0]
        highestname=data[1]

f.close()

print("highest order:")
print("order id:",highestid)
print("customer:",highestname)
print("total amount:",highest)