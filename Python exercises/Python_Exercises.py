class bankAccount():
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance

    def __repr__(self):
        return f"Account Owner: {self.owner}, Balance: {self.balance}"

    def withdraw(self,wtd_amt):
        if self.balance >= wtd_amt:
            self.balance = self.balance - wtd_amt
            print("Your money was withdrawed!")
        else:
            print("Transaction was unsuccessful!")

    def deposit(self,dep_amt):
        self.balance = self.balance + dep_amt
        print("Your money was deposited!")

acc1 = bankAccount("Jose",100)
print(acc1)
print(acc1.owner)
print(acc1.balance)
acc1.withdraw(75)
acc1.deposit(50)
acc1.withdraw(500)
