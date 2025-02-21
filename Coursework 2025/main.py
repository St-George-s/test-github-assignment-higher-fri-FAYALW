import csv # Import the csv module to handle reading data from CSV files

class Order(): # Define an Order class to store detailed order information
    def __init__(self, orderNum, date, email, option, cost, rating):
        self.orderNum = orderNum #Initializes attributes for each order
        self.date = date   
        self.email = email  
        self.option = option      
        self.cost = cost
        self.rating = rating                


def readOrdersFromCSV(): #Defines a function to read the data from the CSV file
    with open('Coursework 2025/orders.txt', 'r') as file: #Opens the file
        reader = csv.reader(file) # Creates a CSV reader to process each row
        header = next(reader) #Skips the header row
        orders = [] #Creates an array to store the data called orders
        for row in reader: #Loops over each row in the CSV file and create an Order object
            newOrder = Order(
                row[0], #orderNum from first column           
                row[1], #date from second column  
                row[2], #email from third column          
                row[3], #option from fourth column   
                float(row[4]), #cost from fifth column converted to a float
                int(row[5]) #rating from sixth column converted to an integer       
            )
            orders.append(newOrder) #Appends the new Order object to the orders array
    return orders #Returns the array


def findPosition(orders):
# 2.1 Set position to -1
    position = -1
# 2.2 Set index to 0
    index = 0
# 2.3 Ask user to enter month to search for
    monthToSearch = input("Enter the first three letters of the month to search: ")
# 2.4 While position is -1 and index is less than the length of the array
    for order in orders:
        while position == -1 and index < len(orders):
# 2.5 If current month is equal to searched month and current rating is 5 then
            if orders[index].date == monthToSearch and orders[index].rating == '5':
# 2.6 Set position to index
                position = index
# 2.7 End if
# 2.8 Add 1 to index
        index += 1
# 2.9 End while
# 2.10 Return position
    return position


def writeDetailsToFile(orders, position): #Defines a function to write the details to a text file
# 3.1 Open new file ‘winningCustomer.txt’
    with open('winningCustomer.csv', 'w') as file: #Opens a new file
# 3.2 If position is 0 or above then
        for order in orders: #Loops through each record in the array
            if order.position >= 0: #Checks if the position is above or equal to 0
# 3.3 Write winning order number, email and cost to ‘winningCustomer.txt’
                file.write(orders[position].orderNum, orders[position].email, orders[position].cost) #If it is, then it write the winning order number, email, and cost to the file
# 3.4 Else
            else:
# 3.5 Write ‘No winner’ to ‘winningCustomer.txt’
                file.write('No winner') #Else it write 'No winner' to the file
# 3.6 End if
# 3.7 Close ‘winningCustomer.txt’
# Writing to a file


def countOption(orders): #Defines a function to count the number of orders delivered and collected
    deliveredCount = 0
    collectedCount = 0
    for counter in range(1, len(orders)):
        if orders[counter].option == 'Delivered':
            deliveredCount += 1
        elif orders[counter].option == 'Collected':
            collectedCount +=1
    return deliveredCount, collectedCount


#Main
orders = readOrdersFromCSV()
#print(orders[3].date)

position = findPosition(orders)
print(position)

writeDetailsToFile(orders, position)

total = countOption(orders)
print(total)


# # 4.1 Call countOption function to return the number of orders delivered
# ordersTotal = countOption(Order)
# # 4.2 Call countOption function to return the number of orders collected
# ordersTotal = countOption(Order)
# # 4.3 Output the total number of orders delivered
# print(ordersTotal)
# # 4.4 Output the total number of orders collected
# print(ordersTotal)