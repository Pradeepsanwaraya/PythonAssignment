# class Employee:
#     company='Infobeans'
#     def __init__(self,name,salary,department):
#         self.name=name
#         self.salary=salary
#         self.department=department
#     def display(self):
#         print(self.name)
#         print(self.salary)
#         print(self.department)
#     @classmethod
#     def change_company(cls,name):
#         cls.company=name
#     @staticmethod
#     def welcome():
#         print("welcome to company")
# obj=Employee("pradeep",10000,"it")
# Employee.welcome()
# obj.display()
# Employee.change_company("abc company")
# print(Employee.change_company)


class Mobile:
    brand_type="Smartphones"
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price

    def display(self):
        print(self.brand)
        print(self.model)
        print(self.price)
    @classmethod
    def change_brand_type(cls,name):
        cls.brand_type=name
    @staticmethod
    def check_price(price):
        if price>20000:
            print("Premium")
        else:
            print("Budget")
oppo=Mobile("A12",12,25000)
oppo.display()
Mobile.check_price(oppo.price)



Mobile.change_brand_type("laptop")
print(Mobile.brand_type)

vivo=Mobile("Z11",11,45000)

Mobile.check_price(vivo.price)

Iqoo=Mobile("s2",2,15000)

Mobile.check_price(Iqoo.price)

lenovo=Mobile("s8",22,55000)
Mobile.check_price(lenovo.price)

lg=Mobile("s5",6,16000)
Mobile.check_price(lg.price)


l=[vivo,oppo,Iqoo,lenovo,lg]
avg=0
max=l[0].price
count=0
avge=0
bcount=0
pcount=0
exp=l[0]
cheap=l[0]
mini=l[0].price
for i in range(len(l)):
    count=count+1
    l[i].display()
    Mobile.check_price(l[i].price)
    if l[i].price>20000:
        pcount=pcount+1
    if l[i].price<=20000:
        bcount=bcount+1
    if l[i].price>max:
        max=l[i].price
        exp=l[i]
    if l[i].price<mini:
        mini=l[i].price
        cheap=l[i]
    avge=avge+l[i].price
    if l[i].price>30000:
        
        l[i].display()
    
avg=avge/count
print(count)
print(bcount)
print(pcount)
exp.display()
cheap.display()
print(avg)
