class BankAccount:
    bank_name="SBI"
    def __init__(self,holder_name,balance):
        self.holder_name=holder_name
        self.balance=balance
    def display(self):
        print(self.holder_name)
        print(self.balance)
    def deposite(self,amount):
        self.amount=amount
        self.balance=self.balance+amount
        print(self.balance)
    def withdraw(self,amount):
        self.amount=amount
        if self.amount<=self.balance:
            self.balance=self.balance-self.amount
            print(self.balance)
        else:
            print("insufficient balance")
    @staticmethod
    def check_balance(balance):
        if balance>10000:
            print("Good balance")
        else:
            print("Low balance")
obj1=BankAccount("pradeep",265000)
obj1.display()
obj1.deposite(12000)
obj1.withdraw(10000)
BankAccount.check_balance(obj1.balance)



obj2=BankAccount("ravi",10000)
obj2.display()
obj2.deposite(15000)
obj2.withdraw(50000)
BankAccount.check_balance(obj2.balance)