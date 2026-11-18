class Mobile:
    def details(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
        print(self.brand)
        print(self.model)
        print(self.price)
ob=Mobile()
ob1=Mobile()
ob2=Mobile()
ob.details("samsung",17,200000)
ob1.details("Apple",16,100000)
ob2.details("Oneplus",15,20000)