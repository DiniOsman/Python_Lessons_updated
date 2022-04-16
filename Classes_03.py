class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def calculate_total(self, x, y):
        return x * y
item1 = Item("DINI", 100, 5)
#item1.name = "PHONE"
#item1.price = 100
#item1.quantity = 5
#print(item1.calculate_total(item1.price, item1.quantity))
print (item1.name, item1.price, item1.quantity)