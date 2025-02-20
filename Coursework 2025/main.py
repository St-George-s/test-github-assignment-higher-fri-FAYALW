import csv

class Order():
    def __init__(self, orderNum, date, email, option, cost, rating):
        self.orderNum = orderNum
        self.date = date   
        self.email = email  
        self.option = option      
        self.cost = cost
        self.rating = rating                


def readOrdersFromCSV():
    orders = []
    with open('Coursework 2025/orders.txt', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            newOrder = Order(
                row[0],            
                row[1],            
                row[2],           
                row[3],    
                row[4],
                row[5]           
            )
            orders.append(newOrder)


def findPosition(orders):
# 2.1 Set position to -1
    position = -1
# 2.2 Set index to 0
    index = 0
# 2.3 Ask user to enter month to search for
    monthToSearch = input("Enter the first three letters of the month to search: ")
# 2.4 While position is -1 and index is less than the length of the array
    while position == -1 and index < len(orders):
# 2.5 If current month is equal to searched month and current rating is 5 then
        if index.date == monthToSearch:
# 2.6 Set position to index
            position = index
# 2.7 End if
# 2.8 Add 1 to index
    index += 1
# 2.9 End while
# 2.10 Return position
    return position


def writeDetailsToFile(orders, position):
# 3.1 Open new file ‘winningCustomer.txt’
    with open('Coursework 2025/winningCustomer.csv', 'w') as file:
# 3.2 If position is 0 or above then
        if position == 0 or position > 0:
# 3.3 Write winning order number, email and cost to ‘winningCustomer.txt’
            file.write(orders.orderNum, orders.email, orders.cost)
# 3.4 Else
        else:
# 3.5 Write ‘No winner’ to ‘winningCustomer.txt’
            file.write('No winner')
# 3.6 End if
# 3.7 Close ‘winningCustomer.txt’


def countOption(orders):
    deliveredCount = 0
    collectedCount = 0
    for x in range(1, len(orders)):
        if x.option == 'Delivered':
            deliveredCount += 1
        elif x.option == 'Collected':
            collectedCount +=1
    return(deliveredCount, collectedCount)


# 4.1 Call countOption function to return the number of orders delivered
ordersTotal = countOption(Order)
# 4.2 Call countOption function to return the number of orders collected
ordersTotal = countOption(Order)
# 4.3 Output the total number of orders delivered
print(ordersTotal)
# 4.4 Output the total number of orders collected
print(ordersTotal)