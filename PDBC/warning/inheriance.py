# class Parent:
#     def display(self):
#         print("This is  parent class")
# class Child(Parent):
#     pass
# obj=Child()
# obj.display()
class Vehicle:
    def __init__(self,brand):
        self.brand=brand
    def display(self):
        print(self.brand)
class Car(Vehicle):
    def __init__(self,brand,model,price):
        super().__init__(brand)
        self.brand=brand
        self.model=model
        self.price=price
        print(self.brand)
        print(self.model)
        print(self.price)

obj=Car("mercedies","m1",40000)
obj.display()



       

