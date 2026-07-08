class Product():
    def __init__(self, PID, Name, Price, Quantity, Discount):
        self.PID = PID
        self.Name = Name
        self.Price = Price
        self.Quantity = Quantity
        self.Discount = Discount
    def display(self):
        print(self.PID, self.Name, self.Price, self.Quantity, self.Discount)
    def buy_option(self, quantity):
        if quantity <= self.Quantity:
            price = quantity * self.Price
            self.Quantity = self.Quantity - quantity
            if self.Discount > 0:
                price = price * self.Discount
            print(price)
        elif quantity > self.Quantity:
            print("Currently not enough products remaining")


p1 = Product(134860, "Milk", 2, 90, 0.8)

p1. buy_option(100)
p1.display()




