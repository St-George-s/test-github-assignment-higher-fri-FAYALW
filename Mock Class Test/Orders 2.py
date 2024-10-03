import csv

class Order():
    def __init__(self,customerID, customerName, productPurchased, amountSpent, category):
        self.customerID = customerID
        self.customerName = customerName
        self.productPurchased = productPurchased
        self.amountSpent = amountSpent
        self.category = category

def readOrdersFromCSV():
    orders = []
    with open('Mock Class Test/ordersExtended.csv', 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        for row in reader:
            newOrder = Order(
                row[0],
                row[1],
                row[2],
                row[3],
                row[4])
            orders.append(newOrder)

    return orders

def findMaxOrderWithTV(orders):
    maxOrder = orders[0]
    for order in orders:
        if "TV" in order.productPurchased and order.amountSpent > maxOrder.amountSpent:
            maxOrder = order
    print(maxOrder.productPurchased, maxOrder.amountSpent)

def discount():
    if orders[0] % 5 == 0:
        print()

#Main Program
orders = readOrdersFromCSV()
findMaxOrderWithTV(orders)