class Bankaccount():
    def __init__(self, acc_number, acc_holder, acc_type, acc_balance):
        self.acc_number = acc_number
        self.acc_holder = acc_holder
        self.acc_type = acc_type
        self.acc_balance = acc_balance
    def deposit(self, amount):
        self.acc_balance = self.acc_balance + amount
    def withdraw(self, amount):
        if self.acc_balance - amount >= 0:
            self.acc_balance = self.acc_balance - amount
        else:
            print("You don' have money")
    def display(self):
        print(self.acc_number, self.acc_holder, self.acc_type, self.acc_balance)




b1 = Bankaccount(830291, "Lara Marie", "saving", 60000000)

b1.display()
b1.deposit(1)
b1.display()
b1.withdraw(30000000)
b1.display()




