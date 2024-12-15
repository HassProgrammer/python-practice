# Qs. Create a class called Order which stores item & its price.
# Use Dunder function _ gt__() to convey that:
# orderl › order2 if price of order1 > price of order2

class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price
    
    def __gt__(self, order2):
        return self.price > order2.price

order1 = Order("chips", 20)
order2 = Order("Tea", 15)

print(order1 > order2)