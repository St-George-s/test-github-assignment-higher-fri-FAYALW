import csv

class Order():
    def __init__(self,customerName, productPurchased, amountSpent):
        self.customerName = customerName
        self.productPurchased = productPurchased
        self.amountSpent = amountSpent

def readOrdersFromCSV():
    orders = []
    with open('Mock Class Test/orders.csv', 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        for row in reader:
            newOrder = Order(
                row[0],
                row[1],
                row[2])
            orders.append(newOrder)

    return orders

def findMaxOrderWithTV(orders):
    maxOrder = orders[0]
    for order in orders:
        if "TV" in order.productPurchased and order.amountSpent > maxOrder.amountSpent:
            maxOrder = order
    print(maxOrder.productPurchased, maxOrder.amountSpent)

#Main Program
orders = readOrdersFromCSV()
findMaxOrderWithTV(orders)