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
    position = -1
    index = 0
    monthToSearch = input("Enter the first three letters of the month to search: ")
    while position == -1 and index < len(orders):
        if monthToSearch in orders[position].date and orders[position].rating == '5':
            position = index
        index += 1
    return position


def writeDetailsToFile(orders, position): #Defines a function to write the details to a text file
    with open('Coursework 2025/winningCustomer.txt', 'w') as file: #Opens a new file
            if position >= 0: #Checks if the position is above or equal to 0
                file.write(str(orders[position].orderNum) + "," + str(orders[position].email) + "," + str(orders[position].cost)) #If it is, then it write the winning order number, email, and cost to the file
            else:
                file.write('No winner') #Else it writes 'No winner' to the file


def countOption(orders, option): #Defines a function to count the number of orders delivered and collected
    count = 0
    for counter in range(len(orders)):
        if orders[counter].option == option:
            count += 1
    return count

#Main
mainOrders = readOrdersFromCSV()

mainPosition = findPosition(mainOrders)
print(mainPosition)

writeDetailsToFile(mainOrders, mainPosition)

deliveryTotal = countOption(mainOrders, "Delivery")
collectionTotal = countOption(mainOrders, "Collection")

print(deliveryTotal)
print(collectionTotal)